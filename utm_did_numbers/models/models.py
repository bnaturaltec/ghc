# -*- coding: utf-8 -*-

from odoo import models, fields, api


class utm_did_numbers(models.Model):
    _name = 'utm.did_numbers'
    _description = 'utm.did_numbers'

    did_number = fields.Char(string='Numero DID')
    source_id = fields.Many2one('utm.source', string='Origen')
    medium_id = fields.Many2one('utm.medium', string='Medio')
    campaign_id = fields.Many2one('utm.campaign', string='Campaña')
    company_id = fields.Many2one('res.company', string='Companía')
    country_id = fields.Many2one('res.country', string='País')

