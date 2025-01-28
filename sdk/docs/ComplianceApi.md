# lusid.ComplianceApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_compliance_template**](ComplianceApi.md#create_compliance_template) | **POST** /api/compliance/templates/{scope} | [EARLY ACCESS] CreateComplianceTemplate: Create a Compliance Rule Template
[**delete_compliance_rule**](ComplianceApi.md#delete_compliance_rule) | **DELETE** /api/compliance/rules/{scope}/{code} | [EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.
[**delete_compliance_template**](ComplianceApi.md#delete_compliance_template) | **DELETE** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] DeleteComplianceTemplate: Delete a ComplianceRuleTemplate
[**get_compliance_rule**](ComplianceApi.md#get_compliance_rule) | **GET** /api/compliance/rules/{scope}/{code} | [EARLY ACCESS] GetComplianceRule: Get compliance rule.
[**get_compliance_rule_result**](ComplianceApi.md#get_compliance_rule_result) | **GET** /api/compliance/runs/summary/{runScope}/{runCode}/{ruleScope}/{ruleCode} | [EARLY ACCESS] GetComplianceRuleResult: Get detailed results for a specific rule within a compliance run.
[**get_compliance_template**](ComplianceApi.md#get_compliance_template) | **GET** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
[**get_decorated_compliance_run_summary**](ComplianceApi.md#get_decorated_compliance_run_summary) | **GET** /api/compliance/runs/summary/{scope}/{code}/$decorate | [EARLY ACCESS] GetDecoratedComplianceRunSummary: Get decorated summary results for a specific compliance run.
[**list_compliance_rules**](ComplianceApi.md#list_compliance_rules) | **GET** /api/compliance/rules | [EARLY ACCESS] ListComplianceRules: List compliance rules.
[**list_compliance_runs**](ComplianceApi.md#list_compliance_runs) | **GET** /api/compliance/runs | [EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.
[**list_compliance_templates**](ComplianceApi.md#list_compliance_templates) | **GET** /api/compliance/templates | [EARLY ACCESS] ListComplianceTemplates: List compliance templates.
[**run_compliance**](ComplianceApi.md#run_compliance) | **POST** /api/compliance/runs | [EARLY ACCESS] RunCompliance: Run a compliance check.
[**run_compliance_preview**](ComplianceApi.md#run_compliance_preview) | **POST** /api/compliance/preview/runs | [EARLY ACCESS] RunCompliancePreview: Run a compliance check.
[**update_compliance_template**](ComplianceApi.md#update_compliance_template) | **PUT** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] UpdateComplianceTemplate: Update a ComplianceRuleTemplate
[**upsert_compliance_rule**](ComplianceApi.md#upsert_compliance_rule) | **POST** /api/compliance/rules | [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.
[**upsert_compliance_run_summary**](ComplianceApi.md#upsert_compliance_run_summary) | **POST** /api/compliance/runs/summary | [EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.


# **create_compliance_template**
> ComplianceRuleTemplate create_compliance_template(scope, create_compliance_template_request)

[EARLY ACCESS] CreateComplianceTemplate: Create a Compliance Rule Template

Use this endpoint to create a compliance template.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    scope = 'scope_example' # str | The scope of the Compliance Rule Template.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_compliance_template_request = CreateComplianceTemplateRequest.from_json("")
    # create_compliance_template_request = CreateComplianceTemplateRequest.from_dict({})
    create_compliance_template_request = CreateComplianceTemplateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_compliance_template(scope, create_compliance_template_request, opts=opts)

        # [EARLY ACCESS] CreateComplianceTemplate: Create a Compliance Rule Template
        api_response = api_instance.create_compliance_template(scope, create_compliance_template_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->create_compliance_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Compliance Rule Template. | 
 **create_compliance_template_request** | [**CreateComplianceTemplateRequest**](CreateComplianceTemplateRequest.md)| Request to create a compliance rule template. | 

### Return type

[**ComplianceRuleTemplate**](ComplianceRuleTemplate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created compliance rule template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_compliance_rule**
> DeletedEntityResponse delete_compliance_rule(scope, code)

[EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.

Use this endpoint to delete a compliance rule. The rule will be recoverable for asat times earlier than the  delete time, but will otherwise appear to have never existed.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    scope = 'scope_example' # str | The compliance rule's scope.
    code = 'code_example' # str | The compliance rule's code.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_compliance_rule(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.
        api_response = api_instance.delete_compliance_rule(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->delete_compliance_rule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule&#39;s scope. | 
 **code** | **str**| The compliance rule&#39;s code. | 

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

# **delete_compliance_template**
> DeletedEntityResponse delete_compliance_template(scope, code)

[EARLY ACCESS] DeleteComplianceTemplate: Delete a ComplianceRuleTemplate

Delete the compliance rule template uniquely defined by the scope and code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    scope = 'scope_example' # str | The scope of the template to be deleted.
    code = 'code_example' # str | The code of the template to be deleted.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_compliance_template(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteComplianceTemplate: Delete a ComplianceRuleTemplate
        api_response = api_instance.delete_compliance_template(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->delete_compliance_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the template to be deleted. | 
 **code** | **str**| The code of the template to be deleted. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting a compliance rule template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_compliance_rule**
> ComplianceRuleResponse get_compliance_rule(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetComplianceRule: Get compliance rule.

Use this endpoint to retrieve a single compliance rule.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    scope = 'scope_example' # str | The compliance rule's scope.
    code = 'code_example' # str | The compliance rule's code.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Asat time for query. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Compliance' domain to decorate onto the rule.              These must take the format {domain}/{scope}/{code}, for example 'Compliance/live/UCITS'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_compliance_rule(scope, code, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] GetComplianceRule: Get compliance rule.
        api_response = api_instance.get_compliance_rule(scope, code, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->get_compliance_rule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule&#39;s scope. | 
 **code** | **str**| The compliance rule&#39;s code. | 
 **as_at** | **datetime**| Optional. Asat time for query. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Compliance&#39; domain to decorate onto the rule.              These must take the format {domain}/{scope}/{code}, for example &#39;Compliance/live/UCITS&#39;. | [optional] 

### Return type

[**ComplianceRuleResponse**](ComplianceRuleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_compliance_rule_result**
> ComplianceRuleResultV2 get_compliance_rule_result(run_scope, run_code, rule_scope, rule_code)

[EARLY ACCESS] GetComplianceRuleResult: Get detailed results for a specific rule within a compliance run.

Specify a run scope and code from a previously run compliance check, and the scope and code of a rule within that run, to get detailed results for that rule.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    run_scope = 'run_scope_example' # str | Required: Run Scope.
    run_code = 'run_code_example' # str | Required: Run Code.
    rule_scope = 'rule_scope_example' # str | Required: Rule Scope.
    rule_code = 'rule_code_example' # str | Required: Rule Code.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_compliance_rule_result(run_scope, run_code, rule_scope, rule_code, opts=opts)

        # [EARLY ACCESS] GetComplianceRuleResult: Get detailed results for a specific rule within a compliance run.
        api_response = api_instance.get_compliance_rule_result(run_scope, run_code, rule_scope, rule_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->get_compliance_rule_result: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_scope** | **str**| Required: Run Scope. | 
 **run_code** | **str**| Required: Run Code. | 
 **rule_scope** | **str**| Required: Rule Scope. | 
 **rule_code** | **str**| Required: Rule Code. | 

### Return type

[**ComplianceRuleResultV2**](ComplianceRuleResultV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance run summary details for a specific rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_compliance_template**
> ComplianceTemplate get_compliance_template(scope, code, as_at=as_at)

[EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.

Use this endpoint to fetch a specific compliance template.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    scope = 'scope_example' # str | Scope of TemplateID
    code = 'code_example' # str | Code of TemplateID
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_compliance_template(scope, code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
        api_response = api_instance.get_compliance_template(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->get_compliance_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of TemplateID | 
 **code** | **str**| Code of TemplateID | 
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 

### Return type

[**ComplianceTemplate**](ComplianceTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_decorated_compliance_run_summary**
> DecoratedComplianceRunSummary get_decorated_compliance_run_summary(scope, code)

[EARLY ACCESS] GetDecoratedComplianceRunSummary: Get decorated summary results for a specific compliance run.

Specify a run scope and code from a previously run compliance check to get an overview of result details.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    scope = 'scope_example' # str | Required: Run Scope.
    code = 'code_example' # str | Required: Run Code.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_decorated_compliance_run_summary(scope, code, opts=opts)

        # [EARLY ACCESS] GetDecoratedComplianceRunSummary: Get decorated summary results for a specific compliance run.
        api_response = api_instance.get_decorated_compliance_run_summary(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->get_decorated_compliance_run_summary: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Required: Run Scope. | 
 **code** | **str**| Required: Run Code. | 

### Return type

[**DecoratedComplianceRunSummary**](DecoratedComplianceRunSummary.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance run details. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_compliance_rules**
> PagedResourceListOfComplianceRuleResponse list_compliance_rules(as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListComplianceRules: List compliance rules.

Use this endpoint to retrieve all compliance rules, or a subset defined by an optional filter.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Asat time. (optional)
    page = 'page_example' # str | Optional. Pagination token. (optional)
    limit = 56 # int | Optional. Entries per page. (optional)
    filter = 'filter_example' # str | Optional. Filter. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Compliance' domain to decorate onto each rule.              These must take the format {domain}/{scope}/{code}, for example 'Compliance/live/UCITS'. If not provided will return all the entitled properties for each rule. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_compliance_rules(as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] ListComplianceRules: List compliance rules.
        api_response = api_instance.list_compliance_rules(as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->list_compliance_rules: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. Asat time. | [optional] 
 **page** | **str**| Optional. Pagination token. | [optional] 
 **limit** | **int**| Optional. Entries per page. | [optional] 
 **filter** | **str**| Optional. Filter. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Compliance&#39; domain to decorate onto each rule.              These must take the format {domain}/{scope}/{code}, for example &#39;Compliance/live/UCITS&#39;. If not provided will return all the entitled properties for each rule. | [optional] 

### Return type

[**PagedResourceListOfComplianceRuleResponse**](PagedResourceListOfComplianceRuleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of compliance rules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_compliance_runs**
> PagedResourceListOfComplianceRunInfoV2 list_compliance_runs(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.

Lists RunIds of prior compliance runs, or a subset with a filter.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | Optional. A list of field names to sort by, each suffixed by \"ASC\" or \"DESC\" (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_compliance_runs(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.
        api_response = api_instance.list_compliance_runs(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->list_compliance_runs: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 
 **page** | **str**| Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Optional. A list of field names to sort by, each suffixed by \&quot;ASC\&quot; or \&quot;DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfComplianceRunInfoV2**](PagedResourceListOfComplianceRunInfoV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of previous compliance RunIds |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_compliance_templates**
> PagedResourceListOfComplianceTemplate list_compliance_templates(as_at=as_at, page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListComplianceTemplates: List compliance templates.

Use this endpoint to fetch a list of all available compliance template ids, or a subset using a filter.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_compliance_templates(as_at=as_at, page=page, limit=limit, filter=filter, opts=opts)

        # [EARLY ACCESS] ListComplianceTemplates: List compliance templates.
        api_response = api_instance.list_compliance_templates(as_at=as_at, page=page, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->list_compliance_templates: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 
 **page** | **str**| Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfComplianceTemplate**](PagedResourceListOfComplianceTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of compliance templates available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **run_compliance**
> ComplianceRunInfoV2 run_compliance(run_scope, rule_scope, is_pre_trade, recipe_id_scope, recipe_id_code)

[EARLY ACCESS] RunCompliance: Run a compliance check.

Use this endpoint to run a compliance check using rules from a specific scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    run_scope = 'run_scope_example' # str | Required: Scope to save the run results in.
    rule_scope = 'rule_scope_example' # str | Required: Scope from which to select rules to be run.
    is_pre_trade = True # bool | Required: Boolean flag indicating if a run should be PreTrade (Including orders). For post-trade only, set to false
    recipe_id_scope = 'recipe_id_scope_example' # str | Required: the scope of the recipe to be used
    recipe_id_code = 'recipe_id_code_example' # str | Required: The code of the recipe to be used. If left blank, the default recipe will be used.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.run_compliance(run_scope, rule_scope, is_pre_trade, recipe_id_scope, recipe_id_code, opts=opts)

        # [EARLY ACCESS] RunCompliance: Run a compliance check.
        api_response = api_instance.run_compliance(run_scope, rule_scope, is_pre_trade, recipe_id_scope, recipe_id_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->run_compliance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_scope** | **str**| Required: Scope to save the run results in. | 
 **rule_scope** | **str**| Required: Scope from which to select rules to be run. | 
 **is_pre_trade** | **bool**| Required: Boolean flag indicating if a run should be PreTrade (Including orders). For post-trade only, set to false | 
 **recipe_id_scope** | **str**| Required: the scope of the recipe to be used | 
 **recipe_id_code** | **str**| Required: The code of the recipe to be used. If left blank, the default recipe will be used. | 

### Return type

[**ComplianceRunInfoV2**](ComplianceRunInfoV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifying information of a compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **run_compliance_preview**
> ComplianceRunInfoV2 run_compliance_preview(run_scope, rule_scope, recipe_id_scope, recipe_id_code, compliance_run_configuration=compliance_run_configuration)

[EARLY ACCESS] RunCompliancePreview: Run a compliance check.

Use this endpoint to run a compliance check using rules from a specific scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    run_scope = 'run_scope_example' # str | Required: Scope to save the run results in.
    rule_scope = 'rule_scope_example' # str | Required: Scope from which to select rules to be run.
    recipe_id_scope = 'recipe_id_scope_example' # str | Required: the scope of the recipe to be used
    recipe_id_code = 'recipe_id_code_example' # str | Required: The code of the recipe to be used. If left blank, the default recipe will be used.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # compliance_run_configuration = ComplianceRunConfiguration.from_json("")
    # compliance_run_configuration = ComplianceRunConfiguration.from_dict({})
    compliance_run_configuration = ComplianceRunConfiguration()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.run_compliance_preview(run_scope, rule_scope, recipe_id_scope, recipe_id_code, compliance_run_configuration=compliance_run_configuration, opts=opts)

        # [EARLY ACCESS] RunCompliancePreview: Run a compliance check.
        api_response = api_instance.run_compliance_preview(run_scope, rule_scope, recipe_id_scope, recipe_id_code, compliance_run_configuration=compliance_run_configuration)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->run_compliance_preview: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_scope** | **str**| Required: Scope to save the run results in. | 
 **rule_scope** | **str**| Required: Scope from which to select rules to be run. | 
 **recipe_id_scope** | **str**| Required: the scope of the recipe to be used | 
 **recipe_id_code** | **str**| Required: The code of the recipe to be used. If left blank, the default recipe will be used. | 
 **compliance_run_configuration** | [**ComplianceRunConfiguration**](ComplianceRunConfiguration.md)| Configuration options for the compliance run. | [optional] 

### Return type

[**ComplianceRunInfoV2**](ComplianceRunInfoV2.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifying information of a compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_compliance_template**
> ComplianceRuleTemplate update_compliance_template(scope, code, update_compliance_template_request)

[EARLY ACCESS] UpdateComplianceTemplate: Update a ComplianceRuleTemplate

Use this endpoint to update a specified compliance template.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)
    scope = 'scope_example' # str | The scope of the Compliance Rule Template.
    code = 'code_example' # str | The code of the Compliance Rule Template.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_compliance_template_request = UpdateComplianceTemplateRequest.from_json("")
    # update_compliance_template_request = UpdateComplianceTemplateRequest.from_dict({})
    update_compliance_template_request = UpdateComplianceTemplateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_compliance_template(scope, code, update_compliance_template_request, opts=opts)

        # [EARLY ACCESS] UpdateComplianceTemplate: Update a ComplianceRuleTemplate
        api_response = api_instance.update_compliance_template(scope, code, update_compliance_template_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->update_compliance_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Compliance Rule Template. | 
 **code** | **str**| The code of the Compliance Rule Template. | 
 **update_compliance_template_request** | [**UpdateComplianceTemplateRequest**](UpdateComplianceTemplateRequest.md)| Request to update a compliance rule template. | 

### Return type

[**ComplianceRuleTemplate**](ComplianceRuleTemplate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated compliance rule template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_compliance_rule**
> ComplianceRuleResponse upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request)

[EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.

Use this endpoint to upsert a single compliance rule. The template and variation specified must already  exist, as must the portfolio group. The parameters passed must match those required by the template variation.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_compliance_rule_request = UpsertComplianceRuleRequest.from_json("")
    # upsert_compliance_rule_request = UpsertComplianceRuleRequest.from_dict({})
    upsert_compliance_rule_request = UpsertComplianceRuleRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request, opts=opts)

        # [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.
        api_response = api_instance.upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->upsert_compliance_rule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_compliance_rule_request** | [**UpsertComplianceRuleRequest**](UpsertComplianceRuleRequest.md)|  | [optional] 

### Return type

[**ComplianceRuleResponse**](ComplianceRuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted compliance rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_compliance_run_summary**
> UpsertComplianceRunSummaryResult upsert_compliance_run_summary(upsert_compliance_run_summary_request=upsert_compliance_run_summary_request)

[EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.

Use this endpoint to upsert a compliance run result summary.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ComplianceApi
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
    api_instance = api_client_factory.build(ComplianceApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_compliance_run_summary_request = UpsertComplianceRunSummaryRequest.from_json("")
    # upsert_compliance_run_summary_request = UpsertComplianceRunSummaryRequest.from_dict({})
    upsert_compliance_run_summary_request = UpsertComplianceRunSummaryRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_compliance_run_summary(upsert_compliance_run_summary_request=upsert_compliance_run_summary_request, opts=opts)

        # [EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.
        api_response = api_instance.upsert_compliance_run_summary(upsert_compliance_run_summary_request=upsert_compliance_run_summary_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ComplianceApi->upsert_compliance_run_summary: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_compliance_run_summary_request** | [**UpsertComplianceRunSummaryRequest**](UpsertComplianceRunSummaryRequest.md)|  | [optional] 

### Return type

[**UpsertComplianceRunSummaryResult**](UpsertComplianceRunSummaryResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted compliance run summary. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

