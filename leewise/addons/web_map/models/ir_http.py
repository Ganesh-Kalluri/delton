# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        if self.env.user.has_group('base.group_user'):
            result.update(
                map_box_token = self.env['ir.config_parameter'].sudo().get_param('web_map.token_map_box',False)
            )
        return result
