# Copyright 2024 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, tools


class IrModelFieldsProxy(models.Model):

    _name = "ir.model.fields.proxy"
    _description = "Kind of proxy for ir.model.fields"
    _auto = False

    id = fields.Integer()
    name = fields.Char()
    description = fields.Char(translate=True)
    ttype = fields.Char(string="Field Type")
    index = fields.Boolean(string="Indexed")
    store = fields.Boolean(string="Stored")
    readonly = fields.Boolean()
    relation = fields.Char(string="Related Model")
    model_id = fields.Integer()

    def init(self):
        tools.drop_view_if_exists(self.env.cr, "ir_model_fields_proxy")
        self.env.cr.execute(
            """
        CREATE VIEW ir_model_fields_proxy AS (
            SELECT
                irmf.id as id,
                irmf.name as name,
                irmf.field_description as description,
                irmf.ttype as ttype,
                irmf.index as index,
                irmf.store as store,
                irmf.readonly as readonly,
                irmf.relation as relation,
                irmf.model_id as model_id
            FROM
                ir_model_fields as irmf
        )"""
        )
