import unittest

from parameterized import parameterized

from features.lusid_feature import lusid_feature


class Valid2Tests(unittest.TestCase):

    def test_dummy_method_1(self):
        pass  # Empty for testing purposes

    @lusid_feature("F3")
    @classmethod
    @parameterized.expand(
        [
            ("test3", 1),
            ("test4", 2)
        ]
    )
    def test_dummy_method_2(cls, test1, test2):
        pass  # Empty for testing purposes

    @lusid_feature("F4")
    @unittest.skip
    def test_control_method(self):
        pass  # Empty for testing purposes

