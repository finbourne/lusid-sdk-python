import json
import os
from typing import Dict, TextIO, Protocol, Union, Iterable
import logging
from lusid.extensions.proxy_config import ProxyConfig
from lusid.extensions.api_configuration import ApiConfiguration

logger = logging.getLogger(__name__)

ENVIRONMENT_CONFIG_KEYS = {
    "token_url": "FBN_TOKEN_URL",
    "api_url": "FBN_LUSID_API_URL",
    "username": "FBN_USERNAME",
    "password": "FBN_PASSWORD",
    "client_id": "FBN_CLIENT_ID",
    "client_secret": "FBN_CLIENT_SECRET",
    "app_name": "FBN_APP_NAME",
    "certificate_filename": "FBN_CLIENT_CERTIFICATE",
    "proxy_address": "FBN_PROXY_ADDRESS",
    "proxy_username": "FBN_PROXY_USERNAME",
    "proxy_password": "FBN_PROXY_PASSWORD",
    "access_token": "FBN_ACCESS_TOKEN"
}

SECRETS_FILE_CONFIG_KEYS = {
    "token_url": "tokenUrl",
    "api_url": "lusidUrl",
    "username": "username",
    "password": "password",
    "client_id": "clientId",
    "client_secret": "clientSecret",
    "app_name": "applicationName",
    "certificate_filename": "clientCertificate",
    "proxy_address": "address",
    "proxy_username": "username",
    "proxy_password": "password",
    "access_token": "accessToken"
}


class ConfigurationLoader(Protocol):
    """
    The ApiConfigurationLoader is responsible for populating the API and Proxy configuration from a secrets file or
    environment variables with preference given to the secrets file.
    """

    def load_config(self) -> Dict[str, str]:
        pass


class SecretsFileConfigurationLoader:
    """Configuration Loader for reading secrets from a json secrets file
    """
    def __init__(
        self,
        api_secrets_file: Union[TextIO, str]
    ):
        """Create SecretsFileConfigurationLoader

        Parameters
        ----------
        api_secrets_file : Union[TextIO, str]
            File to load secrets from
        """
        self._api_secrets_file = api_secrets_file or ""

    def load_config(self) -> Dict[str, str]:
        """reads config from the provided secrets file

        Returns
        -------
        Dict[str, str]
            dictionary that can be loaded into an ApiConfiguration object
        """
        # The secrets file is a nested dictionary, set the names of the top level keys
        logger.debug(f"loading config from secrets file: {self._api_secrets_file}")
        api_config_key = "api"
        proxy_config_key = "proxy"
        try:
            try:
                config = json.load(self._api_secrets_file)
            except AttributeError:
                with open(self._api_secrets_file) as api_secrets_file:
                    config = json.load(api_secrets_file)
        except OSError:
            logger.warning(f"Unable to open secrets file {self._api_secrets_file}")
            return {}
        except json.JSONDecodeError:
            logger.warning("unable to deserialise contents of secrets file to json")
            return {}

        api_config_section = config.get(api_config_key, {})
        populated_api_config_values = {
            key: api_config_section.get(value)
            for key, value in SECRETS_FILE_CONFIG_KEYS.items()
            if "proxy" not in key
        }
        proxy_config_section = config.get(proxy_config_key, {})
        populated_proxy_values = {
            key: proxy_config_section.get(value)
            for key, value in SECRETS_FILE_CONFIG_KEYS.items()
            if "proxy" in key
        }
        populated_config_dict = {
            **populated_api_config_values,
            **populated_proxy_values,
        }
        return populated_config_dict


class EnvironmentVariablesConfigurationLoader:
    """ConfigurationLoader which reads config from environment variables
    """    
    def load_config(self) -> Dict[str, str]:
        """reads config from environment variables

        Returns
        -------
        Dict[str, str]
            dictionary that can be loaded into an ApiConfiguration object
        """
        logger.debug("loading config from environment variables")

        populated_api_config_values = {
            key: os.environ.get(value)
            for key, value in ENVIRONMENT_CONFIG_KEYS.items()
            if "proxy" not in key
        }
        populated_proxy_values = {
            key: os.environ.get(value)
            for key, value in ENVIRONMENT_CONFIG_KEYS.items()
            if "proxy" in key
        }
        populated_config_dict = {
            **populated_api_config_values,
            **populated_proxy_values,
        }
        return populated_config_dict


class ArgsConfigurationLoader:
    """ConfigurationLoader which loads in config from kwargs in constructor
    """
    def __init__(self, **kwargs):
        """kwargs passed to this constructor used to build ApiConfiguration
        """
        self._kwargs = kwargs

    def load_config(self) -> Dict[str, str]:
        """load configuration from kwargs passed to constructor

        Returns
        -------
        Dict[str, str]
            dictionary that can be loaded into an ApiConfiguration object
        """
        logger.debug("loading config from arguments passed to ArgsConfigurationLoader")
        keys = ENVIRONMENT_CONFIG_KEYS.keys()
        return {key: self._kwargs.get(key) for key in keys}


default_config_loaders = (
    EnvironmentVariablesConfigurationLoader(),
    SecretsFileConfigurationLoader(api_secrets_file="secrets.json"),
)

def get_api_configuration(config_loaders: Iterable[ConfigurationLoader]) -> ApiConfiguration:
    """Read configuration from config loaders.
    Update config with values from each loader in order (last write wins).

    Parameters
    ----------
    config_loaders : Iterable[ConfigurationLoader]
        Objects that can be used to fetch config with a load_config function returning a dict.

    Returns
    -------
    ApiConfiguration
        Configuration that can be passed to an ApiClient, RefreshingToken, etc.
    """
    config = {}

    for config_loader in config_loaders:
        loaded_config = {
            key: value
            for key, value in config_loader.load_config().items()
            if value is not None
        }
        config.update(loaded_config)
    proxy_address = config.pop("proxy_address", None)
    proxy_username = config.pop("proxy_username", None)
    proxy_password = config.pop("proxy_password", None)
    # If the proxy address is missing ensure that no proxy is used in the ApiConfiguration
    if all(
        (item is not None for item in (proxy_address, proxy_password, proxy_username))
    ):
        config["proxy_config"] = ProxyConfig(
            address=proxy_address, username=proxy_username, password=proxy_password
        )
    else:
        config["proxy_config"] = None
    # Create and return the ApiConfiguration
    return ApiConfiguration(**config)