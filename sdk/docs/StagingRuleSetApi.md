# lusid.StagingRuleSetApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_staging_rule_set**](StagingRuleSetApi.md#create_staging_rule_set) | **POST** /api/stagingrulesets/{entityType} | [EXPERIMENTAL] CreateStagingRuleSet: Create a StagingRuleSet
[**delete_staging_rule_set**](StagingRuleSetApi.md#delete_staging_rule_set) | **DELETE** /api/stagingrulesets/{entityType} | [EXPERIMENTAL] DeleteStagingRuleSet: Delete a StagingRuleSet
[**get_staging_rule_set**](StagingRuleSetApi.md#get_staging_rule_set) | **GET** /api/stagingrulesets/{entityType} | [EXPERIMENTAL] GetStagingRuleSet: Get a StagingRuleSet
[**list_staging_rule_sets**](StagingRuleSetApi.md#list_staging_rule_sets) | **GET** /api/stagingrulesets | [EXPERIMENTAL] ListStagingRuleSets: List StagingRuleSets
[**update_staging_rule_set**](StagingRuleSetApi.md#update_staging_rule_set) | **PUT** /api/stagingrulesets/{entityType} | [EXPERIMENTAL] UpdateStagingRuleSet: Update a StagingRuleSet


# **create_staging_rule_set**
> StagingRuleSet create_staging_rule_set(entity_type, create_staging_rule_set_request)

[EXPERIMENTAL] CreateStagingRuleSet: Create a StagingRuleSet

Create a new staging rule set.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    StagingRuleSetApi
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
        api_instance = api_client_factory.build(StagingRuleSetApi)
        entity_type = 'entity_type_example' # str | The entity type for which to create the staging rule set.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_staging_rule_set_request = CreateStagingRuleSetRequest()
        # create_staging_rule_set_request = CreateStagingRuleSetRequest.from_json("")
        create_staging_rule_set_request = CreateStagingRuleSetRequest.from_dict({"displayName":"Test Entity Staging Rules","description":"The rules that determine whether a modification is staged","rules":[{"ruleId":"1","description":"Any user updating this entity must get approval from 2 admins","status":"Active","matchCriteria":{"actionIn":["Create","Delete"],"requestingUser":"id.code eq 'not admin'","entityAttributes":"version.asAtVersionNumber gt 10","changedAttributeNameIn":["Properties[myEntityType/myScope/protected-property]"]},"approvalCriteria":{"requiredApprovals":2,"decidingUser":"id.code eq 'admin'","stagingUserCanDecide":true}},{"ruleId":"2","description":"Any user updating this entity must get approval from one admin","status":"Inactive","matchCriteria":{"requestingUser":"id.code eq 'not admin'","entityAttributes":"version.asAtVersionNumber gt 10"},"approvalCriteria":{"requiredApprovals":1,"decidingUser":"id.code eq 'admin'","stagingUserCanDecide":false}}]}) # CreateStagingRuleSetRequest | Request to create a staging rule set.

        try:
            # [EXPERIMENTAL] CreateStagingRuleSet: Create a StagingRuleSet
            api_response = await api_instance.create_staging_rule_set(entity_type, create_staging_rule_set_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StagingRuleSetApi->create_staging_rule_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type for which to create the staging rule set. | 
 **create_staging_rule_set_request** | [**CreateStagingRuleSetRequest**](CreateStagingRuleSetRequest.md)| Request to create a staging rule set. | 

### Return type

[**StagingRuleSet**](StagingRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created staging rule set |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_staging_rule_set**
> DeletedEntityResponse delete_staging_rule_set(entity_type)

[EXPERIMENTAL] DeleteStagingRuleSet: Delete a StagingRuleSet

Delete a staging rule set of a specific entity type. Deletion will be valid from the staging rule set's creation datetime.  This means that the staging rule set will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    StagingRuleSetApi
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
        api_instance = api_client_factory.build(StagingRuleSetApi)
        entity_type = 'entity_type_example' # str | The entity type for which to delete the staging rule set.

        try:
            # [EXPERIMENTAL] DeleteStagingRuleSet: Delete a StagingRuleSet
            api_response = await api_instance.delete_staging_rule_set(entity_type)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StagingRuleSetApi->delete_staging_rule_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type for which to delete the staging rule set. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting staging rule set |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_staging_rule_set**
> StagingRuleSet get_staging_rule_set(entity_type, as_at=as_at)

[EXPERIMENTAL] GetStagingRuleSet: Get a StagingRuleSet

Get the staging rule set for the given entity type at the specific asAt time.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    StagingRuleSetApi
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
        api_instance = api_client_factory.build(StagingRuleSetApi)
        entity_type = 'entity_type_example' # str | The entity type for which to retrieve the staging rule set.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the staging rule set. Defaults to return the latest              version of the staging rule set if not specified. (optional)

        try:
            # [EXPERIMENTAL] GetStagingRuleSet: Get a StagingRuleSet
            api_response = await api_instance.get_staging_rule_set(entity_type, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StagingRuleSetApi->get_staging_rule_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type for which to retrieve the staging rule set. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the staging rule set. Defaults to return the latest              version of the staging rule set if not specified. | [optional] 

### Return type

[**StagingRuleSet**](StagingRuleSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested staging rule set |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_staging_rule_sets**
> PagedResourceListOfStagingRuleSet list_staging_rule_sets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListStagingRuleSets: List StagingRuleSets

List all the staging rule sets matching particular criteria.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    StagingRuleSetApi
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
        api_instance = api_client_factory.build(StagingRuleSetApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the staging rule sets. Defaults to return the latest              version of the staging rule sets if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing staging rule sets from a previous call to list              staging rule sets. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # [EXPERIMENTAL] ListStagingRuleSets: List StagingRuleSets
            api_response = await api_instance.list_staging_rule_sets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StagingRuleSetApi->list_staging_rule_sets: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the staging rule sets. Defaults to return the latest              version of the staging rule sets if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing staging rule sets from a previous call to list              staging rule sets. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfStagingRuleSet**](PagedResourceListOfStagingRuleSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of staging rule sets |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_staging_rule_set**
> StagingRuleSet update_staging_rule_set(entity_type, update_staging_rule_set_request)

[EXPERIMENTAL] UpdateStagingRuleSet: Update a StagingRuleSet

Update an existing staging rule set.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    StagingRuleSetApi
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
        api_instance = api_client_factory.build(StagingRuleSetApi)
        entity_type = 'entity_type_example' # str | The entity type for which to update the staging rule set.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_staging_rule_set_request = UpdateStagingRuleSetRequest()
        # update_staging_rule_set_request = UpdateStagingRuleSetRequest.from_json("")
        update_staging_rule_set_request = UpdateStagingRuleSetRequest.from_dict({"displayName":"Test Entity Staging Rules","description":"The rules that determine whether a modification is staged","rules":[{"ruleId":"1","description":"Any user updating this entity must get approval from 2 admins","status":"Active","matchCriteria":{"actionIn":["Create","Delete"],"requestingUser":"id.code eq 'not admin'","entityAttributes":"version.asAtVersionNumber gt 10","changedAttributeNameIn":["Properties[myEntityType/myScope/protected-property]"]},"approvalCriteria":{"requiredApprovals":2,"decidingUser":"id.code eq 'admin'","stagingUserCanDecide":true}},{"ruleId":"2","description":"Any user updating this entity must get approval from one admin","status":"Inactive","matchCriteria":{"requestingUser":"id.code eq 'not admin'","entityAttributes":"version.asAtVersionNumber gt 10"},"approvalCriteria":{"requiredApprovals":1,"decidingUser":"id.code eq 'admin'","stagingUserCanDecide":false}}]}) # UpdateStagingRuleSetRequest | Request to update a staging rule set.

        try:
            # [EXPERIMENTAL] UpdateStagingRuleSet: Update a StagingRuleSet
            api_response = await api_instance.update_staging_rule_set(entity_type, update_staging_rule_set_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StagingRuleSetApi->update_staging_rule_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type for which to update the staging rule set. | 
 **update_staging_rule_set_request** | [**UpdateStagingRuleSetRequest**](UpdateStagingRuleSetRequest.md)| Request to update a staging rule set. | 

### Return type

[**StagingRuleSet**](StagingRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated staging rule set |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

