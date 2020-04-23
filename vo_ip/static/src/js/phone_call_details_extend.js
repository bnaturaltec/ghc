odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    const Phone = require('voip.PhoneCallDetails')

    Phone.PhoneCallDetails =  Phone.PhoneCallDetails.include({

        start() {
            this._super(...arguments);
        },

    });
    


});