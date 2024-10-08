# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models, _
from leewise.exceptions import AccessError


class Digest(models.Model):
    _inherit = 'digest.digest'

    kpi_helpdesk_tickets_closed = fields.Boolean('Tickets Closed')
    kpi_helpdesk_tickets_closed_value = fields.Integer(compute='_compute_kpi_helpdesk_tickets_closed_value')

    def _compute_kpi_helpdesk_tickets_closed_value(self):
        if not self.env.user.has_group('helpdesk.group_helpdesk_user'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))

        self._calculate_company_based_kpi(
            'helpdesk.ticket',
            'kpi_helpdesk_tickets_closed_value',
            date_field='close_date',
        )

    def _compute_kpis_actions(self, company, user):
        res = super(Digest, self)._compute_kpis_actions(company, user)
        res['kpi_helpdesk_tickets_closed'] = 'helpdesk.helpdesk_team_dashboard_action_main&menu_id=%s' % self.env.ref('helpdesk.menu_helpdesk_root').id
        return res
