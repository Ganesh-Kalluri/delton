# coding: utf-8
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, models


class Onboarding(models.Model):
    _inherit = 'onboarding.onboarding'

    # Appointment Onboarding
    @api.model
    def action_close_panel_appointment(self):
        self.action_close_panel('appointment.onboarding_onboarding_appointment')
