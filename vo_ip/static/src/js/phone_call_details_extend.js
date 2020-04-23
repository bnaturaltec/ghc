odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    const Phone = require('voip.PhoneCallDetails')

    Phone =  Phone.include({

        start() {
            this._super(...arguments);
        },

    });
    


});