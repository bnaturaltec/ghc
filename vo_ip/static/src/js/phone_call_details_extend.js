odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
     
    var Phone = require('voip.PhoneCallDetails');

    Phone = Phone.extend({
           /**
         * @constructor
         */
        init: function (parent, phonecall) {
            //this._super.apply(this, arguments);
            this._super(...arguments);
        },

    });


});