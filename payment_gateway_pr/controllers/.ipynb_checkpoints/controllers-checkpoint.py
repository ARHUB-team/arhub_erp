 -*- coding: utf-8 -*-
 from odoo import http


 class PaymentGatewayPr(http.Controller):
     @http.route('/payment_gateway_pr/payment_gateway_pr', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/payment_gateway_pr/payment_gateway_pr/objects', auth='public')
     def list(self, **kw):
         return http.request.render('payment_gateway_pr.listing', {
             'root': '/payment_gateway_pr/payment_gateway_pr',
             'objects': http.request.env['payment_gateway_pr.payment_gateway_pr'].search([]),
         })

     @http.route('/payment_gateway_pr/payment_gateway_pr/objects/<model("payment_gateway_pr.payment_gateway_pr"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('payment_gateway_pr.object', {
             'object': obj
         })
