# hospital_mario/models/medicos.py
from odoo import models, fields

class HospitalMarioMedicos(models.Model):
    _name = 'hospital_mario.medicos'
    _description = 'Hospital Mario Medicos'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    id_colegiado = fields.Char(string='ID Colegiado', required=True)