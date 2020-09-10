import unittest

from features.feature_extractor import extract_all_features_from_package


class FeatureExtractorTests(unittest.TestCase):
    def test_get_valid_decorators(self):
        package = "features.unit.dummyfiles.valid"
        expected_features = ["F4", "F3", "F1", "F2"]

        feature_list_from_function = extract_all_features_from_package(package)
        expected_set = set(expected_features)
        actual_set = set(feature_list_from_function)

        self.assertEqual(len(feature_list_from_function), 4)
        self.assertEqual(expected_set, actual_set)

    def test_if_throws_error_on_duplicate_decorators(self):
        package = "features.unit.dummyfiles.duplicates"
        expected_duplicate = "F1"

        with self.assertRaises(Exception) as context:
            extract_all_features_from_package(package)

        self.assertTrue(f'lusid_feature error: Feature code "{expected_duplicate}" is a duplicate. '
                        'Please make sure each feature code is unique. Also make sure lusid_feature '
                        'decorator is on top of any other decorators for that function/method.' in str(context.exception))

    def test_if_throws_error_on_empty_string_value_decorators(self):
        package = "features.unit.dummyfiles.empties"

        with self.assertRaises(Exception) as context:
            extract_all_features_from_package(package)

        self.assertTrue("lusid_feature error: Some decorated methods have no value passed. "
                        "Please make sure each lusid_feature decorator has a value code passed." in str(
            context.exception))

    def test_if_throws_error_on_no_input_decorators(self):
        package = "features.unit.dummyfiles.noinput"

        with self.assertRaises(Exception) as context:
            extract_all_features_from_package(package)

        self.assertTrue("lusid_feature() missing 1 required positional argument: 'feature_code'" in str(
            context.exception))

    def test_if_returns_empty_list_with_no_annotations(self):
        package = "features.unit.dummyfiles.notannotated"
        expected_features = []

        feature_list_from_function = extract_all_features_from_package(package)

        self.assertEqual(len(feature_list_from_function), 0)
        self.assertEqual(feature_list_from_function, expected_features)

    def test_if_functions_get_annotated(self):
        package = "features.unit.dummyfiles.functions"
        expected_features = ["F1", "F2", "F3"]

        feature_list_from_functions = extract_all_features_from_package(package)

        self.assertEqual(len(feature_list_from_functions), 3)
        self.assertEqual(set(expected_features), set(feature_list_from_functions))

    def test_if_throws_error_on_no_decorator_brackets(self):
        package = "features.unit.dummyfiles.nobrackets"

        with self.assertRaises(Exception) as context:
            extract_all_features_from_package(package)

        self.assertTrue("lusid_feature error: Decorator requires a string input parameter." in str(
            context.exception))

    def test_if_returns_correct_codes_with_multiple_decorators(self):
        package = "features.unit.dummyfiles.multidecorator"
        expected_features = ["F1", "F2", "F3", "F4"]

        feature_list_from_functions = extract_all_features_from_package(package)

        self.assertEqual(set(expected_features), set(feature_list_from_functions))
