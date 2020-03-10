import tempfile
import json
import os


class TempFileManager:
    """
    This class is used for managing the creation and deletion of temporary files
    """
    @staticmethod
    def create_temp_file(payload):
        """
        Creates a temporary file from a dictionary which is written to the file as JSON

        :param dict payload: The payload to convert to JSON and save to the temp file

        :return: tempfile.NamedTemporaryFile secrets_file: The temporary file
        """
        secrets_file = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        secrets_file.write(json.dumps(payload))
        secrets_file.seek(0)
        return secrets_file

    @staticmethod
    def delete_temp_file(file):
        """
        Deletes a temporary file

        :param tempfile.NamedTemporaryFile file: The file to delete
        :return: None
        """
        file.close()
        os.unlink(file.name)