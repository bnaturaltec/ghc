odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    const Phone = require('voip.PhoneCallDetails');
    
    console.log("este es el widget",Phone);

  
    return Phone.extend({
        
         

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