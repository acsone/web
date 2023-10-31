# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Ace Editor Mode Json",
    "summary": """
        Add json mode to ACE Editor""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://acsone.eu/",
    "depends": [
        "web",
    ],
    "web.assets_backend": [
        "web_ace_mode_json/static/src/js/*.js",
    ],
    "data": [],
    "demo": [],
}
