# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

import json
import logging

log = logging.getLogger(__name__)

class UtmDidNumbers(http.Controller):
    @http.route('/freepbx/', auth='public')
    def index(self, **kw):
        log.info("\n=======XYZinicio\n")
        return "Hello, world GET3"
    
    @http.route('/freepbx/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('utm_did_numbers.listing', {
            'root': '/utm_did_numbers/utm_did_numbers',
            'objects': http.request.env['utm.did_numbers'].search([]),
        })

    @http.route('/freepbx/<string:data>/', auth='public', csrf=False)
    def object(self, data, **kw):
        
        log.info(1593495230)
        odoo_data = request.httprequest.data.decode('utf-8')
        odoo_data_json = json.loads(odoo_data)
        odoo_data_token = odoo_data_json['odoo_token']
        
        model_odoo_system_parameters = http.request.env['ir.config_parameter']
        model_odoo_system_parameters_record = model_odoo_system_parameters.sudo().search([("key","=","voip.curl_token")])
        
        if str(odoo_data_token) == str(model_odoo_system_parameters_record.value):
            log.info("\nSI ES IGUAL EL ODOO DATA TOKEN")
        else:
            error_message = "\nTOKEN NO VALIDO, CONFIGURAR/AGREGAR EN ODOO SYSTEM PARAMETERS, VARIABLE voip.curl Y EL ID"
            log.info(error_message)
            return error_message
        
        log.info(1593495708)
        if data:
            data = data.split("&")
         
        did_number = False
        phone = False
        for data_record in data:
            data_record_list = data_record.split("=")
            if data_record_list[0] == "agi_dnid":
                did_number = data_record_list[1]
            if data_record_list[0] == "agi_callerid":
                phone = data_record_list[1]
        
        if phone and did_number:
            model = http.request.env['utm.did_numbers']
            did_number_data = model.sudo().search([("did_number","=",did_number)])

        else:
            log.info("\n==== Phone or DID Number empty =====\n")
            return "\n==== Phone or DID Number empty =====\n"
        
        response = "No Data"
        record_id = "====DID No Asociado - No se creó Registro para: " + str(phone) + " llamando al: " + str(did_number)
        
        if did_number_data:
            
            if did_number_data.campaign_id:
                campaign_name = did_number_data.campaign_id.name        
            else:
                campaign_name = "DID " + str(did_number) + " no asociado a ninguna campaña"
            
            crm_model=http.request.env['crm.lead']
            
            if did_number_data.country_id.name == "Costa Rica":
                
                phone_country_code = phone[0:3]
                if str(phone_country_code) != "506":
                    phone = "+506" + str(phone)
                if str(phone_country_code) == "506":
                    phone = "+" + str(phone)
                
            record_id = crm_model.sudo().create({
                'name': campaign_name,
                'company_id': did_number_data.company_id.id,
                'country_id': did_number_data.country_id.id,
                'phone' : phone,
                'user_id': False,
                'team_id': False,
                'campaign_id': did_number_data.campaign_id.id,
                'medium_id': did_number_data.medium_id.id,
                'source_id': did_number_data.source_id.id,
            })

        response = "\nRecord ID Created: " + str(record_id)
        
        log.info(response)
        return response