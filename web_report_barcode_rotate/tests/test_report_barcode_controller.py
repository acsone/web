# Copyright 2020 João Marques
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import io

from PIL import Image

from odoo.tests import HttpCase


class TestReportBarcode(HttpCase):
    def test_report_barcode_rotate(self):
        barcode_value = "a0c1s0o1n0e"
        response = self.url_open(f"/report/barcode/Code128/{barcode_value}")
        barcode_image = Image.open(io.BytesIO(response.content))
        barcode_image_size = barcode_image.size
        response = self.url_open(f"/report/barcode/Code128/{barcode_value}?rotate=-90")
        rotated_barcode_image = Image.open(io.BytesIO(response.content))
        rotated_barcode_image_size = rotated_barcode_image.size
        # Ensures that the next test makes sense.
        self.assertNotEquals(*barcode_image_size)
        # Checks that the height and width have been interchanged, which correspond to a 90°
        # rotation.
        self.assertEqual(
            list(barcode_image_size), list(reversed(rotated_barcode_image_size))
        )
