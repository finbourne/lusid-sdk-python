# lusid.StructuredResultDataApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_key_definitions_for_document**](StructuredResultDataApi.md#get_address_key_definitions_for_document) | **GET** /api/unitresults/virtualdocument/{scope}/{code}/{source}/{resultType}/addresskeydefinitions | [EARLY ACCESS] GetAddressKeyDefinitionsForDocument: Get AddressKeyDefinitions for a virtual document.


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
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
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

