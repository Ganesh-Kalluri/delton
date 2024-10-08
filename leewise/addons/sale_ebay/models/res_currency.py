# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields


class ResCurrency(models.Model):
    _inherit = "res.currency"

    ebay_available = fields.Boolean("Use on eBay", help="If activated, can be used for eBay.")
