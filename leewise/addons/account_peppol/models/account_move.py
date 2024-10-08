# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, fields, models, _
from leewise.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    peppol_message_uuid = fields.Char(string='PEPPOL message ID')
    peppol_move_state = fields.Selection(
        selection=[
            ('ready', 'Ready to send'),
            ('to_send', 'Queued'),
            ('skipped', 'Skipped'),
            ('processing', 'Pending Reception'),
            ('canceled', 'Canceled'),
            ('done', 'Done'),
            ('error', 'Error'),
        ],
        compute='_compute_peppol_move_state', store=True,
        string='PEPPOL status',
        copy=False,
    )
    peppol_is_demo_uuid = fields.Boolean(compute="_compute_peppol_is_demo_uuid")

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super().fields_get(allfields, attributes)

        # the orm_cache does not contain the new selections added in stable: clear the cache once
        peppol_move_state_field = self._fields['peppol_move_state']
        if ('skipped', "Skipped") not in peppol_move_state_field.get_description(self.env)['selection']:
            self.env['ir.model.fields'].invalidate_model(['selection_ids'])
            self.env['ir.model.fields.selection']._update_selection(
                'account.move', 'peppol_move_state', peppol_move_state_field.selection)
            self.env.registry.clear_cache()
        return res

    def _need_ubl_cii_xml(self):
        self.ensure_one()

        res = super()._need_ubl_cii_xml()
        partner = self.partner_id.commercial_partner_id
        if partner.ubl_cii_format in {False, 'facturx', 'oioubl_201'} or self.company_id.account_peppol_proxy_state != 'active':
            return res
        if not partner.peppol_eas or not partner.peppol_endpoint:
            return False
        if partner.account_peppol_verification_label == 'not_verified':
            partner.button_account_peppol_check_partner_endpoint()
        return res and partner.account_peppol_is_endpoint_valid

    def action_cancel_peppol_documents(self):
        # if the peppol_move_state is processing/done
        # then it means it has been already sent to peppol proxy and we can't cancel
        if any(move.peppol_move_state in {'processing', 'done'} for move in self):
            raise UserError(_("Cannot cancel an entry that has already been sent to PEPPOL"))
        self.peppol_move_state = 'canceled'
        self.send_and_print_values = False

    @api.depends('peppol_message_uuid')
    def _compute_peppol_is_demo_uuid(self):
        for move in self:
            move.peppol_is_demo_uuid = (move.peppol_message_uuid or '').startswith('demo_')

    @api.depends('state')
    def _compute_peppol_move_state(self):
        for move in self:
            if all([
                move.company_id.account_peppol_proxy_state == 'active',
                move.partner_id.account_peppol_is_endpoint_valid,
                move.state == 'posted',
                move.move_type in ('out_invoice', 'out_refund', 'out_receipt'),
                not move.peppol_move_state,
            ]):
                move.peppol_move_state = 'ready'
            else:
                move.peppol_move_state = move.peppol_move_state
