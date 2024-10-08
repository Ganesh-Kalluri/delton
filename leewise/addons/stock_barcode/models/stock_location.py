# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, api


class Location(models.Model):
    _inherit = 'stock.location'
    _barcode_field = 'barcode'

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        domain = self.env.company.nomenclature_id._preprocess_gs1_search_args(domain, ['location', 'location_dest'])
        return super()._search(domain, offset=offset, limit=limit, order=order, access_rights_uid=access_rights_uid)

    @api.model
    def _get_fields_stock_barcode(self):
        return ['barcode', 'display_name', 'name', 'parent_path', 'usage']
