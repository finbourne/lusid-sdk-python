# lusid.AmortisationRuleSetsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_amortisation_rule_set**](AmortisationRuleSetsApi.md#create_amortisation_rule_set) | **POST** /api/amortisation/rulesets/{scope} | [EXPERIMENTAL] CreateAmortisationRuleSet: Create an amortisation rule set.
[**delete_amortisation_ruleset**](AmortisationRuleSetsApi.md#delete_amortisation_ruleset) | **DELETE** /api/amortisation/rulesets/{scope}/{code} | [EXPERIMENTAL] DeleteAmortisationRuleset: Delete an amortisation rule set.
[**get_amortisation_rule_set**](AmortisationRuleSetsApi.md#get_amortisation_rule_set) | **GET** /api/amortisation/rulesets/{scope}/{code} | [EXPERIMENTAL] GetAmortisationRuleSet: Retrieve the definition of a single amortisation rule set
[**list_amortisation_rule_sets**](AmortisationRuleSetsApi.md#list_amortisation_rule_sets) | **GET** /api/amortisation/rulesets | [EXPERIMENTAL] ListAmortisationRuleSets: List amortisation rule sets.
[**set_amortisation_rules**](AmortisationRuleSetsApi.md#set_amortisation_rules) | **PUT** /api/amortisation/rulesets/{scope}/{code}/rules | [EXPERIMENTAL] SetAmortisationRules: Set Amortisation Rules on an existing Amortisation Rule Set.
[**update_amortisation_rule_set_details**](AmortisationRuleSetsApi.md#update_amortisation_rule_set_details) | **PUT** /api/amortisation/rulesets/{scope}/{code}/details | [EXPERIMENTAL] UpdateAmortisationRuleSetDetails: Update an amortisation rule set.


# **create_amortisation_rule_set**
> AmortisationRuleSet create_amortisation_rule_set(scope, create_amortisation_rule_set_request)

[EXPERIMENTAL] CreateAmortisationRuleSet: Create an amortisation rule set.

Creates an amortisation rule set definition at the given effective time.  The user must be entitled to read any properties specified in each rule.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AmortisationRuleSetsApi
)

def main():

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

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(AmortisationRuleSetsApi)
    scope = 'scope_example' # str | The scope of the rule set.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_amortisation_rule_set_request = CreateAmortisationRuleSetRequest.from_json("")
    # create_amortisation_rule_set_request = CreateAmortisationRuleSetRequest.from_dict({})
    create_amortisation_rule_set_request = CreateAmortisationRuleSetRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_amortisation_rule_set(scope, create_amortisation_rule_set_request, opts=opts)

        # [EXPERIMENTAL] CreateAmortisationRuleSet: Create an amortisation rule set.
        api_response = api_instance.create_amortisation_rule_set(scope, create_amortisation_rule_set_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AmortisationRuleSetsApi->create_amortisation_rule_set: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the rule set. | 
 **create_amortisation_rule_set_request** | [**CreateAmortisationRuleSetRequest**](CreateAmortisationRuleSetRequest.md)| The contents of the rule set. | 

### Return type

[**AmortisationRuleSet**](AmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a rule set for amortisation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_amortisation_ruleset**
> DeletedEntityResponse delete_amortisation_ruleset(scope, code)

[EXPERIMENTAL] DeleteAmortisationRuleset: Delete an amortisation rule set.

Deletes the rule set perpetually, including its rules.    The rule set will remain viewable at previous as at times, but it will no longer be considered applicable.    This cannot be undone.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AmortisationRuleSetsApi
)

def main():

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

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(AmortisationRuleSetsApi)
    scope = 'scope_example' # str | The rule set scope.
    code = 'code_example' # str | The rule set code.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_amortisation_ruleset(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteAmortisationRuleset: Delete an amortisation rule set.
        api_response = api_instance.delete_amortisation_ruleset(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AmortisationRuleSetsApi->delete_amortisation_ruleset: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | 
 **code** | **str**| The rule set code. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_amortisation_rule_set**
> AmortisationRuleSet get_amortisation_rule_set(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAmortisationRuleSet: Retrieve the definition of a single amortisation rule set

Retrieves the amortisation rule set definition at the given effective and as at times.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AmortisationRuleSetsApi
)

def main():

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

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(AmortisationRuleSetsApi)
    scope = 'scope_example' # str | The rule set scope.
    code = 'code_example' # str | The rule set code.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definition.  Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_amortisation_rule_set(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetAmortisationRuleSet: Retrieve the definition of a single amortisation rule set
        api_response = api_instance.get_amortisation_rule_set(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AmortisationRuleSetsApi->get_amortisation_rule_set: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | 
 **code** | **str**| The rule set code. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definition.  Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. | [optional] 

### Return type

[**AmortisationRuleSet**](AmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of one rule set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_amortisation_rule_sets**
> PagedResourceListOfAmortisationRuleSet list_amortisation_rule_sets(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListAmortisationRuleSets: List amortisation rule sets.

Retrieves all amortisation rule sets at the given effective and as at times

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AmortisationRuleSetsApi
)

def main():

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

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(AmortisationRuleSetsApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definitions.  Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing AmortisationRuleSets; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_amortisation_rule_sets(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListAmortisationRuleSets: List amortisation rule sets.
        api_response = api_instance.list_amortisation_rule_sets(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AmortisationRuleSetsApi->list_amortisation_rule_sets: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definitions.  Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing AmortisationRuleSets; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfAmortisationRuleSet**](PagedResourceListOfAmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rule sets available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_amortisation_rules**
> AmortisationRuleSet set_amortisation_rules(scope, code, set_amortisation_rules_request)

[EXPERIMENTAL] SetAmortisationRules: Set Amortisation Rules on an existing Amortisation Rule Set.

Sets the rules on the Amortisation Rule Set, replacing the existing rules with the set provided.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AmortisationRuleSetsApi
)

def main():

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

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(AmortisationRuleSetsApi)
    scope = 'scope_example' # str | The rule set scope.
    code = 'code_example' # str | The rule set code.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # set_amortisation_rules_request = SetAmortisationRulesRequest.from_json("")
    # set_amortisation_rules_request = SetAmortisationRulesRequest.from_dict({})
    set_amortisation_rules_request = SetAmortisationRulesRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_amortisation_rules(scope, code, set_amortisation_rules_request, opts=opts)

        # [EXPERIMENTAL] SetAmortisationRules: Set Amortisation Rules on an existing Amortisation Rule Set.
        api_response = api_instance.set_amortisation_rules(scope, code, set_amortisation_rules_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AmortisationRuleSetsApi->set_amortisation_rules: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | 
 **code** | **str**| The rule set code. | 
 **set_amortisation_rules_request** | [**SetAmortisationRulesRequest**](SetAmortisationRulesRequest.md)| The contents of the rules. | 

### Return type

[**AmortisationRuleSet**](AmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the rules for an amortisation rule set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_amortisation_rule_set_details**
> AmortisationRuleSet update_amortisation_rule_set_details(scope, code, update_amortisation_rule_set_details_request)

[EXPERIMENTAL] UpdateAmortisationRuleSetDetails: Update an amortisation rule set.

Updates the amortisation rule set definition for all effective time.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AmortisationRuleSetsApi
)

def main():

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

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(AmortisationRuleSetsApi)
    scope = 'scope_example' # str | The rule set scope.
    code = 'code_example' # str | The rule set code.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_amortisation_rule_set_details_request = UpdateAmortisationRuleSetDetailsRequest.from_json("")
    # update_amortisation_rule_set_details_request = UpdateAmortisationRuleSetDetailsRequest.from_dict({})
    update_amortisation_rule_set_details_request = UpdateAmortisationRuleSetDetailsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_amortisation_rule_set_details(scope, code, update_amortisation_rule_set_details_request, opts=opts)

        # [EXPERIMENTAL] UpdateAmortisationRuleSetDetails: Update an amortisation rule set.
        api_response = api_instance.update_amortisation_rule_set_details(scope, code, update_amortisation_rule_set_details_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AmortisationRuleSetsApi->update_amortisation_rule_set_details: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | 
 **code** | **str**| The rule set code. | 
 **update_amortisation_rule_set_details_request** | [**UpdateAmortisationRuleSetDetailsRequest**](UpdateAmortisationRuleSetDetailsRequest.md)| The contents of the rule set. | 

### Return type

[**AmortisationRuleSet**](AmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the details of an Amortisation Rule Set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

