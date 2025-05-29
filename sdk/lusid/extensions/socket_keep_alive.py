from typing import Sequence
import socket
import logging
from urllib3.connection import HTTPConnection
import platform

__logger__ = logging.getLogger(__name__)

# The content to send on Mac OS in the TCP Keep Alive probe
TCP_KEEPALIVE = 0x10
# The maximum time to keep the connection idle before sending probes
TCP_KEEP_IDLE = 60
# The interval between probes
TCP_KEEPALIVE_INTERVAL = 60
# The maximum number of failed probes before terminating the connection
TCP_KEEP_CNT = 3


def keep_alive_socket_options() -> Sequence:
    """Returns default socket options for all platforms for
    setting keep alives on tcp connections.

    Returns
    -------
    Sequence
        Set of socket options.
    """
    base_options = HTTPConnection.default_socket_options
    system = platform.system().title()

    if system == "Windows":
        # Only SO_KEEPALIVE is supported and safe on Windows Server 2016
        __logger__.info("Setting socket settings for Windows")
        return base_options + [
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        ]
    elif system == "Darwin":
        # macOS specific
        __logger__.info("Setting socket settings for Darwin (macOS)")
        TCP_KEEPALIVE = 0x10  # from <netinet/tcp.h>
        return base_options + [
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
            (socket.IPPROTO_TCP, TCP_KEEPALIVE, 60)
        ]
    elif system == "Linux":
        # Safe on Linux
        __logger__.info("Setting socket settings for Linux")
        return base_options + [
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
            (socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60),
            (socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60),
            (socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 3)
        ]
    else:
        __logger__.warning("Unsupported platform for TCP keep-alive fine-tuning. Using basic SO_KEEPALIVE.")
        return base_options + [
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        ]
