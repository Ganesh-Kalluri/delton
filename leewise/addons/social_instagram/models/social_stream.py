# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

import dateutil.parser
import requests

from leewise import models
from werkzeug.urls import url_join


class SocialStreamInstagram(models.Model):
    _inherit = 'social.stream'

    def _apply_default_name(self):
        instagram_streams = self.filtered(lambda s: s.media_id.media_type == 'instagram')
        super(SocialStreamInstagram, (self - instagram_streams))._apply_default_name()

        for stream in instagram_streams:
            stream.write({'name': '%s: %s' % (stream.stream_type_id.name, stream.account_id.name)})

    def _fetch_instagram_posts(self):
        self.ensure_one()

        posts_endpoint = url_join(
            self.env['social.media']._INSTAGRAM_ENDPOINT,
            '%s/media' % self.account_id.instagram_account_id)
        response = requests.get(posts_endpoint,
            params={
                'access_token': self.account_id.instagram_access_token,
                'fields': 'id,comments_count,like_count,username,permalink,timestamp,caption,media_url'
            },
            timeout=5
        ).json()

        if 'data' not in response:
            self.account_id._action_disconnect_accounts(response)
            return False

        posts_to_create = []

        existing_posts = {
            post.instagram_post_id: post
            for post in self.env['social.stream.post'].search([
                ('stream_id', '=', self.id)])}

        for post in response['data']:
            values = {
                'author_name': post.get('username'),
                'instagram_comments_count': post.get('comments_count', 0),
                'instagram_facebook_author_id': self.account_id.instagram_facebook_account_id,
                'instagram_likes_count': post.get('like_count', 0),
                'instagram_post_id': post.get('id'),
                'instagram_post_link': post.get('permalink'),
                'message': post.get('caption'),
                'published_date': dateutil.parser.parse(post.get('timestamp'), ignoretz=True),
                'stream_id': self.id,
            }

            media_url = post.get('media_url')
            if values['instagram_post_id'] in existing_posts:
                if media_url:
                    values['stream_post_image_ids'] = [(5, 0, 0), (0, 0, {'image_url': media_url})]
                existing_posts[values['instagram_post_id']].sudo().write(values)
            else:
                if media_url:
                    values['stream_post_image_ids'] = [(0, 0, {'image_url': media_url})]
                posts_to_create.append(values)

        if posts_to_create:
            self.env['social.stream.post'].sudo().create(posts_to_create)

        return bool(posts_to_create)

    def _fetch_stream_data(self):
        if self.media_id.media_type != 'instagram':
            return super(SocialStreamInstagram, self)._fetch_stream_data()

        if self.stream_type_id.stream_type == 'instagram_posts':
            return self._fetch_instagram_posts()
