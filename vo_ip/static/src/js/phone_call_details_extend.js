odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    var Phone = require('voip.PhoneCallDetails');
    
    Phone = Phone.extend({
            /**
         * TODO: reduce coupling between PhoneCallDetails & PhoneCall
         *
         * @override
         * @param {voip.PhoneCallTab} parent
         * @param {voip.PhoneCall} phoneCall
         */
        init(parent, phoneCall) {
            this._super(...arguments);
            console.log("init overrude");
        },
        /**
         * @override
         */
        start() {
            this._super(...arguments);
            console.log("start overrude");
        },

    });
  
    
    console.log(Phone);

});