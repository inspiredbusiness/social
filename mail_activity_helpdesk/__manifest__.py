# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "Activities in Helpdesk",
    "version": "9.0.1.0.0",
    "author": "Inspired Software Pty Ltd, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "category": "Helpdesk",
    "summary": "Backport activities in Helpdesk",
    "depends": [
        'mail_activity',
        'helpdesk',
    ],
    "data": [
        "views/helpdesk_ticket.xml"
    ],
    'auto_install': True,
}
