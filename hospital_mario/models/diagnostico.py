# hospital/models/diagnostico.py
from odoo import models, fields, api

class Diagnostico(models.Model):
    _name = 'hospital_mario.diagnostico'
    _description = 'Diagnóstico de paciente'

    paciente_id = fields.Many2one('hospital_mario.pacientes', string='Paciente', required=True)
    medico_id = fields.Many2many('hospital_mario.medicos', string='Médico', required=True)
    diagnostico = fields.Text(string='Diagnóstico')
    fecha_atencion = fields.Date(string='Fecha de Atención', required=True)

    @api.constrains('fecha_atencion')
    def _check_fecha_atencion(self):
        for record in self:
            if record.fecha_atencion > fields.Date.today():
                raise models.ValidationError('La fecha de atención no puede ser posterior al día de hoy')
            
    
    
