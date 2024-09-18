# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details

from datetime import datetime
from dateutil.relativedelta import relativedelta

from leewise import Command
from leewise.exceptions import AccessError
from leewise.tests import tagged
from leewise.tests.common import users
from leewise.tools import float_compare

from .common import TestIndustryFsmCommon

@tagged('post_install', '-at_install')
class TestFsmTaskAnalysis(TestIndustryFsmCommon):
    def test_tasks_analysis(self):
        self.task.write({
            'user_ids': [Command.set([self.george_user.id])],
            'allocated_hours': 16,
            'timesheet_ids': [
                Command.create({
                    'name': '/',
                    'employee_id': self.employee_user.id,
                    'unit_amount': 4,
                })
            ]
        })
        self.assertEqual(self.task.effective_hours, 4)
        self.assertEqual(self.task.remaining_hours, 12)
        self.assertEqual(self.task.progress, 25)

        self.assertFalse(self.task.working_days_close)
        self.assertFalse(self.task.working_days_open)
        self.task.action_fsm_validate()
        self.task.write({
            'date_end': datetime.today() + relativedelta(months=1),
            'date_assign': datetime.today() + relativedelta(months=2, days=3),
        })

        # As the value of working_days_close might change depending on the calendar (holidays, weekend)
	    # as well as the time of execution, we use an assertTrue instead of an assertEqual.
        self.assertTrue(self.task.working_days_close)
        self.assertTrue(self.task.working_hours_close)
        self.assertTrue(self.task.working_days_open)
        self.assertTrue(self.task.working_hours_open)

        values = self.task.read(['remaining_hours', 'progress', 'allocated_hours', 'effective_hours', 'working_days_close', 'working_hours_close', 'working_days_open', 'working_hours_open'])[0]
        # flush before accessing an SQL view...
        self.env.flush_all()
        task_report = self.env['report.project.task.user'].search_read([('project_id', '=', self.fsm_project.id), ('task_id', '=', self.task.id)], ['remaining_hours', 'progress', 'allocated_hours', 'effective_hours', 'working_days_close', 'working_hours_close', 'working_days_open', 'working_hours_open'])[0]
        for field_name, actual_value in task_report.items():
            expected_value = values[field_name]
            self.assertEqual(float_compare(actual_value, expected_value, 2), 0, f'The value of {field_name} in the report should equal to the one in the task')

    @users('Base user')
    def test_base_user_no_read_report_project_task_user(self):
        with self.assertRaises(AccessError):
            self.env['report.project.task.user'].with_user(self.env.user).search([('project_id', '=', self.fsm_project.id)])

    @users('Project user', 'Project admin', 'Fsm user')
    def test_user_can_read_report_project_task_user(self):
        self.env['report.project.task.user'].with_user(self.env.user).search([('project_id', '=', self.fsm_project.id)])

    @users('Base user', 'Project user', 'Project admin')
    def test_no_read_report_project_task_user_fsm(self):
        with self.assertRaises(AccessError):
            self.env['report.project.task.user.fsm'].with_user(self.env.user).search([('project_id', '=', self.fsm_project.id)])

    @users('Fsm user')
    def test_fsm_user_can_read_report_project_task_user_fsm(self):
        self.env['report.project.task.user.fsm'].with_user(self.env.user).search([('project_id', '=', self.fsm_project.id)])
