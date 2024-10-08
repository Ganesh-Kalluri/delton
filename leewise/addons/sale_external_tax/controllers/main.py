# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise.http import route
from leewise.addons.sale.controllers.portal import CustomerPortal


class CustomerPortalExternalTax(CustomerPortal):
    @route()
    def portal_order_page(self, *args, **kwargs):
        response = super().portal_order_page(*args, **kwargs)
        if 'sale_order' not in response.qcontext:
            return response

        # Update taxes before customers see their quotation. This also ensures that tax validation
        # works (e.g. customer has valid address, ...). Otherwise, errors will occur during quote
        # confirmation.
        response.qcontext['sale_order']._get_and_set_external_taxes_on_eligible_records()

        return response
