#-*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

{
    'name': 'Belgian Payroll - Attendance',
    'countries': ['be'],
    'category': 'Human Resources/Employees',
    'sequence': 95,
    'summary': 'Manage extra hours for your hourly paid employees for belgian payroll',
    'installable': True,
    'auto_install': True,
    'depends': [
        'hr_payroll_attendance',
        'l10n_be_hr_payroll',
    ],
    'license': 'OEEL-1',
}
