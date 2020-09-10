import unittest

from features.feature_extractor import extract_all_features_from_package
from features.features_temp_file_manager import FeaturesTempFileManager


class FeatureFileWriterTests(unittest.TestCase):
    def test_if_writer_writes_test_features_correctly(self):
        package = "features.unit.dummyfiles.valid"

        feature_list_from_function = "\n".join(extract_all_features_from_package(package))
        feature_list_temp = FeaturesTempFileManager.create_temp_file(feature_list_from_function)
        feature_list_from_file = feature_list_temp.read()
        FeaturesTempFileManager.delete_temp_file(feature_list_temp)

        self.assertGreater(len(feature_list_from_function), 0)
        self.assertEqual(feature_list_from_function, feature_list_from_file)

    def test_if_writer_writes_actual_features_correctly(self):
        package = "tests.tutorials"

        feature_list_from_function = "\n".join(extract_all_features_from_package(package))
        feature_list_temp = FeaturesTempFileManager.create_temp_file(feature_list_from_function)
        feature_list_from_file = feature_list_temp.read()
        FeaturesTempFileManager.delete_temp_file(feature_list_temp)

        self.assertEqual(feature_list_from_function, feature_list_from_file)


