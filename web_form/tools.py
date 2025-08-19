# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import ast

from dateutil.relativedelta import relativedelta

from odoo import _, fields
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval


def _check_result(result, code):
    if isinstance(result, int | float | str | bool):
        return result
    raise ValidationError(
        _("Error evaluating code: %s\nType allowed: int, float and str") % code
    )


def evaluate_python_expression(code, data=None):
    if code is None or isinstance(code, bool) or code == "":
        return code
    try:
        return safe_eval(
            code, {"context_today": fields.Date.today, "relativedelta": relativedelta}
        )
    except (ValueError, SyntaxError):  # pylint: disable=except-pass
        pass
    try:
        result = ast.literal_eval(code)
    except (ValueError, SyntaxError):  # pylint: disable=except-pass
        pass
    else:
        return _check_result(result, code)

    try:
        result = data
        for field in code.split("."):
            result = result[field]
    except (KeyError, TypeError) as err:
        raise ValidationError(_("Error evaluating code: %s\n") % code) from err
    else:
        return _check_result(result, code)
