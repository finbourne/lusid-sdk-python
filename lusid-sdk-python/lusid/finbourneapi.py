# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError
from . import models


class FINBOURNEAPIConfiguration(Configuration):
    """Configuration for FINBOURNEAPI
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'http://localhost'

        super(FINBOURNEAPIConfiguration, self).__init__(base_url)

        self.add_user_agent('finbourneapi/{}'.format(VERSION))

        self.credentials = credentials


class FINBOURNEAPI(object):
    """# Immutable Events
    A core tenet of the LUSID platform is the concept of an immutable data store.  This gives the ability to consistently reproduce the state of the system for any given point in bi-temporal space.  In order to achieve this LUSID has implemented an append only event store for all data types.  New events, including historical amendments, are added to the end of the event stream and then played back in order to construct the state.  Given that all the events from T0 are required in order to reconstruct the state, there can be significant computational complexity and cost involved.  FINBOURNE have employed a number of techniques and optimisations in order to produce consistent performance characteristics e.g. using snapshots which has resulted in a highly performance and scalable platform.
    # Scope
    All entities within LUSID live within a logical partitioning of data know as a scope.  Any given entity can only live within one scope and is addressable with a unique identifier.
    For example, prices for equities from different vendors may be uploaded into different scopes such as `client/vendor1` and `client/vendor2`.  A portfolio may then be valued using either of the price sources by referencing the appropriate scope.
    It should be noted that scopes are not hierarchical and 2 different scopes which may contain the same path elements do not have any relationship.
    # Data Model
    Below is a summary of the key data types exposed via the API and their relationships.
    ## Schema
    A detailed description of the entities used by the API and parameters for endpoints which take a JSON document can be retrieved via the `schema` endpoint.
    ## Securities
    LUSID has its own security master implementation (LUSID CORE) which sources reference data form multiple data vendors.  With the appropriate entitlements, clients are able to upload securities into their portfolios using any OpenFIGI identifier.
    Cash can be uploaded using the ISO currency code prefixed with "`CCY_`" e.g. `CCY_GBP`
    For any securities that a client wants to upload but it not supported or recognised by LUSID, LUSID provides the ability to upload a client defined security.  A client defined security is only available within a client's data scope (subject to appropriate entitlements) and also has the ability to have properties and analytics attached to it.  Securitised portfolios and funds can be modelled as client defined securities.
    ## Trade
    A trade represents a transaction in a security or cash.
    ## Holding
    A holding represents an aggregate position in a security or cash on a given `effectiveDate`.  When uploading a holding for a given `effectiveDate`, LUSID will generate any trades required to construct the holding position from previous holdings.  Any generated trades will be marked with a source of `SYSTEM`.
    ## Portfolio
    A portfolio is a container for trades.  Meta data and classifications of portfolios can be attached via properties.
    LUSID also allows for a portfolio to be composed of another portfolio via derived portfolios.  A derived portfolio can contain its own trades and also inherits any trades from a reference portfolio.  Any changes made to the underlying reference portfolio are automatically reflected in derived portfolio.
    Reference portfolios in conjunction with scopes are a powerful construct.  For example, to do pre-trade what-if analysis, a reference portfolio could be created a new namespace linked to the underlying live portfolio.  Analysis can then be undertaken within the reference portfolio without affecting the live portfolio.
    ## Property
    Properties are key-value pairs that can be applied to any entity within a domain (where a domain is `trade`, `portfolio`, `security` etc).  Properties must be defined before use with a `PropertyDefinition` and can then subsequently be added to entities.
    # Movements Engine
    When generating holdings, LUSID passes trades through its Movements Engine which will manage cash flows within the portfolio such as cash balance adjustments, fees, tax etc.
    # Examples
    ## Authentication
    ## Create Portfolio
    ## Add Trades
    ## Add Holdings
    ## Update Trade/Holding
    ## Aggregation
    # Error Codes
    ## 100
    ### Personalisations not found.\n\nThe personalisation(s) identified by the pattern provided could not be found, either because it does not exist or it has been deleted. Please check the pattern your provided.
    ## 101
    NonRecursivePersonalisation
    ## 102
    VersionNotFound
    ## 104
    SecurityByCodeNotFound
    ## 104
    SecurityByCodeNotFound
    ## 105
    PropertyNotFound
    ## 106
    PortfolioRecursionDepth
    ## 108
    GroupNotFound
    ## 109
    PortfolioNotFound
    ## 110
    PropertySchemaNotFound
    ## 112
    PortfolioWithIdAlreadyExists
    ## 113
    OrphanedPortfolio
    ## 119
    MissingBaseClaims
    ## 121
    PropertyNotDefined
    ## 122
    CannotDeleteSystemProperty
    ## 123
    CannotModifyImmutablePropertyField
    ## 124
    PropertyAlreadyExists
    ## 125
    InvalidPropertyLifeTime
    ## 127
    CannotModifyDefaultPropertyFormat
    ## 128
    GroupAlreadyExists
    ## 129
    NoSuchPropertyDataFormat
    ## 132
    ValidationError
    ## 133
    LoopDetectedInGroupHierarchy
    ## 135
    SubGroupAlreadyExists
    ## 138
    PriceSourceNotFound
    ## 139
    AnalyticStoreNotFound
    ## 141
    AnalyticStoreAlreadyExists
    ## 143
    ClientSecurityAlreadyExists
    ## 144
    DuplicateInParameterSet
    ## 147
    ResultsNotFound
    ## 148
    OrderFieldNotInResultSet
    ## 149
    OperationFailed
    ## 150
    ElasticSearchError
    ## 151
    InvalidParameterValue
    ## 152
    ServerConfigurationError
    ## 153
    CommandProcessingFailure
    ## 154
    EntityStateConstructionFailure
    ## 155
    EntityTimelineDoesNotExist
    ## 156
    EventPublishFailure
    ## 157
    InvalidRequestFailure
    ## 158
    EventPublishUnknown
    ## 159
    EventQueryFailure
    ## 160
    BlobDidNotExistFailure
    ## 162
    SubSystemRequestFailure
    ## 163
    SubSystemConfigurationFailure
    ## 165
    FailedToDelete
    ## 166
    UpsertClientSecurityFailure
    ## 167
    IllegalAsAtInterval
    ## 168
    IllegalBitemporalQuery
    ## 169
    InvalidAlternateId
    ## 170
    CannotAddSourcePortfolioPropertyExplicitly
    ## 171
    EntityAlreadyExistsInGroup
    ## 173
    EntityWithIdAlreadyExists
    ## 174
    PortfolioDetailsDoNotExist
    ## 176
    PortfolioWithNameAlreadyExists
    ## 177
    InvalidTrades
    ## 178
    ReferencePortfolioNotFound
    ## 179
    DuplicateIdFailure
    ## 180
    CommandRetrievalFailure
    ## 181
    DataFilterApplicationFailure
    ## 182
    SearchFailed
    ## -1
    Unknown error

    :ivar config: Configuration for client.
    :vartype config: FINBOURNEAPIConfiguration

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = FINBOURNEAPIConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '0.6.23'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def get_by_group(
            self, scope, group_code, request=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data in a group hierarchy.

        :param scope:
        :type scope: str
        :param group_code:
        :type group_code: str
        :param request:
        :type request: ~lusid.models.AggregationRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_by_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'groupCode': self._serialize.url("group_code", group_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GetAggregationResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_group.metadata = {'url': '/v1/api/aggregation/groups/{scope}/{groupCode}'}

    def get_nested_data_aggregation_by_group(
            self, scope, group_code, request=None, custom_headers=None, raw=False, **operation_config):
        """Aggregation request data in a group hierarchy into a data tree.

        :param scope:
        :type scope: str
        :param group_code:
        :type group_code: str
        :param request:
        :type request: ~lusid.models.AggregationRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_nested_data_aggregation_by_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'groupCode': self._serialize.url("group_code", group_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('NestedDataAggregationResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_nested_data_aggregation_by_group.metadata = {'url': '/v1/api/aggregation/groups/nested/{scope}/{groupCode}'}

    def get_by_portfolio(
            self, scope, portfolio_code, request=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data in a portfolio.

        :param scope:
        :type scope: str
        :param portfolio_code:
        :type portfolio_code: str
        :param request:
        :type request: ~lusid.models.AggregationRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_by_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'portfolioCode': self._serialize.url("portfolio_code", portfolio_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GetAggregationResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_portfolio.metadata = {'url': '/v1/api/aggregation/portfolios/{scope}/{portfolioCode}'}

    def get_nested_data_aggregation_by_portfolio(
            self, scope, portfolio_code, request=None, custom_headers=None, raw=False, **operation_config):
        """Aggregation request data in a portfolio into a data tree.

        :param scope:
        :type scope: str
        :param portfolio_code:
        :type portfolio_code: str
        :param request:
        :type request: ~lusid.models.AggregationRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_nested_data_aggregation_by_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'portfolioCode': self._serialize.url("portfolio_code", portfolio_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('NestedDataAggregationResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_nested_data_aggregation_by_portfolio.metadata = {'url': '/v1/api/aggregation/portfolios/nested/{scope}/{portfolioCode}'}

    def get_by_results(
            self, scope, results_key, results_date, request=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data from a result set.

        :param scope:
        :type scope: str
        :param results_key:
        :type results_key: str
        :param results_date:
        :type results_date: str
        :param request:
        :type request: ~lusid.models.AggregationRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_by_results.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'resultsKey': self._serialize.url("results_key", results_key, 'str'),
            'resultsDate': self._serialize.url("results_date", results_date, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GetAggregationResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_results.metadata = {'url': '/v1/api/aggregation/results/{scope}/{resultsKey}/{resultsDate}'}

    def get_nested_data_aggregation_by_results(
            self, scope, results_key, results_date, request=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data from a result set into a nested structure.

        :param scope:
        :type scope: str
        :param results_key:
        :type results_key: str
        :param results_date:
        :type results_date: datetime
        :param request:
        :type request: ~lusid.models.AggregationRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_nested_data_aggregation_by_results.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'resultsKey': self._serialize.url("results_key", results_key, 'str'),
            'resultsDate': self._serialize.url("results_date", results_date, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('NestedDataAggregationResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_nested_data_aggregation_by_results.metadata = {'url': '/v1/api/aggregation/results/nested/{scope}/{resultsKey}/{resultsDate}'}

    def list_analytic_stores(
            self, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """List all analytic stores in client.

        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_analytic_stores.metadata['url']

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListAnalyticStoreKeyDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_analytic_stores.metadata = {'url': '/v1/api/analytics'}

    def create_analytic_store(
            self, request=None, custom_headers=None, raw=False, **operation_config):
        """Create a new analytic store for the given scope for the given date.

        :param request: A valid and fully populated analytic store creation
         request
        :type request: ~lusid.models.CreateAnalyticStoreRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_analytic_store.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreateAnalyticStoreRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('AnalyticStoreDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_analytic_store.metadata = {'url': '/v1/api/analytics'}

    def get_analytic_store(
            self, scope, year, month, day, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get an analytic store.

        :param scope: The analytics data scope
        :type scope: str
        :param year: The year component of the date for the data in the scope
        :type year: int
        :param month: The month component of the date for the data in the
         scope
        :type month: int
        :param day: The day component of the date for the data in the scope
        :type day: int
        :param as_at: AsAt date
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_analytic_store.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'year': self._serialize.url("year", year, 'int'),
            'month': self._serialize.url("month", month, 'int'),
            'day': self._serialize.url("day", day, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AnalyticStoreDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_analytic_store.metadata = {'url': '/v1/api/analytics/{scope}/{year}/{month}/{day}'}

    def delete_analytic_store(
            self, scope, year, month, day, custom_headers=None, raw=False, **operation_config):
        """Create a new analytic store for the given scope for the given date.

        :param scope: The analytics data scope
        :type scope: str
        :param year: The year component of the date for the data in the scope
        :type year: int
        :param month: The month component of the date for the data in the
         scope
        :type month: int
        :param day: The day component of the date for the data in the scope
        :type day: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_analytic_store.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'year': self._serialize.url("year", year, 'int'),
            'month': self._serialize.url("month", month, 'int'),
            'day': self._serialize.url("day", day, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_analytic_store.metadata = {'url': '/v1/api/analytics/{scope}/{year}/{month}/{day}'}

    def insert_analytics(
            self, scope, year, month, day, data=None, custom_headers=None, raw=False, **operation_config):
        """Insert analytics into an existing analytic store for the given scope
        and date.

        :param scope: The analytics data scope
        :type scope: str
        :param year: The year component of the date for the data in the scope
        :type year: int
        :param month: The month component of the date for the data in the
         scope
        :type month: int
        :param day: The day component of the date for the data in the scope
        :type day: int
        :param data:
        :type data: list[~lusid.models.SecurityAnalyticDataDto]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.insert_analytics.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'year': self._serialize.url("year", year, 'int'),
            'month': self._serialize.url("month", month, 'int'),
            'day': self._serialize.url("day", day, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if data is not None:
            body_content = self._serialize.body(data, '[SecurityAnalyticDataDto]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AnalyticStoreDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    insert_analytics.metadata = {'url': '/v1/api/analytics/{scope}/{year}/{month}/{day}/prices'}

    def upsert_classification(
            self, classifications=None, custom_headers=None, raw=False, **operation_config):
        """Update classification data.

        :param classifications:
        :type classifications: list[~lusid.models.SecurityClassificationDto]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_classification.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if classifications is not None:
            body_content = self._serialize.body(classifications, '[SecurityClassificationDto]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('ClassificationsDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_classification.metadata = {'url': '/v1/api/classifications'}

    def get_download_url(
            self, version=None, custom_headers=None, raw=False, **operation_config):
        """

        :param version:
        :type version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_download_url.metadata['url']

        # Construct parameters
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query("version", version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_download_url.metadata = {'url': '/v1/api/excel/download-token'}

    def get_latest_version(
            self, custom_headers=None, raw=False, **operation_config):
        """

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_latest_version.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_latest_version.metadata = {'url': '/v1/api/excel/latest-version'}

    def list_portfolio_groups(
            self, scope, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """List all groups in a specified scope.

        :param scope:
        :type scope: str
        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_portfolio_groups.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListGroupDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_portfolio_groups.metadata = {'url': '/v1/api/groups/portfolios/{scope}'}

    def create_portfolio_group(
            self, scope, request=None, custom_headers=None, raw=False, **operation_config):
        """Create a new group.

        :param scope:
        :type scope: str
        :param request:
        :type request: ~lusid.models.CreateGroupRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreateGroupRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('GroupDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_portfolio_group.metadata = {'url': '/v1/api/groups/portfolios/{scope}'}

    def get_portfolio_group(
            self, scope, code, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param as_at:
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GroupDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_group.metadata = {'url': '/v1/api/groups/portfolios/{scope}/{code}'}

    def delete_portfolio_group(
            self, scope, code, custom_headers=None, raw=False, **operation_config):
        """Delete a group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio_group.metadata = {'url': '/v1/api/groups/portfolios/{scope}/{code}'}

    def get_portfolio_group_commands(
            self, scope, code, from_as_at=None, to_as_at=None, custom_headers=None, raw=False, **operation_config):
        """Gets all commands that modified the portfolio groups(s) with the
        specified id.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The portfolio group id
        :type code: str
        :param from_as_at: Filters commands by those that were processed at or
         after this time. Null means there is no lower limit.
        :type from_as_at: datetime
        :param to_as_at: Filters commands by those that were processed at or
         before this time. Null means there is no upper limit (latest).
        :type to_as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio_group_commands.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_as_at is not None:
            query_parameters['fromAsAt'] = self._serialize.query("from_as_at", from_as_at, 'iso-8601')
        if to_as_at is not None:
            query_parameters['toAsAt'] = self._serialize.query("to_as_at", to_as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListProcessedCommandDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_group_commands.metadata = {'url': '/v1/api/groups/portfolios/{scope}/{code}/commands'}

    def get_portfolio_group_expansion(
            self, scope, code, effective_at=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get a full expansion of an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param effective_at:
        :type effective_at: datetime
        :param as_at:
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio_group_expansion.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ExpandedGroupDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_group_expansion.metadata = {'url': '/v1/api/groups/portfolios/{scope}/{code}/expansion'}

    def add_portfolio_to_group(
            self, scope, code, identifier=None, custom_headers=None, raw=False, **operation_config):
        """Add a portfolio to an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param identifier:
        :type identifier: ~lusid.models.ResourceId
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.add_portfolio_to_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if identifier is not None:
            body_content = self._serialize.body(identifier, 'ResourceId')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('GroupDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_portfolio_to_group.metadata = {'url': '/v1/api/groups/portfolios/{scope}/{code}/portfolios'}

    def delete_portfolio_from_group(
            self, scope, code, portfolio_scope, portfolio_code, custom_headers=None, raw=False, **operation_config):
        """Remove a portfolio that is currently present within an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param portfolio_scope:
        :type portfolio_scope: str
        :param portfolio_code:
        :type portfolio_code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_portfolio_from_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'portfolioScope': self._serialize.url("portfolio_scope", portfolio_scope, 'str'),
            'portfolioCode': self._serialize.url("portfolio_code", portfolio_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GroupDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio_from_group.metadata = {'url': '/v1/api/groups/portfolios/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode}'}

    def add_sub_group_to_group(
            self, scope, code, identifier=None, custom_headers=None, raw=False, **operation_config):
        """Add a sub group to an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param identifier:
        :type identifier: ~lusid.models.ResourceId
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.add_sub_group_to_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if identifier is not None:
            body_content = self._serialize.body(identifier, 'ResourceId')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('GroupDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_sub_group_to_group.metadata = {'url': '/v1/api/groups/portfolios/{scope}/{code}/subgroups'}

    def delete_sub_group_from_group(
            self, scope, code, subgroup_scope, subgroup_code, custom_headers=None, raw=False, **operation_config):
        """Remove a subgroup that is currently present within an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param subgroup_scope:
        :type subgroup_scope: str
        :param subgroup_code:
        :type subgroup_code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_sub_group_from_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'subgroupScope': self._serialize.url("subgroup_scope", subgroup_scope, 'str'),
            'subgroupCode': self._serialize.url("subgroup_code", subgroup_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GroupDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_sub_group_from_group.metadata = {'url': '/v1/api/groups/portfolios/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode}'}

    def update_portfolio_group(
            self, scope, code, request=None, custom_headers=None, raw=False, **operation_config):
        """Update an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param request:
        :type request: ~lusid.models.UpdateGroupRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdateGroupRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('GroupDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_portfolio_group.metadata = {'url': '/v1/api/groups/portfolios/{scope}/{code}/update'}

    def get_health(
            self, custom_headers=None, raw=False, **operation_config):
        """Simple heartbeat method for the api.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_health.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_health.metadata = {'url': '/v1/api/health'}

    def get_login_info(
            self, custom_headers=None, raw=False, **operation_config):
        """Gets the login information.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_login_info.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LoginResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_login_info.metadata = {'url': '/v1/api/login'}

    def store_web_logs(
            self, message=None, custom_headers=None, raw=False, **operation_config):
        """Store a log message.

        :param message:
        :type message: ~lusid.models.WebLogMessage
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.store_web_logs.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if message is not None:
            body_content = self._serialize.body(message, 'WebLogMessage')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [204, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 204:
            deserialized = self._deserialize('str', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    store_web_logs.metadata = {'url': '/v1/api/logs/lusidweb'}

    def get_build_version(
            self, custom_headers=None, raw=False, **operation_config):
        """Returns the current assembly version.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_build_version.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_build_version.metadata = {'url': '/v1/api/metadata/buildversion'}

    def verify_connectivity(
            self, custom_headers=None, raw=False, **operation_config):
        """Returns the current assembly version.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.verify_connectivity.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    verify_connectivity.metadata = {'url': '/v1/api/metadata/verifyconnectivity'}

    def get_version(
            self, custom_headers=None, raw=False, **operation_config):
        """Returns the current assembly version.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_version.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_version.metadata = {'url': '/v1/api/metadata/version'}

    def get_personalisations(
            self, recursive, wildcards, pattern=None, scope=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get a personalisation, recursing to get any referenced if required.

        :param recursive: Whether to recurse into dereference recursive
         settings
        :type recursive: bool
        :param wildcards: Whether to apply wildcards to the provided pattern
         and pull back any matching
        :type wildcards: bool
        :param pattern: The search pattern or specific key
        :type pattern: str
        :param scope: The scope level to request for. Possible values include:
         'User', 'Group', 'Default', 'All'
        :type scope: str
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_personalisations.metadata['url']

        # Construct parameters
        query_parameters = {}
        if pattern is not None:
            query_parameters['pattern'] = self._serialize.query("pattern", pattern, 'str')
        if scope is not None:
            query_parameters['scope'] = self._serialize.query("scope", scope, 'str')
        query_parameters['recursive'] = self._serialize.query("recursive", recursive, 'bool')
        query_parameters['wildcards'] = self._serialize.query("wildcards", wildcards, 'bool')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListPersonalisationDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_personalisations.metadata = {'url': '/v1/api/personalisations'}

    def upsert_personalisations(
            self, personalisations=None, custom_headers=None, raw=False, **operation_config):
        """Upsert one or more personalisations.

        :param personalisations:
        :type personalisations: list[~lusid.models.PersonalisationDto]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_personalisations.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if personalisations is not None:
            body_content = self._serialize.body(personalisations, '[PersonalisationDto]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('UpsertPersonalisationsResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_personalisations.metadata = {'url': '/v1/api/personalisations'}

    def delete_personalisation(
            self, scope, key=None, group=None, custom_headers=None, raw=False, **operation_config):
        """Delete a personalisation at a specific scope (or use scope ALL to purge
        the setting entirely).

        :param scope: The scope to delete at (use ALL to purge the setting
         entirely). Possible values include: 'User', 'Group', 'Default', 'All'
        :type scope: str
        :param key: The key of the setting to be deleted
        :type key: str
        :param group: If deleting a setting at group level, specify the group
         here
        :type group: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_personalisation.metadata['url']

        # Construct parameters
        query_parameters = {}
        if key is not None:
            query_parameters['key'] = self._serialize.query("key", key, 'str')
        query_parameters['scope'] = self._serialize.query("scope", scope, 'str')
        if group is not None:
            query_parameters['group'] = self._serialize.query("group", group, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_personalisation.metadata = {'url': '/v1/api/personalisations'}

    def list_portfolios(
            self, scope, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, property_filter=None, custom_headers=None, raw=False, **operation_config):
        """Get all portfolios.

        Get all portfolios in a scope.

        :param scope: The scope to get portfolios from
        :type scope: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: The asAt date to use
        :type as_at: datetime
        :param sort_by: The columns to sort the returned data by
        :type sort_by: list[str]
        :param start: How many items to skip from the returned set
        :type start: int
        :param limit: How many items to return from the set
        :type limit: int
        :param property_filter:
        :type property_filter: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_portfolios.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if property_filter is not None:
            query_parameters['propertyFilter'] = self._serialize.query("property_filter", property_filter, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListPortfolioDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_portfolios.metadata = {'url': '/v1/api/portfolios/{scope}'}

    def create_portfolio(
            self, scope, create_request=None, custom_headers=None, raw=False, **operation_config):
        """Create portfolio.

        Creates a new portfolio.

        :param scope: The intended scope of the portfolio
        :type scope: str
        :param create_request: The portfolio creation request object
        :type create_request: ~lusid.models.CreatePortfolioRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if create_request is not None:
            body_content = self._serialize.body(create_request, 'CreatePortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_portfolio.metadata = {'url': '/v1/api/portfolios/{scope}'}

    def get_portfolio(
            self, scope, code, effective_at=None, as_at=None, property_filter=None, custom_headers=None, raw=False, **operation_config):
        """Get portfolio.

        Gets a single portfolio by code.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: The asAt date to use
        :type as_at: datetime
        :param property_filter: Optional property filter
        :type property_filter: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if property_filter is not None:
            query_parameters['propertyFilter'] = self._serialize.query("property_filter", property_filter, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio.metadata = {'url': '/v1/api/portfolios/{scope}/{code}'}

    def update_portfolio(
            self, scope, code, request=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """

        :param scope: The scope of the portfolio to be updated
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param request: The update request
        :type request: ~lusid.models.UpdatePortfolioRequest
        :param effective_at: The effective date for the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdatePortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_portfolio.metadata = {'url': '/v1/api/portfolios/{scope}/{code}'}

    def delete_portfolio(
            self, scope, code, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Delete portfolio.

        Deletes a portfolio from the given effectiveAt.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio.metadata = {'url': '/v1/api/portfolios/{scope}/{code}'}

    def get_commands(
            self, scope, code, from_as_at=None, to_as_at=None, custom_headers=None, raw=False, **operation_config):
        """Gets all commands that modified the portfolio(s) with the specified id.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The portfolio id
        :type code: str
        :param from_as_at: Filters commands by those that were processed at or
         after this time. Null means there is no lower limit.
        :type from_as_at: datetime
        :param to_as_at: Filters commands by those that were processed at or
         before this time. Null means there is no upper limit (latest).
        :type to_as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_commands.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_as_at is not None:
            query_parameters['fromAsAt'] = self._serialize.query("from_as_at", from_as_at, 'iso-8601')
        if to_as_at is not None:
            query_parameters['toAsAt'] = self._serialize.query("to_as_at", to_as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListProcessedCommandDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_commands.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/commands'}

    def get_details(
            self, scope, code, effective_at=None, as_at=None, property_filter=None, custom_headers=None, raw=False, **operation_config):
        """Get portfolio details.

        Gets the details for a portfolio.  For a derived portfolio this can be
        the details of another reference portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: The asAt date to use
        :type as_at: datetime
        :param property_filter: Optional property filter
        :type property_filter: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_details.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if property_filter is not None:
            query_parameters['propertyFilter'] = self._serialize.query("property_filter", property_filter, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioDetailsDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_details.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/details'}

    def upsert_details(
            self, scope, code, details=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Add/update portfolio details.

        Update the portfolio details for the given code or add if it doesn't
        already exist. Updates with
        null values will remove any existing values.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param details:
        :type details: ~lusid.models.PortfolioDetailsRequest
        :param effective_at: The effective date of the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_details.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if details is not None:
            body_content = self._serialize.body(details, 'PortfolioDetailsRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioDetailsDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_details.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/details'}

    def delete_details(
            self, scope, code, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Delete portfolio details.

        Deletes the portfolio details for the given code.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: The effective date of the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_details.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_details.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/details'}

    def get_aggregate_holdings(
            self, scope, code, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get holdings.

        Get the aggregate holdings of a portfolio.  If no effectiveAt or asAt
        are supplied then values will be defaulted to the latest system time.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: As at date
        :type as_at: datetime
        :param sort_by: The columns to sort the returned data by
        :type sort_by: list[str]
        :param start: How many items to skip from the returned set
        :type start: int
        :param limit: How many items to return from the set
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_aggregate_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionedResourceListHoldingDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_aggregate_holdings.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/holdings'}

    def adjust_holdings(
            self, scope, code, effective_at, holdings=None, custom_headers=None, raw=False, **operation_config):
        """Adjust holdings.

        Create trades in a specific portfolio to bring it to the specified
        holdings.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param holdings:
        :type holdings: list[~lusid.models.HoldingDto]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.adjust_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if holdings is not None:
            body_content = self._serialize.body(holdings, '[HoldingDto]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpsertPortfolioTradesDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    adjust_holdings.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/holdings/{effectiveAt}'}

    def get_properties(
            self, scope, code, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, property_filter=None, custom_headers=None, raw=False, **operation_config):
        """Get properties.

        Get properties attached to the portfolio.  If the asAt is not specified
        then
        the latest system time is used.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: The asAt date to use
        :type as_at: datetime
        :param sort_by: Property to sort the results by
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param property_filter: Property to filter the results by
        :type property_filter: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_properties.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if property_filter is not None:
            query_parameters['propertyFilter'] = self._serialize.query("property_filter", property_filter, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioPropertiesDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_properties.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/properties'}

    def upsert_portfolio_properties(
            self, scope, code, properties=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Create properties.

        Create one or more properties on a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param properties:
        :type properties: list[~lusid.models.PropertyDto]
        :param effective_at: The effective date for the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_portfolio_properties.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if properties is not None:
            body_content = self._serialize.body(properties, '[PropertyDto]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioPropertiesDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_portfolio_properties.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/properties'}

    def delete_property(
            self, scope, code, property=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Delete property.

        Delete a property from a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param property: The key of the property to be deleted
        :type property: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_property.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if property is not None:
            query_parameters['property'] = self._serialize.query("property", property, 'str')
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_property.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/properties'}

    def delete_properties(
            self, scope, code, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Delete properties.

        Delete all properties from a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: The effective date for the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_properties.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_properties.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/properties/all'}

    def get_trades(
            self, scope, code, from_trade_date=None, to_trade_date=None, as_at=None, sort_by=None, start=None, limit=None, property_filter=None, custom_headers=None, raw=False, **operation_config):
        """Get trades.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param from_trade_date: Include trades with a trade date equal or
         later than this date
        :type from_trade_date: datetime
        :param to_trade_date: Include trades with a trade date equal or before
         this date
        :type to_trade_date: datetime
        :param as_at:
        :type as_at: datetime
        :param sort_by: The columns to sort the returned data by
        :type sort_by: list[str]
        :param start: How many items to skip from the returned set
        :type start: int
        :param limit: How many items to return from the set
        :type limit: int
        :param property_filter:
        :type property_filter: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_trades.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_trade_date is not None:
            query_parameters['fromTradeDate'] = self._serialize.query("from_trade_date", from_trade_date, 'iso-8601')
        if to_trade_date is not None:
            query_parameters['toTradeDate'] = self._serialize.query("to_trade_date", to_trade_date, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if property_filter is not None:
            query_parameters['propertyFilter'] = self._serialize.query("property_filter", property_filter, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionedResourceListTradeDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_trades.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/trades'}

    def upsert_trades(
            self, scope, code, trades=None, custom_headers=None, raw=False, **operation_config):
        """Add/updates trades in a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param trades: The trades to be updated
        :type trades: list[~lusid.models.TradeDto]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_trades.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if trades is not None:
            body_content = self._serialize.body(trades, '[TradeDto]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpsertPortfolioTradesDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_trades.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/trades'}

    def delete_trades(
            self, scope, code, cancel_date, id=None, custom_headers=None, raw=False, **operation_config):
        """Delete trades.

        Delete one or more trades from a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param cancel_date: Date on which trades are deleted
        :type cancel_date: datetime
        :param id: Ids of trades to delete
        :type id: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_trades.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['cancelDate'] = self._serialize.query("cancel_date", cancel_date, 'iso-8601')
        if id is not None:
            query_parameters['id'] = self._serialize.query("id", id, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_trades.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/trades'}

    def add_trade_property(
            self, scope, code, trade_id, properties=None, custom_headers=None, raw=False, **operation_config):
        """Add/update trade properties.

        Add one or more properties to a specific trade in a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param trade_id: Id of trade to add properties to
        :type trade_id: str
        :param properties: Trade properties to add
        :type properties: list[~lusid.models.PropertyDto]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.add_trade_property.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'tradeId': self._serialize.url("trade_id", trade_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if properties is not None:
            body_content = self._serialize.body(properties, '[PropertyDto]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('AddTradePropertyDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_trade_property.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/trades/{tradeId}/properties'}

    def delete_property_from_trade(
            self, scope, code, trade_id, property=None, custom_headers=None, raw=False, **operation_config):
        """Delete trade property.

        Delete a property from a specific trade.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param trade_id: Id of the trade to delete the property from
        :type trade_id: str
        :param property: The key of the property to be deleted
        :type property: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_property_from_trade.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'tradeId': self._serialize.url("trade_id", trade_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if property is not None:
            query_parameters['property'] = self._serialize.query("property", property, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_property_from_trade.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/trades/{tradeId}/properties'}

    def add_trade_property_to_all(
            self, scope, code, properties=None, custom_headers=None, raw=False, **operation_config):
        """Add properties to all trades.

        Add one or more properties to all trades in a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param properties: Properties to add to all trades
        :type properties: list[~lusid.models.PropertyDto]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.add_trade_property_to_all.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if properties is not None:
            body_content = self._serialize.body(properties, '[PropertyDto]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('AddTradePropertyDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_trade_property_to_all.metadata = {'url': '/v1/api/portfolios/{scope}/{code}/trades/properties'}

    def create_derived_portfolio(
            self, scope, portfolio=None, custom_headers=None, raw=False, **operation_config):
        """Create derived portfolio.

        Creates a portfolio that derives from an existing portfolio.

        :param scope: The scope into which to create the new derived portfolio
        :type scope: str
        :param portfolio: The root object of the new derived portfolio,
         containing a populated reference portfolio id and reference scope
        :type portfolio: ~lusid.models.CreateDerivedPortfolioRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_derived_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if portfolio is not None:
            body_content = self._serialize.body(portfolio, 'CreateDerivedPortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_derived_portfolio.metadata = {'url': '/v1/api/portfolios/{scope}/derived'}

    def portfolios_search(
            self, request=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Search portfolios.

        :param request:
        :type request: object
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param filter:
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.portfolios_search.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'object')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListPortfolioSearchResult', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    portfolios_search.metadata = {'url': '/v1/api/portfolios/search'}

    def proxy_search(
            self, request=None, custom_headers=None, raw=False, **operation_config):
        """Search property definitions.

        :param request:
        :type request: object
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.proxy_search.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'object')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    proxy_search.metadata = {'url': '/v1/api/properties/search'}

    def get_property_definition_domains(
            self, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Gets the available property-definition domains.

        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_property_definition_domains.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListPropertyDomain', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_property_definition_domains.metadata = {'url': '/v1/api/propertydefinitions'}

    def create_property_definition(
            self, definition=None, custom_headers=None, raw=False, **operation_config):
        """Creates a new property definition.

        :param definition:
        :type definition: ~lusid.models.CreatePropertyDefinitionRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_property_definition.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if definition is not None:
            body_content = self._serialize.body(definition, 'CreatePropertyDefinitionRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PropertyDefinitionDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_property_definition.metadata = {'url': '/v1/api/propertydefinitions'}

    def get_multiple_property_definitions(
            self, keys=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Gets multiple property definitions.

        :param keys:
        :type keys: list[str]
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_multiple_property_definitions.metadata['url']

        # Construct parameters
        query_parameters = {}
        if keys is not None:
            query_parameters['keys'] = self._serialize.query("keys", keys, '[str]', div=',')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListPropertyDefinitionDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_multiple_property_definitions.metadata = {'url': '/v1/api/propertydefinitions/_keys'}

    def get_all_property_keys_in_domain(
            self, domain, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Gets all available property definitions.

        :param domain: Possible values include: 'Trade', 'Portfolio',
         'Security', 'Holding', 'ReferenceHolding'
        :type domain: str
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_all_property_keys_in_domain.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListPropertyKey', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_all_property_keys_in_domain.metadata = {'url': '/v1/api/propertydefinitions/{domain}'}

    def get_property_definition_scopes_in_domain(
            self, domain, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Gets the available property-definition scopes for the specified domain.

        :param domain: Possible values include: 'Trade', 'Portfolio',
         'Security', 'Holding', 'ReferenceHolding'
        :type domain: str
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_property_definition_scopes_in_domain.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListScope', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_property_definition_scopes_in_domain.metadata = {'url': '/v1/api/propertydefinitions/{domain}/_scopes'}

    def get_all_from_scope(
            self, domain, scope, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Gets all properties in a scope.

        :param domain: Possible values include: 'Trade', 'Portfolio',
         'Security', 'Holding', 'ReferenceHolding'
        :type domain: str
        :param scope:
        :type scope: str
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_all_from_scope.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListPropertyKey', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_all_from_scope.metadata = {'url': '/v1/api/propertydefinitions/{domain}/{scope}'}

    def get_property_definition(
            self, domain, scope, name, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Gets a property definition.

        :param domain: Possible values include: 'Trade', 'Portfolio',
         'Security', 'Holding', 'ReferenceHolding'
        :type domain: str
        :param scope:
        :type scope: str
        :param name:
        :type name: str
        :param as_at:
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_property_definition.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertyDefinitionDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_property_definition.metadata = {'url': '/v1/api/propertydefinitions/{domain}/{scope}/{name}'}

    def update_property_definition(
            self, domain, scope, name, definition=None, custom_headers=None, raw=False, **operation_config):
        """Updates the specified property definition.

        :param domain: Possible values include: 'Trade', 'Portfolio',
         'Security', 'Holding', 'ReferenceHolding'
        :type domain: str
        :param scope:
        :type scope: str
        :param name:
        :type name: str
        :param definition:
        :type definition: ~lusid.models.UpdatePropertyDefinitionRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_property_definition.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if definition is not None:
            body_content = self._serialize.body(definition, 'UpdatePropertyDefinitionRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertyDefinitionDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_property_definition.metadata = {'url': '/v1/api/propertydefinitions/{domain}/{scope}/{name}'}

    def delete_property_definition(
            self, domain, scope, name, custom_headers=None, raw=False, **operation_config):
        """Deletes the property definition.

        :param domain: Possible values include: 'Trade', 'Portfolio',
         'Security', 'Holding', 'ReferenceHolding'
        :type domain: str
        :param scope:
        :type scope: str
        :param name:
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_property_definition.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_property_definition.metadata = {'url': '/v1/api/propertydefinitions/{domain}/{scope}/{name}'}

    def create_property_data_format(
            self, request=None, custom_headers=None, raw=False, **operation_config):
        """Create a new PropertyDataFormat. Note: Only non-default formats can be
        created.

        :param request: The definition of the new format
        :type request: ~lusid.models.CreatePropertyDataFormatRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_property_data_format.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreatePropertyDataFormatRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PropertyDataFormatDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_property_data_format.metadata = {'url': '/v1/api/propertyformats'}

    def list(
            self, scope, include_default=None, include_system=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Lists all property data formats in the specified scope.

        :param scope:
        :type scope: str
        :param include_default:
        :type include_default: bool
        :param include_system:
        :type include_system: bool
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if include_default is not None:
            query_parameters['includeDefault'] = self._serialize.query("include_default", include_default, 'bool')
        if include_system is not None:
            query_parameters['includeSystem'] = self._serialize.query("include_system", include_system, 'bool')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListPropertyDataFormatDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/v1/api/propertyformats/{scope}'}

    def get_property_data_format(
            self, scope, name, custom_headers=None, raw=False, **operation_config):
        """Gets a property data format.

        :param scope:
        :type scope: str
        :param name:
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_property_data_format.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertyDataFormatDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_property_data_format.metadata = {'url': '/v1/api/propertyformats/{scope}/{name}'}

    def update_property_data_format(
            self, scope, name, request=None, custom_headers=None, raw=False, **operation_config):
        """Update a PropertyDataFormat. Note: Only non-default formats can be
        updated.

        :param scope: The scope of the format being updated
        :type scope: str
        :param name: The name of the format to update
        :type name: str
        :param request: The new definition of the format
        :type request: ~lusid.models.UpdatePropertyDataFormatRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_property_data_format.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdatePropertyDataFormatRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertyDataFormatDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_property_data_format.metadata = {'url': '/v1/api/propertyformats/{scope}/{name}'}

    def list_reference_portfolios(
            self, scope, effective_at, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get all reference portfolios in a scope.

        :param scope:
        :type scope: str
        :param effective_at:
        :type effective_at: datetime
        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_reference_portfolios.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListPortfolioDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_reference_portfolios.metadata = {'url': '/v1/api/reference/{scope}'}

    def create_reference_portfolio(
            self, scope, reference_portfolio=None, custom_headers=None, raw=False, **operation_config):
        """Create a new reference portfolio.

        :param scope: The intended scope of the portfolio
        :type scope: str
        :param reference_portfolio: The portfolio creation request object
        :type reference_portfolio: ~lusid.models.CreatePortfolioRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_reference_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if reference_portfolio is not None:
            body_content = self._serialize.body(reference_portfolio, 'CreatePortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_reference_portfolio.metadata = {'url': '/v1/api/reference/{scope}'}

    def get_reference_portfolio(
            self, scope, code, effective_at, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get a reference portfolio by name (as opposed to id).

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param effective_at:
        :type effective_at: datetime
        :param as_at:
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_reference_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListReferencePortfolioConstituentDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_reference_portfolio.metadata = {'url': '/v1/api/reference/{scope}/{code}'}

    def delete_reference_portfolio(
            self, scope, code, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Delete a specific portfolio.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param effective_at:
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_reference_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_reference_portfolio.metadata = {'url': '/v1/api/reference/{scope}/{code}'}

    def get_constituents(
            self, scope, effective_at, code, reference_portfolio_id=None, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get all the constituents in a reference portfolio.

        :param scope:
        :type scope: str
        :param effective_at:
        :type effective_at: datetime
        :param code:
        :type code: str
        :param reference_portfolio_id:
        :type reference_portfolio_id: str
        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_constituents.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if reference_portfolio_id is not None:
            query_parameters['referencePortfolioId'] = self._serialize.query("reference_portfolio_id", reference_portfolio_id, 'str')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListReferencePortfolioConstituentDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_constituents.metadata = {'url': '/v1/api/reference/{scope}/{code}/{effectiveAt}/constituents'}

    def upsert_constituents(
            self, scope, code, effective_at, constituents=None, custom_headers=None, raw=False, **operation_config):
        """Add constituents to a specific reference portfolio.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param effective_at:
        :type effective_at: datetime
        :param constituents:
        :type constituents:
         list[~lusid.models.ReferencePortfolioConstituentDto]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_constituents.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if constituents is not None:
            body_content = self._serialize.body(constituents, '[ReferencePortfolioConstituentDto]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('UpsertReferencePortfolioConstituentsDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_constituents.metadata = {'url': '/v1/api/reference/{scope}/{code}/{effectiveAt}/constituents'}

    def get_results(
            self, scope, key, date_parameter, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Retrieve some previously stored results.

        :param scope: The scope of the data
        :type scope: str
        :param key: The key that identifies the data
        :type key: str
        :param date_parameter: The date for which the data was loaded
        :type date_parameter: datetime
        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_results.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'key': self._serialize.url("key", key, 'str'),
            'date': self._serialize.url("date_parameter", date_parameter, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResultsDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_results.metadata = {'url': '/v1/api/results/{scope}/{key}/{date}'}

    def upsert_results(
            self, scope, key, date_parameter, request=None, custom_headers=None, raw=False, **operation_config):
        """Upsert precalculated results against a specified scope/key/date
        combination.

        :param scope: The scope of the data
        :type scope: str
        :param key: The key that identifies the data
        :type key: str
        :param date_parameter: The date for which the data is relevant
        :type date_parameter: datetime
        :param request: The results to upload
        :type request: ~lusid.models.CreateResultsRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_results.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'key': self._serialize.url("key", key, 'str'),
            'date': self._serialize.url("date_parameter", date_parameter, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreateResultsRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResultsDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_results.metadata = {'url': '/v1/api/results/{scope}/{key}/{date}'}

    def get_entity_schema(
            self, entity, custom_headers=None, raw=False, **operation_config):
        """Gets the schema for a given entity.

        :param entity: Possible values include: 'PropertyKey', 'FieldSchema',
         'Personalisation', 'Security', 'Property', 'Login',
         'PropertyDefinition', 'PropertyDataFormat', 'AggregationResponseNode',
         'Portfolio', 'PortfolioSearchResult', 'PortfolioDetails',
         'PortfolioProperties', 'Version', 'AddTradeProperty', 'AnalyticStore',
         'AnalyticStoreKey', 'UpsertPortfolioTrades', 'Group', 'Constituent',
         'Trade', 'PortfolioHolding', 'ErrorDetail', 'ErrorResponse',
         'InstrumentDefinition', 'ProcessedCommand', 'CreatePortfolio',
         'CreateAnalyticStore', 'CreateClientSecurity',
         'CreateDerivedPortfolio', 'CreateGroup', 'CreatePropertyDataFormat',
         'CreatePropertyDefinition', 'UpdatePortfolio', 'UpdateGroup',
         'UpdatePropertyDataFormat', 'UpdatePropertyDefinition',
         'SecurityAnalytic', 'AggregationRequest', 'Aggregation',
         'NestedAggregation', 'ResultDataSchema', 'Classification',
         'SecurityClassification', 'WebLogMessage', 'UpsertPersonalisation',
         'CreatePortfolioDetails', 'UpsertConstituent', 'CreateResults',
         'Results', 'TryAddClientSecurities', 'TryDeleteClientSecurities',
         'TryLookupSecuritiesFromCodes', 'ExpandedGroup'
        :type entity: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_entity_schema.metadata['url']
        path_format_arguments = {
            'entity': self._serialize.url("entity", entity, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SchemaDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_entity_schema.metadata = {'url': '/v1/api/schema/entities/{entity}'}

    def get_property_schema(
            self, property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Get the schemas for the provided list of property keys.

        :param property_keys: A comma delimited list of property keys in
         string format. e.g.
         "Portfolio/default/PropertyName,Portfolio/differentScope/MyProperty"
        :type property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_property_schema.metadata['url']

        # Construct parameters
        query_parameters = {}
        if property_keys is not None:
            query_parameters['propertyKeys'] = self._serialize.query("property_keys", property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertySchemaDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_property_schema.metadata = {'url': '/v1/api/schema/properties'}

    def get_value_types(
            self, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Gets the available value types that could be returned in a schema.

        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_value_types.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 404, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListUiDataType', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_value_types.metadata = {'url': '/v1/api/schema/types'}

    def try_add_client_security(
            self, definitions=None, custom_headers=None, raw=False, **operation_config):
        """Attempt to create one or more client securities. Failed securities will
        be identified in the body of the response.

        :param definitions:
        :type definitions: list[~lusid.models.CreateClientSecurityRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.try_add_client_security.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if definitions is not None:
            body_content = self._serialize.body(definitions, '[CreateClientSecurityRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('TryAddClientSecuritiesDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    try_add_client_security.metadata = {'url': '/v1/api/securities'}

    def try_delete_client_security(
            self, uids=None, custom_headers=None, raw=False, **operation_config):
        """Attempt to delete one or more client securities. Failed securities will
        be identified in the body of the response.

        :param uids:
        :type uids: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.try_delete_client_security.metadata['url']

        # Construct parameters
        query_parameters = {}
        if uids is not None:
            query_parameters['uids'] = self._serialize.query("uids", uids, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TryDeleteClientSecuritiesDto', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    try_delete_client_security.metadata = {'url': '/v1/api/securities'}

    def get_security(
            self, uid, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get an individual security by the unique security uid.

        :param uid: The uid of the requested security
        :type uid: str
        :param as_at: As at date
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_security.metadata['url']
        path_format_arguments = {
            'uid': self._serialize.url("uid", uid, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SecurityDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_security.metadata = {'url': '/v1/api/securities/{uid}'}

    def lookup_from_codes(
            self, code_type, codes=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Lookup more than one security by supplying a collection of
        non-Finbourne codes.

        :param code_type: The type of identifier. Possible values include:
         'Undefined', 'ReutersAssetId', 'CINS', 'Isin', 'Sedol', 'Cusip',
         'ClientInternal', 'Figi', 'Wertpapier'
        :type code_type: str
        :param codes: An array of codes
        :type codes: list[str]
        :param as_at: As at date
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.lookup_from_codes.metadata['url']
        path_format_arguments = {
            'codeType': self._serialize.url("code_type", code_type, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if codes is not None:
            query_parameters['codes'] = self._serialize.query("codes", codes, '[str]', div=',')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TryLookupSecuritiesFromCodesDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    lookup_from_codes.metadata = {'url': '/v1/api/securities/lookup/{codeType}'}

    def lookup_from_codes_bulk(
            self, code_type, codes=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Lookup a large number of securities by supplying a collection of
        non-Finbourne codes.

        :param code_type: The type of identifier. Possible values include:
         'Undefined', 'ReutersAssetId', 'CINS', 'Isin', 'Sedol', 'Cusip',
         'ClientInternal', 'Figi', 'Wertpapier'
        :type code_type: str
        :param codes: An array of codes
        :type codes: list[str]
        :param as_at: As at date
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.lookup_from_codes_bulk.metadata['url']
        path_format_arguments = {
            'codeType': self._serialize.url("code_type", code_type, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if codes is not None:
            body_content = self._serialize.body(codes, '[str]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TryLookupSecuritiesFromCodesDto', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 500:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    lookup_from_codes_bulk.metadata = {'url': '/v1/api/securities/lookup/{codeType}'}
