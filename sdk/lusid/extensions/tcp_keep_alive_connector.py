import aiohttp
from typing import List, Tuple, Any, Union
import socket
from urllib3 import HTTPSConnectionPool, HTTPConnectionPool
from lusid.extensions.socket_keep_alive import TCP_KEEPALIVE_INTERVAL, TCP_KEEP_IDLE


def adjust_connection_socket(conn):
    """
    Adjusts the socket settings so that the client sends a TCP keep alive probe over the connection. This is only
    applied where possible, if the ability to set the socket options is not available, for example using Anaconda,
    then the settings will be left as is.

    :param conn: The connection to update the socket settings for
    :param str protocol: The protocol of the connection

    :return: None
    """
    try:
        # set TCP keep alive interval on windows connections
        conn.ioctl(
            socket.SIO_KEEPALIVE_VALS,
            (1, TCP_KEEP_IDLE * 1000, TCP_KEEPALIVE_INTERVAL * 1000),
        )
    except AttributeError:
        pass


class TcpKeepAliveConnector(aiohttp.TCPConnector):
    """Replacement for aiohttp.TCPConnector
    which sets socket options on each connection.
    So we can use tcp keep alives which aiohttp has limited support for.
    """
    def __init__(
        self,
        connector: aiohttp.TCPConnector,
        socket_options: Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]]
    ) -> None:
        self.__connector = connector
        self.socket_options = socket_options or []

    @property
    def _timeout_ceil_threshold(self):
        return self.__connector._timeout_ceil_threshold

    @property
    def _loop(self):
        return self.__connector._loop

    @property
    def closed(self):
        return self.__connector.closed

    async def close(self) -> None:
        await self.__connector.close()

    async def connect(
        self,
        req: aiohttp.ClientRequest,
        traces: List[aiohttp.tracing.Trace],
        timeout: aiohttp.ClientTimeout,
    ) -> aiohttp.connector.Connection:
        """Wraps TCP connector, each new connection will have socket options
        and windows ioctl for keep alives applied

        Parameters
        ----------
        req : aiohttp.ClientRequest
        traces : List[aiohttp.tracing.Trace]
        timeout : aiohttp.ClientTimeout
        """
        connection = await self.__connector.connect(req, traces, timeout)
        sock = connection.protocol.transport.get_extra_info("socket")
        for option in self.socket_options:
            sock.setsockopt(*option)
        adjust_connection_socket(sock)
        return connection


class TCPKeepAliveHTTPSConnectionPool(HTTPSConnectionPool):
    """
    This class overrides the _validate_conn method in the HTTPSConnectionPool class. This is the entry point to use
    for modifying the socket as it is called after the socket is created and before the request is made.
    """

    def _validate_conn(self, conn):
        """
        Called right before a request is made, after the socket is created.
        """
        # Call the method on the base class
        super()._validate_conn(conn)

        # Set up TCP Keep Alive probes, this is the only line added to this function
        adjust_connection_socket(conn)


class TCPKeepAliveHTTPConnectionPool(HTTPConnectionPool):
    """
    This class overrides the _validate_conn method in the HTTPSConnectionPool class. This is the entry point to use
    for modifying the socket as it is called after the socket is created and before the request is made.

    In the base class this method is passed completely.
    """

    def _validate_conn(self, conn):
        """
        Called right before a request is made, after the socket is created.
        """
        # Call the method on the base class
        super()._validate_conn(conn)

        # Set up TCP Keep Alive probes, this is the only line added to this function
        adjust_connection_socket(conn)
