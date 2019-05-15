# lusid.PropertyDefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_property_definition**](PropertyDefinitionsApi.md#create_property_definition) | **POST** /api/propertydefinitions | Define a new property
[**delete_property_definition**](PropertyDefinitionsApi.md#delete_property_definition) | **DELETE** /api/propertydefinitions/{domain}/{scope}/{code} | Delete property definition
[**get_multiple_property_definitions**](PropertyDefinitionsApi.md#get_multiple_property_definitions) | **GET** /api/propertydefinitions | Get multiple property definitions
[**get_property_definition**](PropertyDefinitionsApi.md#get_property_definition) | **GET** /api/propertydefinitions/{domain}/{scope}/{code} | Get property definition
[**update_property_definition**](PropertyDefinitionsApi.md#update_property_definition) | **PUT** /api/propertydefinitions/{domain}/{scope}/{code} | Update the definition of the specified existing property


# **create_property_definition**
> PropertyDefinition create_property_definition(definition=definition)

Define a new property

Create a new property definition

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

# create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
definition = lusid.CreatePropertyDefinitionRequest() # CreatePropertyDefinitionRequest | The definition of the new property (optional)

try:
    # Define a new property
    api_response = api_instance.create_property_definition(definition=definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->create_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition** | [**CreatePropertyDefinitionRequest**](CreatePropertyDefinitionRequest.md)| The definition of the new property | [optional] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_definition**
> DeletedEntityResponse delete_property_definition(domain, scope, code)

Delete property definition

Delete the definition of the specified property

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

# create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
domain = 'domain_example' # str | The Property Domain of the property to be deleted
scope = 'scope_example' # str | The scope of the property to be deleted
code = 'code_example' # str | The code of the property to be deleted

try:
    # Delete property definition
    api_response = api_instance.delete_property_definition(domain, scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->delete_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The Property Domain of the property to be deleted | 
 **scope** | **str**| The scope of the property to be deleted | 
 **code** | **str**| The code of the property to be deleted | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_property_definitions**
> ResourceListOfPropertyDefinition get_multiple_property_definitions(property_keys=property_keys, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)

Get multiple property definitions

Get one or more property definitions

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

# create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
property_keys = ['property_keys_example'] # list[str] | One or more keys for properties for which the schema should be returned (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)

try:
    # Get multiple property definitions
    api_response = api_instance.get_multiple_property_definitions(property_keys=property_keys, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->get_multiple_property_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_keys** | [**list[str]**](str.md)| One or more keys for properties for which the schema should be returned | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 

### Return type

[**ResourceListOfPropertyDefinition**](ResourceListOfPropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_definition**
> PropertyDefinition get_property_definition(domain, scope, code, as_at=as_at)

Get property definition

Retrieve the definition for the identified property

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

# create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
domain = 'domain_example' # str | The Property Domain of the requested property
scope = 'scope_example' # str | The scope of the requested property
code = 'code_example' # str | The code of the requested property
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)

try:
    # Get property definition
    api_response = api_instance.get_property_definition(domain, scope, code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->get_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The Property Domain of the requested property | 
 **scope** | **str**| The scope of the requested property | 
 **code** | **str**| The code of the requested property | 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_definition**
> PropertyDefinition update_property_definition(domain, scope, code, definition=definition)

Update the definition of the specified existing property

Not all elements within a property definition are modifiable due to the potential implications for data  already stored against these properties

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

# create an instance of the API class
api_instance = lusid.PropertyDefinitionsApi(lusid.ApiClient(configuration))
domain = 'domain_example' # str | The Property Domain of the property being updated
scope = 'scope_example' # str | The scope of the property to be updated
code = 'code_example' # str | The code of the property to be updated
definition = lusid.UpdatePropertyDefinitionRequest() # UpdatePropertyDefinitionRequest | The updated definition of the property (optional)

try:
    # Update the definition of the specified existing property
    api_response = api_instance.update_property_definition(domain, scope, code, definition=definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyDefinitionsApi->update_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The Property Domain of the property being updated | 
 **scope** | **str**| The scope of the property to be updated | 
 **code** | **str**| The code of the property to be updated | 
 **definition** | [**UpdatePropertyDefinitionRequest**](UpdatePropertyDefinitionRequest.md)| The updated definition of the property | [optional] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

