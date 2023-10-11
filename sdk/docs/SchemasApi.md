# lusid.SchemasApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_schema**](SchemasApi.md#get_entity_schema) | **GET** /api/schemas/entities/{entity} | [EARLY ACCESS] GetEntitySchema: Get schema
[**get_property_schema**](SchemasApi.md#get_property_schema) | **GET** /api/schemas/properties | [EARLY ACCESS] GetPropertySchema: Get property schema
[**get_value_types**](SchemasApi.md#get_value_types) | **GET** /api/schemas/types | [EARLY ACCESS] GetValueTypes: Get value types
[**list_entities**](SchemasApi.md#list_entities) | **GET** /api/schemas/entities | [EARLY ACCESS] ListEntities: List entities


# **get_entity_schema**
> Schema get_entity_schema(entity)

[EARLY ACCESS] GetEntitySchema: Get schema

Gets the schema and meta-data for a given entity

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
    api_instance = lusid.SchemasApi(api_client)
    entity = 'entity_example' # str | The name of a valid entity

    try:
        # [EARLY ACCESS] GetEntitySchema: Get schema
        api_response = api_instance.get_entity_schema(entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchemasApi->get_entity_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| The name of a valid entity | 

### Return type

[**Schema**](Schema.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_schema**
> PropertySchema get_property_schema(property_keys=property_keys, as_at=as_at)

[EARLY ACCESS] GetPropertySchema: Get property schema

Get the schemas for the provided list of property keys.

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
    api_instance = lusid.SchemasApi(api_client)
    property_keys = ['property_keys_example'] # list[str] | One or more property keys for which the schema is requested (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)

    try:
        # [EARLY ACCESS] GetPropertySchema: Get property schema
        api_response = api_instance.get_property_schema(property_keys=property_keys, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchemasApi->get_property_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_keys** | [**list[str]**](str.md)| One or more property keys for which the schema is requested | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 

### Return type

[**PropertySchema**](PropertySchema.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_value_types**
> ResourceListOfValueType get_value_types(sort_by=sort_by, start=start, limit=limit)

[EARLY ACCESS] GetValueTypes: Get value types

Gets the available value types for which a schema is available.

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
    api_instance = lusid.SchemasApi(api_client)
    sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)

    try:
        # [EARLY ACCESS] GetValueTypes: Get value types
        api_response = api_instance.get_value_types(sort_by=sort_by, start=start, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchemasApi->get_value_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfValueType**](ResourceListOfValueType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entities**
> ResourceListOfString list_entities()

[EARLY ACCESS] ListEntities: List entities

List all available entities for which schema information is available.

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
    api_instance = lusid.SchemasApi(api_client)
    
    try:
        # [EARLY ACCESS] ListEntities: List entities
        api_response = api_instance.list_entities()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchemasApi->list_entities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfString**](ResourceListOfString.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

