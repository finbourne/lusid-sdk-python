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
[**update_compliance_template**](ComplianceApi.md#update_compliance_template) | **PUT** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] UpdateComplianceTemplate: Update a ComplianceRuleTemplate
[**upsert_compliance_rule**](ComplianceApi.md#upsert_compliance_rule) | **POST** /api/compliance/rules | [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.
[**upsert_compliance_run_summary**](ComplianceApi.md#upsert_compliance_run_summary) | **POST** /api/compliance/runs/summary | [EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.


# **create_compliance_template**
> ComplianceRuleTemplate create_compliance_template(scope, create_compliance_template_request)

[EARLY ACCESS] CreateComplianceTemplate: Create a Compliance Rule Template

Use this endpoint to create a compliance template.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.compliance_rule_template import ComplianceRuleTemplate
from lusid.models.create_compliance_template_request import CreateComplianceTemplateRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    scope = 'scope_example' # str | The scope of the Compliance Rule Template.
    create_compliance_template_request = {"code":"MyCode","description":"Some compliance rule template description","variations":[{"label":"Some variation label","description":"Some variation description","outcomeDescription":"Some outcome description","referencedGroupLabel":"Some referenced group label","steps":[{"label":"ExcludingCash","complianceStepTypeRequest":"FilterStepRequest"},{"label":"GroupByProperty","complianceStepTypeRequest":"GroupByStepRequest"},{"label":"BranchByProperty","complianceStepTypeRequest":"BranchStepRequest"},{"label":"Compare","complianceStepTypeRequest":"GroupFilterStepRequest"}]}]} # CreateComplianceTemplateRequest | Request to create a compliance rule template.

    try:
        # [EARLY ACCESS] CreateComplianceTemplate: Create a Compliance Rule Template
        api_response = await api_instance.create_compliance_template(scope, create_compliance_template_request)
        print("The response of ComplianceApi->create_compliance_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->create_compliance_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Compliance Rule Template. | 
 **create_compliance_template_request** | [**CreateComplianceTemplateRequest**](CreateComplianceTemplateRequest.md)| Request to create a compliance rule template. | 

### Return type

[**ComplianceRuleTemplate**](ComplianceRuleTemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created compliance rule template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compliance_rule**
> DeletedEntityResponse delete_compliance_rule(scope, code)

[EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.

Use this endpoint to delete a compliance rule. The rule will be recoverable for asat times earlier than the  delete time, but will otherwise appear to have never existed.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    scope = 'scope_example' # str | The compliance rule's scope.
    code = 'code_example' # str | The compliance rule's code.

    try:
        # [EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.
        api_response = await api_instance.delete_compliance_rule(scope, code)
        print("The response of ComplianceApi->delete_compliance_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->delete_compliance_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule&#39;s scope. | 
 **code** | **str**| The compliance rule&#39;s code. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compliance_template**
> DeletedEntityResponse delete_compliance_template(scope, code)

[EARLY ACCESS] DeleteComplianceTemplate: Delete a ComplianceRuleTemplate

Delete the compliance rule template uniquely defined by the scope and code.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    scope = 'scope_example' # str | The scope of the template to be deleted.
    code = 'code_example' # str | The code of the template to be deleted.

    try:
        # [EARLY ACCESS] DeleteComplianceTemplate: Delete a ComplianceRuleTemplate
        api_response = await api_instance.delete_compliance_template(scope, code)
        print("The response of ComplianceApi->delete_compliance_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->delete_compliance_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the template to be deleted. | 
 **code** | **str**| The code of the template to be deleted. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting a compliance rule template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_rule**
> ComplianceRuleResponse get_compliance_rule(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetComplianceRule: Get compliance rule.

Use this endpoint to retrieve a single compliance rule.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.compliance_rule_response import ComplianceRuleResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    scope = 'scope_example' # str | The compliance rule's scope.
    code = 'code_example' # str | The compliance rule's code.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Asat time for query. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Compliance' domain to decorate onto the rule.              These must take the format {domain}/{scope}/{code}, for example 'Compliance/live/UCITS'. (optional)

    try:
        # [EARLY ACCESS] GetComplianceRule: Get compliance rule.
        api_response = await api_instance.get_compliance_rule(scope, code, as_at=as_at, property_keys=property_keys)
        print("The response of ComplianceApi->get_compliance_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_compliance_rule: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_rule_result**
> ComplianceRuleResultV2 get_compliance_rule_result(run_scope, run_code, rule_scope, rule_code)

[EARLY ACCESS] GetComplianceRuleResult: Get detailed results for a specific rule within a compliance run.

Specify a run scope and code from a previously run compliance check, and the scope and code of a rule within that run, to get detailed results for that rule.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.compliance_rule_result_v2 import ComplianceRuleResultV2
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    run_scope = 'run_scope_example' # str | Required: Run Scope.
    run_code = 'run_code_example' # str | Required: Run Code.
    rule_scope = 'rule_scope_example' # str | Required: Rule Scope.
    rule_code = 'rule_code_example' # str | Required: Rule Code.

    try:
        # [EARLY ACCESS] GetComplianceRuleResult: Get detailed results for a specific rule within a compliance run.
        api_response = await api_instance.get_compliance_rule_result(run_scope, run_code, rule_scope, rule_code)
        print("The response of ComplianceApi->get_compliance_rule_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_compliance_rule_result: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance run summary details for a specific rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_template**
> ComplianceTemplate get_compliance_template(scope, code, as_at=as_at)

[EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.

Use this endpoint to fetch a specific compliance template.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.compliance_template import ComplianceTemplate
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    scope = 'scope_example' # str | Scope of TemplateID
    code = 'code_example' # str | Code of TemplateID
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)

    try:
        # [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
        api_response = await api_instance.get_compliance_template(scope, code, as_at=as_at)
        print("The response of ComplianceApi->get_compliance_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_compliance_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of TemplateID | 
 **code** | **str**| Code of TemplateID | 
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 

### Return type

[**ComplianceTemplate**](ComplianceTemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_decorated_compliance_run_summary**
> DecoratedComplianceRunSummary get_decorated_compliance_run_summary(scope, code)

[EARLY ACCESS] GetDecoratedComplianceRunSummary: Get decorated summary results for a specific compliance run.

Specify a run scope and code from a previously run compliance check to get an overview of result details.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.decorated_compliance_run_summary import DecoratedComplianceRunSummary
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    scope = 'scope_example' # str | Required: Run Scope.
    code = 'code_example' # str | Required: Run Code.

    try:
        # [EARLY ACCESS] GetDecoratedComplianceRunSummary: Get decorated summary results for a specific compliance run.
        api_response = await api_instance.get_decorated_compliance_run_summary(scope, code)
        print("The response of ComplianceApi->get_decorated_compliance_run_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_decorated_compliance_run_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Required: Run Scope. | 
 **code** | **str**| Required: Run Code. | 

### Return type

[**DecoratedComplianceRunSummary**](DecoratedComplianceRunSummary.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance run details. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_rules**
> PagedResourceListOfComplianceRuleResponse list_compliance_rules(as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListComplianceRules: List compliance rules.

Use this endpoint to retrieve all compliance rules, or a subset defined by an optional filter.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_compliance_rule_response import PagedResourceListOfComplianceRuleResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Asat time. (optional)
    page = 'page_example' # str | Optional. Pagination token. (optional)
    limit = 56 # int | Optional. Entries per page. (optional)
    filter = 'filter_example' # str | Optional. Filter. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Compliance' domain to decorate onto each rule.              These must take the format {domain}/{scope}/{code}, for example 'Compliance/live/UCITS'. If not provided will return all the entitled properties for each rule. (optional)

    try:
        # [EARLY ACCESS] ListComplianceRules: List compliance rules.
        api_response = await api_instance.list_compliance_rules(as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)
        print("The response of ComplianceApi->list_compliance_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->list_compliance_rules: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of compliance rules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_runs**
> PagedResourceListOfComplianceRunInfoV2 list_compliance_runs(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.

Lists RunIds of prior compliance runs, or a subset with a filter.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_compliance_run_info_v2 import PagedResourceListOfComplianceRunInfoV2
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | Optional. A list of field names to sort by, each suffixed by \"ASC\" or \"DESC\" (optional)

    try:
        # [EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.
        api_response = await api_instance.list_compliance_runs(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        print("The response of ComplianceApi->list_compliance_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->list_compliance_runs: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of previous compliance RunIds |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_templates**
> PagedResourceListOfComplianceTemplate list_compliance_templates(as_at=as_at, page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListComplianceTemplates: List compliance templates.

Use this endpoint to fetch a list of all available compliance template ids, or a subset using a filter.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_compliance_template import PagedResourceListOfComplianceTemplate
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] ListComplianceTemplates: List compliance templates.
        api_response = await api_instance.list_compliance_templates(as_at=as_at, page=page, limit=limit, filter=filter)
        print("The response of ComplianceApi->list_compliance_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->list_compliance_templates: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of compliance templates available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_compliance**
> ComplianceRunInfoV2 run_compliance(run_scope, rule_scope, is_pre_trade, recipe_id_scope, recipe_id_code)

[EARLY ACCESS] RunCompliance: Run a compliance check.

Use this endpoint to run a compliance check using rules from a specific scope.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.compliance_run_info_v2 import ComplianceRunInfoV2
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    run_scope = 'run_scope_example' # str | Required: Scope to save the run results in.
    rule_scope = 'rule_scope_example' # str | Required: Scope from which to select rules to be run.
    is_pre_trade = True # bool | Required: Boolean flag indicating if a run should be PreTrade (Including orders). For post-trade only, set to false
    recipe_id_scope = 'recipe_id_scope_example' # str | Required: the scope of the recipe to be used
    recipe_id_code = 'recipe_id_code_example' # str | Required: The code of the recipe to be used. If left blank, the default recipe will be used.

    try:
        # [EARLY ACCESS] RunCompliance: Run a compliance check.
        api_response = await api_instance.run_compliance(run_scope, rule_scope, is_pre_trade, recipe_id_scope, recipe_id_code)
        print("The response of ComplianceApi->run_compliance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->run_compliance: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifying information of a compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_compliance_template**
> ComplianceRuleTemplate update_compliance_template(scope, code, update_compliance_template_request)

[EARLY ACCESS] UpdateComplianceTemplate: Update a ComplianceRuleTemplate

Use this endpoint to update a specified compliance template.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.compliance_rule_template import ComplianceRuleTemplate
from lusid.models.update_compliance_template_request import UpdateComplianceTemplateRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    scope = 'scope_example' # str | The scope of the Compliance Rule Template.
    code = 'code_example' # str | The code of the Compliance Rule Template.
    update_compliance_template_request = {"code":"MyCode","description":"Some compliance rule template description","variations":[{"label":"Some variation label","description":"Some variation description","outcomeDescription":"Some outcome description","referencedGroupLabel":"Some referenced group label","steps":[{"label":"ExcludingCash","complianceStepTypeRequest":"FilterStepRequest"},{"label":"GroupByProperty","complianceStepTypeRequest":"GroupByStepRequest"},{"label":"BranchByProperty","complianceStepTypeRequest":"BranchStepRequest"},{"label":"Compare","complianceStepTypeRequest":"GroupFilterStepRequest"}]}]} # UpdateComplianceTemplateRequest | Request to update a compliance rule template.

    try:
        # [EARLY ACCESS] UpdateComplianceTemplate: Update a ComplianceRuleTemplate
        api_response = await api_instance.update_compliance_template(scope, code, update_compliance_template_request)
        print("The response of ComplianceApi->update_compliance_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->update_compliance_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Compliance Rule Template. | 
 **code** | **str**| The code of the Compliance Rule Template. | 
 **update_compliance_template_request** | [**UpdateComplianceTemplateRequest**](UpdateComplianceTemplateRequest.md)| Request to update a compliance rule template. | 

### Return type

[**ComplianceRuleTemplate**](ComplianceRuleTemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated compliance rule template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_compliance_rule**
> ComplianceRuleResponse upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request)

[EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.

Use this endpoint to upsert a single compliance rule. The template and variation specified must already  exist, as must the portfolio group. The parameters passed must match those required by the template variation.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.compliance_rule_response import ComplianceRuleResponse
from lusid.models.upsert_compliance_rule_request import UpsertComplianceRuleRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    upsert_compliance_rule_request = {"id":{"scope":"live","code":"exampleRule"},"name":"A friendly name.","description":"A friendly description.","active":true,"templateId":{"scope":"system","code":"PercentCheck"},"variation":"standard","portfolioGroupId":{"scope":"examples","code":"examplePortfolioGroup"},"parameters":{"BoolParameter":{"value":true,"complianceParameterType":"BoolComplianceParameter"},"DecimalParameter":{"value":0,"complianceParameterType":"DecimalComplianceParameter"},"StringParameter":{"value":"An example string parameter","complianceParameterType":"StringComplianceParameter"},"DateTimeParameter":{"value":"2023-06-06T00:00:00.0000000+00:00","complianceParameterType":"DateTimeComplianceParameter"},"PropertyKeyParameter":{"value":"Compliance/live/RuleGroup","complianceParameterType":"PropertyKeyComplianceParameter"},"AddressKeyParameter":{"value":"Valuation/PvInReportCcy","complianceParameterType":"AddressKeyComplianceParameter"},"PortfolioIdParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PortfolioIdComplianceParameter"},"PortfolioGroupIdParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PortfolioGroupIdComplianceParameter"},"DecimalListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"DecimalListComplianceParameter"},"AddressKeyListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"AddressKeyListComplianceParameter"},"BoolListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"BoolListComplianceParameter"},"StringListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"StringListComplianceParameter"},"DateTimeListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"DateTimeListComplianceParameter"},"PropertyKeyListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PropertyKeyListComplianceParameter"},"PortfolioIdListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PortfolioIdListComplianceParameter"},"PortfolioGroupIdListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PortfolioGroupIdListComplianceParameter"}},"properties":{"Compliance/MyScope/SomeRuleProperty":{"key":"Compliance/MyScope/SomeRuleProperty","value":{"labelValue":"XYZ000034567"}}}} # UpsertComplianceRuleRequest |  (optional)

    try:
        # [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.
        api_response = await api_instance.upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request)
        print("The response of ComplianceApi->upsert_compliance_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->upsert_compliance_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_compliance_rule_request** | [**UpsertComplianceRuleRequest**](UpsertComplianceRuleRequest.md)|  | [optional] 

### Return type

[**ComplianceRuleResponse**](ComplianceRuleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted compliance rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_compliance_run_summary**
> UpsertComplianceRunSummaryResult upsert_compliance_run_summary(upsert_compliance_run_summary_request=upsert_compliance_run_summary_request)

[EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.

Use this endpoint to upsert a compliance run result summary.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.upsert_compliance_run_summary_request import UpsertComplianceRunSummaryRequest
from lusid.models.upsert_compliance_run_summary_result import UpsertComplianceRunSummaryResult
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ComplianceApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.ComplianceApi)
    upsert_compliance_run_summary_request = {"runId":{"scope":"SomeScope","code":"run-1"},"instigatedAt":"2020-01-05T00:00:00.0000000+00:00","completedAt":"2020-01-05T00:00:01.0000000+00:00","schedule":"PreTrade","results":[{"ruleId":{"scope":"SomeScope","code":"rule-1"},"templateId":{"scope":"system","code":"template-1"},"variation":"standard","ruleStatus":"passed","affectedPortfolios":[{"scope":"PortfolioScope","code":"PortfolioCode"}],"affectedOrders":[{"scope":"OrderScope","code":"OrderCode"}],"parametersUsed":{"UpperBound":"30","LowerBound":"0"},"ruleBreakdown":[{"groupStatus":"failed","resultsUsed":{"Valuation/PV":650,"Exposure/PV":650},"propertiesUsed":{"Instrument/data/Issuer":[{"key":"Instrument/data/Issuer","value":{"labelValue":"ABC"}}]},"missingDataInformation":["No Missing Data"],"lineage":[{"index":0,"label":"Initial","subLabel":"Initial","infoType":"","information":""},{"index":1,"label":"Step1","subLabel":"SomeStep1Information","infoType":"","information":""},{"index":2,"label":"Step2","subLabel":"Step2","infoType":"","information":""}]}]}]} # UpsertComplianceRunSummaryRequest |  (optional)

    try:
        # [EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.
        api_response = await api_instance.upsert_compliance_run_summary(upsert_compliance_run_summary_request=upsert_compliance_run_summary_request)
        print("The response of ComplianceApi->upsert_compliance_run_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->upsert_compliance_run_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_compliance_run_summary_request** | [**UpsertComplianceRunSummaryRequest**](UpsertComplianceRunSummaryRequest.md)|  | [optional] 

### Return type

[**UpsertComplianceRunSummaryResult**](UpsertComplianceRunSummaryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted compliance run summary. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

