# -*- coding: utf-8 -*-
from odoo import models


class ProjectTask(models.Model):
    _name = 'project.task'
    _inherit = ['project.task', 'mail.activity.mixin']
