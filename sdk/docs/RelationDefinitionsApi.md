# lusid.RelationDefinitionsApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation_definition**](RelationDefinitionsApi.md#create_relation_definition) | **POST** /api/relationdefinitions | [EXPERIMENTAL] CreateRelationDefinition: Create a relation definition
[**delete_relation_definition**](RelationDefinitionsApi.md#delete_relation_definition) | **DELETE** /api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteRelationDefinition: Delete relation definition
[**get_relation_definition**](RelationDefinitionsApi.md#get_relation_definition) | **GET** /api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationDefinition: Get relation definition


# **create_relation_definition**
> RelationDefinition create_relation_definition(create_relation_definition_request)

[EXPERIMENTAL] CreateRelationDefinition: Create a relation definition

Define a new relation.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.RelationDefinitionsApi(api_client)
    create_relation_definition_request = {"scope":"PortfolioManagementTeam","code":"Traders","sourceEntityDomain":"Portfolio","targetEntityDomain":"Person","displayName":"Authorised traders to trade for specific portfolio ","outwardDescription":"can be traded by","inwardDescription":"can trade with portfolio","lifeTime":"TimeVariant","constraintStyle":"Collection"} # CreateRelationDefinitionRequest | The definition of the new relation.

    try:
        # [EXPERIMENTAL] CreateRelationDefinition: Create a relation definition
        api_response = await api_instance.create_relation_definition(create_relation_definition_request)
        print("The response of RelationDefinitionsApi->create_relation_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationDefinitionsApi->create_relation_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_relation_definition_request** | [**CreateRelationDefinitionRequest**](CreateRelationDefinitionRequest.md)| The definition of the new relation. | 

### Return type

[**RelationDefinition**](RelationDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relation definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_relation_definition**
> DeletedEntityResponse delete_relation_definition(scope, code)

[EXPERIMENTAL] DeleteRelationDefinition: Delete relation definition

Delete the definition of the specified relation.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.RelationDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope of the relation to be deleted.
    code = 'code_example' # str | The code of the relation to be deleted. Together with the domain and scope this uniquely              identifies the relation.

    try:
        # [EXPERIMENTAL] DeleteRelationDefinition: Delete relation definition
        api_response = await api_instance.delete_relation_definition(scope, code)
        print("The response of RelationDefinitionsApi->delete_relation_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationDefinitionsApi->delete_relation_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relation to be deleted. | 
 **code** | **str**| The code of the relation to be deleted. Together with the domain and scope this uniquely              identifies the relation. | 

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
**200** | The time that the relation definition was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation_definition**
> RelationDefinition get_relation_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetRelationDefinition: Get relation definition

Retrieve the definition of a specified relation.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.RelationDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope of the specified relation.
    code = 'code_example' # str | The code of the specified relation. Together with the domain and scope this uniquely              identifies the relation.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the relation definition. Defaults to return              the latest version of the definition if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetRelationDefinition: Get relation definition
        api_response = await api_instance.get_relation_definition(scope, code, as_at=as_at)
        print("The response of RelationDefinitionsApi->get_relation_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationDefinitionsApi->get_relation_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified relation. | 
 **code** | **str**| The code of the specified relation. Together with the domain and scope this uniquely              identifies the relation. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relation definition. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**RelationDefinition**](RelationDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested relation definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

