# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.


from leewise import fields, models


class HrJob(models.Model):
    _inherit = 'hr.job'

    default_contract_id = fields.Many2one('hr.contract', domain="[('company_id', '=', company_id), ('employee_id', '=', False)]", string="Contract Template",
        help="Default contract used to generate an offer. If empty, benefits will be taken from current contract of the employee/nothing for an applicant.")
