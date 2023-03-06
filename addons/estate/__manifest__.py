{ 
    'name': "Real State Advertisement", 
    'summary': "Module of real state advertisement", 
    'description': """TODO""", 
    'author': "Technovative Solutions LTD", 
    'license': "AGPL-3", 
    'website': "https://www.technovativesolutions.co.uk", 
    'category': 'Advertisement', 
    'version': '0.0.1', 
    'depends': [
        'web'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}