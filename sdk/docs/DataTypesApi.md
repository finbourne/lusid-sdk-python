# lusid.DataTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_type**](DataTypesApi.md#create_data_type) | **POST** /api/datatypes | Create data type definition
[**get_data_type**](DataTypesApi.md#get_data_type) | **GET** /api/datatypes/{scope}/{code} | Get data type definition
[**get_units_from_data_type**](DataTypesApi.md#get_units_from_data_type) | **GET** /api/datatypes/{scope}/{code}/units | Get units from data type
[**list_data_types**](DataTypesApi.md#list_data_types) | **GET** /api/datatypes/{scope} | List data types
[**update_data_type**](DataTypesApi.md#update_data_type) | **PUT** /api/datatypes/{scope}/{code} | Update data type definition


# **create_data_type**
> DataType create_data_type(request=request)

Create data type definition

Create a new data type definition    Data types cannot be created in either the \"default\" or \"system\" scopes.

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
api_instance = lusid.DataTypesApi(lusid.ApiClient(configuration))
request = lusid.CreateDataTypeRequest() # CreateDataTypeRequest | The definition of the new data type (optional)

try:
    # Create data type definition
    api_response = api_instance.create_data_type(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->create_data_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateDataTypeRequest**](CreateDataTypeRequest.md)| The definition of the new data type | [optional] 

### Return type

[**DataType**](DataType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_type**
> DataType get_data_type(scope, code)

Get data type definition

Get the definition of a specified data type

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
api_instance = lusid.DataTypesApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the data type
code = 'code_example' # str | The code of the data type

try:
    # Get data type definition
    api_response = api_instance.get_data_type(scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->get_data_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | 
 **code** | **str**| The code of the data type | 

### Return type

[**DataType**](DataType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_units_from_data_type**
> ResourceListOfIUnitDefinitionDto get_units_from_data_type(scope, code, units=units, filter=filter)

Get units from data type

Get the definitions of the specified units associated bound to a specific data type

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
api_instance = lusid.DataTypesApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the data type
code = 'code_example' # str | The code of the data type
units = ['units_example'] # list[str] | One or more unit identifiers for which the definition is being requested (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)

try:
    # Get units from data type
    api_response = api_instance.get_units_from_data_type(scope, code, units=units, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->get_units_from_data_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | 
 **code** | **str**| The code of the data type | 
 **units** | [**list[str]**](str.md)| One or more unit identifiers for which the definition is being requested | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 

### Return type

[**ResourceListOfIUnitDefinitionDto**](ResourceListOfIUnitDefinitionDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_types**
> ResourceListOfDataType list_data_types(scope, include_system=include_system, sort_by=sort_by, start=start, limit=limit, filter=filter)

List data types

List all data types in a specified scope

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
api_instance = lusid.DataTypesApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The requested scope of the data types
include_system = True # bool | Whether to additionally include those data types in the \"system\" scope (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)

try:
    # List data types
    api_response = api_instance.list_data_types(scope, include_system=include_system, sort_by=sort_by, start=start, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->list_data_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The requested scope of the data types | 
 **include_system** | **bool**| Whether to additionally include those data types in the \&quot;system\&quot; scope | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 

### Return type

[**ResourceListOfDataType**](ResourceListOfDataType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_type**
> DataType update_data_type(scope, code, request=request)

Update data type definition

Update the definition of the specified existing data type    Not all elements within a data type definition are modifiable due to the potential implications for data  already stored against the types

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
api_instance = lusid.DataTypesApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the data type
code = 'code_example' # str | The code of the data type
request = lusid.UpdateDataTypeRequest() # UpdateDataTypeRequest | The updated definition of the data type (optional)

try:
    # Update data type definition
    api_response = api_instance.update_data_type(scope, code, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->update_data_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | 
 **code** | **str**| The code of the data type | 
 **request** | [**UpdateDataTypeRequest**](UpdateDataTypeRequest.md)| The updated definition of the data type | [optional] 

### Return type

[**DataType**](DataType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

