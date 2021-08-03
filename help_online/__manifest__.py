# Copyright 2014 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Help Online",
    "version": "14.0.1.0.0",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "maintainer": "ACSONE SA/NV",
    "website": "https://github.com/OCA/web",
    "license": "AGPL-3",
    "category": "Documentation",
    "depends": [
        "website",
    ],
    "data": [
        "security/help_online_groups.xml",
        "security/help_online_rules.xml",
        "security/ir.model.access.csv",
        "wizards/export_help_wizard_view.xml",
        "wizards/import_help_wizard_view.xml",
        "views/help_online_view.xml",
        "data/ir_config_parameter_data.xml",
    ],
    "qweb": [
        "static/src/xml/help_online.xml",
    ],
    "installable": True,
}
