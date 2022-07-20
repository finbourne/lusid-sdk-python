# lusid.RelationshipsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship**](RelationshipsApi.md#create_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships | [EARLY ACCESS] CreateRelationship: Create Relationship
[**delete_relationship**](RelationshipsApi.md#delete_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships/$delete | [EARLY ACCESS] DeleteRelationship: Delete Relationship


# **create_relationship**
> CompleteRelationship create_relationship(scope, code, create_relationship_request)

[EARLY ACCESS] CreateRelationship: Create Relationship

Create a relationship between two entity objects by their identifiers

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
    api_instance = lusid.RelationshipsApi(api_client)
    scope = 'scope_example' # str | The scope of the relationship
code = 'code_example' # str | The code of the relationship
create_relationship_request = {"sourceEntityId":{"scope":"UkPortfolio","code":"PortfolioId-148176"},"targetEntityId":{"idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"}} # CreateRelationshipRequest | The details of the relationship to create.

    try:
        # [EARLY ACCESS] CreateRelationship: Create Relationship
        api_response = api_instance.create_relationship(scope, code, create_relationship_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationshipsApi->create_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship | 
 **code** | **str**| The code of the relationship | 
 **create_relationship_request** | [**CreateRelationshipRequest**](CreateRelationshipRequest.md)| The details of the relationship to create. | 

### Return type

[**CompleteRelationship**](CompleteRelationship.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relationship. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_relationship**
> DeletedEntityResponse delete_relationship(scope, code, delete_relationship_request)

[EARLY ACCESS] DeleteRelationship: Delete Relationship

Delete a relationship between two entity objects represented by their identifiers

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
    api_instance = lusid.RelationshipsApi(api_client)
    scope = 'scope_example' # str | The scope of the relationship
code = 'code_example' # str | The code of the relationship
delete_relationship_request = {"sourceEntityId":{"scope":"UkPortfolio","code":"PortfolioId-148176"},"targetEntityId":{"idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"},"effectiveFrom":"2019-01-10T00:00:00.0000000+00:00"} # DeleteRelationshipRequest | The details of the relationship to delete.

    try:
        # [EARLY ACCESS] DeleteRelationship: Delete Relationship
        api_response = api_instance.delete_relationship(scope, code, delete_relationship_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationshipsApi->delete_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship | 
 **code** | **str**| The code of the relationship | 
 **delete_relationship_request** | [**DeleteRelationshipRequest**](DeleteRelationshipRequest.md)| The details of the relationship to delete. | 

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
**200** | The datetime that the relationship is deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

