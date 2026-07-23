from odoo import fields, models


class ConfiguratorSubmission(models.Model):
    _name = 'website.configurator.submission'
    _description = 'Crate Configurator Submission'
    _order = 'create_date desc'

    name = fields.Char(default='Crate Configurator Submission', required=True)
    raw_payload = fields.Text(string='Raw Payload')
