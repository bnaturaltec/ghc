# -*- coding: utf-8 -*-
from odoo import http

# class VoIp(http.Controller):
#     @http.route('/vo_ip/vo_ip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vo_ip/vo_ip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vo_ip.listing', {
#             'root': '/vo_ip/vo_ip',
#             'objects': http.request.env['vo_ip.vo_ip'].search([]),
#         })

#     @http.route('/vo_ip/vo_ip/objects/<model("vo_ip.vo_ip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vo_ip.object', {
#             'object': obj
#         })