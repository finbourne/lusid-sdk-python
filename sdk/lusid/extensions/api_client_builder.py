from lusid.extensions.api_configuration import ApiConfiguration
import logging
import aiohttp
from typing import Union, Any, Optional, Tuple, Callable
from lusid.api_client import ApiClient as AsyncApiClient
from lusid.extensions.api_client import SyncApiClient
from lusid.extensions.refreshing_token import RefreshingToken
from lusid.configuration import Configuration
import lusid.extensions.retry as retry
from lusid.extensions.socket_keep_alive import keep_alive_socket_options
from lusid.extensions.tcp_keep_alive_connector import TcpKeepAliveConnector
import os

logger = logging.getLogger(__name__)


def _get_access_token(
    api_config: ApiConfiguration, id_provider_response_handler=None
):
    try:
        if api_config.access_token is not None:
            return api_config.access_token
        logger.debug(
            "Access token not provided, \
                will attempt to set up client using OIDC parameters"
        )
        return RefreshingToken(
            api_configuration=api_config,
            id_provider_response_handler=id_provider_response_handler,
        )
    except AttributeError:
        logger.exception(
            "Could not retrieve access token - ensure api_config is an ApiConfiguration object"
        )
        raise
    except ValueError:
        logger.exception(
            "Could not retrieve access token - ensure fields required to authenticate are set"
        )
        raise


def build_client(
    api_config: ApiConfiguration,
    build_async_client: bool = False,
    id_provider_response_handler: Callable = None,
    tcp_keep_alive: bool = False,
    socket_options: Optional[
        Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]]
    ] = None,
    correlation_id: Optional[str] = None,
    app_name: Optional[str] = None,
) -> Union[AsyncApiClient, SyncApiClient]:
    """Build an ApiClient that can be used to connect to LUSID.

    Parameters
    ----------
    api_config : ApiConfiguration
        configuration for the ApiClient, including auth.
    build_async_client : bool, optional
        Should a synchronous or async client be built, by default False
    id_provider_response_handler : Callable, optional
        A function that can be used to handle responses from identity providers, by default None
    tcp_keep_alive : bool, optional
        Set tcp_keep_alive options on client connections, by default False
    socket_options : Optional[ Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]] ], optional
        Custom socket options for client connections, by default None
    correlation_id : Optional[str], optional
        Sets an additional header on the client which 
        tags each request with a correlation id, by default None
    app_name : Optional[str], optional
        Name of the application, by default None

    Returns
    -------
    Union[AsyncApiClient, SyncApiClient]
        Either a synchronous or asynchronous ApiClient

    Raises
    ------
    ValueError
        Raised if necessary configuration not provided in ApiConfiguration object
    """
    try:
        if api_config.api_url is None:
            logger.error("Api Url must have a value")
            raise ValueError("Api Url must have a value")
        config = Configuration(
            access_token=_get_access_token(api_config, id_provider_response_handler),
            host=api_config.api_url,
            ssl_ca_cert=api_config.certificate_filename,
        )
        if tcp_keep_alive:
            config.socket_options = socket_options or keep_alive_socket_options()
        # Set the proxy for lusid if needed
        if api_config.proxy_config is not None:
            config.proxy = api_config.proxy_config.address
            config.proxy_headers = api_config.proxy_config.headers
    except (AttributeError, ValueError):
        logger.exception(
            "Unable to build api client, required configuration not provided"
        )
        raise

    if build_async_client:
        # Create and return the ApiClient
        api_client = AsyncApiClient(configuration=config)
        if tcp_keep_alive:
            connector = TcpKeepAliveConnector(
                limit=api_client.rest_client.pool_manager.connector.limit,
                ssl=api_client.rest_client.pool_manager.connector._ssl,
                socket_options=config.socket_options,
            )
            api_client.rest_client.pool_manager = aiohttp.ClientSession(
                connector=connector,
                trust_env=True
            )
        rest_client_wrapper = retry.RetryingRestWrapperAsync

    else:
        # Create and return the ApiClient
        api_client = SyncApiClient(configuration=config)
        rest_client_wrapper = retry.RetryingRestWrapper

    rc = api_client.rest_client
    wrapped_rest_client = rest_client_wrapper(rc)
    api_client.rest_client = wrapped_rest_client

    # set the application name if specified
    if app_name is not None:
        api_client.set_default_header("X-LUSID-Application", app_name)

    # set a correlation id for all requests initiated with this ApiClient
    corr_id = correlation_id or os.getenv("FBN_CORRELATION_ID")
    if corr_id is not None:
        api_client.set_default_header("CorrelationId", corr_id)

    return api_client
