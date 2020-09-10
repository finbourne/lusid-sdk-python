import tempfile
import os


class FeaturesTempFileManager:
    """
    This class is used for managing the creation and deletion of temporary feature files
    """
    @staticmethod
    def create_temp_file(data):
        """
        Creates a temporary file from extracted features which is written to the file as a text file
        :param str data: The data is passed as a text string and saved to the temp file
        :return: tempfile.NamedTemporaryFile features_file: The temporary file
        """
        features_file = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        features_file.write(data)
        features_file.seek(0)
        return features_file

    @staticmethod
    def delete_temp_file(file):
        """
        Deletes a temporary file
        :param tempfile.NamedTemporaryFile file: The file to delete
        :return: None
        """
        file.close()
        os.unlink(file.name)
