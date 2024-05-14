# Copyright 2024 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, tools


class IrModelProxy(models.Model):

    _name = "ir.model.proxy"
    _description = "Kind of proxy for ir.model"
    _auto = False
    _rec_name = "description"

    id = fields.Integer()
    name = fields.Char(string="Model Name")
    description = fields.Char(translate=True)
    state = fields.Selection(
        [("manual", "Custom Object"), ("base", "Base Object")],
        string="Type",
        default="manual",
        readonly=True,
    )
    transient = fields.Boolean(string="Transient Model")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, "ir_model_proxy")
        self.env.cr.execute(
            """
        CREATE VIEW ir_model_proxy AS (
            SELECT
                irm.id as id,
                irm.model as name,
                irm.name as description,
                irm.state as state,
                irm.transient as transient
            FROM
                ir_model as irm
        )"""
        )
