import time
from typing import Optional

import asyncio

from lusid.configuration import Configuration
from lusid.exceptions import ApiException


class RetryingRestWrapper:
    """Wrapper for HTTP requests
    Which retries on failure
    And waits the amount of time specified in the Retry After header.
    """
    def __init__(
        self, 
        rest_object, 
        retries: int = Configuration.DEFAULT_RETRIES, 
        rate_limit_retries: int = Configuration.DEFAULT_RATE_LIMIT_RETRIES
    ):
        if not isinstance(retries, int):
            raise TypeError(f"retries should be an int, found {type(retries)}")
        if retries < 0:
            raise ValueError(f"retries should be greater than or equal to zero but was '{retries}'")
        if not isinstance(rate_limit_retries, int):
            raise TypeError(f"rate_limit_retries should be an int, found {type(rate_limit_retries)}")
        if rate_limit_retries < 0:
            raise ValueError(f"rate_limit_retries should be greater than or equal to zero but was '{rate_limit_retries}'")
        self.retries: int = retries
        self.rate_limit_retries: int = rate_limit_retries
        self.rest_object = rest_object

    def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        body=None,
        post_params=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        retries_count = 0
        rate_limit_retries_count = 0

        while True:
            try:
                return self.rest_object.request(
                    method,
                    url,
                    query_params,
                    headers,
                    body,
                    post_params,
                    _preload_content,
                    _request_timeout,
                    opts,
                )
            except ApiException as ex:

                if ex.status == 429 and ((opts != None and opts.rate_limit_retries != None) or self.rate_limit_retries != None):
                    # check for limit of rate limit retries
                    limit = opts.rate_limit_retries if (opts and opts.rate_limit_retries != None) else self.rate_limit_retries
                    if rate_limit_retries_count >= limit:
                        raise
                    rate_limit_retries_count += 1
                else:
                    # check for limit of all other retries
                    if retries_count >= self.retries:
                        raise
                    retries_count += 1

                retry_after = ex.headers.get("Retry-After")

                # try after delay
                if retry_after is not None:
                    if not isinstance(retry_after, float):
                        try:
                            retry_after = float(retry_after)
                        except ValueError:
                            raise ValueError(
                                f"invalid Retry-After header value: {retry_after}"
                            )
                    time.sleep(retry_after)
                # no retry header
                else:
                    raise

    def get_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params,
                            opts=opts)

    def head_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params,
                            opts=opts)

    def options_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)

    def delete_request(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)

    def post_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)

    def put_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)

    def patch_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)


class RetryingRestWrapperAsync:
    """Wrapper for HTTP requests
    Which retries on failure
    And waits the amount of time specified in the Retry After header.
    """
    def __init__(self, rest_object, retries: int = 3, rate_limit_retries: Optional[int] = Configuration.DEFAULT_RATE_LIMIT_RETRIES):
        if not isinstance(retries, int):
            raise TypeError(f"retries should be an int, found {type(retries)}")
        if retries < 0:
            raise ValueError(f"retries should be greater than or equal to zero but was '{retries}'")
        if not isinstance(rate_limit_retries, int):
            raise TypeError(f"rate_limit_retries should be an int, found {type(rate_limit_retries)}")
        if rate_limit_retries < 0:
            raise ValueError(f"rate_limit_retries should be greater than or equal to zero but was '{rate_limit_retries}'")
        self.retries: int = retries
        self.rate_limit_retries: Optional[int] = rate_limit_retries
        self.rest_object = rest_object

    async def close(self):
        await self.rest_object.close()

    async def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        body=None,
        post_params=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        retries_count = 0
        rate_limit_retries_count = 0
        
        while True:
            try:
                return await self.rest_object.request(
                    method,
                    url,
                    query_params,
                    headers,
                    body,
                    post_params,
                    _preload_content,
                    _request_timeout,
                    opts
                )
            except ApiException as ex:

                if ex.status == 429 and ((opts and opts.rate_limit_retries != None) or self.rate_limit_retries != None):
                    # check for limit of rate limit retries
                    limit = opts.rate_limit_retries if (opts and opts.rate_limit_retries != None) else self.rate_limit_retries
                    if rate_limit_retries_count >= limit:
                        raise
                    rate_limit_retries_count += 1
                else:
                    # check for limit of all other retries
                    if retries_count >= self.retries:
                        raise
                    retries_count += 1

                retry_after = ex.headers.get("Retry-After")

                # try after delay
                if retry_after is not None:
                    if not isinstance(retry_after, float):
                        try:
                            retry_after = float(retry_after)
                        except ValueError:
                            raise ValueError(
                                f"invalid Retry-After header value: {retry_after}"
                            )
                    await asyncio.sleep(retry_after)
                # no retry header
                else:
                    raise

    async def get_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return (await self.request("GET", url,
                                   headers=headers,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   query_params=query_params,
                                   opts=opts))

    async def head_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return (await self.request("HEAD", url,
                                   headers=headers,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   query_params=query_params,
                                   opts=opts))

    async def options_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return (await self.request("OPTIONS", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body,
                                   opts=opts))

    async def delete_request(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return (await self.request("DELETE", url,
                                   headers=headers,
                                   query_params=query_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body,
                                   opts=opts))

    async def post_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return (await self.request("POST", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body,
                                   opts=opts))

    async def put_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return (await self.request("PUT", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body,
                                   opts=opts))

    async def patch_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
        opts=None,
    ):
        return (await self.request("PATCH", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body,
                                   opts=opts))
