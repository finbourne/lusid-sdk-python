# lusid.StructuredResultDataApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_key_definitions_for_document**](StructuredResultDataApi.md#get_address_key_definitions_for_document) | **GET** /api/unitresults/virtualdocument/{scope}/{code}/{source}/{resultType}/addresskeydefinitions | [EARLY ACCESS] GetAddressKeyDefinitionsForDocument: Get AddressKeyDefinitions for a virtual document.
[**get_virtual_document_rows**](StructuredResultDataApi.md#get_virtual_document_rows) | **GET** /api/unitresults/virtualdocument/{scope}/{code}/{source}/{resultType} | [EARLY ACCESS] GetVirtualDocumentRows: Get Virtual Document Rows


# **get_address_key_definitions_for_document**
> ResourceListOfAddressKeyDefinition get_address_key_definitions_for_document(scope, code, source, result_type, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetAddressKeyDefinitionsForDocument: Get AddressKeyDefinitions for a virtual document.

For a given virtual document retrieve all the address key definitions that are in use.

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
    api_instance = lusid.StructuredResultDataApi(api_client)
    scope = 'scope_example' # str | The scope of the document for which address key definitions are retrieved.
code = 'code_example' # str | The code of the document for which address key definitions are retrieved.
source = 'source_example' # str | The source of the document for which address key definitions are retrieved.
result_type = 'result_type_example' # str | The result type of the document for which address key definitions are retrieved.
effective_at = 'effective_at_example' # str | The effective datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified. (optional)

    try:
        # [EARLY ACCESS] GetAddressKeyDefinitionsForDocument: Get AddressKeyDefinitions for a virtual document.
        api_response = api_instance.get_address_key_definitions_for_document(scope, code, source, result_type, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StructuredResultDataApi->get_address_key_definitions_for_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the document for which address key definitions are retrieved. | 
 **code** | **str**| The code of the document for which address key definitions are retrieved. | 
 **source** | **str**| The source of the document for which address key definitions are retrieved. | 
 **result_type** | **str**| The result type of the document for which address key definitions are retrieved. | 
 **effective_at** | **str**| The effective datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfAddressKeyDefinition**](ResourceListOfAddressKeyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of address key definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_document_rows**
> PagedResourceListOfVirtualRow get_virtual_document_rows(scope, code, source, result_type, effective_at, as_at=as_at, page=page, limit=limit, filter=filter)

[EARLY ACCESS] GetVirtualDocumentRows: Get Virtual Document Rows

Retrieve the rows of the virtual document with the specified identifiers and the given effectiveAt date time.    Get virtual document rows merges multiple StructuredResultData items upserted with UpsertStructuredResultData  for a single StructuredResultDataId.                Since an item of StructuredResultData is always upserted with a StructuredResultDataId, of which  effectiveAt is a part, then merging across the asAt dimension is supported but not merging across the  effectiveAt dimension.

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
    api_instance = lusid.StructuredResultDataApi(api_client)
    scope = 'scope_example' # str | The scope in which to retrieve the virtual document.
code = 'code_example' # str | The code of the virtual document to retrieve.
source = 'source_example' # str | The source of the virtual document to retrieve.
result_type = 'result_type_example' # str | The result type of the virtual document to retrieve.
effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the virtual document.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the virtual document. Defaults to returning the latest version if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing virtual document rows from a previous               call to list virtual document rows. This value is returned from the previous call. If a pagination token is               provided the filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:               https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] GetVirtualDocumentRows: Get Virtual Document Rows
        api_response = api_instance.get_virtual_document_rows(scope, code, source, result_type, effective_at, as_at=as_at, page=page, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StructuredResultDataApi->get_virtual_document_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to retrieve the virtual document. | 
 **code** | **str**| The code of the virtual document to retrieve. | 
 **source** | **str**| The source of the virtual document to retrieve. | 
 **result_type** | **str**| The result type of the virtual document to retrieve. | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the virtual document. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the virtual document. Defaults to returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing virtual document rows from a previous               call to list virtual document rows. This value is returned from the previous call. If a pagination token is               provided the filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:               https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfVirtualRow**](PagedResourceListOfVirtualRow.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rows of the virtual document. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

