# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.api import Environment
import leewise.tests
from leewise.tools import html2plaintext

@leewise.tests.tagged('post_install', '-at_install')
class TestWebsiteHrRecruitmentForm(leewise.tests.HttpCase):
    def test_tour(self):
        job_guru = self.env['hr.job'].create({
            'name': 'Guru',
            'is_published': True,
        })
        job_intern = self.env['hr.job'].create({
            'name': 'Internship',
            'is_published': True,
        })
        self.start_tour(self.env['website'].get_client_action_url('/jobs'), 'website_hr_recruitment_tour_edit_form', login='admin')

        with leewise.tests.RecordCapturer(self.env['hr.applicant'], []) as capt:
            self.start_tour("/", 'website_hr_recruitment_tour')

        # check result
        self.assertEqual(len(capt.records), 2)

        guru_applicant = capt.records[0]
        self.assertEqual(guru_applicant.partner_name, 'John Smith')
        self.assertEqual(guru_applicant.email_from, 'john@smith.com')
        self.assertEqual(guru_applicant.partner_mobile, '118.218')
        self.assertEqual(html2plaintext(guru_applicant.description), '### [GURU] HR RECRUITMENT TEST DATA ###')
        self.assertEqual(guru_applicant.job_id, job_guru)

        internship_applicant = capt.records[1]
        self.assertEqual(internship_applicant.partner_name, 'Jack Doe')
        self.assertEqual(internship_applicant.email_from, 'jack@doe.com')
        self.assertEqual(internship_applicant.partner_mobile, '118.712')
        self.assertEqual(html2plaintext(internship_applicant.description), '### HR [INTERN] RECRUITMENT TEST DATA ###')
        self.assertEqual(internship_applicant.job_id, job_intern)
