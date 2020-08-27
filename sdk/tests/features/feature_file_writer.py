import os


def write_features_to_file(feature_list, filepath):
    text_to_write = "\n".join(feature_list)
    with open(filepath, "w+") as f:
        f.write(text_to_write)


def remove_file(filepath):
    is_file = os.path.isfile(filepath)
    if is_file:
        os.remove(filepath)


def read_file(filepath):
    with open(filepath, "r") as f:
        features_from_file = f.read().splitlines()
    return features_from_file
