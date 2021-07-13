# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class bt_account_payment_register(models.TransientModel):  
    _inherit = "account.payment.register"

    ref_payment = fields.Char(string='Referencia')

    def get_payments_vals(self):
        resp = super(bt_account_payment_register, self).get_payments_vals()
        for x in resp:
            x["ref_payment"] = self.ref_payment
        return resp
    