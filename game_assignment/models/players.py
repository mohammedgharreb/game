# -*- coding:utf-8 -*-

from odoo import models, fields, api, _


class Players(models.Model):
    _inherit = 'res.partner'
    _name = 'players.players'
    no_of_wins = fields.Integer(string="# of Wins")
    no_of_loses = fields.Integer(string="# of Loses")
    average_game_duration = fields.Float(string="Average game duration")
    no_of_games = fields.Integer(string="Number of games for each field size")
    field_size = fields.Char(string="Field Size")
    notes = fields.Text(string="Notes")

    # players details
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    email = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()
    color = fields.Integer(string='Color Index', default=0)
    image = fields.Binary("Image", attachment=True,
                          help="This field holds the image used as avatar for this contact, limited to 1024x1024px", )
    image_small = fields.Binary("Small-sized image", attachment=True,
                               help="Small-sized image of this contact. It is automatically " \
                                    "resized as a 64x64px image, with aspect ratio preserved. " \
                                    "Use this field anywhere a small image is required.")
    image_medium = fields.Binary("Medium-sized image", attachment=True,
                                 help="Medium-sized logo of the brand. It is automatically "
                                      "resized as a 128x128px image, with aspect ratio preserved. "
                                      "Use this field in form views or some kanban views.")