# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, models


class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'

    @api.model
    def _get_payment_method_information(self):
        res = super()._get_payment_method_information()
        res['nacha'] = {
            'mode': 'multi',
            'domain': [('type', '=', 'bank')],
            'currency_ids': self.env.ref("base.USD").ids,
            'country_id': self.env.ref("base.us").id
        }
        return res
