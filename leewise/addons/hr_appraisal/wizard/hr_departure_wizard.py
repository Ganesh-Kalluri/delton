# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, fields, models


class HrDepartureWizard(models.TransientModel):
    _inherit = 'hr.departure.wizard'

    cancel_appraisal = fields.Boolean(string="Cancel Future Appraisals", default=True,
        help="Cancel all appraisal after contract end date.")

    def action_register_departure(self):
        super(HrDepartureWizard, self).action_register_departure()
        if self.cancel_appraisal:
            future_appraisals = self.env["hr.appraisal"].search([
                ('employee_id', '=', self.employee_id.id), 
                ('state', 'in', ['new', 'pending'])])
            future_appraisals.action_cancel()
