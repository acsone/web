# -*- coding: utf-8 -*-
# Copyright 2022 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Web Widget Formio Builder",
    "summary": """
        <form.io> widgets for odoo""",
    "version": "10.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://acsone.eu/",
    "depends": ["web"],
    "demo": [],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'data': [
        'views/web_widget_formio.xml',
    ],
}
