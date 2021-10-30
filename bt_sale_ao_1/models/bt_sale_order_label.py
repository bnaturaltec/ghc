# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class bt_sale_order_label(models.Model):
    _name = "bt.sale.order.label"
    _description = "BT - Sale Order - Label"
    _rec_name = "name"
    _check_company_auto = True

    name = fields.Char(string='Name', required=True)

    company_id = fields.Many2one('res.company', required=True, 
                    index=True, default=lambda self: self.env.company)

    active = fields.Boolean(string='Active', default=True,
                                copy=False)

