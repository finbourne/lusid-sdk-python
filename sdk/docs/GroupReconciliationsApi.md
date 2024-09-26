# lusid.GroupReconciliationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comparison_ruleset**](GroupReconciliationsApi.md#create_comparison_ruleset) | **POST** /api/reconciliations/comparisonrulesets | [EXPERIMENTAL] CreateComparisonRuleset: Create a Group Reconciliation Comparison Ruleset
[**create_group_reconciliation_definition**](GroupReconciliationsApi.md#create_group_reconciliation_definition) | **POST** /api/reconciliations/groupreconciliationdefinitions | [EXPERIMENTAL] CreateGroupReconciliationDefinition: Create Group Reconciliation Definition
[**delete_comparison_ruleset**](GroupReconciliationsApi.md#delete_comparison_ruleset) | **DELETE** /api/reconciliations/comparisonrulesets/{scope}/{code} | [EXPERIMENTAL] DeleteComparisonRuleset: Deletes a particular Group Reconciliation Comparison Ruleset
[**delete_group_reconciliation_definition**](GroupReconciliationsApi.md#delete_group_reconciliation_definition) | **DELETE** /api/reconciliations/groupreconciliationdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteGroupReconciliationDefinition: Delete Group Reconciliation Definition
[**get_comparison_ruleset**](GroupReconciliationsApi.md#get_comparison_ruleset) | **GET** /api/reconciliations/comparisonrulesets/{scope}/{code} | [EXPERIMENTAL] GetComparisonRuleset: Get a single Group Reconciliation Comparison Ruleset by scope and code
[**get_group_reconciliation_definition**](GroupReconciliationsApi.md#get_group_reconciliation_definition) | **GET** /api/reconciliations/groupreconciliationdefinitions/{scope}/{code} | [EXPERIMENTAL] GetGroupReconciliationDefinition: Get group reconciliation definition
[**list_comparison_rulesets**](GroupReconciliationsApi.md#list_comparison_rulesets) | **GET** /api/reconciliations/comparisonrulesets | [EXPERIMENTAL] ListComparisonRulesets: Get a set of Group Reconciliation Comparison Rulesets
[**list_group_reconciliation_definitions**](GroupReconciliationsApi.md#list_group_reconciliation_definitions) | **GET** /api/reconciliations/groupreconciliationdefinitions | [EXPERIMENTAL] ListGroupReconciliationDefinitions: List group reconciliation definitions
[**update_comparison_ruleset**](GroupReconciliationsApi.md#update_comparison_ruleset) | **PUT** /api/reconciliations/comparisonrulesets/{scope}/{code} | [EXPERIMENTAL] UpdateComparisonRuleset: Update Group Reconciliation Comparison Ruleset defined by scope and code
[**update_group_reconciliation_definition**](GroupReconciliationsApi.md#update_group_reconciliation_definition) | **PUT** /api/reconciliations/groupreconciliationdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateGroupReconciliationDefinition: Update group reconciliation definition


# **create_comparison_ruleset**
> GroupReconciliationComparisonRuleset create_comparison_ruleset(create_group_reconciliation_comparison_ruleset_request=create_group_reconciliation_comparison_ruleset_request)

[EXPERIMENTAL] CreateComparisonRuleset: Create a Group Reconciliation Comparison Ruleset

Creates a set of core and aggregate rules to be run for a group reconciliation

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_group_reconciliation_comparison_ruleset_request = CreateGroupReconciliationComparisonRulesetRequest()
        # create_group_reconciliation_comparison_ruleset_request = CreateGroupReconciliationComparisonRulesetRequest.from_json("")
        create_group_reconciliation_comparison_ruleset_request = CreateGroupReconciliationComparisonRulesetRequest.from_dict({"id":{"scope":"MySourceScope","code":"MySourcePortfolioCode"},"displayName":"Compare by instrument and strategy","reconciliationType":"Holding","coreAttributeRules":[{"left":{"key":"path to instrument property","operation":"Value"},"right":{"key":"path to LUID property","operation":"Value"},"allowableStringMappings":[{"leftValue":"Microsoft","rightValue":"MSFT","direction":"UniDirectional"}],"isComparisonCaseSensitive":false},{"left":{"key":"path to strategy property","operation":"Value"},"right":{"key":"path to investment strategy property","operation":"Value"},"allowableStringMappings":[{"leftValue":"HighRisk","rightValue":"HR","direction":"BiDirectional"}],"isComparisonCaseSensitive":true}],"aggregateAttributeRules":[{"left":{"key":"path to units property","operation":"Sum"},"right":{"key":"path to count property","operation":"Sum"},"tolerance":{"type":"Absolute","value":10}},{"left":{"key":"path to price property","operation":"Sum"},"right":{"key":"path to price property","operation":"Sum"},"tolerance":{"type":"Relative","value":2}}]}) # CreateGroupReconciliationComparisonRulesetRequest | The request containing the details of the ruleset (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_comparison_ruleset(create_group_reconciliation_comparison_ruleset_request=create_group_reconciliation_comparison_ruleset_request, opts=opts)

            # [EXPERIMENTAL] CreateComparisonRuleset: Create a Group Reconciliation Comparison Ruleset
            api_response = await api_instance.create_comparison_ruleset(create_group_reconciliation_comparison_ruleset_request=create_group_reconciliation_comparison_ruleset_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->create_comparison_ruleset: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_reconciliation_comparison_ruleset_request** | [**CreateGroupReconciliationComparisonRulesetRequest**](CreateGroupReconciliationComparisonRulesetRequest.md)| The request containing the details of the ruleset | [optional] 

### Return type

[**GroupReconciliationComparisonRuleset**](GroupReconciliationComparisonRuleset.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created comparison ruleset |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_group_reconciliation_definition**
> GroupReconciliationDefinition create_group_reconciliation_definition(create_group_reconciliation_definition_request=create_group_reconciliation_definition_request)

[EXPERIMENTAL] CreateGroupReconciliationDefinition: Create Group Reconciliation Definition

Creates a Group Reconciliation Definition

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_group_reconciliation_definition_request = CreateGroupReconciliationDefinitionRequest()
        # create_group_reconciliation_definition_request = CreateGroupReconciliationDefinitionRequest.from_json("")
        create_group_reconciliation_definition_request = CreateGroupReconciliationDefinitionRequest.from_dict({"id":{"scope":"MyScope","code":"MyCode"},"displayName":"My Group Reconciliation Definition","description":"The Group Reconciliation Definition description","portfolioEntityIds":{"left":[{"scope":"MyPortfolioScope","code":"MyPortfolioCode","portfolioEntityType":"SinglePortfolio"}],"right":[{"scope":"MyOtherPortfolioScope","code":"MyOtherPortfolioCode","portfolioEntityType":"SinglePortfolio"}]},"recipeIds":{"left":{"scope":"MyRecipeScope","code":"MyRecipeCode"},"right":{"scope":"MyOtherRecipeScope","code":"MyOtherRecipeCode"}},"currencies":{"left":"USD","right":"CHF"},"comparisonRulesetIds":{"valuationReconciliation":{"scope":"MyValuationComparisonRulesetScope","code":"MyValuationComparisonRulesetCode"}},"breakCodeSource":{"dataTypeId":{"scope":"MyBreakCodeSourceScope","code":"MyBreakCodeSourceCode"}}}) # CreateGroupReconciliationDefinitionRequest | The definition Group Reconciliation Definition details (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_group_reconciliation_definition(create_group_reconciliation_definition_request=create_group_reconciliation_definition_request, opts=opts)

            # [EXPERIMENTAL] CreateGroupReconciliationDefinition: Create Group Reconciliation Definition
            api_response = await api_instance.create_group_reconciliation_definition(create_group_reconciliation_definition_request=create_group_reconciliation_definition_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->create_group_reconciliation_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_reconciliation_definition_request** | [**CreateGroupReconciliationDefinitionRequest**](CreateGroupReconciliationDefinitionRequest.md)| The definition Group Reconciliation Definition details | [optional] 

### Return type

[**GroupReconciliationDefinition**](GroupReconciliationDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Group Reconciliation Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_comparison_ruleset**
> DeletedEntityResponse delete_comparison_ruleset(scope, code)

[EXPERIMENTAL] DeleteComparisonRuleset: Deletes a particular Group Reconciliation Comparison Ruleset

The deletion will take effect from the reconciliation comparison ruleset deletion datetime.  i.e. will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)
        scope = 'scope_example' # str | The scope of the specified comparison ruleset.
        code = 'code_example' # str | The code of the specified comparison ruleset. Together with the domain and scope this uniquely              identifies the reconciliation comparison ruleset.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_comparison_ruleset(scope, code, opts=opts)

            # [EXPERIMENTAL] DeleteComparisonRuleset: Deletes a particular Group Reconciliation Comparison Ruleset
            api_response = await api_instance.delete_comparison_ruleset(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->delete_comparison_ruleset: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified comparison ruleset. | 
 **code** | **str**| The code of the specified comparison ruleset. Together with the domain and scope this uniquely              identifies the reconciliation comparison ruleset. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_group_reconciliation_definition**
> DeletedEntityResponse delete_group_reconciliation_definition(scope, code)

[EXPERIMENTAL] DeleteGroupReconciliationDefinition: Delete Group Reconciliation Definition

Delete the group reconciliation definition.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)
        scope = 'scope_example' # str | The scope of the group reconciliation definition to delete.
        code = 'code_example' # str | The code of the group reconciliation definition to delete. Together with the scope this uniquely identifies the group reconciliation definition to delete.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_group_reconciliation_definition(scope, code, opts=opts)

            # [EXPERIMENTAL] DeleteGroupReconciliationDefinition: Delete Group Reconciliation Definition
            api_response = await api_instance.delete_group_reconciliation_definition(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->delete_group_reconciliation_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group reconciliation definition to delete. | 
 **code** | **str**| The code of the group reconciliation definition to delete. Together with the scope this uniquely identifies the group reconciliation definition to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the group reconciliation definition was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_comparison_ruleset**
> GroupReconciliationComparisonRuleset get_comparison_ruleset(scope, code, as_at=as_at)

[EXPERIMENTAL] GetComparisonRuleset: Get a single Group Reconciliation Comparison Ruleset by scope and code

Retrieves one Group Reconciliation Comparison Ruleset by scope and code

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)
        scope = 'scope_example' # str | The scope of the specified comparison ruleset.
        code = 'code_example' # str | The code of the specified comparison ruleset. Together with the domain and scope this uniquely              identifies the reconciliation comparison ruleset.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the comparison ruleset definition. Defaults to return              the latest version of the definition if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_comparison_ruleset(scope, code, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetComparisonRuleset: Get a single Group Reconciliation Comparison Ruleset by scope and code
            api_response = await api_instance.get_comparison_ruleset(scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->get_comparison_ruleset: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified comparison ruleset. | 
 **code** | **str**| The code of the specified comparison ruleset. Together with the domain and scope this uniquely              identifies the reconciliation comparison ruleset. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the comparison ruleset definition. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**GroupReconciliationComparisonRuleset**](GroupReconciliationComparisonRuleset.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested comparison ruleset |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_group_reconciliation_definition**
> GroupReconciliationDefinition get_group_reconciliation_definition(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetGroupReconciliationDefinition: Get group reconciliation definition

Retrieves a Group Reconciliation Definition by scope and code

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)
        scope = 'scope_example' # str | The scope of the group reconciliation definition to retrieve.
        code = 'code_example' # str | The code of the group reconciliation definition to retrieve. Together with the scope              this uniquely identifies the group reconciliation definition.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the group reconciliation definition. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the group reconciliation definition. Defaults to return the latest version of the portfolio group definition if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_group_reconciliation_definition(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetGroupReconciliationDefinition: Get group reconciliation definition
            api_response = await api_instance.get_group_reconciliation_definition(scope, code, effective_at=effective_at, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->get_group_reconciliation_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group reconciliation definition to retrieve. | 
 **code** | **str**| The code of the group reconciliation definition to retrieve. Together with the scope              this uniquely identifies the group reconciliation definition. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the group reconciliation definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the group reconciliation definition. Defaults to return the latest version of the portfolio group definition if not specified. | [optional] 

### Return type

[**GroupReconciliationDefinition**](GroupReconciliationDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested group reconciliation definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_comparison_rulesets**
> PagedResourceListOfGroupReconciliationComparisonRuleset list_comparison_rulesets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListComparisonRulesets: Get a set of Group Reconciliation Comparison Rulesets

Retrieves all Group Reconciliation Comparison Ruleset that fit the filter, in a specific order if sortBy is provided  Supports pagination

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the staging rule sets. Defaults to return the latest              version of the staging rule sets if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing comparison rulesets from a previous call to list              comparison rulesets. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many per page. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_comparison_rulesets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

            # [EXPERIMENTAL] ListComparisonRulesets: Get a set of Group Reconciliation Comparison Rulesets
            api_response = await api_instance.list_comparison_rulesets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->list_comparison_rulesets: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the staging rule sets. Defaults to return the latest              version of the staging rule sets if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing comparison rulesets from a previous call to list              comparison rulesets. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many per page. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfGroupReconciliationComparisonRuleset**](PagedResourceListOfGroupReconciliationComparisonRuleset.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested list of comparison rulesets |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_group_reconciliation_definitions**
> PagedResourceListOfGroupReconciliationDefinition list_group_reconciliation_definitions(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListGroupReconciliationDefinitions: List group reconciliation definitions

Lists Group Reconciliation Definitions matching any provided filter, limit and sorting rules

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the group reconciliation definitions. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the group reconciliation definitions. Defaults to return the latest version of each group reconciliation definition if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing group reconciliation definitions from a previous call to list group reconciliation definitions. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy  and asAt fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to no limit if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Display Name, use \"displayName eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_group_reconciliation_definitions(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

            # [EXPERIMENTAL] ListGroupReconciliationDefinitions: List group reconciliation definitions
            api_response = await api_instance.list_group_reconciliation_definitions(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->list_group_reconciliation_definitions: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the group reconciliation definitions. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the group reconciliation definitions. Defaults to return the latest version of each group reconciliation definition if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing group reconciliation definitions from a previous call to list group reconciliation definitions. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to no limit if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Display Name, use \&quot;displayName eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfGroupReconciliationDefinition**](PagedResourceListOfGroupReconciliationDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group reconciliation definition in the specified scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_comparison_ruleset**
> GroupReconciliationComparisonRuleset update_comparison_ruleset(scope, code, update_group_reconciliation_comparison_ruleset_request=update_group_reconciliation_comparison_ruleset_request)

[EXPERIMENTAL] UpdateComparisonRuleset: Update Group Reconciliation Comparison Ruleset defined by scope and code

Overwrites an existing Group Reconciliation Comparison Ruleset  Update request has the same required fields as Create apart from the Id

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)
        scope = 'scope_example' # str | The scope of the specified comparison ruleset.
        code = 'code_example' # str | The code of the specified comparison ruleset. Together with the domain and scope this uniquely                  identifies the reconciliation comparison ruleset.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_group_reconciliation_comparison_ruleset_request = UpdateGroupReconciliationComparisonRulesetRequest()
        # update_group_reconciliation_comparison_ruleset_request = UpdateGroupReconciliationComparisonRulesetRequest.from_json("")
        update_group_reconciliation_comparison_ruleset_request = UpdateGroupReconciliationComparisonRulesetRequest.from_dict({"displayName":"Compare by instrument and strategy","reconciliationType":"Holding","coreAttributeRules":[{"left":{"key":"path to instrument property","operation":"Value"},"right":{"key":"path to LUID property","operation":"Value"},"allowableStringMappings":[{"leftValue":"Microsoft","rightValue":"MSFT","direction":"UniDirectional"}],"isComparisonCaseSensitive":false},{"left":{"key":"path to strategy property","operation":"Value"},"right":{"key":"path to investment strategy property","operation":"Value"},"allowableStringMappings":[{"leftValue":"HighRisk","rightValue":"HR","direction":"BiDirectional"}],"isComparisonCaseSensitive":true}],"aggregateAttributeRules":[{"left":{"key":"path to units property","operation":"Sum"},"right":{"key":"path to count property","operation":"Sum"},"tolerance":{"type":"Absolute","value":10}},{"left":{"key":"path to price property","operation":"Sum"},"right":{"key":"path to price property","operation":"Sum"},"tolerance":{"type":"Relative","value":2}}]}) # UpdateGroupReconciliationComparisonRulesetRequest | The request containing the updated details of the ruleset (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_comparison_ruleset(scope, code, update_group_reconciliation_comparison_ruleset_request=update_group_reconciliation_comparison_ruleset_request, opts=opts)

            # [EXPERIMENTAL] UpdateComparisonRuleset: Update Group Reconciliation Comparison Ruleset defined by scope and code
            api_response = await api_instance.update_comparison_ruleset(scope, code, update_group_reconciliation_comparison_ruleset_request=update_group_reconciliation_comparison_ruleset_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->update_comparison_ruleset: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified comparison ruleset. | 
 **code** | **str**| The code of the specified comparison ruleset. Together with the domain and scope this uniquely                  identifies the reconciliation comparison ruleset. | 
 **update_group_reconciliation_comparison_ruleset_request** | [**UpdateGroupReconciliationComparisonRulesetRequest**](UpdateGroupReconciliationComparisonRulesetRequest.md)| The request containing the updated details of the ruleset | [optional] 

### Return type

[**GroupReconciliationComparisonRuleset**](GroupReconciliationComparisonRuleset.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version of the requested comparison ruleset |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_group_reconciliation_definition**
> GroupReconciliationDefinition update_group_reconciliation_definition(scope, code, update_group_reconciliation_definition_request=update_group_reconciliation_definition_request)

[EXPERIMENTAL] UpdateGroupReconciliationDefinition: Update group reconciliation definition

Update the group reconciliation definition.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    GroupReconciliationsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)
        scope = 'scope_example' # str | The scope of the group reconciliation definition to update the details for.
        code = 'code_example' # str | The code of the group reconciliation definition to update the details for. Together with the scope this uniquely identifies the group reconciliation definition.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_group_reconciliation_definition_request = UpdateGroupReconciliationDefinitionRequest()
        # update_group_reconciliation_definition_request = UpdateGroupReconciliationDefinitionRequest.from_json("")
        update_group_reconciliation_definition_request = UpdateGroupReconciliationDefinitionRequest.from_dict({"displayName":"My Group Reconciliation Definition","description":"The Group Reconciliation Definition description","portfolioEntityIds":{"left":[{"scope":"MyPortfolioScope","code":"MyPortfolioCode","portfolioEntityType":"SinglePortfolio"}],"right":[{"scope":"MyOtherPortfolioScope","code":"MyOtherPortfolioCode","portfolioEntityType":"SinglePortfolio"}]},"recipeIds":{"left":{"scope":"MyRecipeScope","code":"MyRecipeCode"},"right":{"scope":"MyOtherRecipeScope","code":"MyOtherRecipeCode"}},"currencies":{"left":"USD","right":"CHF"},"comparisonRulesetIds":{"valuationReconciliation":{"scope":"MyValuationComparisonRulesetScope","code":"MyValuationComparisonRulesetCode"}},"breakCodeSource":{"dataTypeId":{"scope":"MyBreakCodeSourceScope","code":"MyBreakCodeSourceCode"}}}) # UpdateGroupReconciliationDefinitionRequest | The updated group reconciliation definition. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_group_reconciliation_definition(scope, code, update_group_reconciliation_definition_request=update_group_reconciliation_definition_request, opts=opts)

            # [EXPERIMENTAL] UpdateGroupReconciliationDefinition: Update group reconciliation definition
            api_response = await api_instance.update_group_reconciliation_definition(scope, code, update_group_reconciliation_definition_request=update_group_reconciliation_definition_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling GroupReconciliationsApi->update_group_reconciliation_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group reconciliation definition to update the details for. | 
 **code** | **str**| The code of the group reconciliation definition to update the details for. Together with the scope this uniquely identifies the group reconciliation definition. | 
 **update_group_reconciliation_definition_request** | [**UpdateGroupReconciliationDefinitionRequest**](UpdateGroupReconciliationDefinitionRequest.md)| The updated group reconciliation definition. | [optional] 

### Return type

[**GroupReconciliationDefinition**](GroupReconciliationDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated details of the group reconciliation definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

