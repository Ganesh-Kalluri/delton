# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_pdf_and_send_invoice_vals(self, template, **kwargs):
        # EXTENDS account
        vals = super()._get_pdf_and_send_invoice_vals(template, **kwargs)
        vals['checkbox_send_by_post'] = False
        return vals
