import argparse
import os
import sys

from features.feature_extractor import extract_all_features_from_package
from features.feature_file_writer import write_features_to_file
from features.get_project_root import get_project_root


def main(argv):
    ap = argparse.ArgumentParser(description="Get arguments from command line")
    ap.add_argument('-p', '--package', help='package name from the root folder, not including the root folder. Eg if '
                                            'root folder is "sdk", then package name should be "tests.tutorials", '
                                            'not "sdk.tests.tutorials"')
    ap.add_argument('-f', '--filepath', help='Path and name of the features file to be created. By default '
                                             '"features.txt" which will be created in the root sdk folder.')

    args = vars(ap.parse_args())
    package_name = args["package"]
    filepath = args["filepath"]

    if package_name is None:
        package_name = "tests.tutorials"

    if filepath is None:
        filepath = os.path.join(get_project_root(), 'features.txt')

    feature_list = extract_all_features_from_package(package_name)
    write_features_to_file(feature_list, filepath)
    print("File written to: " + filepath)


if __name__ == "__main__":
    main(sys.argv)
