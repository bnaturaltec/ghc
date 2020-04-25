odoo.define('voip.PhoneCallDetailsExtend', function (require) {
    "use strict";
    const Phone = require('voip.PhoneCallDetails');
    
    console.log("este es el widget",Phone);

  
    return Phone.extend({
        
            /**
         * @constructor
         */
        init: function (parent, phonecall) {
            this._super.apply(this, arguments);
            console.log("hello world");
        },

    });
  
    




});