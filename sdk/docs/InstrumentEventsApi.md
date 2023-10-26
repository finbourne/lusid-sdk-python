# lusid.InstrumentEventsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_bucketed_cash_flows**](InstrumentEventsApi.md#query_bucketed_cash_flows) | **POST** /api/instrumentevents/$queryBucketedCashFlows | [EXPERIMENTAL] QueryBucketedCashFlows: Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.
[**query_cash_flows**](InstrumentEventsApi.md#query_cash_flows) | **POST** /api/instrumentevents/$queryCashFlows | [EXPERIMENTAL] QueryCashFlows: Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.
[**query_instrument_events**](InstrumentEventsApi.md#query_instrument_events) | **POST** /api/instrumentevents/$query | [EXPERIMENTAL] QueryInstrumentEvents: Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.
[**query_trade_tickets**](InstrumentEventsApi.md#query_trade_tickets) | **POST** /api/instrumentevents/$queryTradeTickets | [EXPERIMENTAL] QueryTradeTickets: Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.


# **query_bucketed_cash_flows**
> BucketedCashFlowResponse query_bucketed_cash_flows(query_bucketed_cash_flows_request=query_bucketed_cash_flows_request)

[EXPERIMENTAL] QueryBucketedCashFlows: Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.

Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.bucketed_cash_flow_response import BucketedCashFlowResponse
from lusid.models.query_bucketed_cash_flows_request import QueryBucketedCashFlowsRequest
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.InstrumentEventsApi)
    query_bucketed_cash_flows_request = {"windowStart":"2015-01-01T00:00:00.0000000+00:00","windowEnd":"2023-01-01T00:00:00.0000000+00:00","portfolioEntityIds":[{"scope":"portfolioScope","code":"portfolioCode","portfolioEntityType":"SinglePortfolio"}],"effectiveAt":"2022-01-01T00:00:00.0000000+00:00","recipeId":{"scope":"default","code":"default"},"roundingMethod":"RoundUp","bucketingDates":["2020-01-01T00:00:00.0000000+00:00","2020-07-01T00:00:00.0000000+00:00","2021-01-01T00:00:00.0000000+00:00","2021-07-01T00:00:00.0000000+00:00"],"reportCurrency":"USD","equipWithSubtotals":false,"excludeUnsettledTrades":false,"cashFlowType":"InstrumentCashFlow"} # QueryBucketedCashFlowsRequest | The Query Information. (optional)

    try:
        # [EXPERIMENTAL] QueryBucketedCashFlows: Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.
        api_response = await api_instance.query_bucketed_cash_flows(query_bucketed_cash_flows_request=query_bucketed_cash_flows_request)
        print("The response of InstrumentEventsApi->query_bucketed_cash_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentEventsApi->query_bucketed_cash_flows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_bucketed_cash_flows_request** | [**QueryBucketedCashFlowsRequest**](QueryBucketedCashFlowsRequest.md)| The Query Information. | [optional] 

### Return type

[**BucketedCashFlowResponse**](BucketedCashFlowResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query bucketed cashflows across portfolios. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_cash_flows**
> ResourceListOfInstrumentCashFlow query_cash_flows(limit=limit, page=page, query_cash_flows_request=query_cash_flows_request)

[EXPERIMENTAL] QueryCashFlows: Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.

Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.query_cash_flows_request import QueryCashFlowsRequest
from lusid.models.resource_list_of_instrument_cash_flow import ResourceListOfInstrumentCashFlow
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.InstrumentEventsApi)
    limit = 1000 # int | Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. (optional) (default to 1000)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, queryBody, and limit must not  be modified. (optional)
    query_cash_flows_request = {"windowStart":"2015-01-01T00:00:00.0000000+00:00","windowEnd":"2030-01-01T00:00:00.0000000+00:00","portfolioEntityIds":[{"scope":"portfolioScope","code":"portfolioCode","portfolioEntityType":"SinglePortfolio"}],"recipeId":{"scope":"default","code":"default"},"effectiveAt":"2022-01-01T00:00:00.0000000+00:00"} # QueryCashFlowsRequest | The filter parameters used to retrieve instrument events. (optional)

    try:
        # [EXPERIMENTAL] QueryCashFlows: Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.
        api_response = await api_instance.query_cash_flows(limit=limit, page=page, query_cash_flows_request=query_cash_flows_request)
        print("The response of InstrumentEventsApi->query_cash_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentEventsApi->query_cash_flows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, queryBody, and limit must not  be modified. | [optional] 
 **query_cash_flows_request** | [**QueryCashFlowsRequest**](QueryCashFlowsRequest.md)| The filter parameters used to retrieve instrument events. | [optional] 

### Return type

[**ResourceListOfInstrumentCashFlow**](ResourceListOfInstrumentCashFlow.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events as Cashflows. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_instrument_events**
> ResourceListOfInstrumentEventHolder query_instrument_events(limit=limit, page=page, query_instrument_events_request=query_instrument_events_request)

[EXPERIMENTAL] QueryInstrumentEvents: Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.

Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.query_instrument_events_request import QueryInstrumentEventsRequest
from lusid.models.resource_list_of_instrument_event_holder import ResourceListOfInstrumentEventHolder
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.InstrumentEventsApi)
    limit = 1000 # int | Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. (optional) (default to 1000)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, queryBody, and limit must not  be modified. (optional)
    query_instrument_events_request = {"asAt":"2022-06-01T01:01:00.0000000+00:00","windowStart":"2015-01-01T00:00:00.0000000+00:00","windowEnd":"2030-01-01T00:00:00.0000000+00:00","portfolioEntityIds":[{"scope":"portfolioScope","code":"portfolioCode","portfolioEntityType":"SinglePortfolio"}],"effectiveAt":"2022-01-01T00:00:00.0000000+00:00","recipeId":{"scope":"default","code":"default"},"filterInstrumentEvents":""} # QueryInstrumentEventsRequest | The filter parameters used to retrieve instrument events. (optional)

    try:
        # [EXPERIMENTAL] QueryInstrumentEvents: Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.
        api_response = await api_instance.query_instrument_events(limit=limit, page=page, query_instrument_events_request=query_instrument_events_request)
        print("The response of InstrumentEventsApi->query_instrument_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentEventsApi->query_instrument_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, queryBody, and limit must not  be modified. | [optional] 
 **query_instrument_events_request** | [**QueryInstrumentEventsRequest**](QueryInstrumentEventsRequest.md)| The filter parameters used to retrieve instrument events. | [optional] 

### Return type

[**ResourceListOfInstrumentEventHolder**](ResourceListOfInstrumentEventHolder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_trade_tickets**
> ResourceListOfPortfolioTradeTicket query_trade_tickets(limit=limit, page=page, query_trade_tickets_request=query_trade_tickets_request)

[EXPERIMENTAL] QueryTradeTickets: Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.

Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.    These trade tickets are derived from events that involve transition of instrument states, such as transitions  on exercise or default of an instrument. The trade tickets are to allow the new position to be created given the  existing portfolio configuration.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.query_trade_tickets_request import QueryTradeTicketsRequest
from lusid.models.resource_list_of_portfolio_trade_ticket import ResourceListOfPortfolioTradeTicket
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.InstrumentEventsApi)
    limit = 1000 # int | Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. (optional) (default to 1000)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, queryBody, and limit must not  be modified. (optional)
    query_trade_tickets_request = {"windowStart":"2015-01-01T00:00:00.0000000+00:00","windowEnd":"2030-01-01T00:00:00.0000000+00:00","portfolioEntityIds":[{"scope":"portfolioScope","code":"portfolioCode","portfolioEntityType":"SinglePortfolio"}],"recipeId":{"scope":"default","code":"default"},"effectiveAt":"2022-01-01T00:00:00.0000000+00:00"} # QueryTradeTicketsRequest | The filter parameters used to retrieve instrument events. (optional)

    try:
        # [EXPERIMENTAL] QueryTradeTickets: Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.
        api_response = await api_instance.query_trade_tickets(limit=limit, page=page, query_trade_tickets_request=query_trade_tickets_request)
        print("The response of InstrumentEventsApi->query_trade_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentEventsApi->query_trade_tickets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, queryBody, and limit must not  be modified. | [optional] 
 **query_trade_tickets_request** | [**QueryTradeTicketsRequest**](QueryTradeTicketsRequest.md)| The filter parameters used to retrieve instrument events. | [optional] 

### Return type

[**ResourceListOfPortfolioTradeTicket**](ResourceListOfPortfolioTradeTicket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events as Upsertable TradeTickets. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

