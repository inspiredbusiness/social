# -*- coding: utf-8 -*-
from odoo import models


class Ticket(models.Model):
    _name = 'helpdesk.ticket'
    _inherit = ['helpdesk.ticket', 'mail.activity.mixin']
