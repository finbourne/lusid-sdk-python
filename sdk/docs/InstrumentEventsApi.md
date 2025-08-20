# lusid.InstrumentEventsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_applicable_instrument_events**](InstrumentEventsApi.md#query_applicable_instrument_events) | **POST** /api/instrumentevents/$queryApplicableInstrumentEvents | QueryApplicableInstrumentEvents: Returns a list of applicable instrument events based on the holdings of the portfolios and date range specified in the query.
[**query_bucketed_cash_flows**](InstrumentEventsApi.md#query_bucketed_cash_flows) | **POST** /api/instrumentevents/$queryBucketedCashFlows | QueryBucketedCashFlows: Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.
[**query_cash_flows**](InstrumentEventsApi.md#query_cash_flows) | **POST** /api/instrumentevents/$queryCashFlows | QueryCashFlows: Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.
[**query_instrument_events**](InstrumentEventsApi.md#query_instrument_events) | **POST** /api/instrumentevents/$query | QueryInstrumentEvents: Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.
[**query_trade_tickets**](InstrumentEventsApi.md#query_trade_tickets) | **POST** /api/instrumentevents/$queryTradeTickets | QueryTradeTickets: Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.


# **query_applicable_instrument_events**
> ResourceListOfApplicableInstrumentEvent query_applicable_instrument_events(as_at=as_at, limit=limit, page=page, query_applicable_instrument_events_request=query_applicable_instrument_events_request)

QueryApplicableInstrumentEvents: Returns a list of applicable instrument events based on the holdings of the portfolios and date range specified in the query.

Returns a list of applicable instrument events based on the holdings of the portfolios and date range specified in the query.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(InstrumentEventsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The as at time to use. (optional)
    limit = 100 # int | Optional. When paginating, limit the number of returned results to this many. If not specified, a default of 100 is used. (optional) (default to 100)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing items from a previous call. Page values are return from list calls, and must be supplied exactly as returned. Additionally, when specifying this (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_applicable_instrument_events_request = QueryApplicableInstrumentEventsRequest.from_json("")
    # query_applicable_instrument_events_request = QueryApplicableInstrumentEventsRequest.from_dict({})
    query_applicable_instrument_events_request = QueryApplicableInstrumentEventsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.query_applicable_instrument_events(as_at=as_at, limit=limit, page=page, query_applicable_instrument_events_request=query_applicable_instrument_events_request, opts=opts)

        # QueryApplicableInstrumentEvents: Returns a list of applicable instrument events based on the holdings of the portfolios and date range specified in the query.
        api_response = api_instance.query_applicable_instrument_events(as_at=as_at, limit=limit, page=page, query_applicable_instrument_events_request=query_applicable_instrument_events_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventsApi->query_applicable_instrument_events: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The as at time to use. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default of 100 is used. | [optional] [default to 100]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are return from list calls, and must be supplied exactly as returned. Additionally, when specifying this | [optional] 
 **query_applicable_instrument_events_request** | [**QueryApplicableInstrumentEventsRequest**](QueryApplicableInstrumentEventsRequest.md)| The filter parameters used to retrieve applicable instrument events. | [optional] 

### Return type

[**ResourceListOfApplicableInstrumentEvent**](ResourceListOfApplicableInstrumentEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applicable Instrument Events |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **query_bucketed_cash_flows**
> BucketedCashFlowResponse query_bucketed_cash_flows(query_bucketed_cash_flows_request=query_bucketed_cash_flows_request)

QueryBucketedCashFlows: Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.

Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(InstrumentEventsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_bucketed_cash_flows_request = QueryBucketedCashFlowsRequest.from_json("")
    # query_bucketed_cash_flows_request = QueryBucketedCashFlowsRequest.from_dict({})
    query_bucketed_cash_flows_request = QueryBucketedCashFlowsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.query_bucketed_cash_flows(query_bucketed_cash_flows_request=query_bucketed_cash_flows_request, opts=opts)

        # QueryBucketedCashFlows: Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.
        api_response = api_instance.query_bucketed_cash_flows(query_bucketed_cash_flows_request=query_bucketed_cash_flows_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventsApi->query_bucketed_cash_flows: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_bucketed_cash_flows_request** | [**QueryBucketedCashFlowsRequest**](QueryBucketedCashFlowsRequest.md)| The Query Information. | [optional] 

### Return type

[**BucketedCashFlowResponse**](BucketedCashFlowResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query bucketed cashflows across portfolios. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **query_cash_flows**
> ResourceListOfInstrumentCashFlow query_cash_flows(limit=limit, page=page, query_cash_flows_request=query_cash_flows_request)

QueryCashFlows: Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.

Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(InstrumentEventsApi)
    limit = 1000 # int | Optional. When paginating, limit the number of returned results to this many. If not specified, a default of 1000 is used. (optional) (default to 1000)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing items from a previous call. Page values are return from list calls, and must be supplied exactly as returned. Additionally, when specifying this value, queryBody, and limit must not be modified. (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_cash_flows_request = QueryCashFlowsRequest.from_json("")
    # query_cash_flows_request = QueryCashFlowsRequest.from_dict({})
    query_cash_flows_request = QueryCashFlowsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.query_cash_flows(limit=limit, page=page, query_cash_flows_request=query_cash_flows_request, opts=opts)

        # QueryCashFlows: Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.
        api_response = api_instance.query_cash_flows(limit=limit, page=page, query_cash_flows_request=query_cash_flows_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventsApi->query_cash_flows: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are return from list calls, and must be supplied exactly as returned. Additionally, when specifying this value, queryBody, and limit must not be modified. | [optional] 
 **query_cash_flows_request** | [**QueryCashFlowsRequest**](QueryCashFlowsRequest.md)| The filter parameters used to retrieve instrument events. | [optional] 

### Return type

[**ResourceListOfInstrumentCashFlow**](ResourceListOfInstrumentCashFlow.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events as Cashflows. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **query_instrument_events**
> ResourceListOfInstrumentEventHolder query_instrument_events(limit=limit, page=page, query_instrument_events_request=query_instrument_events_request)

QueryInstrumentEvents: Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.

Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(InstrumentEventsApi)
    limit = 1000 # int | Optional. When paginating, limit the number of returned results to this many. If not specified, a default of 1000 is used. (optional) (default to 1000)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing items from a previous call. Page values are return from list calls, and must be supplied exactly as returned. Additionally, when specifying this value, queryBody, and limit must not be modified. (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_instrument_events_request = QueryInstrumentEventsRequest.from_json("")
    # query_instrument_events_request = QueryInstrumentEventsRequest.from_dict({})
    query_instrument_events_request = QueryInstrumentEventsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.query_instrument_events(limit=limit, page=page, query_instrument_events_request=query_instrument_events_request, opts=opts)

        # QueryInstrumentEvents: Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.
        api_response = api_instance.query_instrument_events(limit=limit, page=page, query_instrument_events_request=query_instrument_events_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventsApi->query_instrument_events: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are return from list calls, and must be supplied exactly as returned. Additionally, when specifying this value, queryBody, and limit must not be modified. | [optional] 
 **query_instrument_events_request** | [**QueryInstrumentEventsRequest**](QueryInstrumentEventsRequest.md)| The filter parameters used to retrieve instrument events. | [optional] 

### Return type

[**ResourceListOfInstrumentEventHolder**](ResourceListOfInstrumentEventHolder.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **query_trade_tickets**
> ResourceListOfPortfolioTradeTicket query_trade_tickets(limit=limit, page=page, query_trade_tickets_request=query_trade_tickets_request)

QueryTradeTickets: Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.

Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.  These trade tickets are derived from events that involve transition of instrument states, such as transitions on exercise or default of an instrument. The trade tickets are to allow the new position to be created given the existing portfolio configuration.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(InstrumentEventsApi)
    limit = 1000 # int | Optional. When paginating, limit the number of returned results to this many. If not specified, a default of 1000 is used. (optional) (default to 1000)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing items from a previous call. Page values are return from list calls, and must be supplied exactly as returned. Additionally, when specifying this value, queryBody, and limit must not be modified. (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_trade_tickets_request = QueryTradeTicketsRequest.from_json("")
    # query_trade_tickets_request = QueryTradeTicketsRequest.from_dict({})
    query_trade_tickets_request = QueryTradeTicketsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.query_trade_tickets(limit=limit, page=page, query_trade_tickets_request=query_trade_tickets_request, opts=opts)

        # QueryTradeTickets: Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.
        api_response = api_instance.query_trade_tickets(limit=limit, page=page, query_trade_tickets_request=query_trade_tickets_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventsApi->query_trade_tickets: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are return from list calls, and must be supplied exactly as returned. Additionally, when specifying this value, queryBody, and limit must not be modified. | [optional] 
 **query_trade_tickets_request** | [**QueryTradeTicketsRequest**](QueryTradeTicketsRequest.md)| The filter parameters used to retrieve instrument events. | [optional] 

### Return type

[**ResourceListOfPortfolioTradeTicket**](ResourceListOfPortfolioTradeTicket.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events as Upsertable TradeTickets. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

