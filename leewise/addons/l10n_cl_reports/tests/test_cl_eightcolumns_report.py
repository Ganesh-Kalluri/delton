# -*- coding: utf-8 -*-
from leewise.addons.account_reports.tests.common import TestAccountReportsCommon
from leewise import fields
from leewise.tests import tagged


@tagged('post_install_l10n', 'post_install', '-at_install')
class TestClEightColumnsReport(TestAccountReportsCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref='cl'):
        super().setUpClass(chart_template_ref=chart_template_ref)
        cls.partner_a.write({
            'country_id': cls.env.ref('base.cl').id,
            'l10n_cl_sii_taxpayer_type': '1',
            'vat': 'CL762012243',
        })

        invoice = cls.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': cls.partner_a.id,
            'invoice_date': '2017-01-01',
            'date': '2017-01-01',
            'invoice_line_ids': [(0, 0, {
                'product_id': cls.product_a.id,
                'tax_ids': [(6, 0, cls.company_data['default_tax_sale'].ids)],
                'quantity': 1.0,
                'price_unit': 1000.0,
            })],
        })
        invoice.action_post()

    def test_whole_report(self):
        report = self.env.ref('l10n_cl_reports.cl_eightcolumns_report')
        options = self._generate_options(report, fields.Date.from_string('2017-01-01'), fields.Date.from_string('2017-12-31'))

        # pylint: disable=bad-whitespace
        self.assertLinesValues(
            report._get_lines(options),
            # pylint: disable=C0326
            #   Account                                 Debit      Credit   Debitor  Creditor    Active  Passive Loss    Gain
            [   0,                                       1,         2,       3,       4,          5,      6,       7,        8],
            [
                ('110310 Customers',                1190.0,         0,  1190.0,       0,     1190.0,      0,       0,        0),
                ('210710 VAT Tax Debit',                 0,     190.0,       0,   190.0,          0,  190.0,       0,        0),
                ('310110 Consulting revenues',           0,    1000.0,       0,  1000.0,          0,      0,       0,   1000.0),
                ('Subtotal',                        1190.0,    1190.0,  1190.0,  1190.0,     1190.0,   190.0,      0,   1000.0),
                ('Profit and Loss',                      0,         0,       0,       0,          0,  1000.0,  1000.0,       0),
                ('Total',                           1190.0,    1190.0,  1190.0,  1190.0,     1190.0,  1190.0,  1000.0,  1000.0),
            ],
            options,
        )
