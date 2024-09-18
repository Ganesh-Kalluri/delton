# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _get_countries_allowing_tax_representative(self):
        rslt = super()._get_countries_allowing_tax_representative()
        rslt.add('NL')
        return rslt
