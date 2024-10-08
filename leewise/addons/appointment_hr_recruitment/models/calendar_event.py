# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields, api, _

class CalendarEventRecruitment(models.Model):
    _inherit = 'calendar.event'

    applicant_id = fields.Many2one(related="appointment_invite_id.applicant_id", readonly=False, store=True)
