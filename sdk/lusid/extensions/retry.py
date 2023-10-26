import time
from typing import overload

from lusid import ApiException
import asyncio


class RetryingRestWrapper:
    """Wrapper for HTTP requests
    Which retries on failure
    And waits the amount of time specified in the Retry After header.
    """
    def __init__(self, rest_object, retries: int = 3):
        if not isinstance(retries, int):
            raise ValueError(f"retries should be an int, found {type(self.retries)}")
        self.retries: int = retries
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
    ):
        tries = 0
        while tries < self.retries + 1:
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
                )
            except ApiException as ex:
                
                retry_after = ex.headers.get("Retry-After")

                # have done max number of retries
                if tries >= self.retries:
                    raise

                # try after delay
                elif retry_after is not None:
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
                tries += 1

    def get_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def head_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def options_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def delete_request(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def post_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def put_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def patch_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class RetryingRestWrapperAsync:
    """Wrapper for HTTP requests
    Which retries on failure
    And waits the amount of time specified in the Retry After header.
    """
    def __init__(self, rest_object, retries: int = 3):
        if not isinstance(retries, int):
            raise ValueError(f"retries should be an int, found {type(self.retries)}")
        self.retries: int = retries
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
    ):
        tries = 0
        while tries < self.retries + 1:
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
                )
            except ApiException as ex:
                retry_after = ex.headers.get("Retry-After")

                # have done max number of retries
                if tries >= self.retries:
                    raise

                # try after delay
                elif retry_after is not None:
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
                tries += 1

    async def get_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return (await self.request("GET", url,
                                   headers=headers,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   query_params=query_params))

    async def head_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return (await self.request("HEAD", url,
                                   headers=headers,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   query_params=query_params))

    async def options_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return (await self.request("OPTIONS", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))

    async def delete_request(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return (await self.request("DELETE", url,
                                   headers=headers,
                                   query_params=query_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))

    async def post_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return (await self.request("POST", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))

    async def put_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return (await self.request("PUT", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))

    async def patch_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return (await self.request("PATCH", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))
