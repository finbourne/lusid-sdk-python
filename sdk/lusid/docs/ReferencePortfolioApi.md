# lusid.ReferencePortfolioApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reference_portfolio**](ReferencePortfolioApi.md#create_reference_portfolio) | **POST** /api/referenceportfolios/{scope} | Create reference portfolio
[**get_reference_portfolio_constituents**](ReferencePortfolioApi.md#get_reference_portfolio_constituents) | **GET** /api/referenceportfolios/{scope}/{code}/constituents | Get constituents
[**list_constituents_adjustments**](ReferencePortfolioApi.md#list_constituents_adjustments) | **GET** /api/referenceportfolios/{scope}/{code}/constituentsadjustments | Gets constituents adjustments in an interval of effective time.
[**upsert_reference_portfolio_constituents**](ReferencePortfolioApi.md#upsert_reference_portfolio_constituents) | **POST** /api/referenceportfolios/{scope}/{code}/constituents | Add constituents


# **create_reference_portfolio**
> Portfolio create_reference_portfolio(scope, create_reference_portfolio_request=create_reference_portfolio_request)

Create reference portfolio

Create a new reference portfolio.

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
api_instance = lusid.ReferencePortfolioApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The intended scope of the portfolio
create_reference_portfolio_request = lusid.CreateReferencePortfolioRequest() # CreateReferencePortfolioRequest | The portfolio creation request object (optional)

try:
    # Create reference portfolio
    api_response = api_instance.create_reference_portfolio(scope, create_reference_portfolio_request=create_reference_portfolio_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferencePortfolioApi->create_reference_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The intended scope of the portfolio | 
 **create_reference_portfolio_request** | [**CreateReferencePortfolioRequest**](CreateReferencePortfolioRequest.md)| The portfolio creation request object | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_portfolio_constituents**
> GetReferencePortfolioConstituentsResponse get_reference_portfolio_constituents(scope, code, effective_at=effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit)

Get constituents

Get all the constituents in the specified reference portfolio

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
api_instance = lusid.ReferencePortfolioApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the constituents to retrieve (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many (optional)

try:
    # Get constituents
    api_response = api_instance.get_reference_portfolio_constituents(scope, code, effective_at=effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferencePortfolioApi->get_reference_portfolio_constituents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **datetime**| Optional. The effective date of the constituents to retrieve | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many | [optional] 

### Return type

[**GetReferencePortfolioConstituentsResponse**](GetReferencePortfolioConstituentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_constituents_adjustments**
> ResourceListOfConstituentsAdjustmentHeader list_constituents_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at_time=as_at_time)

Gets constituents adjustments in an interval of effective time.

Specify a time period in which you'd like to see the list of times that adjustments where made to this portfolio

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
api_instance = lusid.ReferencePortfolioApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | Code for the portfolio
from_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Events between this time (inclusive) and the toEffectiveAt are returned. (optional)
to_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Events between this time (inclusive) and the fromEffectiveAt are returned. (optional)
as_at_time = '2013-10-20T19:20:30+01:00' # datetime | The as-at time for which the result is valid. (optional)

try:
    # Gets constituents adjustments in an interval of effective time.
    api_response = api_instance.list_constituents_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at_time=as_at_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferencePortfolioApi->list_constituents_adjustments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| Code for the portfolio | 
 **from_effective_at** | **datetime**| Events between this time (inclusive) and the toEffectiveAt are returned. | [optional] 
 **to_effective_at** | **datetime**| Events between this time (inclusive) and the fromEffectiveAt are returned. | [optional] 
 **as_at_time** | **datetime**| The as-at time for which the result is valid. | [optional] 

### Return type

[**ResourceListOfConstituentsAdjustmentHeader**](ResourceListOfConstituentsAdjustmentHeader.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_reference_portfolio_constituents**
> UpsertReferencePortfolioConstituentsResponse upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request=upsert_reference_portfolio_constituents_request)

Add constituents

Add constituents to the specified reference portfolio.

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
api_instance = lusid.ReferencePortfolioApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
upsert_reference_portfolio_constituents_request = lusid.UpsertReferencePortfolioConstituentsRequest() # UpsertReferencePortfolioConstituentsRequest | The constituents to upload to the portfolio (optional)

try:
    # Add constituents
    api_response = api_instance.upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request=upsert_reference_portfolio_constituents_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferencePortfolioApi->upsert_reference_portfolio_constituents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **upsert_reference_portfolio_constituents_request** | [**UpsertReferencePortfolioConstituentsRequest**](UpsertReferencePortfolioConstituentsRequest.md)| The constituents to upload to the portfolio | [optional] 

### Return type

[**UpsertReferencePortfolioConstituentsResponse**](UpsertReferencePortfolioConstituentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

