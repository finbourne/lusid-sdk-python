# lusid.BlocksApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_block**](BlocksApi.md#delete_block) | **DELETE** /api/blocks/{scope}/{code} | [EARLY ACCESS] DeleteBlock: Delete block
[**get_block**](BlocksApi.md#get_block) | **GET** /api/blocks/{scope}/{code} | [EARLY ACCESS] GetBlock: Get Block
[**list_blocks**](BlocksApi.md#list_blocks) | **GET** /api/blocks | [EARLY ACCESS] ListBlocks: List Blocks
[**upsert_blocks**](BlocksApi.md#upsert_blocks) | **POST** /api/blocks | [EARLY ACCESS] UpsertBlocks: Upsert Block


# **delete_block**
> DeletedEntityResponse delete_block(scope, code)

[EARLY ACCESS] DeleteBlock: Delete block

Delete an block. Deletion will be valid from the block's creation datetime.  This means that the block will no longer exist at any effective datetime from the asAt datetime of deletion.

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
    api_instance = lusid.BlocksApi(api_client)
    scope = 'scope_example' # str | The block scope.
code = 'code_example' # str | The block's code. This, together with the scope uniquely identifies the block to delete.

    try:
        # [EARLY ACCESS] DeleteBlock: Delete block
        api_response = api_instance.delete_block(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlocksApi->delete_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The block scope. | 
 **code** | **str**| The block&#39;s code. This, together with the scope uniquely identifies the block to delete. | 

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
**200** | The response from deleting an block. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block**
> Block get_block(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetBlock: Get Block

Fetch a Block that matches the specified identifier

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
    api_instance = lusid.BlocksApi(api_client)
    scope = 'scope_example' # str | The scope to which the block belongs.
code = 'code_example' # str | The block's unique identifier.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the block. Defaults to return the latest version of the block if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Block\" domain to decorate onto the block.              These take the format {domain}/{scope}/{code} e.g. \"Block/system/Name\". (optional)

    try:
        # [EARLY ACCESS] GetBlock: Get Block
        api_response = api_instance.get_block(scope, code, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlocksApi->get_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the block belongs. | 
 **code** | **str**| The block&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the block. Defaults to return the latest version of the block if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Block\&quot; domain to decorate onto the block.              These take the format {domain}/{scope}/{code} e.g. \&quot;Block/system/Name\&quot;. | [optional] 

### Return type

[**Block**](Block.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The block matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blocks**
> PagedResourceListOfBlock list_blocks(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListBlocks: List Blocks

Fetch the last pre-AsAt date version of each block in scope (does not fetch the entire history).

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
    api_instance = lusid.BlocksApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the block. Defaults to return the latest version of the block if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing blocks from a previous call to list blocks.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Block\" domain to decorate onto each block.                  These take the format {domain}/{scope}/{code} e.g. \"Block/system/Name\". (optional)

    try:
        # [EARLY ACCESS] ListBlocks: List Blocks
        api_response = api_instance.list_blocks(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlocksApi->list_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the block. Defaults to return the latest version of the block if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing blocks from a previous call to list blocks.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Block\&quot; domain to decorate onto each block.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Block/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfBlock**](PagedResourceListOfBlock.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Blocks in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_blocks**
> ResourceListOfBlock upsert_blocks(block_set_request=block_set_request)

[EARLY ACCESS] UpsertBlocks: Upsert Block

Upsert; update existing blocks with given ids, or create new blocks otherwise.

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
    api_instance = lusid.BlocksApi(api_client)
    block_set_request = {"requests":[{"id":{"scope":"MyScope","code":"BLOC00000123"},"orderIds":[{"scope":"MyScope","code":"BLOC00000123"}],"properties":{"block/MyScope/SomeBlockProperty":{"key":"Block/MyScope/SomeBlockProperty","value":{"labelValue":"XYZ000034567"}}},"instrumentIdentifiers":{"instrument/default/Currency":"GBP"},"quantity":100,"side":"Buy","type":"Limit","timeInForce":"GoodTilCancel","createdDate":"2006-04-11T00:00:00.0000000+00:00","limitPrice":{"amount":12413.33,"currency":"USD"},"stopPrice":{"amount":122345.33,"currency":"USD"}}]} # BlockSetRequest | The collection of block requests. (optional)

    try:
        # [EARLY ACCESS] UpsertBlocks: Upsert Block
        api_response = api_instance.upsert_blocks(block_set_request=block_set_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlocksApi->upsert_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_set_request** | [**BlockSetRequest**](BlockSetRequest.md)| The collection of block requests. | [optional] 

### Return type

[**ResourceListOfBlock**](ResourceListOfBlock.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of blocks. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

