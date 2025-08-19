# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import ast
import logging

from dateutil.relativedelta import relativedelta

from odoo import _, fields
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)


def evaluate_python_expression(code, data=None):
    """Safely evaluate a user-defined Python expression.

    :param code: Python expression as string
    :param data: Optional dict with safe variables (e.g. {'object': record})
    :return: Evaluated result
    """
    if code is None or code == "" or isinstance(code, bool):
        return code

    # Safe globals
    safe_locals = {
        "context_today": fields.Date.today,
        "relativedelta": relativedelta,
    }

    # Add custom data (like 'object' etc.)
    if data:
        safe_locals.update(data)

    # Try evaluating as a Python expression
    try:
        return safe_eval(code, safe_locals)
    except Exception as e:
        _logger.warning("safe_eval failed for code %r: %s", code, e)

    # Fallback: try literal eval (for static strings, numbers, lists, etc.)
    try:
        return ast.literal_eval(code)
    except Exception as e:
        raise ValidationError(
            _("Invalid expression: `%(code)s`"), params={"code": code}
        ) from e
