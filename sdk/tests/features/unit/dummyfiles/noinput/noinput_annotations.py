import unittest

from features.lusid_feature import lusid_feature


class NoinputTest(unittest.TestCase):

    @lusid_feature()
    def test_dummy_method_1(self):
        pass  # Empty for testing purposes

    @lusid_feature("F2")
    def test_control_method(self):
        pass  # Empty for testing purposes
