import json
import os
from pathlib import Path


class CredentialsSource:

    @classmethod
    def secrets_path(cls) -> Path:
        return Path(__file__).parent.parent.joinpath('secrets.json')

    @classmethod
    def config_keys_path(cls) -> Path:
        return Path(__file__).parent.parent.parent.joinpath('lusid/utilities/config_keys.json')

    @classmethod
    def optional_config(cls) -> Path:
        return Path(__file__).parent.joinpath('sample.json')

    @classmethod
    def fetch_config_keys(cls):
        with open(cls.config_keys_path()) as config_key_file:
            config_keys = json.load(config_key_file)
        return config_keys

    @staticmethod
    def custom_name_func(testcase_func, param_num, param):
        return f"{testcase_func.__name__}: {param.args[0]}"

    @classmethod
    def fetch_pat(cls):
        return os.getenv("FBN_ACCESS_TOKEN", None)

    @classmethod
    def fetch_credentials(cls):
        credentials = cls.secrets_path()

        # Get all the required variables available as environment variables
        vars = {
            "token_url": os.getenv("FBN_TOKEN_URL", None),
            "username": os.getenv("FBN_USERNAME", None),
            "password": os.getenv("FBN_PASSWORD", None),
            "client_id": os.getenv("FBN_CLIENT_ID", None),
            "client_secret": os.getenv("FBN_CLIENT_SECRET", None),
            "api_url": os.getenv("FBN_LUSID_API_URL", None)
        }

        # If there is a secrets file get the required variables from here too
        if os.path.isfile(credentials):
            with open(credentials) as secrets_file:
                secrets = json.load(secrets_file)

                config_vars = {
                    "token_url": secrets["api"].get("tokenUrl", None),
                    "username": secrets["api"].get("username", None),
                    "password": secrets["api"].get("password", None),
                    "client_id": secrets["api"].get("clientId", None),
                    "client_secret": secrets["api"].get("clientSecret", None),
                    "api_url": secrets["api"].get("apiUrl", None),
                }

            # Enrich the values from the environment variables with the secrets file
            for key, value in vars.items():
                if value is None:
                    vars[key] = config_vars[key]

        # Allow the Personal Access Token (PAT) to take precedence.
        # If the PAT exists, then an API URL must also exist in either an env var, or the secrets file.
        if cls.fetch_pat() is not None:
            vars_pat = {
                "access_token": cls.fetch_pat(),
                "api_url": vars.get("api_url", None)
            }
            return vars_pat

        if None in vars.values():
            assert False, "Source test configuration missing values from both secrets file and environment variables"

        vars_optional = {
            "app_name": os.getenv("FBN_APP_NAME", None),
            "certificate_filename": os.getenv("FBN_CLIENT_CERTIFICATE", None),
            "proxy_address": os.getenv("FBN_PROXY_ADDRESS", None),
            "proxy_username": os.getenv("FBN_PROXY_USERNAME", None),
            "proxy_password": os.getenv("FBN_PROXY_PASSWORD", None)
        }

        # If there is a secrets file get the required variables from here too
        if os.path.isfile(credentials):
            with open(credentials) as secrets_file:
                secrets = json.load(secrets_file)

                config_vars_optional = {
                    "app_name": secrets["api"].get("applicationName", None),
                    "certificate_filename": secrets["api"].get("clientCertificate", None),
                    "proxy_address": secrets.get("proxy", {}).get("address", None),
                    "proxy_username": secrets.get("proxy", {}).get("username", None),
                    "proxy_password": secrets.get("proxy", {}).get("password", None),
                }

            # Enrich the values from the environment variables with the secrets file
            for key, value in vars_optional.items():
                if value is None:
                    vars_optional[key] = config_vars_optional[key]

        vars.update(vars_optional)
        return vars