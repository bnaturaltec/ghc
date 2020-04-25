odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    var PhoneCallDetails = require('voip.PhoneCallDetails');
    
    PhoneCallDetails = PhoneCallDetails.extend({
        events: _.extend({},  PhoneCallDetails.events, {
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
         /**
         * TODO: reduce coupling between PhoneCallDetails & PhoneCall
         *
         * @override
         * @param {voip.PhoneCallTab} parent
         * @param {voip.PhoneCall} phoneCall
         */
        init(parent, phoneCall) {
            this._super(...arguments);
        },
        /**
         * @override
         */
        start() {
            this._super(...arguments);
        },
           /**
         * @private
         * @param {MouseEvent} ev
         * @return {Promise}
         */
        _onToSaleOrderClick: function (ev) {
            console.log("click");
            ev.preventDefault();
            if (this.partnerId) {
                this.do_action({
                    type: 'ir.actions.act_window',
                    res_model: "sale.order",
                    views: [[false, 'form']],
                    target: 'current',
                    context: {
                        default_partner_id: this.partnerId,
                    },
                });
            } else {
                this.do_action({
                    type: 'ir.actions.act_window',
                    res_model: "sale.order",
                    views: [[false, 'form']],
                    target: 'current',
                    context: {},
                });
            }
        },

    });
  

});