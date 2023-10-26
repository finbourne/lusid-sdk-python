from __future__ import annotations
from lusid.extensions.configuration_loaders import (
    ConfigurationLoader,
    default_config_loaders,
)
from lusid.extensions.api_client_builder import build_client
from lusid.extensions.configuration_loaders import get_api_configuration
import logging
from typing import TypeVar, Type, Iterable

logger = logging.getLogger(__name__)

T = TypeVar("T")


class SyncApiClientFactory:
    def __init__(
        self,
        config_loaders: Iterable[ConfigurationLoader] = default_config_loaders,
        id_provider_response_handler=None,
        tcp_keep_alive=None,
        correlation_id=None,
        app_name=None
    ):
        """Create an ApiClientFactory which can build api objects with a configured ApiClient object

        Parameters
        ----------
        config_loaders : Iterable[ConfigurationLoader], optional
            An Iterable of ConfigurationLoaders we can load configuration from.
            Config settings are updated by each loader (last write wins), by default default_config_loaders
        id_provider_response_handler : _type_, optional
             A function that is called when a response is received from the token_url., by default None
        tcp_keep_alive : _type_, optional
            Should ApiClient be configured to send tcp keep alives., by default None
        correlation_id : _type_, optional
            A correlation ID that can be sent with each request., by default None
        app_name : _type_, optional
            The name of the application in LUSID., by default None
        """
        api_config = get_api_configuration(config_loaders=config_loaders)
        self.__api_client = build_client(
            api_config,
            build_async_client=False,
            id_provider_response_handler=id_provider_response_handler,
            tcp_keep_alive=tcp_keep_alive,
            correlation_id=correlation_id,
            app_name=app_name
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
        id_provider_response_handler=None,
        tcp_keep_alive=None,
        correlation_id=None,
        app_name=None
    ):
        """Create an ApiClientFactory which can build api objects with a configured ApiClient object

        Parameters
        ----------
        config_loaders : Iterable[ConfigurationLoader], optional
            An Iterable of ConfigurationLoaders we can load configuration from.
            Config settings are updated by each loader (last write wins), by default default_config_loaders
        id_provider_response_handler : _type_, optional
             A function that is called when a response is received from the token_url., by default None
        tcp_keep_alive : _type_, optional
            Should ApiClient be configured to send tcp keep alives., by default None
        correlation_id : _type_, optional
            A correlation ID that can be sent with each request., by default None
        app_name : _type_, optional
            The name of the application in LUSID., by default None
        """
        api_config = get_api_configuration(config_loaders=config_loaders)
        self.__api_client = build_client(
            api_config,
            build_async_client=True,
            id_provider_response_handler=id_provider_response_handler,
            tcp_keep_alive=tcp_keep_alive,
            correlation_id=correlation_id,
            app_name=app_name
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
