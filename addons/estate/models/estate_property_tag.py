# models/estate_property_tag.py

from odoo import models, fields

class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tag'

    name = fields.Char('Tag', required=True)
