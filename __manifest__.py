{
    'name': 'Exe Add Subindustry',
    'version': '18.0',
    'category': 'Tools',
    'author':'Mauro Bogado,Exemax',
    'summary': 'Modulo para poder agregar subindustrias a los contactos',
    'depends': ['base','sale', 'account', 'mail', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/exe_add_subindustry.xml',
        
        
    ],

    'installable': True,
    'application': False,
}   