# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "Activities in purchase",
    "version": "9.0.1.0.0",
    "author": "Inspired Software Pty Ltd, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "category": "Discuss",
    "summary": "Backport activities in stock",
    "depends": [
        'mail_activity',
        'purchase',
    ],
    "data": [
        "views/purchase.xml"
    ],
    'auto_install': True,
}
