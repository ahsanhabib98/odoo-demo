# models/estate_property_type.py

from odoo import models, fields

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'

    name = fields.Char('Type', required=True)
