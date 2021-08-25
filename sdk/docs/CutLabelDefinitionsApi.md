# lusid.CutLabelDefinitionsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:33218*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cut_label_definition**](CutLabelDefinitionsApi.md#create_cut_label_definition) | **POST** /api/systemconfiguration/cutlabels | [EARLY ACCESS] Create a Cut Label
[**delete_cut_label_definition**](CutLabelDefinitionsApi.md#delete_cut_label_definition) | **DELETE** /api/systemconfiguration/cutlabels/{code} | [EARLY ACCESS] Delete a Cut Label
[**get_cut_label_definition**](CutLabelDefinitionsApi.md#get_cut_label_definition) | **GET** /api/systemconfiguration/cutlabels/{code} | [EARLY ACCESS] Get a Cut Label
[**list_cut_label_definitions**](CutLabelDefinitionsApi.md#list_cut_label_definitions) | **GET** /api/systemconfiguration/cutlabels | [EARLY ACCESS] List Existing Cut Labels
[**update_cut_label_definition**](CutLabelDefinitionsApi.md#update_cut_label_definition) | **PUT** /api/systemconfiguration/cutlabels/{code} | [EARLY ACCESS] Update a Cut Label


# **create_cut_label_definition**
> CutLabelDefinition create_cut_label_definition(create_cut_label_definition_request=create_cut_label_definition_request)

[EARLY ACCESS] Create a Cut Label

Create a Cut Label valid in all scopes

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:33218
configuration.host = "http://local-unit-test-server.lusid.com:33218"
# Create an instance of the API class
api_instance = lusid.CutLabelDefinitionsApi(lusid.ApiClient(configuration))
create_cut_label_definition_request = {"code":"CutLabelCode","displayName":"CutLabelDisplayName","description":"description of cut label","cutLocalTime":{"hours":17,"minutes":0},"timeZone":"GB"} # CreateCutLabelDefinitionRequest | The cut label definition (optional)

try:
    # [EARLY ACCESS] Create a Cut Label
    api_response = api_instance.create_cut_label_definition(create_cut_label_definition_request=create_cut_label_definition_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CutLabelDefinitionsApi->create_cut_label_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cut_label_definition_request** | [**CreateCutLabelDefinitionRequest**](CreateCutLabelDefinitionRequest.md)| The cut label definition | [optional] 

### Return type

[**CutLabelDefinition**](CutLabelDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created cut label |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cut_label_definition**
> datetime delete_cut_label_definition(code)

[EARLY ACCESS] Delete a Cut Label

Delete a specified cut label

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:33218
configuration.host = "http://local-unit-test-server.lusid.com:33218"
# Create an instance of the API class
api_instance = lusid.CutLabelDefinitionsApi(lusid.ApiClient(configuration))
code = 'code_example' # str | The Code of the Cut Label that is being Deleted

try:
    # [EARLY ACCESS] Delete a Cut Label
    api_response = api_instance.delete_cut_label_definition(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CutLabelDefinitionsApi->delete_cut_label_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The Code of the Cut Label that is being Deleted | 

### Return type

**datetime**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time of deletion |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cut_label_definition**
> CutLabelDefinition get_cut_label_definition(code, as_at=as_at)

[EARLY ACCESS] Get a Cut Label

Get a specified cut label at a given time

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:33218
configuration.host = "http://local-unit-test-server.lusid.com:33218"
# Create an instance of the API class
api_instance = lusid.CutLabelDefinitionsApi(lusid.ApiClient(configuration))
code = 'code_example' # str | The Code of the Cut Label that is being queried
as_at = '2013-10-20T19:20:30+01:00' # datetime | The time at which to get the Cut Label (optional)

try:
    # [EARLY ACCESS] Get a Cut Label
    api_response = api_instance.get_cut_label_definition(code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CutLabelDefinitionsApi->get_cut_label_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The Code of the Cut Label that is being queried | 
 **as_at** | **datetime**| The time at which to get the Cut Label | [optional] 

### Return type

[**CutLabelDefinition**](CutLabelDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested cut label |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cut_label_definitions**
> PagedResourceListOfCutLabelDefinition list_cut_label_definitions(as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter, page=page)

[EARLY ACCESS] List Existing Cut Labels

List all the Cut Label Definitions that are valid at the given AsAt time

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:33218
configuration.host = "http://local-unit-test-server.lusid.com:33218"
# Create an instance of the API class
api_instance = lusid.CutLabelDefinitionsApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The As At time at which listed Cut Labels are valid (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set.              For example, to filter on code, use \"code eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
page = 'page_example' # str | The pagination token to use to continue listing cut labels from a previous call This value is returned from the previous call.  If a pagination token is provided the sortBy, filter, and asAt fields  must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)

try:
    # [EARLY ACCESS] List Existing Cut Labels
    api_response = api_instance.list_cut_label_definitions(as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CutLabelDefinitionsApi->list_cut_label_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The As At time at which listed Cut Labels are valid | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.              For example, to filter on code, use \&quot;code eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **page** | **str**| The pagination token to use to continue listing cut labels from a previous call This value is returned from the previous call.  If a pagination token is provided the sortBy, filter, and asAt fields  must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 

### Return type

[**PagedResourceListOfCutLabelDefinition**](PagedResourceListOfCutLabelDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of cut labels |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cut_label_definition**
> CutLabelDefinition update_cut_label_definition(code, update_cut_label_definition_request=update_cut_label_definition_request)

[EARLY ACCESS] Update a Cut Label

Update a specified cut label

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:33218
configuration.host = "http://local-unit-test-server.lusid.com:33218"
# Create an instance of the API class
api_instance = lusid.CutLabelDefinitionsApi(lusid.ApiClient(configuration))
code = 'code_example' # str | The Code of the Cut Label that is being updated
update_cut_label_definition_request = {"displayName":"CutLabelDisplayName","description":"description of cut label","cutLocalTime":{"hours":17,"minutes":0},"timeZone":"GB"} # UpdateCutLabelDefinitionRequest | The cut label update definition (optional)

try:
    # [EARLY ACCESS] Update a Cut Label
    api_response = api_instance.update_cut_label_definition(code, update_cut_label_definition_request=update_cut_label_definition_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CutLabelDefinitionsApi->update_cut_label_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The Code of the Cut Label that is being updated | 
 **update_cut_label_definition_request** | [**UpdateCutLabelDefinitionRequest**](UpdateCutLabelDefinitionRequest.md)| The cut label update definition | [optional] 

### Return type

[**CutLabelDefinition**](CutLabelDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cut label |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

