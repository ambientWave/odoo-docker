# -*- coding: utf-8 -*-

{
    'name': 'Zero Quantity Stock',
    'version': '16.0',
    'sequence': -100,
    'category': 'Sales/Sales',
    'summary': 'A module that disallows users to make a sale order or an inventory transfer with zero or negative quantity of products',
    'description': 
    """
    This module is intended to modify the behaviour of sale module by preventing users from saling or transfering a product that
    has a quantity of zero or less from a specific inventory.
    """,
    'author': 'Mina Samir Wahib',
    'website': "https://www.qs-solutions.com",
    'company': 'Quick Services Solutions',
    'maintainer': 'Quick Services Solutions',
    'depends': ['sales_team', 'stock', 'utm', 'sale', 'mail', 'l10n_co',
                'point_of_sale'],
    'data': ['views/inventory_location_added_to_sales_form.xml',
             ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
