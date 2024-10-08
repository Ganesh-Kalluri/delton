# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from collections import defaultdict
from leewise import _, api, fields, models
from ..models.l10n_lu_tax_report_data import MULTI_COLUMN_FIELDS

class LuAnnualTaxReportCustomHandler(models.AbstractModel):
    _name = 'l10n_lu.annual.tax.report.handler'
    _inherit = 'l10n_lu.tax.report.handler'
    _description = 'Luxembourgish Annual Tax Report Custom Handler'

    def _custom_options_initializer(self, report, options, previous_options=None):
        super()._custom_options_initializer(report, options, previous_options=previous_options)
        # closing entry button shouldn't be visible in the annual tax report
        options['buttons'] = [button for button in options['buttons'] if button['action'] != 'action_periodic_vat_entries']

    def _get_field_values(self, lines):
        field_types_dict = {
            'string': 'char',
            'boolean': 'boolean',
        }
        values = {}
        for line in lines:
            # tax report's `code` would contain alpha-numeric string like `LUTAX_XXX` where characters
            # at last three positions will be digits, hence we split `code` with `_` and build dictionary
            # having `code` as dictionary key
            line_code = code = line.get('code', '') and line['code'].split('_')[-1]
            if not (line_code and line_code.isdigit()):
                continue

            for column in line['columns']:
                value = column['no_format']
                if value is None:
                    continue

                # every expression in such line corresponds to a different field in the report
                # so we match the correct field using the line code and the expression_label (column)
                if code in MULTI_COLUMN_FIELDS:
                    line_code = MULTI_COLUMN_FIELDS[code][column['expression_label']]

                field_type = field_types_dict.get(column['figure_type']) or 'float'
                if field_type == 'boolean':
                    value = str(int(value))
                if line_code == '998' and value == '0': # we set either 998 or 999 depending on the value
                    line_code, value = '999', '1'

                values[line_code] = {'value': value, 'field_type': field_type}

        return values


class LuReportAppendixA(models.AbstractModel):
    _name = 'l10n_lu.appendix.a.tax.report.handler'
    _inherit = 'account.tax.report.handler'
    _description = 'Custom Handler for the Appendix A of the LU Annual Tax Report'

    def _get_account_details(self, ln):
        model, active_id = self.env['account.report']._get_model_info_from_id(ln['id'])
        if model == 'account.account':
            account = self.env['account.account'].browse(active_id)
            return account.tag_ids, account.name
        return False, False

    @api.model
    def _get_precomputed_lines(self, year, lines, annex_options, result=None):
        expenditures_table = []
        excluded_index, invoiced_index = 0, 1
        # in case the columns are manually reordered
        for i, column in enumerate(annex_options['columns']):
            if column['expression_label'] == 'net':
                excluded_index = i
            elif column['expression_label'] == 'tax':
                invoiced_index = i

        for ln in lines:
            account_tag_ids, account_name = self._get_account_details(ln)
            if account_tag_ids:
                # The tags are formatted to end with the code. So in the loop we get this code and concatenate to L10N_LU_TAX
                # Which will be used in the appendix A of the report.
                matching = ["L10N_LU_TAX_" + tag.get_external_id()[tag.id].split("_")[-1] for tag in account_tag_ids]
                for code in matching:
                    vat_excluded = ln['columns'][excluded_index]['no_format']
                    vat_invoiced = ln['columns'][invoiced_index]['no_format']
                    if code == 'L10N_LU_TAX_361':
                        expenditures_table.append({
                            'year': year,
                            'company_id': self.env.company.id,
                            'report_section_411': account_name[:31].rstrip(), # The maximum length for the "Detail of Expense" field is 30 characters
                            'report_section_412': vat_excluded,
                            'report_section_413': vat_invoiced,
                        })
                    elif result and f'{code}_vat_excluded' in result and f'{code}_vat_invoiced' in result:
                        result[f'{code}_vat_excluded'] += vat_excluded
                        result[f'{code}_vat_invoiced'] += vat_invoiced

        return result, expenditures_table

    def _report_custom_engine_l10n_lu_annual_vat(self, expressions, options, date_scope, current_groupby, next_groupby, offset=0, limit=None, warnings=None):
        # precompute values based on the account codes mapping
        grouped_tax_report = self.env.ref('account.generic_tax_report_tax_account')
        annex_options = grouped_tax_report.get_options(options)
        lines = grouped_tax_report._get_lines(annex_options)
        date_to = options['date']['date_to']
        year = fields.Date.from_string(date_to).year
        result = {}
        for expression in expressions:
            result.update({
                f'{expression.report_line_id.code}_vat_excluded': 0.0,
                f'{expression.report_line_id.code}_vat_invoiced': 0.0,
            })
        result, _expenditures_table = self._get_precomputed_lines(year=year, lines=lines, annex_options=annex_options, result=result)

        return result


class LuReportAppendixOpEx(models.AbstractModel):
    _name = 'l10n_lu.appendix.opex.tax.report.handler'
    _inherit = 'account.tax.report.handler'
    _description = 'Custom Handler for the Appendix to Operational Expenditures of the LU Annual Tax Report'

    def _get_custom_display_config(self):
        return {
            'components': {
                'AccountReportLineName': 'l10n_lu_reports.AppendixLineName',
            },
        }

    def action_open_appendix_view(self, options, params=None):
        date_to = options['date']['date_to']
        year = fields.Date.from_string(date_to).year
        domain = [
            ('company_id', 'in', [comp['id'] for comp in options['companies']]),
            ('year', '=', year),
        ]
        if params and params.get('recompute'):
            grouped_tax_report = self.env.ref('account.generic_tax_report_tax_account')
            annex_options = grouped_tax_report.get_options(options)
            lines = grouped_tax_report._get_lines(annex_options)
            _result, expenditures_table = self.env['l10n_lu.appendix.a.tax.report.handler']._get_precomputed_lines(year, lines, annex_options)
            # unlink existing appendix lines because we are recomputing from scratch
            # and there is no way to know what has been already computed before and what was manually created
            self.env['l10n_lu_reports.report.appendix.expenditures'].search(domain).unlink()
            self.env['l10n_lu_reports.report.appendix.expenditures'].create(expenditures_table)

        return {
            'name': _("Appendix to the Operational Expenditures"),
            'type': 'ir.actions.act_window',
            'views': [(
                self.env.ref('l10n_lu_reports.l10n_lu_yearly_tax_report_appendix_view_tree').id,
                'list',
            )],
            'res_model': 'l10n_lu_reports.report.appendix.expenditures',
            'context': {'year': year},
            'domain': domain,
            'target': 'current',
        }

    def _dynamic_lines_generator(self, report, options, all_column_groups_expression_totals, warnings=None):
        # it only makes sense to compare appendix lines based on the year
        grouped_columns = defaultdict(list)
        for column_group_key, column_group_options in report._split_options_per_column_group(options).items():
            date_to = column_group_options['date']['date_to']
            year = str(fields.Date.from_string(date_to).year)
            grouped_columns[year].append((column_group_key, column_group_options)) # grouping to avoid duplicate computation later

        appendix_lines = self.env['l10n_lu_reports.report.appendix.expenditures'].search_read(
            domain=[
                ('company_id', 'in', [comp['id'] for comp in options['companies']]),
                ('year', 'in', list(grouped_columns.keys())),
            ],
            fields=['id', 'report_section_411', 'report_section_412', 'report_section_413', 'year']
        )

        totals_by_column_group = {
            column_group_key: {
                'vat_excluded': 0.0,
                'vat_invoiced': 0.0,
            }
            for column_group_key in options['column_groups']
        }

        lines = []
        if options['export_mode'] != 'print': # don't print "add lines" in the pdf report
            # this is a line that just has an action that opens the appendix tree view
            # to add as many appendix lines as the user needs
            action_line = self._get_appendix_line(report, options, {}, _('Add appendix lines'))
            action_line[1]['unfoldable'] = True
            lines.append(action_line)

        for appendix_line in appendix_lines:
            values = {}
            year = appendix_line['year']
            for column_group_key, column_group_options in grouped_columns[year]:
                values[column_group_key] = {
                    'vat_excluded': appendix_line['report_section_412'],
                    'vat_invoiced': appendix_line['report_section_413'],
                }
            lines.append(self._get_appendix_line(report, column_group_options, values,
                appendix_line['report_section_411'], level=2, line_id=appendix_line["id"]))
            self._update_total_values(totals_by_column_group, column_group_options, values)

        lines.append(self._get_appendix_line(report, options, totals_by_column_group,
            _('Total to be carried forward to line 43'), is_line_total=True))
        return lines

    def _get_appendix_line(self, report, options, column_vals, name, level=1, line_id=None, is_line_total=False):
        markup = 'total' if is_line_total else ''
        column_values = []

        for column in options['columns']:
            vals = column_vals.get(column['column_group_key'], {})
            col_val = vals.get(column['expression_label'])
            column_values.append(
                report._build_column_dict(col_val, column, options=options, digits=2)
            )

        vals = {
            'id': report._get_generic_line_id('l10n_lu_reports.report.appendix.expenditures', line_id, markup=markup),
            'name': name,
            'level': level,
            'columns': column_values,
        }
        if is_line_total:
            vals['code'] = 'L10N_LU_TAX_43'
        return (0, vals)

    def _update_total_values(self, totals_by_column_group, options, values):
        for column_group_key in options['column_groups']:
            for key in totals_by_column_group[column_group_key]:
                totals_by_column_group[column_group_key][key] += values.get(column_group_key, {}).get(key) or 0.0
