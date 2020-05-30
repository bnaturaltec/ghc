# -*- coding: utf-8 -*-

from odoo import models, fields, api


class utm_did_numbers(models.Model):
    _name = 'utm.did_numbers'
    _description = 'utm.did_numbers'

    did_number = fields.Char(string='Numero DID')
    source = fields.Many2one('utm.source', string='Origen')
    medium = fields.Many2one('utm.medium', string='Medio')
    campaign = fields.Many2one('utm.campaign', string='Campaña')
    company = fields.Many2one('res.company', string='Companía')

