# Copyright 2024 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    _logger.info("Create columns proxy_model_id and proxy_field_id")
    openupgrade.logged_query(
        env.cr,
        """
        ALTER TABLE ir_model_fields_tooltip
        ADD COLUMN IF NOT EXISTS proxy_model_id INTEGER;
        ALTER TABLE ir_model_fields_tooltip
        ADD COLUMN IF NOT EXISTS proxy_field_id INTEGER;
        """,
    )
    _logger.info("Fill columns proxy_model_id and proxy_field_id")
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE ir_model_fields_tooltip
        SET proxy_model_id = model_id, proxy_field_id = field_id
        """,
    )
