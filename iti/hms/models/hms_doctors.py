from odoo import models, fields


class HmsDoctors(models.Model):
    _name = "hms.doctors"
    _rec_name = 'firstname'

    firstname = fields.Char(required=True)
    lastname = fields.Char(required=True)
    image = fields.Image()
