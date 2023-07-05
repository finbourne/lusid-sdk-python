# lusid.CorporateActionSourcesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_upsert_corporate_actions**](CorporateActionSourcesApi.md#batch_upsert_corporate_actions) | **POST** /api/corporateactionsources/{scope}/{code}/corporateactions | [EARLY ACCESS] BatchUpsertCorporateActions: Batch upsert corporate actions (instrument transition events) to corporate action source.
[**create_corporate_action_source**](CorporateActionSourcesApi.md#create_corporate_action_source) | **POST** /api/corporateactionsources | [EARLY ACCESS] CreateCorporateActionSource: Create corporate action source
[**delete_corporate_actions**](CorporateActionSourcesApi.md#delete_corporate_actions) | **DELETE** /api/corporateactionsources/{scope}/{code}/corporateactions | [EARLY ACCESS] DeleteCorporateActions: Delete corporate actions
[**delete_instrument_events**](CorporateActionSourcesApi.md#delete_instrument_events) | **DELETE** /api/corporateactionsources/{scope}/{code}/instrumentevents | [EARLY ACCESS] DeleteInstrumentEvents: Delete corporate actions (instrument transition events) from the corporate action source.
[**get_corporate_actions**](CorporateActionSourcesApi.md#get_corporate_actions) | **GET** /api/corporateactionsources/{scope}/{code}/corporateactions | [EARLY ACCESS] GetCorporateActions: List corporate actions (instrument transition events) from the corporate action source.
[**get_instrument_events**](CorporateActionSourcesApi.md#get_instrument_events) | **GET** /api/corporateactionsources/{scope}/{code}/instrumentevents | [EARLY ACCESS] GetInstrumentEvents: Get extrinsic instrument events out of a given corporate actions source.
[**list_corporate_action_sources**](CorporateActionSourcesApi.md#list_corporate_action_sources) | **GET** /api/corporateactionsources | [EARLY ACCESS] ListCorporateActionSources: List corporate action sources
[**upsert_instrument_events**](CorporateActionSourcesApi.md#upsert_instrument_events) | **POST** /api/corporateactionsources/{scope}/{code}/instrumentevents | [EARLY ACCESS] UpsertInstrumentEvents: Upsert instrument events to the provided corporate actions source.


# **batch_upsert_corporate_actions**
> UpsertCorporateActionsResponse batch_upsert_corporate_actions(scope, code, upsert_corporate_action_request=upsert_corporate_action_request)

[EARLY ACCESS] BatchUpsertCorporateActions: Batch upsert corporate actions (instrument transition events) to corporate action source.

Create or update one or more corporate actions in a particular corporate action source. Failures are identified in the body of the response.                If a corporate action is upserted at exactly the same effective datetime as a transaction for the same instrument, the corporate action takes precedence. Depending on the nature of the corporate action, this may mean it affects the transaction.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    scope = 'scope_example' # str | The scope of corporate action source
code = 'code_example' # str | The code of the corporate action source
upsert_corporate_action_request = [{"corporateActionCode":"MyStockSplitId","description":"2-for-1 stock split of instrument BBG001S6PJ31","announcementDate":"2018-03-01T00:00:00.0000000+00:00","exDate":"2018-06-01T00:00:00.0000000+00:00","recordDate":"2018-06-02T00:00:00.0000000+00:00","paymentDate":"2018-08-02T00:00:00.0000000+00:00","transitions":[{"inputTransition":{"instrumentIdentifiers":{"Instrument/default/Figi":"BBG001S6PJ31"},"unitsFactor":1,"costFactor":1},"outputTransitions":[{"instrumentIdentifiers":{"Instrument/default/Figi":"BBG001S6PJ31"},"unitsFactor":2,"costFactor":1}]}]}] # list[UpsertCorporateActionRequest] | The corporate action definitions (optional)

    try:
        # [EARLY ACCESS] BatchUpsertCorporateActions: Batch upsert corporate actions (instrument transition events) to corporate action source.
        api_response = api_instance.batch_upsert_corporate_actions(scope, code, upsert_corporate_action_request=upsert_corporate_action_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->batch_upsert_corporate_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of corporate action source | 
 **code** | **str**| The code of the corporate action source | 
 **upsert_corporate_action_request** | [**list[UpsertCorporateActionRequest]**](UpsertCorporateActionRequest.md)| The corporate action definitions | [optional] 

### Return type

[**UpsertCorporateActionsResponse**](UpsertCorporateActionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created corporate actions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_corporate_action_source**
> CorporateActionSource create_corporate_action_source(create_corporate_action_source_request)

[EARLY ACCESS] CreateCorporateActionSource: Create corporate action source

Create a corporate action source.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    create_corporate_action_source_request = {"scope":"ExampleScope","code":"ExampleCode","displayName":"ExampleDisplayName","description":"Example Description","instrumentScopes":[]} # CreateCorporateActionSourceRequest | The corporate action source definition

    try:
        # [EARLY ACCESS] CreateCorporateActionSource: Create corporate action source
        api_response = api_instance.create_corporate_action_source(create_corporate_action_source_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->create_corporate_action_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_corporate_action_source_request** | [**CreateCorporateActionSourceRequest**](CreateCorporateActionSourceRequest.md)| The corporate action source definition | 

### Return type

[**CorporateActionSource**](CorporateActionSource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created corporate action source |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_corporate_actions**
> DeletedEntityResponse delete_corporate_actions(scope, code, corporate_action_ids)

[EARLY ACCESS] DeleteCorporateActions: Delete corporate actions

Delete one or more corporate actions from a particular corporate action source.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    scope = 'scope_example' # str | The scope of the corporate action source
code = 'code_example' # str | The code of the corporate action source
corporate_action_ids = ['corporate_action_ids_example'] # list[str] | The IDs of the corporate actions to delete

    try:
        # [EARLY ACCESS] DeleteCorporateActions: Delete corporate actions
        api_response = api_instance.delete_corporate_actions(scope, code, corporate_action_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->delete_corporate_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the corporate action source | 
 **code** | **str**| The code of the corporate action source | 
 **corporate_action_ids** | [**list[str]**](str.md)| The IDs of the corporate actions to delete | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Corporate Actions Deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instrument_events**
> DeletedEntityResponse delete_instrument_events(scope, code, instrument_event_ids)

[EARLY ACCESS] DeleteInstrumentEvents: Delete corporate actions (instrument transition events) from the corporate action source.

Delete one or more corporate actions from a particular corporate action source.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    scope = 'scope_example' # str | The scope of the corporate action source
code = 'code_example' # str | The code of the corporate action source
instrument_event_ids = ['instrument_event_ids_example'] # list[str] | The IDs of the instrument events to delete

    try:
        # [EARLY ACCESS] DeleteInstrumentEvents: Delete corporate actions (instrument transition events) from the corporate action source.
        api_response = api_instance.delete_instrument_events(scope, code, instrument_event_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->delete_instrument_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the corporate action source | 
 **code** | **str**| The code of the corporate action source | 
 **instrument_event_ids** | [**list[str]**](str.md)| The IDs of the instrument events to delete | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events Deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporate_actions**
> ResourceListOfCorporateAction get_corporate_actions(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, sort_by=sort_by, limit=limit, filter=filter)

[EARLY ACCESS] GetCorporateActions: List corporate actions (instrument transition events) from the corporate action source.

Get corporate actions from a particular corporate action source.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    scope = 'scope_example' # str | The scope of the corporate action source.
code = 'code_example' # str | The code of the corporate action source.
from_effective_at = 'from_effective_at_example' # str | Optional. The start effective date of the data range. (optional)
to_effective_at = 'to_effective_at_example' # str | Optional. The end effective date of the data range. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data. (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
limit = 56 # int | Optional. When paginating, limit the results to this number. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set.              For example, to filter on the Announcement Date, use \"announcementDate eq '2020-03-06'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] GetCorporateActions: List corporate actions (instrument transition events) from the corporate action source.
        api_response = api_instance.get_corporate_actions(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->get_corporate_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the corporate action source. | 
 **code** | **str**| The code of the corporate action source. | 
 **from_effective_at** | **str**| Optional. The start effective date of the data range. | [optional] 
 **to_effective_at** | **str**| Optional. The end effective date of the data range. | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the results to this number. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.              For example, to filter on the Announcement Date, use \&quot;announcementDate eq &#39;2020-03-06&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfCorporateAction**](ResourceListOfCorporateAction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Corporate Actions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_events**
> PagedResourceListOfInstrumentEventHolder get_instrument_events(scope, code, as_at=as_at, limit=limit, page=page, filter=filter)

[EARLY ACCESS] GetInstrumentEvents: Get extrinsic instrument events out of a given corporate actions source.

Retrieves extrinsic corporate actions out of a corporate actions source

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio.
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data. (optional)
limit = 1000 # int | Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. (optional) (default to 1000)
page = 'page_example' # str | Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, asAt, filter and limit must not  be modified. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set. (optional)

    try:
        # [EARLY ACCESS] GetInstrumentEvents: Get extrinsic instrument events out of a given corporate actions source.
        api_response = api_instance.get_instrument_events(scope, code, as_at=as_at, limit=limit, page=page, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->get_instrument_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. | 
 **as_at** | **datetime**| Optional. The AsAt date of the data. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, asAt, filter and limit must not  be modified. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set. | [optional] 

### Return type

[**PagedResourceListOfInstrumentEventHolder**](PagedResourceListOfInstrumentEventHolder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_corporate_action_sources**
> PagedResourceListOfCorporateActionSource list_corporate_action_sources(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)

[EARLY ACCESS] ListCorporateActionSources: List corporate action sources

Gets a list of all corporate action sources

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
limit = 100 # int | Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 100 is used. (optional) (default to 100)
filter = 'filter_example' # str | Optional. Expression to filter the result set. For example, to  filter on the Display Name, use \"displayName eq 'string'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
page = 'page_example' # str | Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, the filter, asAt, and limit must not  be modified. (optional)

    try:
        # [EARLY ACCESS] ListCorporateActionSources: List corporate action sources
        api_response = api_instance.list_corporate_action_sources(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->list_corporate_action_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 100 is used. | [optional] [default to 100]
 **filter** | **str**| Optional. Expression to filter the result set. For example, to  filter on the Display Name, use \&quot;displayName eq &#39;string&#39;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, the filter, asAt, and limit must not  be modified. | [optional] 

### Return type

[**PagedResourceListOfCorporateActionSource**](PagedResourceListOfCorporateActionSource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All Existing Corporate Action Sources |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instrument_events**
> UpsertInstrumentEventsResponse upsert_instrument_events(scope, code, upsert_instrument_event_request=upsert_instrument_event_request)

[EARLY ACCESS] UpsertInstrumentEvents: Upsert instrument events to the provided corporate actions source.

Batch upsert instrument events to corporate action sources.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    scope = 'scope_example' # str | The scope of the corporate action source.
code = 'code_example' # str | The code of the corporate action source.
upsert_instrument_event_request = [{"instrumentEventId":"MyStockSplitId","instrumentIdentifiers":{"Instrument/default/Figi":"BBG001S6PJ31"},"description":"2-for-1 stock split of instrument BBG001S6PJ31","instrumentEvent":{"announcementDate":"2018-03-01T00:00:00.0000000+00:00","exDate":"2018-06-01T00:00:00.0000000+00:00","recordDate":"2018-06-02T00:00:00.0000000+00:00","paymentDate":"2018-08-02T00:00:00.0000000+00:00","inputTransition":{"unitsFactor":1,"costFactor":1},"outputTransitions":[{"instrumentIdentifiers":{"Instrument/default/Figi":"BBG001S6PJ31"},"unitsFactor":2,"costFactor":1,"rounding":{"stockUnits":{"roundingType":"NearestRoundHalfAwayFromZero"}}}],"instrumentEventType":"TransitionEvent"},"properties":[]}] # list[UpsertInstrumentEventRequest] | The instrument event definitions. (optional)

    try:
        # [EARLY ACCESS] UpsertInstrumentEvents: Upsert instrument events to the provided corporate actions source.
        api_response = api_instance.upsert_instrument_events(scope, code, upsert_instrument_event_request=upsert_instrument_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->upsert_instrument_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the corporate action source. | 
 **code** | **str**| The code of the corporate action source. | 
 **upsert_instrument_event_request** | [**list[UpsertInstrumentEventRequest]**](UpsertInstrumentEventRequest.md)| The instrument event definitions. | [optional] 

### Return type

[**UpsertInstrumentEventsResponse**](UpsertInstrumentEventsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Instrument Events Upserted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

