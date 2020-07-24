# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
log = logging.getLogger(__name__)

class State(models.Model):
    _name = 'hc.state'
    _order = 'sequence'
    name = fields.Char(string='Nombre')
    orders = fields.One2many('sale.order', 'order_state', string='ordenes')
    sequence = fields.Integer(string='sequence', default = 1)
