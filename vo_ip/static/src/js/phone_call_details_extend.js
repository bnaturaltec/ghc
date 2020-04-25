odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    const Phone = require('voip.PhoneCallDetails')
    
    console.log("este es el widget",Phone)

    console.log("phone.xxxxxx.xxxxxxxxx.xxxxxxx",Phone.extend({
        events: _.extend({}, Phonecall.PhonecallDetails.events, {
            'click .o_dial_activity_done': '_onClickActivityDone',
            'click .o_dial_call_number': '_onClickCallNumber',
            'click .o_dial_activity_cancel': '_onClickCancel',
            'click .o_phonecall_details_close': '_onClickDetailsClose',
            'click .o_dial_email': '_onClickEmail',
            'click .o_dial_log': '_onClickLog',
            'click .o_dial_mute_button': '_onClickMuteButton',
            'click .o_dial_reschedule_activity': '_onClickRescheduleActivity',
            'click .o_dial_to_partner': '_onClickToPartner',
            'click .o_dial_to_record': '_onClickToRecord',
            'click .o_dial_transfer_button': '_onClickTransferButton',
            'click .o_dial_to_sale_order': '_onToSaleOrderClick',
        }),
    }))

    Phone = Phone.extend({
        
        
    });
  
    




});