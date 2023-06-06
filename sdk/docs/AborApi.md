# lusid.AborApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_abor**](AborApi.md#create_abor) | **POST** /api/abor/{scope} | [EXPERIMENTAL] CreateAbor: Create an Abor.
[**delete_abor**](AborApi.md#delete_abor) | **DELETE** /api/abor/{scope}/{code} | [EXPERIMENTAL] DeleteAbor: Delete an Abor.
[**get_abor**](AborApi.md#get_abor) | **GET** /api/abor/{scope}/{code} | [EXPERIMENTAL] GetAbor: Get Abor.
[**get_je_lines**](AborApi.md#get_je_lines) | **POST** /api/abor/{scope}/{code}/JELines/$query | [EXPERIMENTAL] GetJELines: Get the JELines for the given Abor.
[**list_abors**](AborApi.md#list_abors) | **GET** /api/abor | [EXPERIMENTAL] ListAbors: List Abors.
[**upsert_abor_properties**](AborApi.md#upsert_abor_properties) | **POST** /api/abor/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertAborProperties: Upsert Abor properties


# **create_abor**
> Abor create_abor(scope, abor_request)

[EXPERIMENTAL] CreateAbor: Create an Abor.

Create the given Abor.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AborApi(api_client)
    scope = 'scope_example' # str | The scope of the Abor.
    abor_request = {"code":"AborCode","portfolioIds":[{"scope":"portfolioScope","code":"portfolioCode","portfolioEntityType":"SinglePortfolio"}],"description":"Standard Abor","aborConfig":{"scope":"ConfigScope","code":"ConfigCode"},"properties":{"Abor/MyScope/FundManagerName":{"key":"Abor/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2020-03-05T00:00:00.0000000+00:00"}}} # AborRequest | The definition of the Abor.

    try:
        # [EXPERIMENTAL] CreateAbor: Create an Abor.
        api_response = await api_instance.create_abor(scope, abor_request)
        print("The response of AborApi->create_abor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->create_abor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **abor_request** | [**AborRequest**](AborRequest.md)| The definition of the Abor. | 

### Return type

[**Abor**](Abor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created abor. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_abor**
> DeletedEntityResponse delete_abor(scope, code)

[EXPERIMENTAL] DeleteAbor: Delete an Abor.

Delete the given Abor.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AborApi(api_client)
    scope = 'scope_example' # str | The scope of the Abor to be deleted.
    code = 'code_example' # str | The code of the Abor to be deleted. Together with the scope this uniquely identifies the Abor.

    try:
        # [EXPERIMENTAL] DeleteAbor: Delete an Abor.
        api_response = await api_instance.delete_abor(scope, code)
        print("The response of AborApi->delete_abor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->delete_abor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor to be deleted. | 
 **code** | **str**| The code of the Abor to be deleted. Together with the scope this uniquely identifies the Abor. | 

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
**200** | The datetime that the Abor was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_abor**
> Abor get_abor(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetAbor: Get Abor.

Retrieve the definition of a particular Abor.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AborApi(api_client)
    scope = 'scope_example' # str | The scope of the Abor.
    code = 'code_example' # str | The code of the Abor. Together with the scope this uniquely identifies the Abor.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Abor properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Abor definition. Defaults to returning the latest version of the Abor definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Abor' domain to decorate onto the Abor.              These must take the format {domain}/{scope}/{code}, for example 'Abor/Manager/Id'. If not provided will return all the entitled properties for that Abor. (optional)

    try:
        # [EXPERIMENTAL] GetAbor: Get Abor.
        api_response = await api_instance.get_abor(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        print("The response of AborApi->get_abor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->get_abor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. Together with the scope this uniquely identifies the Abor. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Abor properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Abor definition. Defaults to returning the latest version of the Abor definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Abor&#39; domain to decorate onto the Abor.              These must take the format {domain}/{scope}/{code}, for example &#39;Abor/Manager/Id&#39;. If not provided will return all the entitled properties for that Abor. | [optional] 

### Return type

[**Abor**](Abor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Abor definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_je_lines**
> VersionedResourceListOfJELines get_je_lines(scope, code, je_lines_query_parameters, as_at=as_at, limit=limit, page=page)

[EXPERIMENTAL] GetJELines: Get the JELines for the given Abor.

Gets the JELines for the given Abor                The JE Lines have been generated from transactions and translated via posting rules

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AborApi(api_client)
    scope = 'scope_example' # str | The scope of the Abor.
    code = 'code_example' # str | The code of the Abor. Together with the scope is creating the unique identifier for the given Abor.
    je_lines_query_parameters = {"startDate":"2018-03-05T00:00:00.0000000+00:00","endDate":"2018-03-19T00:00:00.0000000+00:00","propertyKeys":[]} # JELinesQueryParameters | The query parameters used in running the generation of the JELines.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve JELines. Defaults to returning the latest version               of each transaction if not specified. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing JELines from a previous call to GetJELines. (optional)

    try:
        # [EXPERIMENTAL] GetJELines: Get the JELines for the given Abor.
        api_response = await api_instance.get_je_lines(scope, code, je_lines_query_parameters, as_at=as_at, limit=limit, page=page)
        print("The response of AborApi->get_je_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->get_je_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. Together with the scope is creating the unique identifier for the given Abor. | 
 **je_lines_query_parameters** | [**JELinesQueryParameters**](JELinesQueryParameters.md)| The query parameters used in running the generation of the JELines. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve JELines. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing JELines from a previous call to GetJELines. | [optional] 

### Return type

[**VersionedResourceListOfJELines**](VersionedResourceListOfJELines.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested JELines for the specified Abor. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_abors**
> PagedResourceListOfAbor list_abors(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListAbors: List Abors.

List all the Abors matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AborApi(api_client)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the Abor. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Abor. Defaults to returning the latest version of each Abor if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Abor; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Abor type, specify \"id.Code eq 'Abor1'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Abor' domain to decorate onto each Abor.              These must take the format {domain}/{scope}/{code}, for example 'Abor/Manager/Id'. (optional)

    try:
        # [EXPERIMENTAL] ListAbors: List Abors.
        api_response = await api_instance.list_abors(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)
        print("The response of AborApi->list_abors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->list_abors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Abor. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Abor. Defaults to returning the latest version of each Abor if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Abor; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Abor type, specify \&quot;id.Code eq &#39;Abor1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Abor&#39; domain to decorate onto each Abor.              These must take the format {domain}/{scope}/{code}, for example &#39;Abor/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfAbor**](PagedResourceListOfAbor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested abors. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_abor_properties**
> AborProperties upsert_abor_properties(scope, code, request_body=request_body)

[EXPERIMENTAL] UpsertAborProperties: Upsert Abor properties

Update or insert one or more properties onto a single Abor. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Abor'.                Upserting a property that exists for an Abor, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AborApi(api_client)
    scope = 'scope_example' # str | The scope of the Abor to update or insert the properties onto.
    code = 'code_example' # str | The code of the Abor to update or insert the properties onto. Together with the scope this uniquely identifies the Abor.
    request_body = {"Abor/MyScope/FundManagerName":{"key":"Abor/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Abor/MyScope/SomeProperty":{"key":"Abor/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Abor/MyScope/AnotherProperty":{"key":"Abor/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Abor/MyScope/ReBalanceInterval":{"key":"Abor/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be updated or inserted onto the chart of account. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"Abor/Manager/Id\". (optional)

    try:
        # [EXPERIMENTAL] UpsertAborProperties: Upsert Abor properties
        api_response = await api_instance.upsert_abor_properties(scope, code, request_body=request_body)
        print("The response of AborApi->upsert_abor_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->upsert_abor_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor to update or insert the properties onto. | 
 **code** | **str**| The code of the Abor to update or insert the properties onto. Together with the scope this uniquely identifies the Abor. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the chart of account. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Abor/Manager/Id\&quot;. | [optional] 

### Return type

[**AborProperties**](AborProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

