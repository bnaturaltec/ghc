# -*- coding: utf-8 -*-
from odoo import http

# class Hc(http.Controller):
#     @http.route('/hc/hc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc/hc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc.listing', {
#             'root': '/hc/hc',
#             'objects': http.request.env['hc.hc'].search([]),
#         })

#     @http.route('/hc/hc/objects/<model("hc.hc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc.object', {
#             'object': obj
#         })