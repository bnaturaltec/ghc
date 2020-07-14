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

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    order_state = fields.Many2one('hc.state', string='Estado Interno',default = lambda self: self.env['hc.state'].search([("sequence","=",0)]) )
    phone = fields.Char(string='Telefono',related='partner_id.phone',store = True) 
    movil = fields.Char(string='Celular',related='partner_id.mobile',store = True) 
    address = fields.Char(compute='_compute_address',string='Direccion')
    confirmador = fields.Many2one('res.users', string='Confirmador')


    @api.depends('partner_id')
    def _compute_address(self):
         
         country = ''
         if self.partner_id.country_id.name:
             country = ",{}".format(self.partner_id.country_id.name)
         state = ''
         if self.partner_id.state_id.name:
            state = ",{}".format(self.partner_id.state_id.name)
        
         self.address ="{0} {1} {2} {3} {4} {5}".format(self.partner_id.street or '',self.partner_id.street2 or '',
         self.partner_id.city or '',state,self.partner_id.zip or '',country)
    '''
    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)
        if(vals.get('order_state')):
            state = self.env['hc.state'].search([("id","=",vals['order_state'])])
            body = "Creada con estado: {0}".format(state.name)
            self.write_chatter(body)
        return result
    '''
    def write(self, vals):
        for s in self:
            before_state = s.order_state.name
            before_confirmador = s.confirmador
            result = super(SaleOrder, s).write(vals)
            
            body = ''
            if(vals.get('confirmador')):
                if before_confirmador:
                    body += "Confirmador {0}  se cambio por -> {1} <br/>".format(before_confirmador.name,s.confirmador.name)
                else:
                    log.info(" confirmador --> {} ".format(s.confirmador))
                    body += "Nuevo Confirmador: {0} <br/>".format(s.confirmador.name)
        
            if(vals.get('order_state')):
              state = s.env['hc.state'].search([("id","=",vals['order_state'])])
              if before_state:
                body += "Estado {0}  se cambio por -> {1}".format(before_state,state.name)
              else:
                body += "Nuevo estado: {0}".format(state.name)
            
            if body:
                s.write_chatter(body)
        

    
    def set_confirmador(self):
        before_confirmador = self.confirmador
        if before_confirmador:
            self.confirmador = self.env.user
            body = "Confirmador {0}  se cambio por -> {1}".format(before_confirmador.name,self.confirmador.name)
        else:
            self.confirmador = self.env.user
            log.info(" confirmador --> {} ".format(self.confirmador))
            body = "Nuevo Confirmador: {0}".format(self.confirmador.name)
        self.write_chatter(body)

        
    def write_chatter(self,body):
            log.info('--> write_chatter')
            chatter = self.env['mail.message']
            chatter.create({
                            'res_id': self.id,
                            'model':'sale.order',
                            'body': body,
                        })

    
        



    

    
