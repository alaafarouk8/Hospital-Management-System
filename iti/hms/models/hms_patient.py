import datetime
import re

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HmsPatient(models.Model):
    _name = "hms.patient"
    _rec_name = 'firstname'
    firstname = fields.Char(required=True)
    lastname = fields.Char(required=True)
    email = fields.Char()
    birthdate = fields.Date()
    crRatio = fields.Float()
    Blood = fields.Selection([('o', 'O'), ('A', 'a'), ('ab', 'AB'), ('b', 'B')])
    PCR = fields.Boolean(required=True)
    image = fields.Image()
    address = fields.Text()
    age = fields.Integer()
    history = fields.Html()
    doctor_id = fields.Many2many('hms.doctors')
    department_id = fields.Many2one('hms.departments')
    capacity = fields.Integer(related='department_id.capacity')
    log_id = fields.One2many('hms.loghistory', 'patient_id')
    state = fields.Selection(
        [('undetermined', 'Undetermined'), ('good', 'Good'), ('fair', 'Fair'), ('serious', 'Serious')],
        default='undetermined')
    _sql_constraints = [
        ('unique_email', 'unique (email)', 'Email address already exists!')
    ]

    @api.onchange('age')
    def _onchange_age(self):
        if self.age < 30:
            self.PCR = True
            return {
                'warning': {
                    'title': 'Alert',
                    'message': 'PCR has been checked'
                }
            }

    @api.onchange('birthdate')
    def _calc_patient_age(self):
        if self.birthdate:
            self.age = datetime.date.today().year - self.birthdate.year

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')

    @api.onchange('state')
    def _onchange_state(self):
        if self.state:
            self.env['hms.loghistory'].create({
                'description': self.state,
                'patient_id': self.id
            })
