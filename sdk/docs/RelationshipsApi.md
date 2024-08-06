# lusid.RelationshipsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship**](RelationshipsApi.md#create_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships | CreateRelationship: Create Relationship
[**delete_relationship**](RelationshipsApi.md#delete_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships/$delete | [EARLY ACCESS] DeleteRelationship: Delete Relationship


# **create_relationship**
> CompleteRelationship create_relationship(scope, code, create_relationship_request)

CreateRelationship: Create Relationship

Create a relationship between two entity objects by their identifiers

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationshipsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "lusidUrl":"https://<your-domain>.lusid.com/api",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RelationshipsApi)
        scope = 'scope_example' # str | The scope of the relationship
        code = 'code_example' # str | The code of the relationship

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_relationship_request = CreateRelationshipRequest()
        # create_relationship_request = CreateRelationshipRequest.from_json("")
        create_relationship_request = CreateRelationshipRequest.from_dict({"sourceEntityId":{"scope":"UkPortfolio","code":"PortfolioId-148176"},"targetEntityId":{"idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"},"effectiveFrom":"2019-01-01T12:00:00.0000000+00:00","effectiveUntil":"2022-01-01T12:00:00.0000000+00:00"}) # CreateRelationshipRequest | The details of the relationship to create.

        try:
            # CreateRelationship: Create Relationship
            api_response = await api_instance.create_relationship(scope, code, create_relationship_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationshipsApi->create_relationship: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship | 
 **code** | **str**| The code of the relationship | 
 **create_relationship_request** | [**CreateRelationshipRequest**](CreateRelationshipRequest.md)| The details of the relationship to create. | 

### Return type

[**CompleteRelationship**](CompleteRelationship.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relationship. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_relationship**
> DeletedEntityResponse delete_relationship(scope, code, delete_relationship_request)

[EARLY ACCESS] DeleteRelationship: Delete Relationship

Delete a relationship between two entity objects represented by their identifiers

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationshipsApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "lusidUrl":"https://<your-domain>.lusid.com/api",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RelationshipsApi)
        scope = 'scope_example' # str | The scope of the relationship
        code = 'code_example' # str | The code of the relationship

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # delete_relationship_request = DeleteRelationshipRequest()
        # delete_relationship_request = DeleteRelationshipRequest.from_json("")
        delete_relationship_request = DeleteRelationshipRequest.from_dict({"sourceEntityId":{"scope":"UkPortfolio","code":"PortfolioId-148176"},"targetEntityId":{"idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"},"effectiveFrom":"2019-01-10T00:00:00.0000000+00:00"}) # DeleteRelationshipRequest | The details of the relationship to delete.

        try:
            # [EARLY ACCESS] DeleteRelationship: Delete Relationship
            api_response = await api_instance.delete_relationship(scope, code, delete_relationship_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationshipsApi->delete_relationship: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship | 
 **code** | **str**| The code of the relationship | 
 **delete_relationship_request** | [**DeleteRelationshipRequest**](DeleteRelationshipRequest.md)| The details of the relationship to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the relationship is deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

