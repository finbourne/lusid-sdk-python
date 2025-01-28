# lusid.TaxRuleSetsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_rule_set**](TaxRuleSetsApi.md#create_tax_rule_set) | **POST** /api/tax/rulesets | [EXPERIMENTAL] CreateTaxRuleSet: Create a tax rule set.
[**delete_tax_rule_set**](TaxRuleSetsApi.md#delete_tax_rule_set) | **DELETE** /api/tax/rulesets/{scope}/{code} | [EXPERIMENTAL] DeleteTaxRuleSet: Delete a tax rule set.
[**get_tax_rule_set**](TaxRuleSetsApi.md#get_tax_rule_set) | **GET** /api/tax/rulesets/{scope}/{code} | [EXPERIMENTAL] GetTaxRuleSet: Retrieve the definition of single tax rule set.
[**list_tax_rule_sets**](TaxRuleSetsApi.md#list_tax_rule_sets) | **GET** /api/tax/rulesets | [EXPERIMENTAL] ListTaxRuleSets: List tax rule sets.
[**update_tax_rule_set**](TaxRuleSetsApi.md#update_tax_rule_set) | **PUT** /api/tax/rulesets/{scope}/{code} | [EXPERIMENTAL] UpdateTaxRuleSet: Update a tax rule set.


# **create_tax_rule_set**
> TaxRuleSet create_tax_rule_set(create_tax_rule_set_request, effective_at=effective_at)

[EXPERIMENTAL] CreateTaxRuleSet: Create a tax rule set.

Creates a tax rule set definition at the given effective time.  The user must be entitled to read any properties specified in each rule.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxRuleSetsApi
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
    api_instance = api_client_factory.build(TaxRuleSetsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_tax_rule_set_request = CreateTaxRuleSetRequest.from_json("")
    # create_tax_rule_set_request = CreateTaxRuleSetRequest.from_dict({})
    create_tax_rule_set_request = CreateTaxRuleSetRequest()
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the rule set will take effect.  Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_tax_rule_set(create_tax_rule_set_request, effective_at=effective_at, opts=opts)

        # [EXPERIMENTAL] CreateTaxRuleSet: Create a tax rule set.
        api_response = api_instance.create_tax_rule_set(create_tax_rule_set_request, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxRuleSetsApi->create_tax_rule_set: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tax_rule_set_request** | [**CreateTaxRuleSetRequest**](CreateTaxRuleSetRequest.md)| The contents of the rule set. | 
 **effective_at** | **str**| The effective datetime or cut label at which the rule set will take effect.  Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**TaxRuleSet**](TaxRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a rule set for tax calculations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_tax_rule_set**
> DeletedEntityResponse delete_tax_rule_set(scope, code)

[EXPERIMENTAL] DeleteTaxRuleSet: Delete a tax rule set.

               Deletes the rule set for all effective time.                               The rule set will remain viewable at previous as at times, but it will no longer be considered applicable.                               This cannot be undone.              

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxRuleSetsApi
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
    api_instance = api_client_factory.build(TaxRuleSetsApi)
    scope = 'scope_example' # str | The rule set scope.
    code = 'code_example' # str | The rule set code.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_tax_rule_set(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteTaxRuleSet: Delete a tax rule set.
        api_response = api_instance.delete_tax_rule_set(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxRuleSetsApi->delete_tax_rule_set: %s\n" % e)

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

# **get_tax_rule_set**
> TaxRuleSet get_tax_rule_set(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetTaxRuleSet: Retrieve the definition of single tax rule set.

Retrieves the tax rule set definition at the given effective and as at times.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxRuleSetsApi
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
    api_instance = api_client_factory.build(TaxRuleSetsApi)
    scope = 'scope_example' # str | The rule set scope.
    code = 'code_example' # str | The rule set code.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definition.  Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_tax_rule_set(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetTaxRuleSet: Retrieve the definition of single tax rule set.
        api_response = api_instance.get_tax_rule_set(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxRuleSetsApi->get_tax_rule_set: %s\n" % e)

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

[**TaxRuleSet**](TaxRuleSet.md)

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

# **list_tax_rule_sets**
> ResourceListOfTaxRuleSet list_tax_rule_sets(effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] ListTaxRuleSets: List tax rule sets.

Retrieves all tax rule set definitions at the given effective and as at times

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxRuleSetsApi
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
    api_instance = api_client_factory.build(TaxRuleSetsApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definitions.  Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_tax_rule_sets(effective_at=effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] ListTaxRuleSets: List tax rule sets.
        api_response = api_instance.list_tax_rule_sets(effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxRuleSetsApi->list_tax_rule_sets: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definitions.  Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. | [optional] 

### Return type

[**ResourceListOfTaxRuleSet**](ResourceListOfTaxRuleSet.md)

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

# **update_tax_rule_set**
> TaxRuleSet update_tax_rule_set(scope, code, update_tax_rule_set_request, effective_at=effective_at)

[EXPERIMENTAL] UpdateTaxRuleSet: Update a tax rule set.

Updates the tax rule set definition at the given effective time.  The changes will take place from this effective time until the next effective time that the rule has been updated at.  For example, consider a rule that has been created or updated effective at the first day of the coming month.  An upsert effective from the current day will only change the definition until that day.  An additional upsert at the same time (first day of the month) is required if the newly-updated definition is to supersede the future definition.  The user must be entitled to read any properties specified in each rule.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxRuleSetsApi
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
    api_instance = api_client_factory.build(TaxRuleSetsApi)
    scope = 'scope_example' # str | The rule set scope.
    code = 'code_example' # str | The rule set code.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_tax_rule_set_request = UpdateTaxRuleSetRequest.from_json("")
    # update_tax_rule_set_request = UpdateTaxRuleSetRequest.from_dict({})
    update_tax_rule_set_request = UpdateTaxRuleSetRequest()
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the rule set will take effect.  Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_tax_rule_set(scope, code, update_tax_rule_set_request, effective_at=effective_at, opts=opts)

        # [EXPERIMENTAL] UpdateTaxRuleSet: Update a tax rule set.
        api_response = api_instance.update_tax_rule_set(scope, code, update_tax_rule_set_request, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxRuleSetsApi->update_tax_rule_set: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | 
 **code** | **str**| The rule set code. | 
 **update_tax_rule_set_request** | [**UpdateTaxRuleSetRequest**](UpdateTaxRuleSetRequest.md)| The contents of the rule set. | 
 **effective_at** | **str**| The effective datetime or cut label at which the rule set will take effect.  Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**TaxRuleSet**](TaxRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update rules for tax calculations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

