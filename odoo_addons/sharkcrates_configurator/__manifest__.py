{
    'name': 'SharkCrates Crate Configurator',
    'summary': 'Embeds the DriveWorks Live crate configurator on the Odoo website',
    'description': """
Re-hosts the DriveWorks Live "Configurator" project (the same one embedded on
the WordPress site via the [driveworks_embed] shortcode) on an Odoo website
page, using the same server_url / group_alias / project_name.
""",
    'version': '18.0.1.0.0',
    'category': 'Website',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/configurator_templates.xml',
        'views/configurator_submission_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'sharkcrates_configurator/static/src/css/configurator.css',
            'sharkcrates_configurator/static/src/js/configurator.js',
        ],
    },
    'installable': True,
    'application': False,
}
