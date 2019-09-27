import os
import json
from urllib.request import pathname2url
from .api_configuration import ApiConfiguration


class ApiConfigurationLoader:

    @staticmethod
    def load(api_secrets_filename):
        """
        :param api_secrets_filename: name of api configuration file
        :return: populated ApiConfiguration
        """

        # Load our configuration details from the environment variables
        token_url = os.getenv("FBN_TOKEN_URL", None)
        api_url = os.getenv("FBN_LUSID_API_URL", None)
        username = os.getenv("FBN_USERNAME", None)
        password_raw = os.getenv("FBN_PASSWORD", None)
        client_id_raw = os.getenv("FBN_CLIENT_ID", None)
        client_secret_raw = os.getenv("FBN_CLIENT_SECRET", None)
        app_name = os.getenv("FBN_APP_NAME", "")

        # If any of the environmental variables are missing use a local secrets file
        if token_url is None or username is None or password_raw is None or client_id_raw is None \
                or client_secret_raw is None or api_url is None:

            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(os.path.join(dir_path, api_secrets_filename), "r") as secrets:
                config = json.load(secrets)

            token_url = os.getenv("FBN_TOKEN_URL", config["api"]["tokenUrl"])
            username = os.getenv("FBN_USERNAME", config["api"]["username"])
            password = pathname2url(os.getenv("FBN_PASSWORD", config["api"]["password"]))
            client_id = pathname2url(os.getenv("FBN_CLIENT_ID", config["api"]["clientId"]))
            client_secret = pathname2url(os.getenv("FBN_CLIENT_SECRET", config["api"]["clientSecret"]))
            api_url = os.getenv("FBN_LUSID_API_URL", config["api"]["apiUrl"])
            app_name = os.getenv("FBN_APP_NAME", config["api"].get("applicationName", ""))

        else:
            password = pathname2url(password_raw)
            client_id = pathname2url(client_id_raw)
            client_secret = pathname2url(client_secret_raw)

        return ApiConfiguration(
            token_url=token_url,
            api_url=api_url,
            username=username,
            password=password,
            client_id=client_id,
            client_secret=client_secret,
            app_name=app_name
        )

