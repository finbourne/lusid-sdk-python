# lusid.RelationDefinitionsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:37477*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation_definition**](RelationDefinitionsApi.md#create_relation_definition) | **POST** /api/relationdefinitions | [DEPRECATED] Create a relation definition
[**get_relation_definition**](RelationDefinitionsApi.md#get_relation_definition) | **GET** /api/relationdefinitions/{scope}/{code} | [DEPRECATED] Get relation definition


# **create_relation_definition**
> RelationDefinition create_relation_definition(create_relation_definition_request)

[DEPRECATED] Create a relation definition

Define a new relation.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:37477
configuration.host = "http://local-unit-test-server.lusid.com:37477"
# Create an instance of the API class
api_instance = lusid.RelationDefinitionsApi(lusid.ApiClient(configuration))
create_relation_definition_request = {"scope":"PortfolioManagementTeam","code":"Traders","sourceEntityDomain":"Portfolio","targetEntityDomain":"Person","displayName":"Authorised traders to trade for specific portfolio ","outwardDescription":"can be traded by","inwardDescription":"can trade with portfolio","lifeTime":"TimeVariant","constraintStyle":"Collection"} # CreateRelationDefinitionRequest | The definition of the new relation.

try:
    # [DEPRECATED] Create a relation definition
    api_response = api_instance.create_relation_definition(create_relation_definition_request)
    pprint(api_response)
except ApiException as e:
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

# **get_relation_definition**
> RelationDefinition get_relation_definition(scope, code, as_at=as_at)

[DEPRECATED] Get relation definition

Retrieve the definition of a specified relation.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:37477
configuration.host = "http://local-unit-test-server.lusid.com:37477"
# Create an instance of the API class
api_instance = lusid.RelationDefinitionsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the specified relation.
code = 'code_example' # str | The code of the specified relation. Together with the domain and scope this uniquely              identifies the relation.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the relation definition. Defaults to return              the latest version of the definition if not specified. (optional)

try:
    # [DEPRECATED] Get relation definition
    api_response = api_instance.get_relation_definition(scope, code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
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

