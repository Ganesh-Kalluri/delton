# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

{
    'name': 'United States - Accounting',
    'website': 'https://www.leewise.in/documentation/17.0/applications/finance/fiscal_localizations.html',
    'icon': '/account/static/description/l10n.png',
    'countries': ['us'],
    'version': '1.1',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
United States - Chart of accounts.
==================================
    """,
    'depends': ['account'],
    'data': [
        'data/res_company_data.xml',
        'views/res_partner_bank_views.xml'
    ],
    'license': 'LGPL-3',
}
