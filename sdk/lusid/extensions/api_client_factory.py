from __future__ import annotations
from lusid.api_client import ApiClient
from lusid.extensions.retry import (
    RetryingRestWrapper,
    RetryingRestWrapperAsync
)
from lusid.extensions.api_client import SyncApiClient
from lusid.extensions.configuration_loaders import (
    ConfigurationLoader,
    default_config_loaders,
    get_api_configuration
)
from lusid.extensions.socket_keep_alive import keep_alive_socket_options
from lusid.extensions.tcp_keep_alive_connector import (
    TcpKeepAliveConnector,
    TCPKeepAliveHTTPConnectionPool,
    TCPKeepAliveHTTPSConnectionPool,
)
from aiohttp import ClientSession
import logging
from typing import Any, Callable, Optional, Tuple, TypeVar, Type, Iterable, Union
import os
from requests import Response

logger = logging.getLogger(__name__)

T = TypeVar("T")


def set_additional_api_client_headers(
    api_client: Union[ApiClient, SyncApiClient],
    app_name: Optional[str] = None,
    correlation_id: Optional[str] = None,
) -> None:
    """Sets additional headers for additional debugging info in LUSID

    Parameters
    ----------
    api_client : Union[ApiClient, SyncApiClient]
        api client to set headers on
    app_name : Optional[str], optional
        name of the application in LUSID, by default None
    correlation_id : Optional[str], optional
        correlation id to track requests in LUSID, by default None
    """
    try:
        # set the application name if specified
        if app_name is not None:
            api_client.set_default_header("X-LUSID-Application", app_name)

        # set a correlation id for all requests initiated with this ApiClient
        corr_id = correlation_id or os.getenv("FBN_CORRELATION_ID")
        if corr_id is not None:
            api_client.set_default_header("CorrelationId", corr_id)
    except AttributeError:
        logger.exception("api_client must be either an ApiClient or a SyncApiClient")
        raise


class SyncApiClientFactory:
    def __init__(
        self,
        config_loaders: Iterable[ConfigurationLoader] = default_config_loaders,
        id_provider_response_handler: Callable[[Response], None] = None,
        tcp_keep_alive: bool = True,
        socket_options: Optional[
            Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]]
        ] = keep_alive_socket_options(),
        correlation_id: Optional[str] = None,
        app_name: Optional[str] = None,
    ):
        """Create an ApiClientFactory which can build
        api objects with a configured ApiClient object

        Parameters
        ----------
        config_loaders : Iterable[ConfigurationLoader], optional
        An Iterable of ConfigurationLoaders we can load configuration from.
        Config settings are updated by each loader (last write wins),
        by default default_config_loaders,
        by default default_config_loaders
        id_provider_response_handler : Callable[[Response], None], optional
        A function that is called when a response is received from the token_url,
        by default None
        tcp_keep_alive : bool, optional
        Should ApiClient be configured to send tcp keep alives, by default True
        socket_options : Optional[ Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]] ], optional
        Set of socket options that should be applied to each connection, 
        by default keep_alive_socket_options
        correlation_id : Optional[str], optional
        A correlation ID that can be sent with each request, by default None
        app_name : Optional[str], optional
        The name of the application in LUSID, by default None
        """
        api_config = get_api_configuration(config_loaders=config_loaders)
        api_client_config = api_config.build_api_client_config(
            tcp_keep_alive=tcp_keep_alive,
            socket_options=socket_options,
            id_provider_response_handler=id_provider_response_handler
        )
        self.__api_client = SyncApiClient(
            configuration=api_client_config,
        )

        rest_client_wrapper = RetryingRestWrapper
        rc = self.__api_client.rest_client
        if tcp_keep_alive:
            rc.pool_manager.pool_classes_by_scheme = {"http": TCPKeepAliveHTTPConnectionPool, "https": TCPKeepAliveHTTPSConnectionPool}

        wrapped_rest_client = rest_client_wrapper(rc)
        self.__api_client.rest_client = wrapped_rest_client

        set_additional_api_client_headers(
            self.__api_client, app_name=app_name, correlation_id=correlation_id
        )

    def __enter__(self):
        self.__api_client.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__api_client.__exit__(exc_type, exc_value, traceback)

    def build(
        self,
        metaclass: Type[T],
    ) -> T:
        """Returns an instance of the api metaclass with a configured ApiClient

        Parameters
        ----------
        metaclass : Type[T]
            A lusid.api class.


        Returns
        -------
        T
            An instance of the lusid.api class with a configured ApiClient
        """
        return metaclass(self.__api_client)


class ApiClientFactory:
    def __init__(
        self,
        config_loaders: Iterable[ConfigurationLoader] = default_config_loaders,
        id_provider_response_handler: Callable[[Response], None] = None,
        tcp_keep_alive: bool = True,
        socket_options: Optional[
            Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]]
        ] = keep_alive_socket_options(),
        correlation_id: Optional[str] = None,
        app_name: Optional[str] = None,
        client_session: Optional[ClientSession] = None
    ):
        """Create an ApiClientFactory which can build api 
        objects with a configured ApiClient object

        Parameters
        ----------
        config_loaders : Iterable[ConfigurationLoader], optional
        An Iterable of ConfigurationLoaders we can load configuration from.
        Config settings are updated by each loader (last write wins), ]
        by default default_config_loaders
        id_provider_response_handler : Callable[[Response], None], optional
        A function that is called when a response is received from the token_url,
        by default None
        tcp_keep_alive : bool, optional
        Should ApiClient be configured to send tcp keep alives, by default True
        socket_options : Optional[ Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]] ], optional
        Set of socket options that should be applied to each connection,
        by default keep_alive_socket_options
        correlation_id : Optional[str], optional
        A correlation ID that can be sent with each request, by default None
        app_name : Optional[str], optional
        The name of the application in LUSID, by default None
        client_session : Optional[ClientSession], optional
        An aiohttp.ClientSession, pass this to re-use 
        connections across different ApiFactories,
        by default None
        """
        api_config = get_api_configuration(config_loaders=config_loaders)
        api_client_config = api_config.build_api_client_config(
            tcp_keep_alive=tcp_keep_alive,
            socket_options=socket_options,
            id_provider_response_handler=id_provider_response_handler
        )
        self.__api_client = ApiClient(
            configuration=api_client_config,
        )
        rc = self.__api_client.rest_client
        try:
            if client_session is not None:
                connector = client_session.connector
            else:
                connector = rc.pool_manager.connector
            if tcp_keep_alive:
                connector = TcpKeepAliveConnector(connector=connector, socket_options=socket_options)
            rc.pool_manager = ClientSession(
                connector=connector,
                trust_env=True
            )
        except AttributeError:
            logger.exception("client_session must be an aiohttp.ClientSession"
                             " object with an initialised TCP Connector")
        rest_client_wrapper = RetryingRestWrapperAsync
        wrapped_rest_client = rest_client_wrapper(rc)
        self.__api_client.rest_client = wrapped_rest_client
        set_additional_api_client_headers(
            self.__api_client, app_name=app_name, correlation_id=correlation_id
        )

    async def __aenter__(self):
        await self.__api_client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.__api_client.__aexit__(exc_type, exc_value, traceback)

    def build(
        self,
        metaclass: Type[T],
    ) -> T:
        """Returns an instance of the api metaclass with a configured ApiClient

        Parameters
        ----------
        metaclass : Type[T]
            A lusid.api class.


        Returns
        -------
        T
            An instance of the lusid.api class with a configured ApiClient
        """
        return metaclass(self.__api_client)
