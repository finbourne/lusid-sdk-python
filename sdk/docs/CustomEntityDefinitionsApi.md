# lusid.CustomEntityDefinitionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_entity_definition**](CustomEntityDefinitionsApi.md#create_custom_entity_definition) | **POST** /api/customentities/entitytypes | [EARLY ACCESS] CreateCustomEntityDefinition: Define a new Custom Entity type.
[**get_custom_entity_definition**](CustomEntityDefinitionsApi.md#get_custom_entity_definition) | **GET** /api/customentities/entitytypes/{entityType} | [EARLY ACCESS] GetCustomEntityDefinition: Get a Custom Entity type definition.
[**get_definition**](CustomEntityDefinitionsApi.md#get_definition) | **GET** /api/customentities/entitytypes/{entityType}/$deprecated | [DEPRECATED] GetDefinition: Get a Custom Entity type definition.
[**list_custom_entity_definitions**](CustomEntityDefinitionsApi.md#list_custom_entity_definitions) | **GET** /api/customentities/entitytypes | [EARLY ACCESS] ListCustomEntityDefinitions: List the Custom Entity type definitions
[**update_custom_entity_definition**](CustomEntityDefinitionsApi.md#update_custom_entity_definition) | **PUT** /api/customentities/entitytypes/{entityType} | [EARLY ACCESS] UpdateCustomEntityDefinition: Modify an existing Custom Entity type.


# **create_custom_entity_definition**
> CustomEntityDefinition create_custom_entity_definition(custom_entity_definition_request)

[EARLY ACCESS] CreateCustomEntityDefinition: Define a new Custom Entity type.

The API will return a Bad Request if the Custom Entity type already exists.

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
    api_instance = lusid.CustomEntityDefinitionsApi(api_client)
    custom_entity_definition_request = {"entityTypeName":"SupportTicket","displayName":"Support Ticket","description":"Support Ticket","fieldSchema":[{"name":"clientId","lifetime":"Perpetual","type":"String","required":true},{"name":"issueDescription","lifetime":"TimeVariant","type":"String","required":true},{"name":"internalNotes","lifetime":"TimeVariant","type":"String","required":false},{"name":"isResolved","lifetime":"TimeVariant","type":"Boolean","required":false}]} # CustomEntityDefinitionRequest | The payload containing the description of the Custom Entity type.

    try:
        # [EARLY ACCESS] CreateCustomEntityDefinition: Define a new Custom Entity type.
        api_response = api_instance.create_custom_entity_definition(custom_entity_definition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomEntityDefinitionsApi->create_custom_entity_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_entity_definition_request** | [**CustomEntityDefinitionRequest**](CustomEntityDefinitionRequest.md)| The payload containing the description of the Custom Entity type. | 

### Return type

[**CustomEntityDefinition**](CustomEntityDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created Custom Entity type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_entity_definition**
> CustomEntityDefinition get_custom_entity_definition(entity_type, as_at=as_at)

[EARLY ACCESS] GetCustomEntityDefinition: Get a Custom Entity type definition.

Retrieve a CustomEntityDefinition by a specific entityType at a point in AsAt time

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
    api_instance = lusid.CustomEntityDefinitionsApi(api_client)
    entity_type = 'entity_type_example' # str | The identifier for the Custom Entity type, derived from the \"entityTypeName\" provided on creation.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the definition. (optional)

    try:
        # [EARLY ACCESS] GetCustomEntityDefinition: Get a Custom Entity type definition.
        api_response = api_instance.get_custom_entity_definition(entity_type, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomEntityDefinitionsApi->get_custom_entity_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the Custom Entity type, derived from the \&quot;entityTypeName\&quot; provided on creation. | 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the definition. | [optional] 

### Return type

[**CustomEntityDefinition**](CustomEntityDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Custom Entity definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_definition**
> CustomEntityDefinition get_definition(entity_type, as_at=as_at)

[DEPRECATED] GetDefinition: Get a Custom Entity type definition.

Retrieve a CustomEntityDefinition by a specific entityType at a point in AsAt time

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
    api_instance = lusid.CustomEntityDefinitionsApi(api_client)
    entity_type = 'entity_type_example' # str | The identifier for the Custom Entity type, derived from the \"entityTypeName\" provided on creation.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the definition. (optional)

    try:
        # [DEPRECATED] GetDefinition: Get a Custom Entity type definition.
        api_response = api_instance.get_definition(entity_type, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomEntityDefinitionsApi->get_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the Custom Entity type, derived from the \&quot;entityTypeName\&quot; provided on creation. | 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the definition. | [optional] 

### Return type

[**CustomEntityDefinition**](CustomEntityDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Custom Entity definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_entity_definitions**
> PagedResourceListOfCustomEntityDefinition list_custom_entity_definitions(as_at=as_at, limit=limit, filter=filter, page=page)

[EARLY ACCESS] ListCustomEntityDefinitions: List the Custom Entity type definitions

List all Custom Entity type definitions matching particular criteria.

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
    api_instance = lusid.CustomEntityDefinitionsApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
page = 'page_example' # str | The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, limit              and asAt fields must not have changed since the original request. (optional)

    try:
        # [EARLY ACCESS] ListCustomEntityDefinitions: List the Custom Entity type definitions
        api_response = api_instance.list_custom_entity_definitions(as_at=as_at, limit=limit, filter=filter, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomEntityDefinitionsApi->list_custom_entity_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **page** | **str**| The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, limit              and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfCustomEntityDefinition**](PagedResourceListOfCustomEntityDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Custom Entity type definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_entity_definition**
> CustomEntityDefinition update_custom_entity_definition(entity_type, update_custom_entity_definition_request)

[EARLY ACCESS] UpdateCustomEntityDefinition: Modify an existing Custom Entity type.

The API will return a Bad Request if the Custom Entity type does not exist.

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
    api_instance = lusid.CustomEntityDefinitionsApi(api_client)
    entity_type = 'entity_type_example' # str | The identifier for the Custom Entity type, derived from the \"entityTypeName\" provided on creation.
update_custom_entity_definition_request = {"displayName":"Support Ticket","description":"Support Ticket","fieldSchema":[{"name":"clientId","lifetime":"Perpetual","type":"String","required":true},{"name":"issueDescription","lifetime":"TimeVariant","type":"String","required":true},{"name":"internalNotes","lifetime":"TimeVariant","type":"String","required":false},{"name":"isResolved","lifetime":"TimeVariant","type":"Boolean","required":false}]} # UpdateCustomEntityDefinitionRequest | The payload containing the description of the Custom Entity type.

    try:
        # [EARLY ACCESS] UpdateCustomEntityDefinition: Modify an existing Custom Entity type.
        api_response = api_instance.update_custom_entity_definition(entity_type, update_custom_entity_definition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomEntityDefinitionsApi->update_custom_entity_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the Custom Entity type, derived from the \&quot;entityTypeName\&quot; provided on creation. | 
 **update_custom_entity_definition_request** | [**UpdateCustomEntityDefinitionRequest**](UpdateCustomEntityDefinitionRequest.md)| The payload containing the description of the Custom Entity type. | 

### Return type

[**CustomEntityDefinition**](CustomEntityDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Custom Entity type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

