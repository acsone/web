# Copyright 2019 - TODAY Serpent Consulting Services Pvt. Ltd.
# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Web Field Tooltip",
    "summary": """
        Displays customizable tooltips for fields""",
    "version": "16.0.1.0.1",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/web",
    "depends": ["web"],
    "data": [
        "security/res_groups.xml",
        "security/ir_model_access.xml",
        "views/ir_model_fields_tooltip.xml",
        "views/ir_model_proxy_views.xml",
        "views/ir_model_fields_proxy_views.xml",
        "views/res_users.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "/web_field_tooltip/static/src/components/field_tooltip/field_tooltip.esm.js",
            "/web_field_tooltip/static/src/components/field_tooltip/field_tooltip.scss",
            "/web_field_tooltip/static/src/components/field_tooltip/field_tooltip.xml",
            "/web_field_tooltip/static/src/views/form/form_controller.esm.js",
            "/web_field_tooltip/static/src/views/form/form_label.esm.js",
            "/web_field_tooltip/static/src/views/form/form_label.xml",
            "/web_field_tooltip/static/src/views/list/list_renderer.esm.js",
            "/web_field_tooltip/static/src/views/list/list_renderer.xml",
        ],
    },
}
