from typing import Sequence
import socket
import logging
from urllib3.connection import HTTPConnection

__logger__ = logging.getLogger(__name__)


def keep_alive_socket_options() -> Sequence:
    """Returns default socket options for all platforms for
    setting keep alives on tcp connections.

    Returns
    -------
    Sequence
        Set of socket options.
    """
    # The content to send on Mac OS in the TCP Keep Alive probe
    TCP_KEEPALIVE = 0x10
    # The maximum time to keep the connection idle before sending probes
    TCP_KEEP_IDLE = 60
    # The interval between probes
    TCP_KEEPALIVE_INTERVAL = 60
    # The maximum number of failed probes before terminating the connection
    TCP_KEEP_CNT = 3

    try:
        # linux and some windows runtimes
        return HTTPConnection.default_socket_options + [
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
            (socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, TCP_KEEP_IDLE),
            (socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, TCP_KEEPALIVE_INTERVAL),
            (socket.IPPROTO_TCP, socket.TCP_KEEPCNT, TCP_KEEP_CNT),
        ]
    except AttributeError:
        pass
    try:
        # other windows runtimes
        return HTTPConnection.default_socket_options + [
            socket.SIO_KEEPALIVE_VALS,
            (1, TCP_KEEP_IDLE * 1000, TCP_KEEPALIVE_INTERVAL * 1000),
        ]
    except AttributeError:
        pass
    try:
        # darwin
        return HTTPConnection.default_socket_options + [
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
            (socket.IPPROTO_TCP, TCP_KEEPALIVE, TCP_KEEPALIVE_INTERVAL),
        ]
    except AttributeError:
        __logger__.exception("Unable to set TCP Keep-alive socket options")
        raise
