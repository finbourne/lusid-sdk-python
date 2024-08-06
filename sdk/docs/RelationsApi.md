# lusid.RelationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation**](RelationsApi.md#create_relation) | **POST** /api/relations/{scope}/{code} | [EXPERIMENTAL] CreateRelation: Create Relation
[**delete_relation**](RelationsApi.md#delete_relation) | **POST** /api/relations/{scope}/{code}/$delete | [EXPERIMENTAL] DeleteRelation: Delete a relation


# **create_relation**
> CompleteRelation create_relation(scope, code, create_relation_request, effective_at=effective_at)

[EXPERIMENTAL] CreateRelation: Create Relation

Create a relation between two entity objects by their identifiers

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationsApi
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
        api_instance = api_client_factory.build(RelationsApi)
        scope = 'scope_example' # str | The scope of the relation definition
        code = 'code_example' # str | The code of the relation definition

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_relation_request = CreateRelationRequest()
        # create_relation_request = CreateRelationRequest.from_json("")
        create_relation_request = CreateRelationRequest.from_dict({"sourceEntityId":{"IdTypeScope":"HrSystem1","IdTypeCode":"InternalId","Code":"XY10001111"},"targetEntityId":{"IdTypeScope":"HrSystem1","IdTypeCode":"InternalId","Code":"XY10001111"}}) # CreateRelationRequest | The details of the relation to create.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified. (optional)

        try:
            # [EXPERIMENTAL] CreateRelation: Create Relation
            api_response = await api_instance.create_relation(scope, code, create_relation_request, effective_at=effective_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationsApi->create_relation: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_relation**
> DeletedEntityResponse delete_relation(scope, code, delete_relation_request, effective_at=effective_at)

[EXPERIMENTAL] DeleteRelation: Delete a relation

Delete a relation between two entity objects represented by their identifiers

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationsApi
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
        api_instance = api_client_factory.build(RelationsApi)
        scope = 'scope_example' # str | The scope of the relation definition
        code = 'code_example' # str | The code of the relation definition

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # delete_relation_request = DeleteRelationRequest()
        # delete_relation_request = DeleteRelationRequest.from_json("")
        delete_relation_request = DeleteRelationRequest.from_dict({"sourceEntityId":{"EntityType":"PortfolioGroup","Scope":"UkPortfolio","Code":"PortfolioId-148176"},"targetEntityId":{"EntityType":"Person","IdTypeScope":"HrSystem1","IdTypeCode":"InternalId","Code":"XY10001111"}}) # DeleteRelationRequest | The details of the relation to delete.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified. (optional)

        try:
            # [EXPERIMENTAL] DeleteRelation: Delete a relation
            api_response = await api_instance.delete_relation(scope, code, delete_relation_request, effective_at=effective_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationsApi->delete_relation: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the relation is deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

