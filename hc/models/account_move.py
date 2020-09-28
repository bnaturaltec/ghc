# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
log = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    #warehouse_id = fields.Many2one(string='Almacen',related='stock.warehouse',store = True) 
    warehouse_id = fields.Many2one('stock.warehouse', string="Warehouse",store = True)

    state_id = fields.Char(string='Provincia',related='partner_id.state_id.name', store=True)
    canton_id = fields.Char(string='Canton',related='partner_id.canton_id.name', store=True)
    distrito_id = fields.Char(string='Distrito',related='partner_id.distrito_id.name', store=True)
