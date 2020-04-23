odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    //1585936426
    var Phonecall = require('voip.PhoneCallDetails')
    Phonecall.PhoneCallDetails = Phonecall.PhonecallDetails.extend({
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
        /**
         * @constructor
         */
        init: function (parent, phonecall) {
            this._super.apply(this, arguments);
        },


            /**
         * @private
         * @param {MouseEvent} ev
         * @return {Promise}
         */
        async _onClickToPartner(ev) {
            ev.preventDefault();
            let resId = this.partnerId;
            if (!this.partnerId) {
                let domain = [];
                if (this.phoneNumber && this.mobileNumber) {
                    domain = ['|',
                        ['phone', '=', this.phoneNumber],
                        ['mobile', '=', this.mobileNumber]];
                } else if (this.phoneNumber) {
                    domain = ['|',
                        ['phone', '=', this.phoneNumber],
                        ['mobile', '=', this.phoneNumber]];
                } else if (this.mobileNumber) {
                    domain = [['mobile', '=', this.mobileNumber]];
                }
                const ids = await this._rpc({
                    method: 'search_read',
                    model: "res.partner",
                    kwargs: {
                        domain,
                        fields: ['id'],
                        limit: 1,
                    }
                });
                if (ids.length) {
                    resId = ids[0].id;
                }
            }
            if (resId !== undefined) {
                this.do_action({
                    res_id: resId,
                    res_model: "sale.order",
                    target: 'current',
                    type: 'ir.actions.act_window',
                    views: [[false, 'form']],
                    /*context: {
                        default_partner_id: ids[0], 
                    }*/
                });
            } else {
                this.do_action({
                    context: {
                        /*default_email: this.email,
                        default_phone: this.phoneNumber,
                        default_mobile: this.mobileNumber,
                        */
                        default_partner_id: this.partnerId,
                    },
                    res_model: 'sale.order',
                    target: 'current',
                    type: 'ir.actions.act_window',
                    views: [[false, 'form']],
                });
            }
        },

 
        
    });
});