# lusid.RelationsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:64378*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation**](RelationsApi.md#create_relation) | **POST** /api/relations/{scope}/{code} | [DEPRECATED] Create Relation
[**delete_relation**](RelationsApi.md#delete_relation) | **POST** /api/relations/{scope}/{code}/$delete | [DEPRECATED] Delete a relation


# **create_relation**
> CompleteRelation create_relation(scope, code, create_relation_request, effective_at=effective_at)

[DEPRECATED] Create Relation

Create a relation between two entity objects by their identifiers

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:64378
configuration.host = "http://local-unit-test-server.lusid.com:64378"
# Create an instance of the API class
api_instance = lusid.RelationsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the relation definition
code = 'code_example' # str | The code of the relation definition
create_relation_request = {"sourceEntityId":{"idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"},"targetEntityId":{"idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"}} # CreateRelationRequest | The details of the relation to create.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified. (optional)

try:
    # [DEPRECATED] Create Relation
    api_response = api_instance.create_relation(scope, code, create_relation_request, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
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

[DEPRECATED] Delete a relation

Delete a relation between two entity objects represented by their identifiers

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:64378
configuration.host = "http://local-unit-test-server.lusid.com:64378"
# Create an instance of the API class
api_instance = lusid.RelationsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the relation definition
code = 'code_example' # str | The code of the relation definition
delete_relation_request = {"sourceEntityId":{"entityType":"PortfolioGroup","scope":"UkPortfolio","code":"PortfolioId-148176"},"targetEntityId":{"entityType":"Person","idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"}} # DeleteRelationRequest | The details of the relation to delete.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified. (optional)

try:
    # [DEPRECATED] Delete a relation
    api_response = api_instance.delete_relation(scope, code, delete_relation_request, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
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

