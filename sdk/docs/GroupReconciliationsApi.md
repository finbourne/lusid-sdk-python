# lusid.GroupReconciliationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comparison_ruleset**](GroupReconciliationsApi.md#create_comparison_ruleset) | **POST** /api/reconciliations/comparisonrulesets | [EXPERIMENTAL] CreateComparisonRuleset: Create a Group Reconciliation Comparison Ruleset
[**get_comparison_ruleset**](GroupReconciliationsApi.md#get_comparison_ruleset) | **GET** /api/reconciliations/comparisonrulesets/{scope}/{code} | [EXPERIMENTAL] GetComparisonRuleset: Get a single Group Reconciliation Comparison Ruleset by scope and code


# **create_comparison_ruleset**
> GroupReconciliationComparisonRuleset create_comparison_ruleset(create_group_reconciliation_comparison_ruleset_request=create_group_reconciliation_comparison_ruleset_request)

[EXPERIMENTAL] CreateComparisonRuleset: Create a Group Reconciliation Comparison Ruleset

Creates a set of core and aggregate rules to be run for a group reconciliation

### Example

```python
import asyncio
from lusid.exceptions import ApiException
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

# **get_comparison_ruleset**
> GroupReconciliationComparisonRuleset get_comparison_ruleset(scope, code, as_at=as_at)

[EXPERIMENTAL] GetComparisonRuleset: Get a single Group Reconciliation Comparison Ruleset by scope and code

Retrieves one Group Reconciliation Comparison Ruleset by scope and code

### Example

```python
import asyncio
from lusid.exceptions import ApiException
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(GroupReconciliationsApi)
        scope = 'scope_example' # str | The scope of the specified comparison ruleset.
        code = 'code_example' # str | The code of the specified comparison ruleset. Together with the domain and scope this uniquely              identifies the reconciliation comparison ruleset.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the comparison ruleset definition. Defaults to return              the latest version of the definition if not specified. (optional)

        try:
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

