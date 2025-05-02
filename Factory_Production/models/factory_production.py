# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class FactoryProduction(models.Model):
    _name = 'factory.production'  
    
     
    
    ref = fields.Char(default='New', readonly=1)  
    factory_name = fields.Char(string='Factory Name',default='Name', required=True)  #اسم المصنع
    product_name = fields.Char(string='Product Name')  #اسم المنتج
    qty_produced = fields.Integer(string='Qty Produced')  #الكمية
    production_date = fields.Date(string='Production Date', default=fields.Date.today) #تاريخ اصدار المنتج
    note = fields.Text(string='Notes',)  #ملاحظات
    production_required = fields.Integer(string='Production Required')  #اجمالي الانتاجاو المطلوب
    rest = fields.Integer(string='The Rest', compute='_compute_rest',)  #الباقي من الكمية
    prepared = fields.Char(string='The Report is Prepared',)  #معد التقرير{تراجع:لو مانت في موديل وحده افضل}
    status = fields.Selection(
        [
            ('completed', 'Completed'),
            ('in_progress', 'In Progress'),
            ('pending', 'Pending'),
            
        ],default="completed" ) #حالة المنتج
    

    
    # @api.depends('') عملية حساب لمعرفة الباقي عن طريق (طرح المطلوب الانتاجي من الكمية)
    def _compute_rest(self):  
        for rec in self:
            rec.rest = rec.production_required - rec.qty_produced
    
    
    @api.model
    def create(self, vals_list): #عملية(رقم التصنيع)
        res = super(FactoryProduction, self).create(vals_list)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('production_seq')
        return res
    