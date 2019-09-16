# lusid.PropertyDefinitionsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_property_definition**](PropertyDefinitionsApi.md#create_property_definition) | **POST** /api/propertydefinitions | [EARLY ACCESS] Create property definition
[**delete_property_definition**](PropertyDefinitionsApi.md#delete_property_definition) | **DELETE** /api/propertydefinitions/{domain}/{scope}/{code} | [EARLY ACCESS] Delete property definition
[**get_multiple_property_definitions**](PropertyDefinitionsApi.md#get_multiple_property_definitions) | **GET** /api/propertydefinitions | [EARLY ACCESS] Get multiple property definitions
[**get_property_definition**](PropertyDefinitionsApi.md#get_property_definition) | **GET** /api/propertydefinitions/{domain}/{scope}/{code} | [EARLY ACCESS] Get property definition
[**update_property_definition**](PropertyDefinitionsApi.md#update_property_definition) | **PUT** /api/propertydefinitions/{domain}/{scope}/{code} | [EARLY ACCESS] Update property definition


# **create_property_definition**
> PropertyDefinition create_property_definition(definition)

[EARLY ACCESS] Create property definition

Define a new property.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
definition = lusid.CreatePropertyDefinitionRequest() # CreatePropertyDefinitionRequest | The definition of the new property.

try:
    # [EARLY ACCESS] Create property definition
    api_response = api_instance.create_property_definition(definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->create_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition** | [**CreatePropertyDefinitionRequest**](CreatePropertyDefinitionRequest.md)| The definition of the new property. | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_definition**
> DeletedEntityResponse delete_property_definition(domain, scope, code)

[EARLY ACCESS] Delete property definition

Delete the definition of the specified property.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
domain = 'domain_example' # str | The domain of the property to be deleted.
scope = 'scope_example' # str | The scope of the property to be deleted.
code = 'code_example' # str | The code of the property to be deleted. Together with the domain and scope this uniquely              identifies the property.

try:
    # [EARLY ACCESS] Delete property definition
    api_response = api_instance.delete_property_definition(domain, scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->delete_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property to be deleted. | 
 **scope** | **str**| The scope of the property to be deleted. | 
 **code** | **str**| The code of the property to be deleted. Together with the domain and scope this uniquely              identifies the property. | 

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
**200** | The time that the property definition was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_property_definitions**
> ResourceListOfPropertyDefinition get_multiple_property_definitions(property_keys, as_at=as_at, filter=filter)

[EARLY ACCESS] Get multiple property definitions

Retrieve the definition of one or more specified properties.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
property_keys = ['property_keys_example'] # list[str] | One or more property keys which identify each property that a definition should              be retrieved for. The format for each property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the property definitions. Defaults to return              the latest version of each definition if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EARLY ACCESS] Get multiple property definitions
    api_response = api_instance.get_multiple_property_definitions(property_keys, as_at=as_at, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->get_multiple_property_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_keys** | [**list[str]**](str.md)| One or more property keys which identify each property that a definition should              be retrieved for. The format for each property key is {domain}/{scope}/{code}, e.g. &#39;Portfolio/Manager/Id&#39;. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the property definitions. Defaults to return              the latest version of each definition if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfPropertyDefinition**](ResourceListOfPropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definitions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_definition**
> PropertyDefinition get_property_definition(domain, scope, code, as_at=as_at)

[EARLY ACCESS] Get property definition

Retrieve the definition of a specified property.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
domain = 'domain_example' # str | The domain of the specified property.
scope = 'scope_example' # str | The scope of the specified property.
code = 'code_example' # str | The code of the specified property. Together with the domain and scope this uniquely              identifies the property.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the property definition. Defaults to return              the latest version of the definition if not specified. (optional)

try:
    # [EARLY ACCESS] Get property definition
    api_response = api_instance.get_property_definition(domain, scope, code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->get_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the specified property. | 
 **scope** | **str**| The scope of the specified property. | 
 **code** | **str**| The code of the specified property. Together with the domain and scope this uniquely              identifies the property. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the property definition. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_definition**
> PropertyDefinition update_property_definition(domain, scope, code, definition=definition)

[EARLY ACCESS] Update property definition

Update the definition of a specified existing property. Not all elements within a property definition  are modifiable due to the potential implications for values already stored against the property.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
domain = 'domain_example' # str | The domain of the property being updated.
scope = 'scope_example' # str | The scope of the property being updated.
code = 'code_example' # str | The code of the property being updated. Together with the domain and scope this uniquely              identifies the property.
definition = lusid.UpdatePropertyDefinitionRequest() # UpdatePropertyDefinitionRequest | The updated definition of the property. (optional)

try:
    # [EARLY ACCESS] Update property definition
    api_response = api_instance.update_property_definition(domain, scope, code, definition=definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->update_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property being updated. | 
 **scope** | **str**| The scope of the property being updated. | 
 **code** | **str**| The code of the property being updated. Together with the domain and scope this uniquely              identifies the property. | 
 **definition** | [**UpdatePropertyDefinitionRequest**](UpdatePropertyDefinitionRequest.md)| The updated definition of the property. | [optional] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

