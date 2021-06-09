# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Course Management system""",

    'description': """
        This an odoo app, going through the odoo building module tutorial.
The app is ment to be a tool to practice odoo concepts.
The app is totaly hypothetical and only useful for learning
    """,

    'author': "Jose Velasquez",
    'website': "http://www.yourcompany.com",
    'maintainer': "Syntax LTD",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}