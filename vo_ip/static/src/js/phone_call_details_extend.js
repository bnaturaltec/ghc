odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    const core = require('web.core');
    const session = require('web.session');
    const Widget = require('web.Widget');

    const QWeb = core.qweb;
    const _t = core._t;

    const Phone = require('voip.PhoneCallDetails');

    Phone.PhoneCallDetails = Phone.PhoneCallDetails.extend({
           /**
         * @constructor
         */
        init: function (parent, phonecall) {
            //this._super.apply(this, arguments);
            this._super(...arguments);
        },

    });


});