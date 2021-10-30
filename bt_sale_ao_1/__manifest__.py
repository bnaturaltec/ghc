# -*- coding: utf-8 -*-
# Developer: Carlos Avila.
# Mail: car.josavica@gmail.com
# Boostech CR
# 21.07.13

{
    'name' : 'Custom fields and Changes in PDF',
    'version' : '21.10.29',
    'summary': 'Custom fields and Changes in PDF - Grupo HC',
    'sequence': 0,
    'description': """
Contiene
====================

    Custom fields for:
    * Driver
    * Label
    
    Changes in PDF:
    * Remove from PDF Origin
    * Add in PDF Label
    
    """,
    'category': 'Boostech/Addons',
    'author': "Boostech CR",
    'website': 'https://boostechcr.com/',
    'images' : [
    ],
    'depends' : [
        'sale_management',
    ],
    'data': [
        'views/views_bt_sale_order_driver.xml',
        'views/views_bt_sale_order_label.xml',
        
        'views_inherits/views_bt_sale_order.xml',
        
        'reports_inherits/report_bt_sale_order.xml',

        'data/menu/menu.xml',
        
        'security/rules.xml',
        'security/ir.model.access.csv',
        
        # 'views_inherits/views_bt_account_payment.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
