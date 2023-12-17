# -*- coding: utf-8 -*-
{
    'name' : 'my_dashboard_owl',
    'version' : '1.0',
    'summary': 'My Dashboard Owl',
    'sequence': -1,
    'description': """OWL Tutorial Custom Dashboard""",
    'category': 'OWL',
    'depends' : ['web', 'base', 'sale', 'board'],
    'data': [
        'views/my_dashboard.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            # 'owl/static/src/components/my_dashboard.js',
            # 'owl/static/src/components/my_dashboard.xml',
            'my_dashboard_owl/static/src/components/*',
            'my_dashboard_owl/static/src/components/**/*'
        ],
    },
}