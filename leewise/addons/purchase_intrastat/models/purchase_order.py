# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        if self.partner_id.country_id.intrastat:
            res["intrastat_country_id"] = self.partner_id.country_id.id
        return res
