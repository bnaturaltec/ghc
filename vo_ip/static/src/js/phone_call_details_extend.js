odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    var Phone = require('voip.PhoneCallDetails');
    
    console.log("este es el widget",Phone);
    const core = require('web.core');
    const session = require('web.session');
    const Widget = require('web.Widget');

    const QWeb = core.qweb;
    const _t = core._t;
  
    Phone.include({
        events: _.include({}, Phone.prototype.events, {
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


    });
  
    
    console.log("override",Phone)

});