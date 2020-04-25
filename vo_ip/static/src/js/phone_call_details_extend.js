odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    var Phone = require('voip.PhoneCallDetails');
    
    console.log("este es el widget",Phone);
    const core = require('web.core');
    const session = require('web.session');
    const Widget = require('web.Widget');

    const QWeb = core.qweb;
    const _t = core._t;
  
    Phone.extend({
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