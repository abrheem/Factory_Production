# -*- coding: utf-8 -*-
{
    'name': 'Factory Production',
    'version': '18.0.0.1',
    'author': 'ibrahem Bamoman',
    'website': '',
    'category': '',
    'depends': ['base','website', 'portal'],
    'data': [
        
        # Security
        'security/ir.model.access.csv',
        
        #Data
        'data/sequence_data.xml',
        
        # Views
        'views/factory_menu.xml',
        'views/factory_production.xml',
        
        
        # 'views/factory_menu.xml',
        
        #Report
        'report/production_report.xml',
    
        ],
    'demo': [],
    'application': True,
}
