# -*- coding: utf-8 -*-
# from odoo import http


# class Reto-odoo(http.Controller):
#     @http.route('/reto-odoo/reto-odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reto-odoo/reto-odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reto-odoo.listing', {
#             'root': '/reto-odoo/reto-odoo',
#             'objects': http.request.env['reto-odoo.reto-odoo'].search([]),
#         })

#     @http.route('/reto-odoo/reto-odoo/objects/<model("reto-odoo.reto-odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reto-odoo.object', {
#             'object': obj
#         })
