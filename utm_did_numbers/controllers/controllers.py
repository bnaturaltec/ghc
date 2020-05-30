# -*- coding: utf-8 -*-
# from odoo import http


# class UtmDidNumbers(http.Controller):
#     @http.route('/utm_did_numbers/utm_did_numbers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/utm_did_numbers/utm_did_numbers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('utm_did_numbers.listing', {
#             'root': '/utm_did_numbers/utm_did_numbers',
#             'objects': http.request.env['utm_did_numbers.utm_did_numbers'].search([]),
#         })

#     @http.route('/utm_did_numbers/utm_did_numbers/objects/<model("utm_did_numbers.utm_did_numbers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('utm_did_numbers.object', {
#             'object': obj
#         })
