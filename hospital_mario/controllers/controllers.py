# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalMario(http.Controller):
#     @http.route('/hospital_mario/hospital_mario', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_mario/hospital_mario/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_mario.listing', {
#             'root': '/hospital_mario/hospital_mario',
#             'objects': http.request.env['hospital_mario.hospital_mario'].search([]),
#         })

#     @http.route('/hospital_mario/hospital_mario/objects/<model("hospital_mario.hospital_mario"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_mario.object', {
#             'object': obj
#         })

