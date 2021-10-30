# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class bt_sale_order(models.Model):  
    _inherit = "sale.order"

    driver = fields.Many2one('bt.sale.order.driver', string='Driver')
    label = fields.Many2one('bt.sale.order.label', string='Label')
    