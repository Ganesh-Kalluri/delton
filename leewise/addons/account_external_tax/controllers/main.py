# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise.http import route
from leewise.addons.account.controllers.portal import CustomerPortal


class CustomerPortalExternalTax(CustomerPortal):
    @route()
    def portal_my_invoice_detail(self, *args, **kw):
        response = super().portal_my_invoice_detail(*args, **kw)
        if 'invoice' not in response.qcontext:
            return response

        response.qcontext['invoice']._get_and_set_external_taxes_on_eligible_records()

        return response
