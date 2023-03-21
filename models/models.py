# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

# class reto-odoo(models.Model):
#     _name = 'reto-odoo.reto-odoo'
#     _description = 'reto-odoo.reto-odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Subject(models.Model):
    _name = 'reto_odoo.subject'
    _description = 'Modelo Subject'

    name = fields.Char('Nombres')
    credits = fields.Integer(string='Creditos')
    max_students = fields.Integer(string='Máxima cantidad de estudiantes')
    active = fields.Boolean(string='Activo')
    
    students_ids = fields.Many2many('reto_odoo.student', string='Estudiantes')
    teacher_id = fields.Many2one('reto_odoo.teacher', string='Profesores')

class Student(models.Model):
    _name = 'reto_odoo.student'
    _description = 'Modelo Student'

    name = fields.Char('Nombre del Estudiante')
    birth_date = fields.Date()
    age = fields.Integer(string='Edad', compute='_obtain_age')
    final_exam_grade = fields.Float('Nota', (4,2), default=0.0, max=20.0, min=0.0)

    subject_ids = fields.Many2many('reto_odoo.subject', string='Subject')

    @api.depends('birth_date')
    def _obtain_age(self):
        for student in self:
            today = date.today()
            student.age = relativedelta(today, student.birth_date).years

class Teacher(models.Model):
    _name = 'reto_odoo.teacher'
    _description = 'Modelo Profesor'

    name = fields.Char('Nombre de Profesor')
    profile = fields.Text('Perfil del profesor')

    subject_ids = fields.One2many('reto_odoo.subject', 'teacher_id', string='Curso')