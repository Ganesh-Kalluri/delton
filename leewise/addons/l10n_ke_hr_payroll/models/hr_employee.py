# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, fields, models, _
from leewise.exceptions import UserError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    l10n_ke_mortgage = fields.Monetary(string="Mortgage Interest", currency_field='currency_id', groups="hr.group_hr_user")
    l10n_ke_kra_pin = fields.Char(string="KRA PIN", help="KRA PIN provided by the KRA", groups="hr.group_hr_user")
    l10n_ke_nssf_number = fields.Char(string="NSSF Number", help="NSSF Number provided by the NSSF", groups="hr.group_hr_user")
    l10n_ke_nhif_number = fields.Char("NHIF Number", groups="hr.group_hr_user")
    l10n_ke_pin = fields.Char(string="Employee's PIN", groups="hr.group_hr_user")
    l10n_ke_disabled = fields.Boolean(string="Disability", help="If the employee is declared disabled by law", groups="hr.group_hr_user")
    l10n_ke_helb_number = fields.Char(string="HELB Number", groups="hr.group_hr_user")

    @api.constrains('l10n_ke_mortgage')
    def _check_l10n_ke_mortgage(self):
        max_amount_yearly = self.env['hr.rule.parameter'].sudo()._get_parameter_from_code('l10n_ke_max_mortgage', raise_if_not_found=False)
        for employee in self:
            if max_amount_yearly and employee.l10n_ke_mortgage > max_amount_yearly:
                raise UserError(_('The mortgage interest cannot exceed %s Ksh yearly.', max_amount_yearly))

    @api.constrains('l10n_ke_nssf_number', 'country_id')
    def _check_l10n_ke_nssf_number(self):
        for employee in self:
            number = employee.l10n_ke_nssf_number
            if number and (not number.isdigit() or len(number) > 10 or len(number) < 9):
                raise UserError(_('The NSSF number must be a nine or ten digits number.'))
