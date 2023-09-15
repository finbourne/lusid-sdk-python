# lusid.ComplianceApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_compliance_rule**](ComplianceApi.md#delete_compliance_rule) | **DELETE** /api/compliance/rules/{scope}/{code} | [EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.
[**get_compliance_rule**](ComplianceApi.md#get_compliance_rule) | **GET** /api/compliance/rules/{scope}/{code} | [EARLY ACCESS] GetComplianceRule: Get compliance rule.
[**get_compliance_run_summary**](ComplianceApi.md#get_compliance_run_summary) | **GET** /api/compliance/runs/summary/{scope}/{code} | [EARLY ACCESS] GetComplianceRunSummary: Get summary results for a specific compliance run.
[**get_compliance_template**](ComplianceApi.md#get_compliance_template) | **GET** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
[**list_compliance_rules**](ComplianceApi.md#list_compliance_rules) | **GET** /api/compliance/rules | [EARLY ACCESS] ListComplianceRules: List compliance rules.
[**list_compliance_runs**](ComplianceApi.md#list_compliance_runs) | **GET** /api/compliance/runs | [EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.
[**list_compliance_templates**](ComplianceApi.md#list_compliance_templates) | **GET** /api/compliance/templates | [EARLY ACCESS] ListComplianceTemplates: List compliance templates.
[**run_compliance**](ComplianceApi.md#run_compliance) | **POST** /api/compliance/runs | [EARLY ACCESS] RunCompliance: Run a compliance check.
[**upsert_compliance_rule**](ComplianceApi.md#upsert_compliance_rule) | **POST** /api/compliance/rules | [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.
[**upsert_compliance_run_summary**](ComplianceApi.md#upsert_compliance_run_summary) | **POST** /api/compliance/runs/summary | [EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.


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
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    scope = 'scope_example' # str | The compliance rule's scope.
code = 'code_example' # str | The compliance rule's code.

    try:
        # [EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.
        api_response = api_instance.delete_compliance_rule(scope, code)
        pprint(api_response)
    except ApiException as e:
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
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    scope = 'scope_example' # str | The compliance rule's scope.
code = 'code_example' # str | The compliance rule's code.
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Asat time for query. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'Compliance' domain to decorate onto the rule.              These must take the format {domain}/{scope}/{code}, for example 'Compliance/live/UCITS'. (optional)

    try:
        # [EARLY ACCESS] GetComplianceRule: Get compliance rule.
        api_response = api_instance.get_compliance_rule(scope, code, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->get_compliance_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule&#39;s scope. | 
 **code** | **str**| The compliance rule&#39;s code. | 
 **as_at** | **datetime**| Optional. Asat time for query. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;Compliance&#39; domain to decorate onto the rule.              These must take the format {domain}/{scope}/{code}, for example &#39;Compliance/live/UCITS&#39;. | [optional] 

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

# **get_compliance_run_summary**
> ComplianceRunSummary get_compliance_run_summary(scope, code)

[EARLY ACCESS] GetComplianceRunSummary: Get summary results for a specific compliance run.

Specify a run scope and code from a previously run compliance check to get summarised results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    scope = 'scope_example' # str | Required: Run Scope.
code = 'code_example' # str | Required: Run Code.

    try:
        # [EARLY ACCESS] GetComplianceRunSummary: Get summary results for a specific compliance run.
        api_response = api_instance.get_compliance_run_summary(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->get_compliance_run_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Required: Run Scope. | 
 **code** | **str**| Required: Run Code. | 

### Return type

[**ComplianceRunSummary**](ComplianceRunSummary.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The requested compliance run summary. |  -  |
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
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    scope = 'scope_example' # str | Scope of TemplateID
code = 'code_example' # str | Code of TemplateID
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)

    try:
        # [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
        api_response = api_instance.get_compliance_template(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
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
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Asat time. (optional)
page = 'page_example' # str | Optional. Pagination token. (optional)
limit = 56 # int | Optional. Entries per page. (optional)
filter = 'filter_example' # str | Optional. Filter. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'Compliance' domain to decorate onto each rule.              These must take the format {domain}/{scope}/{code}, for example 'Compliance/live/UCITS'. If not provided will return all the entitled properties for each rule. (optional)

    try:
        # [EARLY ACCESS] ListComplianceRules: List compliance rules.
        api_response = api_instance.list_compliance_rules(as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->list_compliance_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. Asat time. | [optional] 
 **page** | **str**| Optional. Pagination token. | [optional] 
 **limit** | **int**| Optional. Entries per page. | [optional] 
 **filter** | **str**| Optional. Filter. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;Compliance&#39; domain to decorate onto each rule.              These must take the format {domain}/{scope}/{code}, for example &#39;Compliance/live/UCITS&#39;. If not provided will return all the entitled properties for each rule. | [optional] 

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
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)
page = 'page_example' # str | Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. A list of field names to sort by, each suffixed by \"ASC\" or \"DESC\" (optional)

    try:
        # [EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.
        api_response = api_instance.list_compliance_runs(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->list_compliance_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 
 **page** | **str**| Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. A list of field names to sort by, each suffixed by \&quot;ASC\&quot; or \&quot;DESC\&quot; | [optional] 

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
> PagedResourceListOfComplianceTemplate list_compliance_templates(as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EARLY ACCESS] ListComplianceTemplates: List compliance templates.

Use this endpoint to fetch a list of all available compliance template ids, or a subset using a filter.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)
page = 'page_example' # str | Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | Optional. When paginating, skip this number of results. (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] ListComplianceTemplates: List compliance templates.
        api_response = api_instance.list_compliance_templates(as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->list_compliance_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 
 **page** | **str**| Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results. | [optional] 
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
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    run_scope = 'run_scope_example' # str | Required: Scope to save the run results in.
rule_scope = 'rule_scope_example' # str | Required: Scope from which to select rules to be run.
is_pre_trade = True # bool | Required: Boolean flag indicating if a run should be PreTrade (Including orders). For post-trade only, set to false
recipe_id_scope = 'recipe_id_scope_example' # str | Required: the scope of the recipe to be used
recipe_id_code = 'recipe_id_code_example' # str | Required: The code of the recipe to be used. If left blank, the default recipe will be used.

    try:
        # [EARLY ACCESS] RunCompliance: Run a compliance check.
        api_response = api_instance.run_compliance(run_scope, rule_scope, is_pre_trade, recipe_id_scope, recipe_id_code)
        pprint(api_response)
    except ApiException as e:
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
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    upsert_compliance_rule_request = {"id":{"scope":"live","code":"exampleRule"},"name":"A friendly name.","description":"A friendly description.","active":true,"templateId":{"scope":"system","code":"PortfolioLuidMetricCheck"},"variation":"standard","portfolioGroupId":{"scope":"examples","code":"examplePortfolioGroup"},"parameters":{"BoolParameter":{"value":true,"complianceParameterType":"BoolComplianceParameter"},"DecimalParameter":{"value":0,"complianceParameterType":"DecimalComplianceParameter"},"StringParameter":{"value":"An example string parameter","complianceParameterType":"StringComplianceParameter"},"DateTimeParameter":{"value":"2023-06-06T00:00:00.0000000+00:00","complianceParameterType":"DateTimeComplianceParameter"},"PropertyKeyParameter":{"value":"Compliance/live/RuleGroup","complianceParameterType":"PropertyKeyComplianceParameter"},"AddressKeyParameter":{"value":"Valuation/PvInReportCcy","complianceParameterType":"AddressKeyComplianceParameter"},"PortfolioIdParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PortfolioIdComplianceParameter"},"PortfolioGroupIdParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PortfolioGroupIdComplianceParameter"},"DecimalListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"DecimalListComplianceParameter"},"AddressKeyListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"AddressKeyListComplianceParameter"},"BoolListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"BoolListComplianceParameter"},"StringListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"StringListComplianceParameter"},"DateTimeListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"DateTimeListComplianceParameter"},"PropertyKeyListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PropertyKeyListComplianceParameter"},"PortfolioIdListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PortfolioIdListComplianceParameter"},"PortfolioGroupIdListParameter":{"value":{"scope":"testscope","code":"testcode"},"complianceParameterType":"PortfolioGroupIdListComplianceParameter"}},"properties":{"Compliance/MyScope/SomeRuleProperty":{"key":"Compliance/MyScope/SomeRuleProperty","value":{"labelValue":"XYZ000034567"}}}} # UpsertComplianceRuleRequest |  (optional)

    try:
        # [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.
        api_response = api_instance.upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request)
        pprint(api_response)
    except ApiException as e:
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
> ComplianceRunSummary upsert_compliance_run_summary(upsert_compliance_run_summary_request=upsert_compliance_run_summary_request)

[EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.

Use this endpoint to upsert a compliance run result summary.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    upsert_compliance_run_summary_request = {"runId":{"scope":"SomeScope","code":"run-1"},"instigatedAt":"2020-01-05T00:00:00.0000000+00:00","completedAt":"2020-01-05T00:00:01.0000000+00:00","schedule":"PreTrade","results":[{"ruleId":{"scope":"SomeScope","code":"rule-1"},"templateId":{"scope":"system","code":"template-1"},"variation":"standard","ruleStatus":"passed","affectedPortfolios":[{"scope":"PortfolioScope","code":"PortfolioCode"}],"affectedOrders":[{"scope":"OrderScope","code":"OrderCode"}],"ruleBreakdown":{"[LUID_ABC,LUID_ABC,PortfolioScope/PortfolioCode,ExcludeCash,Initial]":{"groupStatus":"failed","resultsUsed":{"Valuation/PV":650,"Exposure/PV":650},"propertiesUsed":{"Instrument/data/Issuer":[{"key":"Instrument/data/Issuer","value":{"labelValue":"ABC"}}]},"parametersUsed":{"UpperBound":"30","LowerBound":"0"},"missingDataInformation":["No Missing Data"]}}}]} # UpsertComplianceRunSummaryRequest |  (optional)

    try:
        # [EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.
        api_response = api_instance.upsert_compliance_run_summary(upsert_compliance_run_summary_request=upsert_compliance_run_summary_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->upsert_compliance_run_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_compliance_run_summary_request** | [**UpsertComplianceRunSummaryRequest**](UpsertComplianceRunSummaryRequest.md)|  | [optional] 

### Return type

[**ComplianceRunSummary**](ComplianceRunSummary.md)

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

