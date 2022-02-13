from odoo import models, fields


class HmsDepartments(models.Model):
    _name = "hms.departments"

    name = fields.Char(required=True)
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patient_id = fields.One2many('hms.patient', 'department_id')
