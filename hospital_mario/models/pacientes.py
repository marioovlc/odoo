# hospital_mario/models/pacientes.py

from odoo import models, fields

class HospitalMarioPacientes(models.Model):
    _name = 'hospital_mario.pacientes'
    _description = 'Hospital Mario Pacientes'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    sintomas = fields.Text(string='Síntomas')