# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class HrLeave(models.Model):
    _name = 'hr.leave'
    _inherit = ['hr.leave', 'documents.mixin']

    def _get_document_folder(self):
        return self.employee_id.company_id.documents_hr_folder

    def _check_create_documents(self):
        return self.employee_id.company_id.documents_hr_settings and super()._check_create_documents()

    def _get_document_owner(self):
        return self.user_id

    def _get_document_partner(self):
        return self.employee_id.work_contact_id
