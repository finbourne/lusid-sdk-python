# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic.v1 import Field, constr, validator

from lusid.models.create_simple_position_portfolio_request import CreateSimplePositionPortfolioRequest
from lusid.models.portfolio import Portfolio

from lusid.api_client import ApiClient
from lusid.api_response import ApiResponse
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid.extensions.configuration_options import ConfigurationOptions


class SimplePositionPortfoliosApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def create_simple_position_portfolio(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope in which to create the simple position portfolio.")], create_simple_position_portfolio_request : Annotated[CreateSimplePositionPortfolioRequest, Field(..., description="The definition of the simple position portfolio.")], **kwargs) -> Portfolio:  # noqa: E501
        ...

    @overload
    def create_simple_position_portfolio(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope in which to create the simple position portfolio.")], create_simple_position_portfolio_request : Annotated[CreateSimplePositionPortfolioRequest, Field(..., description="The definition of the simple position portfolio.")], async_req: Optional[bool]=True, **kwargs) -> Portfolio:  # noqa: E501
        ...

    @validate_arguments
    def create_simple_position_portfolio(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope in which to create the simple position portfolio.")], create_simple_position_portfolio_request : Annotated[CreateSimplePositionPortfolioRequest, Field(..., description="The definition of the simple position portfolio.")], async_req: Optional[bool]=None, **kwargs) -> Union[Portfolio, Awaitable[Portfolio]]:  # noqa: E501
        """[EARLY ACCESS] CreateSimplePositionPortfolio: Create simple position portfolio  # noqa: E501

        Create a simple position portfolio in a particular scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_simple_position_portfolio(scope, create_simple_position_portfolio_request, async_req=True)
        >>> result = thread.get()

        :param scope: The scope in which to create the simple position portfolio. (required)
        :type scope: str
        :param create_simple_position_portfolio_request: The definition of the simple position portfolio. (required)
        :type create_simple_position_portfolio_request: CreateSimplePositionPortfolioRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Portfolio
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_simple_position_portfolio_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.create_simple_position_portfolio_with_http_info(scope, create_simple_position_portfolio_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_simple_position_portfolio_with_http_info(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope in which to create the simple position portfolio.")], create_simple_position_portfolio_request : Annotated[CreateSimplePositionPortfolioRequest, Field(..., description="The definition of the simple position portfolio.")], **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] CreateSimplePositionPortfolio: Create simple position portfolio  # noqa: E501

        Create a simple position portfolio in a particular scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_simple_position_portfolio_with_http_info(scope, create_simple_position_portfolio_request, async_req=True)
        >>> result = thread.get()

        :param scope: The scope in which to create the simple position portfolio. (required)
        :type scope: str
        :param create_simple_position_portfolio_request: The definition of the simple position portfolio. (required)
        :type create_simple_position_portfolio_request: CreateSimplePositionPortfolioRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Portfolio, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'scope',
            'create_simple_position_portfolio_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_simple_position_portfolio" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['scope']:
            _path_params['scope'] = _params['scope']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_simple_position_portfolio_request'] is not None:
            _body_params = _params['create_simple_position_portfolio_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '201': "Portfolio",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/simpleposition/{scope}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))