# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class Property(models.Model):
    _name = "estate.property"
    _description = "Real state advertisement property"

    name = fields.Char('Property Name', required=True)
    description = fields.Text('Property Description', required=True)
    postcode = fields.Char('Postcode', required=True)
    date_availability = fields.Date('Date Availability', required=True, copy=False, default=lambda self: fields.Date.to_string(fields.Date.today() + relativedelta(months=3)))
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer('Bedrooms', required=True, default=2)
    living_area = fields.Integer('Living Area', required=True)
    facades = fields.Integer('Facades', required=True)
    garage = fields.Boolean('Garage', required=True)
    garden = fields.Boolean('Garden', required=True)
    garden_area = fields.Integer('Garden Area', required=True)
    garden_orientation = fields.Selection([
        ('north', 'North'), 
        ('south', 'South'), 
        ('east', 'East'), 
        ('west', 'West')
        ], string='Garden Orientation', default='north', help="Garden Orientation is used to separate position or area")
    active = fields.Boolean(default=True)
    status = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ], string='Status', default='new', required=True)
    property_type_id = fields.Many2one('estate.property.type', string='Type')
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    total_area = fields.Float(compute='_compute_total_area', store=True)
    best_price = fields.Float(compute='_compute_best_price', store=True)

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            offer_prices = record.offer_ids.mapped('price')
            if offer_prices:
                record.best_price = max(offer_prices)
            else:
                record.best_price = 0.0

    @api.onchange('garden')
    def onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = ''
