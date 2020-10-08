# lusid.SearchApi

All URIs are relative to *http://localhost:58761*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portfolio_groups_search**](SearchApi.md#portfolio_groups_search) | **POST** /api/search/portfoliogroups | [DEPRECATED] Portfolio groups search
[**portfolios_search**](SearchApi.md#portfolios_search) | **POST** /api/search/portfolios | [DEPRECATED] Portfolios search
[**properties_search**](SearchApi.md#properties_search) | **POST** /api/search/propertydefinitions | [DEPRECATED] Search property definitions


# **portfolio_groups_search**
> ResourceListOfPortfolioGroup portfolio_groups_search(body, filter=filter)

[DEPRECATED] Portfolio groups search

Search across all portfolio groups across all scopes.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:58761
configuration.host = "http://localhost:58761"
# Create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
body = None # object | The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request.
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [DEPRECATED] Portfolio groups search
    api_response = api_instance.portfolio_groups_search(body, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->portfolio_groups_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request. | 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfPortfolioGroup**](ResourceListOfPortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio groups found by the search |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolios_search**
> ResourceListOfPortfolioSearchResult portfolios_search(body, filter=filter)

[DEPRECATED] Portfolios search

Search across all portfolios across all scopes.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:58761
configuration.host = "http://localhost:58761"
# Create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
body = None # object | The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request.
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [DEPRECATED] Portfolios search
    api_response = api_instance.portfolios_search(body, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->portfolios_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request. | 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfPortfolioSearchResult**](ResourceListOfPortfolioSearchResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolios found by the search |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_search**
> ResourceListOfPropertyDefinition properties_search(body, filter=filter)

[DEPRECATED] Search property definitions

Search across all user defined property definitions across all scopes.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:58761
configuration.host = "http://localhost:58761"
# Create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
body = None # object | The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request.
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [DEPRECATED] Search property definitions
    api_response = api_instance.properties_search(body, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->properties_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request. | 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfPropertyDefinition**](ResourceListOfPropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The property definitions found by the search |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

