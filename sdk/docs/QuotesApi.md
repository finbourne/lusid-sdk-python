# lusid.QuotesApi

All URIs are relative to *http://local-unit-test-server.lusid.com:42748*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_quotes**](QuotesApi.md#delete_quotes) | **POST** /api/quotes/{scope}/$delete | [EARLY ACCESS] DeleteQuotes: Delete quotes
[**get_quotes**](QuotesApi.md#get_quotes) | **POST** /api/quotes/{scope}/$get | [EARLY ACCESS] GetQuotes: Get quotes
[**list_quotes**](QuotesApi.md#list_quotes) | **GET** /api/quotes/{scope}/$deprecated | [DEPRECATED] ListQuotes: List quotes
[**list_quotes_for_scope**](QuotesApi.md#list_quotes_for_scope) | **GET** /api/quotes/{scope} | [EARLY ACCESS] ListQuotesForScope: List quotes for scope
[**upsert_quotes**](QuotesApi.md#upsert_quotes) | **POST** /api/quotes/{scope} | [EARLY ACCESS] UpsertQuotes: Upsert quotes


# **delete_quotes**
> AnnulQuotesResponse delete_quotes(scope, request_body=request_body)

[EARLY ACCESS] DeleteQuotes: Delete quotes

Delete one or more specified quotes from a single scope. A quote is identified by its unique id which includes information about  the type of quote as well as the exact effective datetime (to the microsecond) from which it became valid.                In the request each quote must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each quote in the response.                The response will return both the collection of successfully deleted quotes, as well as those that failed.  For the failures a reason will be provided explaining why the quote could not be deleted.                It is important to always check the failed set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:42748
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.QuotesApi(api_client)
    scope = 'scope_example' # str | The scope of the quotes to delete.
request_body = {"dS-VOD-PRICE-MID":{"quoteSeriesId":{"provider":"DataScope","priceSource":"","instrumentId":"GB00BH4HKS39","instrumentIdType":"Isin","quoteType":"Price","field":"mid"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00"}} # dict(str, QuoteId) | The quotes to delete keyed by a unique correlation id. (optional)

    try:
        # [EARLY ACCESS] DeleteQuotes: Delete quotes
        api_response = api_instance.delete_quotes(scope, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QuotesApi->delete_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes to delete. | 
 **request_body** | [**dict(str, QuoteId)**](QuoteId.md)| The quotes to delete keyed by a unique correlation id. | [optional] 

### Return type

[**AnnulQuotesResponse**](AnnulQuotesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully deleted quotes along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes**
> GetQuotesResponse get_quotes(scope, effective_at=effective_at, as_at=as_at, max_age=max_age, request_body=request_body)

[EARLY ACCESS] GetQuotes: Get quotes

Get one or more quotes from a single scope.                Each quote can be identified by its time invariant quote series id.                For each quote series id LUSID will return the most recent quote with respect to the provided (or default) effective datetime.                 An optional maximum age range window can be specified which defines how far back to look back for a quote from the specified effective datetime.  LUSID will return the most recent quote within this window.                In the request each quote series id must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each quote in the response.                The response will return three collections. One, the successfully retrieved quotes. Two, those that had a  valid quote series id but could not be found. Three, those that failed because LUSID could not construct a valid quote series id from the request.    For the quotes that failed or could not be found a reason will be provided explaining why the quote could not be retrieved.                It is important to always check the failed and not found sets for any unsuccessful results.  The maximum number of quotes that this method can get per request is 2,000.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:42748
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.QuotesApi(api_client)
    scope = 'scope_example' # str | The scope of the quotes to retrieve.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the quotes. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the quotes. Defaults to return the latest version of each quote if not specified. (optional)
max_age = 'max_age_example' # str | The duration of the look back window in an ISO8601 time interval format e.g. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime or cut label to generate a effective datetime window inside which a quote must exist to be retrieved. (optional)
request_body = {"dS-VOD-PRICE-MID":{"provider":"DataScope","priceSource":"","instrumentId":"GB00BH4HKS39","instrumentIdType":"Isin","quoteType":"Price","field":"mid"}} # dict(str, QuoteSeriesId) | The time invariant quote series ids of the quotes to retrieve. These need to be               keyed by a unique correlation id allowing the retrieved quote to be identified in the response. (optional)

    try:
        # [EARLY ACCESS] GetQuotes: Get quotes
        api_response = api_instance.get_quotes(scope, effective_at=effective_at, as_at=as_at, max_age=max_age, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QuotesApi->get_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes to retrieve. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the quotes. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the quotes. Defaults to return the latest version of each quote if not specified. | [optional] 
 **max_age** | **str**| The duration of the look back window in an ISO8601 time interval format e.g. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime or cut label to generate a effective datetime window inside which a quote must exist to be retrieved. | [optional] 
 **request_body** | [**dict(str, QuoteSeriesId)**](QuoteSeriesId.md)| The time invariant quote series ids of the quotes to retrieve. These need to be               keyed by a unique correlation id allowing the retrieved quote to be identified in the response. | [optional] 

### Return type

[**GetQuotesResponse**](GetQuotesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved quotes along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quotes**
> ResourceListOfQuote list_quotes(scope, as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[DEPRECATED] ListQuotes: List quotes

List all the quotes from a single scope at the specified date/time  Please use M:Finbourne.WebApi.Controllers.QuotesController.ListQuotesForScope(System.String,System.Nullable{System.DateTimeOffset},System.String,System.Nullable{System.Int32},System.Nullable{System.Int32},System.String) - the signature and behaviour of this endpoint will be changing to omit scope

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:42748
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.QuotesApi(api_client)
    scope = 'scope_example' # str | The scope of the quotes to list.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the quotes. Defaults to latest if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing quotes from a previous call to list quotes.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [DEPRECATED] ListQuotes: List quotes
        api_response = api_instance.list_quotes(scope, as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QuotesApi->list_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes to list. | 
 **as_at** | **datetime**| The asAt datetime at which to list the quotes. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing quotes from a previous call to list quotes.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfQuote**](ResourceListOfQuote.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested quotes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quotes_for_scope**
> ResourceListOfQuote list_quotes_for_scope(scope, as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EARLY ACCESS] ListQuotesForScope: List quotes for scope

List all the quotes from a single scope at the specified date/time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:42748
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.QuotesApi(api_client)
    scope = 'scope_example' # str | The scope of the quotes to list.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the quotes. Defaults to latest if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing quotes from a previous call to list quotes.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] ListQuotesForScope: List quotes for scope
        api_response = api_instance.list_quotes_for_scope(scope, as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QuotesApi->list_quotes_for_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes to list. | 
 **as_at** | **datetime**| The asAt datetime at which to list the quotes. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing quotes from a previous call to list quotes.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfQuote**](ResourceListOfQuote.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested quotes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_quotes**
> UpsertQuotesResponse upsert_quotes(scope, request_body=request_body)

[EARLY ACCESS] UpsertQuotes: Upsert quotes

Update or insert one or more quotes in a single scope. A quote will be updated if it already exists  and inserted if it does not.                In the request each quote must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each quote in the response.                The response will return both the collection of successfully updated or inserted quotes, as well as those that failed.  For the failures a reason will be provided explaining why the quote could not be updated or inserted.                It is important to always check the failed set for any unsuccessful results.  The maximum number of quotes that this method can upsert per request is 2,000.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:42748
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42748"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.QuotesApi(api_client)
    scope = 'scope_example' # str | The scope to use when updating or inserting the quotes.
request_body = {"dS-VOD-PRICE-MID":{"quoteId":{"quoteSeriesId":{"provider":"DataScope","priceSource":"","instrumentId":"GB00BH4HKS39","instrumentIdType":"Isin","quoteType":"Price","field":"mid"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00"},"metricValue":{"value":1460,"unit":"CNY"}},"o-C-EURUSD-PRICE-BID":{"quoteId":{"quoteSeriesId":{"provider":"Oanda","priceSource":"Citi","instrumentId":"EUR/USD","instrumentIdType":"CurrencyPair","quoteType":"Price","field":"bid"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00"},"metricValue":{"value":1.367,"unit":"EUR/USD"},"lineage":"Oanda/FxRates_2018-10-22T00:00:00.0000000+00:00.csv"}} # dict(str, UpsertQuoteRequest) | The quotes to update or insert keyed by a unique correlation id. (optional)

    try:
        # [EARLY ACCESS] UpsertQuotes: Upsert quotes
        api_response = api_instance.upsert_quotes(scope, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QuotesApi->upsert_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the quotes. | 
 **request_body** | [**dict(str, UpsertQuoteRequest)**](UpsertQuoteRequest.md)| The quotes to update or insert keyed by a unique correlation id. | [optional] 

### Return type

[**UpsertQuotesResponse**](UpsertQuotesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted quotes along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

