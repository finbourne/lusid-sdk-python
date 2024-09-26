import json
import os
from typing import Dict, TextIO, Protocol, Union, Iterable, Optional
import logging
from lusid.extensions.proxy_config import ProxyConfig
from lusid.extensions.api_configuration import ApiConfiguration
from lusid.extensions.file_access_token import FileAccessToken
from lusid.extensions.configuration_options import ConfigurationOptions

logger = logging.getLogger(__name__)

ENVIRONMENT_CONFIG_KEYS = {
    "token_url": "FBN_TOKEN_URL",
    "api_url": "FBN_LUSID_URL",
    "previous_api_url": "FBN_LUSID_API_URL",
    "username": "FBN_USERNAME",
    "password": "FBN_PASSWORD",
    "client_id": "FBN_CLIENT_ID",
    "client_secret": "FBN_CLIENT_SECRET",
    "app_name": "FBN_APP_NAME",
    "certificate_filename": "FBN_CLIENT_CERTIFICATE",
    "proxy_address": "FBN_PROXY_ADDRESS",
    "proxy_username": "FBN_PROXY_USERNAME",
    "proxy_password": "FBN_PROXY_PASSWORD",
    "access_token": "FBN_ACCESS_TOKEN",
    "total_timeout_ms": "FBN_TOTAL_TIMEOUT_MS",
    "connect_timeout_ms": "FBN_CONNECT_TIMEOUT_MS",
    "read_timeout_ms": "FBN_READ_TIMEOUT_MS",
    "rate_limit_retries": "FBN_RATE_LIMIT_RETRIES",
}

SECRETS_FILE_CONFIG_KEYS = {
    "token_url": "tokenUrl",
    "api_url": "lusidUrl",
    "previous_api_url": "lusidUrl",
    "username": "username",
    "password": "password",
    "client_id": "clientId",
    "client_secret": "clientSecret",
    "app_name": "applicationName",
    "certificate_filename": "clientCertificate",
    "proxy_address": "address",
    "proxy_username": "username",
    "proxy_password": "password",
    "access_token": "accessToken",
    "total_timeout_ms": "totalTimeoutMs",
    "connect_timeout_ms": "connectTimeoutMs",
    "read_timeout_ms": "readTimeoutMs",
    "rate_limit_retries": "rateLimitRetries",
}


class ConfigurationLoader(Protocol):
    """
    The ApiConfigurationLoader is responsible for populating the API and Proxy configuration from a secrets file or
    environment variables with preference given to the secrets file.
    """

    def load_config(self) -> Dict[str, object]:
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

    def load_config(self) -> Dict[str, object]:
        """reads config from the provided secrets file

        Returns
        -------
        Dict[str, object]
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
        if not populated_api_config_values["api_url"]:
            populated_api_config_values["api_url"] = populated_api_config_values["previous_api_url"]
        del(populated_api_config_values["previous_api_url"])
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
    def load_config(self) -> Dict[str, object]:
        """reads config from environment variables

        Returns
        -------
        Dict[str, object]
            dictionary that can be loaded into an ApiConfiguration object
        """
        logger.debug("loading config from environment variables")

        populated_api_config_values = {
            key: os.environ.get(value)
            for key, value in ENVIRONMENT_CONFIG_KEYS.items()
            if "proxy" not in key
        }
        if not populated_api_config_values["api_url"]:
            populated_api_config_values["api_url"] = populated_api_config_values["previous_api_url"]
        # ensure that these values are ints
        for key in ["total_timeout_ms", "connect_timeout_ms", "read_timeout_ms", "rate_limit_retries"]:
            if populated_api_config_values[key]:
                try:
                    populated_api_config_values[key] = int(populated_api_config_values[key])
                except ValueError as e:
                    raise ValueError(f"invalid value for '{key}' - value must be an integer if set")
        del(populated_api_config_values["previous_api_url"])
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
    def __init__(self,
        token_url:Optional[str]=None,
        api_url:Optional[str]=None,
        username:Optional[str]=None,
        password:Optional[str]=None,
        client_id:Optional[str]=None,
        client_secret:Optional[str]=None,
        app_name:Optional[str]=None,
        certificate_filename:Optional[str]=None,
        proxy_address:Optional[str]=None,
        proxy_username:Optional[str]=None,
        proxy_password:Optional[str]=None,
        access_token:Optional[str]=None,
        total_timeout_ms:Optional[int]=None,
        connect_timeout_ms:Optional[int]=None,
        read_timeout_ms:Optional[int]=None,
        rate_limit_retries:Optional[int]=None,
        ):
        """kwargs passed to this constructor used to build ApiConfiguration
        """
        self.__token_url = token_url
        self.__api_url = api_url
        self.__username = username
        self.__password = password
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__app_name = app_name
        self.__certificate_filename = certificate_filename
        self.__proxy_address = proxy_address
        self.__proxy_username = proxy_username
        self.__proxy_password = proxy_password
        self.__access_token = access_token
        self.__total_timeout_ms = total_timeout_ms
        self.__connect_timeout_ms = connect_timeout_ms
        self.__read_timeout_ms = read_timeout_ms
        self.__rate_limit_retries = rate_limit_retries

    def load_config(self) -> Dict[str, object]:
        """load configuration from kwargs passed to constructor

        Returns
        -------
        Dict[str, object]
            dictionary that can be loaded into an ApiConfiguration object
        """
        logger.debug("loading config from arguments passed to ArgsConfigurationLoader")
        return {
            "token_url" : self.__token_url, 
            "api_url" : self.__api_url, 
            "username" : self.__username, 
            "password" : self.__password, 
            "client_id" : self.__client_id, 
            "client_secret" : self.__client_secret, 
            "app_name" : self.__app_name, 
            "certificate_filename" : self.__certificate_filename, 
            "proxy_address" : self.__proxy_address, 
            "proxy_username" : self.__proxy_username, 
            "proxy_password" : self.__proxy_password, 
            "access_token" : self.__access_token,
            "total_timeout_ms" : self.__total_timeout_ms,
            "connect_timeout_ms" : self.__connect_timeout_ms,
            "read_timeout_ms" : self.__read_timeout_ms,
            "rate_limit_retries" : self.__rate_limit_retries,
        }


class FileTokenConfigurationLoader:
    """ConfigurationLoader which loads in access token from file
        if FBN_ACCESS_TOKEN_FILE is set,
        or if an access_token_location is passed to the initialiser
    """

    def __init__(
        self, access_token_location: str = os.getenv("FBN_ACCESS_TOKEN_FILE", "")
    ):
        self.access_token = None
        # if neither are provided we won't want to override config from other loaders
        if access_token_location is not None and access_token_location != "":
            self.access_token = FileAccessToken(access_token_location)

    def load_config(self) -> Dict[str, Union[FileAccessToken, None]]:
        """load access token from file

        Returns
        -------
        Dict[str, str]
            dictionary that can be loaded into an ApiConfiguration object
        """
        return {"access_token": self.access_token}


default_config_loaders = (
    EnvironmentVariablesConfigurationLoader(),
    SecretsFileConfigurationLoader(api_secrets_file="secrets.json"),
    FileTokenConfigurationLoader()
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
            if value is not None and value != None
        }
        config.update(loaded_config)
    proxy_address = config.pop("proxy_address", None)
    proxy_username = config.pop("proxy_username", None)
    proxy_password = config.pop("proxy_password", None)
    # If the proxy address is missing ensure that no proxy is used in the ApiConfiguration
    if proxy_address is not None:
        config["proxy_config"] = ProxyConfig(
            address=proxy_address, username=proxy_username, password=proxy_password
        )
    else:
        config["proxy_config"] = None
    # Create and return the ApiConfiguration
    return ApiConfiguration(**config)