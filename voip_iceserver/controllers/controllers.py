# -*- coding: utf-8 -*-
from odoo import http

# class VoipCustom(http.Controller):
#     @http.route('/voip_custom/voip_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/voip_custom/voip_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('voip_custom.listing', {
#             'root': '/voip_custom/voip_custom',
#             'objects': http.request.env['voip_custom.voip_custom'].search([]),
#         })

#     @http.route('/voip_custom/voip_custom/objects/<model("voip_custom.voip_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('voip_custom.object', {
#             'object': obj
#         })