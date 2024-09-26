import re
import logging
from typing import Optional, Union, Tuple, Any, Callable
from lusid.configuration import Configuration, Timeouts
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.extensions.refreshing_token import RefreshingToken
from lusid.extensions.socket_keep_alive import keep_alive_socket_options
from lusid.extensions.proxy_config import ProxyConfig
from requests import Response
logger = logging.getLogger(__name__)


class ApiConfiguration:
    def __init__(
        self,
        token_url=None,
        api_url=None,
        username=None,
        password=None,
        client_id=None,
        client_secret=None,
        app_name=None,
        certificate_filename=None,
        proxy_config:Optional[ProxyConfig]=None,
        access_token=None,
        total_timeout_ms=None,
        connect_timeout_ms=None,
        read_timeout_ms=None,
        rate_limit_retries=None,
    ):
        """
        The configuration required to access LUSID, read more at https://support.finbourne.com/getting-started-with-apis-sdks

        :param str token_url: The token URL of the identity provider
        :param str api_url: The API URL for the LUSID client
        :param str username: The username to use
        :param str password: The password to use
        :param str client_id: The client id to use
        :param str client_secret: The client secret to use
        :param str app_name: The name of the application calling LUSID
        :param str certificate_filename: Name of the certificate file (.pem, .cer or .crt)
        :param lusid.extensions.ProxyConfig proxy_config: The proxy configuration to use
        """
        self.__token_url = token_url
        self.__api_url = api_url
        self.__username = username
        self.__password = password
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__app_name = app_name
        self.__certificate_filename = certificate_filename
        self.__proxy_config = proxy_config
        self.__access_token = access_token
        self.__total_timeout_ms = total_timeout_ms
        self.__connect_timeout_ms = connect_timeout_ms
        self.__read_timeout_ms = read_timeout_ms
        self.__rate_limit_retries = rate_limit_retries

    @property
    def token_url(self):
        return self.__token_url

    @token_url.setter
    def token_url(self, value):
        def format_token_url(url: str) -> str:
            """
            Given an Okta issuer url (ie: https://lusid-testdomain.okta.com/oauth2/asd8f7a98sdf89a7ad), this function
            will return a full token url (ie: https://lusid-testdomain.okta.com/oauth2/asd8f7a98sdf89a7ad/v1/token)
            :param url: The url to format
            :return: An Okta token url (if the input is an Okta issuer url). The original url otherwise.
            """
            if (
                url is not None
                and
                # and it's an Okta oauth2 URL
                re.search(
                    r"^http(s)?:\/\/.*\.okta\.com\/oauth2\/.+", url, flags=re.IGNORECASE
                )
                is not None
                and
                # and it's missing the token suffix
                re.search(r"\/v\d+\/token$", url, flags=re.IGNORECASE) is None
            ):
                return url.rstrip("/") + "/v1/token"
            return url

        self.__token_url = format_token_url(value)

    @property
    def api_url(self):
        return self.__api_url

    @api_url.setter
    def api_url(self, value):
        self.__api_url = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def client_secret(self):
        return self.__client_secret

    @client_secret.setter
    def client_secret(self, value):
        self.__client_secret = value

    @property
    def app_name(self):
        return self.__app_name

    @app_name.setter
    def app_name(self, value):
        self.__app_name = value

    @property
    def certificate_filename(self):
        return self.__certificate_filename

    @certificate_filename.setter
    def certificate_filename(self, value):
        self.__certificate_filename = value

    @property
    def proxy_config(self):
        return self.__proxy_config

    @proxy_config.setter
    def proxy_config(self, value):
        self.__proxy_config = value

    def __setattr__(self, name, value):
        if name == "access_token":
            self.__access_token = value
        super(ApiConfiguration, self).__setattr__(name, value)

    def get_access_token(
        self, id_provider_response_handler: Callable[[Response], None] = None
    ) -> Union[str, RefreshingToken]:
        """Gets either the set personal access token, or a RefreshingToken using OIDC parameters

        Returns
        -------
        Union[str, RefreshingToken]
            Token that can be used to authenticate to LUSID

        """
        try:
            if self.__access_token is not None:
                return self.__access_token
            logger.debug(
                "Access token not provided, \
                    will attempt to set up client using OIDC parameters"
            )
            return RefreshingToken(
                api_configuration=self,
                id_provider_response_handler=id_provider_response_handler,
            )
        except AttributeError:
            logger.exception(
                "Could not retrieve access token - "
                "ensure api_config is an ApiConfiguration object"
            )
            raise
        except ValueError:
            logger.exception(
                "Could not retrieve access token - "
                "ensure fields required to authenticate are set"
            )
            raise

    @property
    def total_timeout_ms(self):
        return self.__total_timeout_ms

    @total_timeout_ms.setter
    def total_timeout_ms(self, value):
        self.__total_timeout_ms = value

    @property
    def connect_timeout_ms(self):
        return self.__connect_timeout_ms

    @connect_timeout_ms.setter
    def connect_timeout_ms(self, value):
        self.__connect_timeout_ms = value

    @property
    def read_timeout_ms(self):
        return self.__read_timeout_ms

    @read_timeout_ms.setter
    def read_timeout_ms(self, value):
        self.__read_timeout_ms = value

    @property
    def rate_limit_retries(self):
        return self.__rate_limit_retries


    def build_api_client_config(
        self,
        tcp_keep_alive: bool = True,
        socket_options: Optional[
            Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]]
        ] = keep_alive_socket_options(),
        id_provider_response_handler: Optional[Callable[[Response], None]] = None,
        opts: ConfigurationOptions = None,
    ) -> Configuration:
        """Builds lusid.Configuration for initialising an api client.

        Parameters
        ----------
        tcp_keep_alive : bool, optional
            Should socket options for tcp keep alive pings be set, by default True
        socket_options : Optional[ Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]] ], optional
            A set of custom options to configure on connections, by default keep_alive_socket_options()
        id_provider_response_handler : Optional[Callable[[Response], None]], optional
            A function to run on response from the identity provider, by default None

        Returns
        -------
        Configuration
            config which can be used to initialise an api client
        """
        access_token = self.get_access_token(
            id_provider_response_handler=id_provider_response_handler
        )
        try:
            if self.api_url is None:
                logger.error("Api Url must have a value")
                raise ValueError("Api Url must have a value")
            if access_token is None:
                logger.error("Access token must have a value")
                raise ValueError("Access token must have a value")
            config = Configuration(
                access_token=access_token,
                host=self.api_url,
                ssl_ca_cert=self.certificate_filename,
                timeouts=Timeouts(
                    total_timeout_ms=opts.total_timeout_ms if opts and opts.total_timeout_ms != None else 
                        self.total_timeout_ms if self.total_timeout_ms != None else Configuration.DEFAULT_TOTAL_TIMEOUT_MS,
                    connect_timeout_ms=opts.connect_timeout_ms if opts and opts.connect_timeout_ms != None else 
                        self.connect_timeout_ms if self.connect_timeout_ms != None else Configuration.DEFAULT_CONNECT_TIMEOUT_MS,
                    read_timeout_ms=opts.read_timeout_ms if opts and opts.read_timeout_ms != None else 
                        self.read_timeout_ms if self.read_timeout_ms != None else Configuration.DEFAULT_READ_TIMEOUT_MS
                ),
                rate_limit_retries=opts.rate_limit_retries if opts != None and opts.rate_limit_retries != None else 
                        self.rate_limit_retries if self.rate_limit_retries != None else Configuration.DEFAULT_RATE_LIMIT_RETRIES
            )
            if tcp_keep_alive:
                config.socket_options = socket_options or keep_alive_socket_options()
            # Set the proxy for lusid if needed
            if self.proxy_config is not None:
                config.proxy = self.proxy_config.address
                config.proxy_headers = self.proxy_config.headers
            return config
        except (AttributeError, ValueError):
            logger.exception(
                "Unable to build api client, required configuration not provided"
            )
            raise
