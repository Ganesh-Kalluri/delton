# Part of Leewise. See LICENSE file for full copyright and licensing details.

import leewise.tests
from leewise import Command
from leewise.addons.base.tests.common import HttpCaseWithUserDemo


@leewise.tests.tagged('post_install', '-at_install')
class TestUi(HttpCaseWithUserDemo):

    def test_01_mail_tour(self):
        self.start_tour("/web", 'discuss_channel_tour', login="admin")

    def test_02_mail_create_channel_no_mail_tour(self):
        self.env['res.users'].create({
            'email': '', # User should be able to create a channel even if no email is defined
            'groups_id': [Command.set([self.ref('base.group_user')])],
            'name': 'Test User',
            'login': 'testuser',
            'password': 'testuser',
        })
        self.start_tour("/web", 'discuss_channel_tour', login='testuser')
