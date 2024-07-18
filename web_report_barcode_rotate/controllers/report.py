# Part of Odoo. See LICENSE file for full copyright and licensing details.
import io
import logging

from PIL import Image

from odoo import http

from odoo.addons.web.controllers.report import ReportController as ReportControllerBase

_logger = logging.getLogger(__name__)


class ReportController(ReportControllerBase):
    @http.route(
        ["/report/barcode", "/report/barcode/<barcode_type>/<path:value>"],
        type="http",
        auth="public",
    )
    def report_barcode(self, barcode_type, value, **kwargs):
        """
        Overrides :meth:`ReportControllerBase.report_barcode` that allow passing a rotation
        instruction in the kwargs.
        :param rotate: Angle as Integer will rotate the barcode counter clockwise
                       using the provided rotation angle. A negative value will rotate the
                       barcode clockwise.
        """
        # Route override that allows specifying a rotation.
        request = super().report_barcode(barcode_type, value, **kwargs)
        if angle := kwargs.get("rotate"):
            if (angle if angle[0] != "-" else angle[1:]).isnumeric() and request.data:
                image = Image.open(io.BytesIO(request.data))
                image = image.rotate(int(angle), expand=True)
                image_bytes = io.BytesIO()
                image.save(image_bytes, format="png")
                request.data = image_bytes.getvalue()
        return request
