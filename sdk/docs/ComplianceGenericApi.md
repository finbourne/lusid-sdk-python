# lusid.ComplianceGenericApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_compliance_rule2**](ComplianceGenericApi.md#delete_compliance_rule2) | **DELETE** /api/compliance/generic/rules/{scope}/{code} | [EARLY ACCESS] DeleteComplianceRule2: Get compliance rule.
[**get_compliance_rule2**](ComplianceGenericApi.md#get_compliance_rule2) | **GET** /api/compliance/generic/rules/{scope}/{code} | [EARLY ACCESS] GetComplianceRule2: Get compliance rule.
[**get_compliance_template**](ComplianceGenericApi.md#get_compliance_template) | **GET** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
[**list_compliance_rules2**](ComplianceGenericApi.md#list_compliance_rules2) | **GET** /api/compliance/generic/rules | [EARLY ACCESS] ListComplianceRules2: List compliance rules.
[**list_compliance_templates**](ComplianceGenericApi.md#list_compliance_templates) | **GET** /api/compliance/templates | [EARLY ACCESS] ListComplianceTemplates: Get a specific compliance template
[**upsert_compliance_rule**](ComplianceGenericApi.md#upsert_compliance_rule) | **POST** /api/compliance/generic/rules | [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.


# **delete_compliance_rule2**
> DeletedEntityResponse delete_compliance_rule2(scope, code)

[EARLY ACCESS] DeleteComplianceRule2: Get compliance rule.

PLEASE NOTE: loopback EarlyAccess endpoint for discussion only.

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
    api_instance = lusid.ComplianceGenericApi(api_client)
    scope = 'scope_example' # str | The compliance rule's scope.
code = 'code_example' # str | The compliance rule's code.

    try:
        # [EARLY ACCESS] DeleteComplianceRule2: Get compliance rule.
        api_response = api_instance.delete_compliance_rule2(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceGenericApi->delete_compliance_rule2: %s\n" % e)
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

# **get_compliance_rule2**
> ComplianceRuleResponse get_compliance_rule2(scope, code, as_at=as_at)

[EARLY ACCESS] GetComplianceRule2: Get compliance rule.

PLEASE NOTE: loopback EarlyAccess endpoint for discussion only.

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
    api_instance = lusid.ComplianceGenericApi(api_client)
    scope = 'scope_example' # str | The compliance rule's scope.
code = 'code_example' # str | The compliance rule's code.
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Asat time for query. (optional)

    try:
        # [EARLY ACCESS] GetComplianceRule2: Get compliance rule.
        api_response = api_instance.get_compliance_rule2(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceGenericApi->get_compliance_rule2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule&#39;s scope. | 
 **code** | **str**| The compliance rule&#39;s code. | 
 **as_at** | **datetime**| Optional. Asat time for query. | [optional] 

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
    api_instance = lusid.ComplianceGenericApi(api_client)
    scope = 'scope_example' # str | Scope of TemplateID
code = 'code_example' # str | Code of TemplateID
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)

    try:
        # [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
        api_response = api_instance.get_compliance_template(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceGenericApi->get_compliance_template: %s\n" % e)
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

# **list_compliance_rules2**
> PagedResourceListOfComplianceRuleResponse list_compliance_rules2(as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EARLY ACCESS] ListComplianceRules2: List compliance rules.

PLEASE NOTE: loopback EarlyAccess endpoint for discussion only.

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
    api_instance = lusid.ComplianceGenericApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Asat time. (optional)
page = 'page_example' # str | Optional. Pagination token. (optional)
start = 56 # int | Optional. Entry at which to start. (optional)
limit = 56 # int | Optional. Entries per page. (optional)
filter = 'filter_example' # str | Optional. Filter. (optional)

    try:
        # [EARLY ACCESS] ListComplianceRules2: List compliance rules.
        api_response = api_instance.list_compliance_rules2(as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceGenericApi->list_compliance_rules2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. Asat time. | [optional] 
 **page** | **str**| Optional. Pagination token. | [optional] 
 **start** | **int**| Optional. Entry at which to start. | [optional] 
 **limit** | **int**| Optional. Entries per page. | [optional] 
 **filter** | **str**| Optional. Filter. | [optional] 

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

# **list_compliance_templates**
> PagedResourceListOfComplianceTemplate list_compliance_templates(as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EARLY ACCESS] ListComplianceTemplates: Get a specific compliance template

Use this endpoint to fetch a list of all available compliance template ids.

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
    api_instance = lusid.ComplianceGenericApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)
page = 'page_example' # str | Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | Optional. When paginating, skip this number of results. (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] ListComplianceTemplates: Get a specific compliance template
        api_response = api_instance.list_compliance_templates(as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceGenericApi->list_compliance_templates: %s\n" % e)
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

# **upsert_compliance_rule**
> ComplianceRuleResponse upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request)

[EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.

PLEASE NOTE: loopback EarlyAccess endpoint for discussion only.

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
    api_instance = lusid.ComplianceGenericApi(api_client)
    upsert_compliance_rule_request = {"id":{"scope":"live","code":"exampleRule"},"name":"A friendly name.","description":"A friendly description.","active":true,"templateId":{"scope":"live","code":"exampleTemplate"},"variation":"Single","parameters":{"UpperBound":{"parameterType":"Decimal","value":15}},"properties":{"Compliance/MyScope/SomeRuleProperty":{"key":"Compliance/MyScope/SomeRuleProperty","value":{"labelValue":"XYZ000034567"}}}} # UpsertComplianceRuleRequest |  (optional)

    try:
        # [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.
        api_response = api_instance.upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceGenericApi->upsert_compliance_rule: %s\n" % e)
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

