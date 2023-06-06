# lusid.StructuredResultDataApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_map**](StructuredResultDataApi.md#create_data_map) | **POST** /api/unitresults/datamap/{scope} | [EXPERIMENTAL] CreateDataMap: Create data map
[**delete_structured_result_data**](StructuredResultDataApi.md#delete_structured_result_data) | **POST** /api/unitresults/{scope}/$delete | [EXPERIMENTAL] DeleteStructuredResultData: Delete structured result data
[**get_data_map**](StructuredResultDataApi.md#get_data_map) | **POST** /api/unitresults/datamap/{scope}/$get | [EXPERIMENTAL] GetDataMap: Get data map
[**get_structured_result_data**](StructuredResultDataApi.md#get_structured_result_data) | **POST** /api/unitresults/{scope}/$get | [EXPERIMENTAL] GetStructuredResultData: Get structured result data
[**get_virtual_document**](StructuredResultDataApi.md#get_virtual_document) | **POST** /api/unitresults/virtualdocument/{scope}/$get | [EXPERIMENTAL] GetVirtualDocument: Get Virtual Documents
[**upsert_result_value**](StructuredResultDataApi.md#upsert_result_value) | **POST** /api/unitresults/resultvalue/{scope} | [EXPERIMENTAL] UpsertResultValue: Upsert result value
[**upsert_structured_result_data**](StructuredResultDataApi.md#upsert_structured_result_data) | **POST** /api/unitresults/{scope} | [BETA] UpsertStructuredResultData: Upsert structured result data


# **create_data_map**
> UpsertStructuredDataResponse create_data_map(scope, request_body)

[EXPERIMENTAL] CreateDataMap: Create data map

Create or update one or more structured result store address definition data maps in a particular scope. Note these are immutable and cannot be changed once created.                In the request, each data map must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data map object in the response.                The response returns both the collection of successfully created or updated data maps, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

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
    api_instance = lusid.StructuredResultDataApi(api_client)
    scope = 'scope_example' # str | The scope in which to create or update data maps.
    request_body = {} # Dict[str, CreateDataMapRequest] | Individual data map creation requests.

    try:
        # [EXPERIMENTAL] CreateDataMap: Create data map
        api_response = await api_instance.create_data_map(scope, request_body)
        print("The response of StructuredResultDataApi->create_data_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructuredResultDataApi->create_data_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create or update data maps. | 
 **request_body** | [**Dict[str, CreateDataMapRequest]**](CreateDataMapRequest.md)| Individual data map creation requests. | 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created or updated data maps along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_structured_result_data**
> AnnulStructuredDataResponse delete_structured_result_data(scope, request_body)

[EXPERIMENTAL] DeleteStructuredResultData: Delete structured result data

Delete one or more structured result data items from a particular scope. Each item is identified by a unique ID which includes  information about its type as well as the exact effective datetime (to the microsecond) at which it entered the system (became valid).                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns both the collection of successfully deleted data items, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

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
    api_instance = lusid.StructuredResultDataApi(api_client)
    scope = 'scope_example' # str | The scope from which to delete data items.
    request_body = {"SomeCorrelationId1":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"}} # Dict[str, StructuredResultDataId] | The data IDs to delete, each keyed by a unique, ephemeral correlation ID.

    try:
        # [EXPERIMENTAL] DeleteStructuredResultData: Delete structured result data
        api_response = await api_instance.delete_structured_result_data(scope, request_body)
        print("The response of StructuredResultDataApi->delete_structured_result_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructuredResultDataApi->delete_structured_result_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope from which to delete data items. | 
 **request_body** | [**Dict[str, StructuredResultDataId]**](StructuredResultDataId.md)| The data IDs to delete, each keyed by a unique, ephemeral correlation ID. | 

### Return type

[**AnnulStructuredDataResponse**](AnnulStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully deleted data items along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_map**
> GetDataMapResponse get_data_map(scope, request_body)

[EXPERIMENTAL] GetDataMap: Get data map

Retrieve one or more structured result store address definition data maps from a particular scope.                Each data map can be identified by its invariant key, which can be thought of as a permanent URL.  For each ID, LUSID returns the most recently matched item.                In the request, each data map must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data map in the response.                The response returns three collections. The first contains successfully retrieved data maps. The second contains those with a  valid identifier but that could not be found. The third contains those that failed because LUSID could not construct a valid identifier from the request.                For the IDs that failed to resolve or could not be found, a reason is provided.                It is important to check the failed sets for any unsuccessful results.

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
    api_instance = lusid.StructuredResultDataApi(api_client)
    scope = 'scope_example' # str | The scope from which to retrieve data maps.
    request_body = {} # Dict[str, DataMapKey] | The data map keys to look up, each keyed by a unique, ephemeral correlation ID.

    try:
        # [EXPERIMENTAL] GetDataMap: Get data map
        api_response = await api_instance.get_data_map(scope, request_body)
        print("The response of StructuredResultDataApi->get_data_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructuredResultDataApi->get_data_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope from which to retrieve data maps. | 
 **request_body** | [**Dict[str, DataMapKey]**](DataMapKey.md)| The data map keys to look up, each keyed by a unique, ephemeral correlation ID. | 

### Return type

[**GetDataMapResponse**](GetDataMapResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved data maps along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_structured_result_data**
> GetStructuredResultDataResponse get_structured_result_data(scope, request_body, as_at=as_at, max_age=max_age)

[EXPERIMENTAL] GetStructuredResultData: Get structured result data

Retrieve one or more structured result data items from a particular scope.                Each item can be identified by its time invariant structured result data identifier. For each ID, LUSID  returns the most recently matched item with respect to the provided (or default) effective datetime.                 An optional maximum age range window can be specified to control how far back to look from the specified  effective datetime. LUSID returns the most recent item within this window.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.    The response returns three collections. The first contains successfully retrieved data items. The second contains those with a  valid identifier but that could not be found. The third contains those that failed because LUSID could not construct a valid identifier from the request.    For the IDs that failed to resolve or could not be found, a reason is provided.                It is important to check the failed sets for any unsuccessful results.

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
    api_instance = lusid.StructuredResultDataApi(api_client)
    scope = 'scope_example' # str | The scope from which to retrieve data items.
    request_body = {"SomeCorrelationId1":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"}} # Dict[str, StructuredResultDataId] | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified. (optional)
    max_age = 'max_age_example' # str | The duration of the look-back window in ISO8601 time interval format, for example 'P1Y2M3DT4H30M' (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a data item must exist to be retrieved. (optional)

    try:
        # [EXPERIMENTAL] GetStructuredResultData: Get structured result data
        api_response = await api_instance.get_structured_result_data(scope, request_body, as_at=as_at, max_age=max_age)
        print("The response of StructuredResultDataApi->get_structured_result_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructuredResultDataApi->get_structured_result_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope from which to retrieve data items. | 
 **request_body** | [**Dict[str, StructuredResultDataId]**](StructuredResultDataId.md)| The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified. | [optional] 
 **max_age** | **str**| The duration of the look-back window in ISO8601 time interval format, for example &#39;P1Y2M3DT4H30M&#39; (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a data item must exist to be retrieved. | [optional] 

### Return type

[**GetStructuredResultDataResponse**](GetStructuredResultDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved data items along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_document**
> GetVirtualDocumentResponse get_virtual_document(scope, request_body, as_at=as_at)

[EXPERIMENTAL] GetVirtualDocument: Get Virtual Documents

Retrieve one or more virtual documents from a particular scope.                Each item can be identified by its time invariant structured result data identifier. For each ID, LUSID  returns the most recently matched item with respect to the provided effective datetime.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns two collections. The first contains successfully retrieved data items. The second contains those with a  valid identifier but that could not be found, or those that failed because LUSID could not construct a valid identifier from the request.                For the IDs that failed to resolve or could not be found, a reason is provided.                It is important to check the failed sets for any unsuccessful results.

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
    api_instance = lusid.StructuredResultDataApi(api_client)
    scope = 'scope_example' # str | The scope in which to construct the virtual documents.
    request_body = {"SomeCorrelationId1":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"}} # Dict[str, StructuredResultDataId] | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetVirtualDocument: Get Virtual Documents
        api_response = await api_instance.get_virtual_document(scope, request_body, as_at=as_at)
        print("The response of StructuredResultDataApi->get_virtual_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructuredResultDataApi->get_virtual_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to construct the virtual documents. | 
 **request_body** | [**Dict[str, StructuredResultDataId]**](StructuredResultDataId.md)| The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**GetVirtualDocumentResponse**](GetVirtualDocumentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved virtual documents along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_result_value**
> UpsertStructuredDataResponse upsert_result_value(scope, request_body)

[EXPERIMENTAL] UpsertResultValue: Upsert result value

Create or update one or more Upsert one or more result values in a particular scope. An item is updated if it already exists  and created if it does not.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns both the collection of successfully created or updated data items, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

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
    api_instance = lusid.StructuredResultDataApi(api_client)
    scope = 'scope_example' # str | The scope in which to construct the virtual documents.
    request_body = {"SomeCorrelationId1":{"documentId":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"UnitResult/Analytic"},"key":{"UnitResult/LusidInstrumentId":"LUID_0000ABCD"},"dataAddress":"UnitResult/Valuation/InstrumentAccrued","resultValue":{"units":"USD","value":0.0102,"dimension":0,"resultValueType":"ResultValue0D"}}} # Dict[str, UpsertResultValuesDataRequest] | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.

    try:
        # [EXPERIMENTAL] UpsertResultValue: Upsert result value
        api_response = await api_instance.upsert_result_value(scope, request_body)
        print("The response of StructuredResultDataApi->upsert_result_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructuredResultDataApi->upsert_result_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to construct the virtual documents. | 
 **request_body** | [**Dict[str, UpsertResultValuesDataRequest]**](UpsertResultValuesDataRequest.md)| The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved virtual documents along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_structured_result_data**
> UpsertStructuredDataResponse upsert_structured_result_data(scope, request_body)

[BETA] UpsertStructuredResultData: Upsert structured result data

Create or update one or more structured result data items in a particular scope. An item is updated if it already exists  and created if it does not.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns both the collection of successfully created or updated data items, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

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
    api_instance = lusid.StructuredResultDataApi(api_client)
    scope = 'scope_example' # str | The scope in which to create or update data items.
    request_body = {"first-item":{"id":{"source":"Client","code":"MyUploadedRiskResults-1","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"},"data":{"documentFormat":"Xml","version":"1.0.0","name":"free text identifier of document 1","document":"<xml>data</xml>"}},"second-item":{"id":{"source":"Client","code":"MyUploadedRiskResults-2","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"},"data":{"documentFormat":"Json","version":"1.0.0","name":"free text identifier of document 2","document":"{ \"some\":\"valid json\"}"}}} # Dict[str, UpsertStructuredResultDataRequest] | The set of data items to create or update, keyed by a unique, ephemeral correlation ID.

    try:
        # [BETA] UpsertStructuredResultData: Upsert structured result data
        api_response = await api_instance.upsert_structured_result_data(scope, request_body)
        print("The response of StructuredResultDataApi->upsert_structured_result_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructuredResultDataApi->upsert_structured_result_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create or update data items. | 
 **request_body** | [**Dict[str, UpsertStructuredResultDataRequest]**](UpsertStructuredResultDataRequest.md)| The set of data items to create or update, keyed by a unique, ephemeral correlation ID. | 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created or updated data items along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

