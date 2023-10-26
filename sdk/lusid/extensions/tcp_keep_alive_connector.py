from ssl import SSLContext
import aiohttp
import asyncio
from typing import List, Tuple, Any, Union, Optional


class TcpKeepAliveConnector(aiohttp.TCPConnector):
    """Replacement for aiohttp.TCPConnector
    which sets socket options on each connection.
    So we can use tcp keep alives which aiohttp has limited support for.
    """
    def __init__(
        self,
        *,
        verify_ssl: bool = True,
        fingerprint: Optional[bytes] = None,
        use_dns_cache: bool = True,
        ttl_dns_cache: Optional[int] = 10,
        family: int = 0,
        ssl_context: Optional[SSLContext] = None,
        ssl: Union[None, bool, aiohttp.Fingerprint, SSLContext] = None,
        local_addr: Optional[Tuple[str, int]] = None,
        resolver: Optional[aiohttp.abc.AbstractResolver] = None,
        keepalive_timeout: Union[None, float, object] = aiohttp.helpers.sentinel,
        force_close: bool = False,
        limit: int = 100,
        limit_per_host: int = 0,
        enable_cleanup_closed: bool = False,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        socket_options: Union[Tuple[Any, Any, Any], Tuple[Any, Any, None, int]]
    ) -> None:
        super().__init__(
            verify_ssl=verify_ssl,
            fingerprint=fingerprint,
            use_dns_cache=use_dns_cache,
            ttl_dns_cache=ttl_dns_cache,
            family=family,
            ssl_context=ssl_context,
            ssl=ssl,
            local_addr=local_addr,
            resolver=resolver,
            keepalive_timeout=keepalive_timeout,
            force_close=force_close,
            limit=limit,
            limit_per_host=limit_per_host,
            enable_cleanup_closed=enable_cleanup_closed,
            loop=loop,
        )
        self.socket_options = socket_options or []

    async def _create_connection(
        self,
        req: aiohttp.ClientRequest,
        traces: List[aiohttp.tracing.Trace],
        timeout: aiohttp.ClientTimeout,
    ) -> aiohttp.client_proto.ResponseHandler:
        if req.proxy:
            transport, proto = await self._create_proxy_connection(req, traces, timeout)
        else:
            transport, proto = await self._create_direct_connection(
                req, traces, timeout
            )
        sock = transport.get_extra_info("socket")
        for option in self.socket_options:
            sock.setsockopt(*option)
        return proto
