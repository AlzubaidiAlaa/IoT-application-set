"""
    SmartKettle

    App that controls an smart electric kettle. Part of the IoT-dataset for fuzzing Smart Home Appliances.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import smartkettle
from smartkettle.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_boil_liquid_by_viscosity_get(self):
        """Test case for boil_liquid_by_viscosity_get

        """
        pass

    def test_make_tea_post(self):
        """Test case for make_tea_post

        """
        pass

    def test_stir_liquid_rpm_get(self):
        """Test case for stir_liquid_rpm_get

        """
        pass

    def test_warm_liquid_by_date_post(self):
        """Test case for warm_liquid_by_date_post

        """
        pass

    def test_warm_liquid_temperature_scale_get(self):
        """Test case for warm_liquid_temperature_scale_get

        """
        pass


if __name__ == '__main__':
    unittest.main()