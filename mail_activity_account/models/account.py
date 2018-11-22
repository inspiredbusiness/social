# -*- coding: utf-8 -*-
from odoo import models


class AccountInvoice(models.Model):
    _name = 'account.invoice'
    _inherit = ['account.invoice', 'mail.activity.mixin']
