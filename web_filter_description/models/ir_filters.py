# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class IrFilters(models.Model):
    _inherit = 'ir.filters'

    description = fields.Text(string="Description", required=False)

    @api.model
    def get_filters(self, model, action_id=None):
        action_domain = self._get_action_domain(action_id)
        filters = self.search(
            action_domain
            + [('model_id', '=', model), ('user_id', 'in', [self._uid, False])]
        )
        user_context = self.env.user.context_get()
        return filters.with_context(user_context).read(
            [
                'name',
                'is_default',
                'domain',
                'context',
                'user_id',
                'sort',
                'description',
            ]
        )
