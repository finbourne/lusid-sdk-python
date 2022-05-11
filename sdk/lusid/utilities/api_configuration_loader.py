import json
import os
from pathlib import Path
import logging

from lusid.utilities.api_configuration import ApiConfiguration
from lusid.utilities.proxy_config import ProxyConfig


class ApiConfigurationLoader:
    """
    The ApiConfigurationLoader is responsible for populating the API and Proxy configuration from a secrets file or
    environment variables with preference given to the secrets file.
    """
    @staticmethod
    def load(api_secrets_filename=None):
        """
        :param str api_secrets_filename: The full path to the JSON file containing the API credentials and optional proxy details

        :return: lusid.utilities.ApiConfiguration: The populated ApiConfiguration
        """

        # Get the config keys which contain the mapping between the ApiConfiguration attributes and the variable names
        # in the secrets.json file and environment variables e.g. token_url is tokenUrl (secrets.json) and
        # FBN_TOKEN_URL (env variable)
        with open(Path(__file__).parent.joinpath('config_keys.json')) as json_file:
            config_keys = json.load(json_file)

        # The secrets file is a nested dictionary, set the names of the top level keys
        api_config_key = "api"
        proxy_config_key = "proxy"

        def _load_config_from_secrets_file():

            # If there is a secrets file specified and it exists get the details from it
            if api_secrets_filename is not None and os.path.exists(api_secrets_filename) and os.path.isfile(api_secrets_filename):
                with open(api_secrets_filename, "r") as secrets:
                    config = json.load(secrets)

            # If there is a secrets file specified and it does not exist log a warning to indicate that the specified file
            # could not be found and create an empty config
            elif api_secrets_filename is not None and (not os.path.exists(api_secrets_filename) or not os.path.isfile(api_secrets_filename)):
                logging.debug(f"Provided secrets file of {api_secrets_filename} can not be found, please ensure you "
                                 f"have correctly specified the full path to the file or don't provide a secrets file to use "
                                 f"environment variables instead.")
                config = {}
            # If no secrets file is specified just create an empty config
            else:
                config = {}

            return config

        def _get_access_api_config():

            config = _load_config_from_secrets_file()

            # Populate the values for the api configuration preferring the secrets file over the environment variables
            populated_api_config_values = {
                key: config.get(api_config_key, {}).get(value["config"], os.getenv(value["env"], None))
                for key, value in config_keys.items() if "proxy" not in key
            }

            return populated_api_config_values

        def _get_proxy_api_config():

            config = _load_config_from_secrets_file()

            # Populate the values for the proxy preferring the secrets file over the environment variables
            populated_proxy_values = {
                key.replace("proxy_", ""): config.get(proxy_config_key, {}).get(value["config"], os.getenv(value["env"], None))
                for key, value in config_keys.items() if "proxy" in key
            }

            return populated_proxy_values

        populated_api_config_values = _get_access_api_config()
        populated_proxy_values = _get_proxy_api_config()

        # If the proxy address is missing ensure that no proxy is used in the ApiConfiguration
        if populated_proxy_values.get("address", None) is None:
            populated_api_config_values["proxy_config"] = None
        # Otherwise create a ProxyConfig to use
        else:
            populated_api_config_values["proxy_config"] = ProxyConfig(**populated_proxy_values)
        # Create and return the ApiConfiguration
        return ApiConfiguration(**populated_api_config_values)
