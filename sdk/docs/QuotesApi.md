# lusid.QuotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_quotes**](QuotesApi.md#delete_quotes) | **POST** /api/quotes/{scope}/$delete | Delete a quote
[**get_quotes**](QuotesApi.md#get_quotes) | **POST** /api/quotes/{scope}/$get | Get quotes
[**upsert_quotes**](QuotesApi.md#upsert_quotes) | **POST** /api/quotes/{scope} | Upsert quotes


# **delete_quotes**
> DeleteQuotesResponse delete_quotes(scope, delete_quote_request=delete_quote_request)

Delete a quote

Delete the specified quotes. In order for a quote to be deleted the id and effectiveFrom date must exactly match.

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.QuotesApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the quote
delete_quote_request = NULL # list[DeleteQuoteRequest] | The quotes to delete (optional)

try:
    # Delete a quote
    api_response = api_instance.delete_quotes(scope, delete_quote_request=delete_quote_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->delete_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quote | 
 **delete_quote_request** | [**list[DeleteQuoteRequest]**](list.md)| The quotes to delete | [optional] 

### Return type

[**DeleteQuotesResponse**](DeleteQuotesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes**
> GetQuotesResponse get_quotes(scope, effective_at=effective_at, as_at=as_at, max_age=max_age, page=page, limit=limit, quote_id=quote_id)

Get quotes

Get quotes effective at the specified date/time (if any). An optional maximum age of quotes can be specified, and is infinite by default.  Quotes which are older than this at the time of the effective date/time will not be returned.  MaxAge is a duration of time represented in an ISO8601 format, eg. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).  The results are paged, and by default the 1st page of results is returned with a limit of 100 results per page

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.QuotesApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the quotes
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The date/time from which the quotes are effective (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The 'AsAt' date/time (optional)
max_age = 'max_age_example' # str | Optional. The quote staleness tolerance (optional)
page = 56 # int | Optional. The page of results to return (optional)
limit = 56 # int | Optional. The number of results per page (optional)
quote_id = NULL # list[QuoteId] | The ids of the quotes (optional)

try:
    # Get quotes
    api_response = api_instance.get_quotes(scope, effective_at=effective_at, as_at=as_at, max_age=max_age, page=page, limit=limit, quote_id=quote_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes | 
 **effective_at** | **datetime**| Optional. The date/time from which the quotes are effective | [optional] 
 **as_at** | **datetime**| Optional. The &#39;AsAt&#39; date/time | [optional] 
 **max_age** | **str**| Optional. The quote staleness tolerance | [optional] 
 **page** | **int**| Optional. The page of results to return | [optional] 
 **limit** | **int**| Optional. The number of results per page | [optional] 
 **quote_id** | [**list[QuoteId]**](list.md)| The ids of the quotes | [optional] 

### Return type

[**GetQuotesResponse**](GetQuotesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_quotes**
> UpsertQuotesResponse upsert_quotes(scope, upsert_quote_request=upsert_quote_request)

Upsert quotes

Upsert quotes effective at the specified time. If a quote is added with the same id (and is effective at the same time) as an existing quote, then the more recently added quote will be returned when queried

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.QuotesApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the quotes
upsert_quote_request = NULL # list[UpsertQuoteRequest] | The quotes to upsert (optional)

try:
    # Upsert quotes
    api_response = api_instance.upsert_quotes(scope, upsert_quote_request=upsert_quote_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->upsert_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes | 
 **upsert_quote_request** | [**list[UpsertQuoteRequest]**](list.md)| The quotes to upsert | [optional] 

### Return type

[**UpsertQuotesResponse**](UpsertQuotesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

