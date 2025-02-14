# -*- coding: utf-8 -*-
{
    'name': "Biblioteca Comics Simple",  # Titulo del módulo
    'summary': "Gestionar comics :) (Version simple)",  # Resumen de la funcionalidad
    'description': """
Gestor de bibliotecas (Version Simple)
==============
    """,  

    # Indicamos que es una aplicación
    'application': True,
    'author': "Flor",
    'website': "odoo.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        # Estos dos primeros ficheros:
        # 1) El primero indica grupo de seguridad basado en rol
        # 2) El segundo indica la política de acceso del modelo
        # Más información en https://www.odoo.com/documentation/17.0/es/developer/howtos/rdtraining/05_securityintro.html
        # Y en www.odoo.yenthevg.com/creating-security-groups-odoo/
        'security/groups.xml',
        'security/ir.model.access.csv',
        # Cargamos la vista de la biblioteca de comics
        'views/biblioteca_comic.xml',
        'views/socios_views.xml',
        'views/ejemplar_prestamo_views.xml',
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
