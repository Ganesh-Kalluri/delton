# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import http
from leewise.http import request


class AccountInvoiceExtractController(http.Controller):
    @http.route('/account_invoice_extract/request_done/<string:extract_document_uuid>', type='http', auth='public', csrf=False)
    def request_done(self, extract_document_uuid):
        """ This webhook is called when the extraction server is done processing a request."""
        move_to_update = request.env['account.move'].sudo().search([('extract_document_uuid', '=', extract_document_uuid),
                                                                    ('extract_state', 'in', ['waiting_extraction', 'extract_not_ready']),
                                                                    ('state', '=', 'draft')])
        for move in move_to_update:
            move._check_ocr_status()
        return 'OK'
