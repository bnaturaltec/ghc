odoo.define('voip.phonecall_extend', function (require) {
    "use strict";
    //1585936426
    var Phonecall = require('voip.phonecall')
    
    //1585936465
    Phonecall.PhonecallDetails = Phonecall.PhonecallDetails.extend({
        events: _.extend({}, Phonecall.PhonecallDetails.events, {
            "click .o_dial_activity_cancel": "_onCancel",
            "click .o_dial_activity_done": "_onMarkAsDone",
            "click .o_dial_call_number": "_onCallNumber",
            "click .o_dial_email": "_onSendEmail",
            "click .o_dial_log": "_onLogCall",
            "click .o_dial_mute_button": "_onMuteButtonClick",
            "click .o_dial_unmute_button": "_onUnmuteButtonClick",
            "click .o_dial_reschedule_activity": "_onRescheduleActivity",
            "click .o_dial_to_partner": "_onToPartnerClick",
            "click .o_dial_to_record": "_onToRecordClick",
            "click .o_dial_transfer_button": "_onTransferButtonClick",
            "click .o_phonecall_details_close": "_onClosePhonecallDetails",
            "click .o_dial_to_sale_order": "_onToSaleOrderClick",
        }),
        /**
         * @constructor
         */
        init: function (parent, phonecall) {
            this._super.apply(this, arguments);
        },

        _onToSaleOrderClick: function (ev) {
            ev.preventDefault();
            if (this.partner_id) {
                this.do_action({
                    type: 'ir.actions.act_window',
                    res_model: "sale.order",
                    views: [[false, 'form']],
                    target: 'current',
                    context: {
                        default_partner_id: this.partner_id,
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
