# lusid.AggregationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregation_by_group**](AggregationApi.md#get_aggregation_by_group) | **POST** /api/portfoliogroups/{scope}/{code}/$aggregate | Aggregate data in a portfolio group
[**get_aggregation_by_portfolio**](AggregationApi.md#get_aggregation_by_portfolio) | **POST** /api/portfolios/{scope}/{code}/$aggregate | Aggregate data in a portfolio
[**get_aggregation_by_result_set**](AggregationApi.md#get_aggregation_by_result_set) | **POST** /api/results/{scope}/{resultsKey}/$aggregate | Aggregate using result data
[**get_nested_aggregation_by_group**](AggregationApi.md#get_nested_aggregation_by_group) | **POST** /api/portfoliogroups/{scope}/{code}/$aggregatenested | Aggregate data in a portfolio group, as nested


# **get_aggregation_by_group**
> ListAggregationResponse get_aggregation_by_group(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)

Aggregate data in a portfolio group

Aggregate data sourced from the specified portfolio group

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
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
aggregation_request = lusid.AggregationRequest() # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # Aggregate data in a portfolio group
    api_response = api_instance.get_aggregation_by_group(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_aggregation_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_by_portfolio**
> ListAggregationResponse get_aggregation_by_portfolio(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)

Aggregate data in a portfolio

Aggregate data sourced from the specified portfolio

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
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
aggregation_request = lusid.AggregationRequest() # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # Aggregate data in a portfolio
    api_response = api_instance.get_aggregation_by_portfolio(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_aggregation_by_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_by_result_set**
> ListAggregationResponse get_aggregation_by_result_set(scope, results_key, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)

Aggregate using result data

Aggregate data from a previously-run Result data set into a flat row of results

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
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the Result data set
results_key = 'results_key_example' # str | The key of the Result data set
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
aggregation_request = lusid.AggregationRequest() # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # Aggregate using result data
    api_response = api_instance.get_aggregation_by_result_set(scope, results_key, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_aggregation_by_result_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Result data set | 
 **results_key** | **str**| The key of the Result data set | 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nested_aggregation_by_group**
> NestedAggregationResponse get_nested_aggregation_by_group(scope, code, aggregation_request=aggregation_request)

Aggregate data in a portfolio group, as nested

Obsolete - Aggregate data sourced from the specified portfolio group into a nested structure. Data is nested following the group-by specifications.

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
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
aggregation_request = lusid.AggregationRequest() # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # Aggregate data in a portfolio group, as nested
    api_response = api_instance.get_nested_aggregation_by_group(scope, code, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_nested_aggregation_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**NestedAggregationResponse**](NestedAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

