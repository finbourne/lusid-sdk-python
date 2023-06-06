# lusid.RelationsApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation**](RelationsApi.md#create_relation) | **POST** /api/relations/{scope}/{code} | [EXPERIMENTAL] CreateRelation: Create Relation
[**delete_relation**](RelationsApi.md#delete_relation) | **POST** /api/relations/{scope}/{code}/$delete | [EXPERIMENTAL] DeleteRelation: Delete a relation


# **create_relation**
> CompleteRelation create_relation(scope, code, create_relation_request, effective_at=effective_at)

[EXPERIMENTAL] CreateRelation: Create Relation

Create a relation between two entity objects by their identifiers

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
    api_instance = lusid.RelationsApi(api_client)
    scope = 'scope_example' # str | The scope of the relation definition
    code = 'code_example' # str | The code of the relation definition
    create_relation_request = {"sourceEntityId":{"IdTypeScope":"HrSystem1","IdTypeCode":"InternalId","Code":"XY10001111"},"targetEntityId":{"IdTypeScope":"HrSystem1","IdTypeCode":"InternalId","Code":"XY10001111"}} # CreateRelationRequest | The details of the relation to create.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # [EXPERIMENTAL] CreateRelation: Create Relation
        api_response = await api_instance.create_relation(scope, code, create_relation_request, effective_at=effective_at)
        print("The response of RelationsApi->create_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->create_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relation definition | 
 **code** | **str**| The code of the relation definition | 
 **create_relation_request** | [**CreateRelationRequest**](CreateRelationRequest.md)| The details of the relation to create. | 
 **effective_at** | **str**| The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**CompleteRelation**](CompleteRelation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created relation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_relation**
> DeletedEntityResponse delete_relation(scope, code, delete_relation_request, effective_at=effective_at)

[EXPERIMENTAL] DeleteRelation: Delete a relation

Delete a relation between two entity objects represented by their identifiers

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
    api_instance = lusid.RelationsApi(api_client)
    scope = 'scope_example' # str | The scope of the relation definition
    code = 'code_example' # str | The code of the relation definition
    delete_relation_request = {"sourceEntityId":{"EntityType":"PortfolioGroup","Scope":"UkPortfolio","Code":"PortfolioId-148176"},"targetEntityId":{"EntityType":"Person","IdTypeScope":"HrSystem1","IdTypeCode":"InternalId","Code":"XY10001111"}} # DeleteRelationRequest | The details of the relation to delete.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # [EXPERIMENTAL] DeleteRelation: Delete a relation
        api_response = await api_instance.delete_relation(scope, code, delete_relation_request, effective_at=effective_at)
        print("The response of RelationsApi->delete_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->delete_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relation definition | 
 **code** | **str**| The code of the relation definition | 
 **delete_relation_request** | [**DeleteRelationRequest**](DeleteRelationRequest.md)| The details of the relation to delete. | 
 **effective_at** | **str**| The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the relation is deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

