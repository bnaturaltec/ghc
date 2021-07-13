# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class bt_account_payment(models.Model):  
    _inherit = "account.payment"

    ref_payment = fields.Char(string='Referencia')
    