# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.tests import HttpCase, tagged, users


@tagged('post_install', '-at_install')
class AppointmentHrRecruitmentTest(HttpCase):

    @users('admin')
    def test_tour_default_opportunity_propagation(self):
        """ Test that the applicant is correctly propagated to the appointment invitation created """
        self.env.user.tz = "Europe/Brussels"
        dep_rd = self.env['hr.department'].create({
            'name': 'Research & Development',
        })
        job_developer = self.env['hr.job'].create({
            'name': 'Test Job',
            'department_id': dep_rd.id,
            'no_of_recruitment': 5,
        })
        applicant = self.env['hr.applicant'].sudo().create({
            'name': 'Test Applicant',
            'partner_name': 'Test Applicant',
            'job_id': job_developer.id,
        })
        appointment_type = self.env['appointment.type'].create({'name': "Test AppointmentHrRecruitment"})
        self.start_tour('/web', 'appointment_hr_recruitment_tour', login='admin')
        appointment_invite = self.env['appointment.invite'].search([('appointment_type_ids', 'in', appointment_type.ids)])
        self.assertTrue(appointment_invite.applicant_id == applicant)
