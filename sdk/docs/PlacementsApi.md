# lusid.PlacementsApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_placement**](PlacementsApi.md#delete_placement) | **DELETE** /api/placements/{scope}/{code} | [EARLY ACCESS] DeletePlacement: Delete placement
[**get_placement**](PlacementsApi.md#get_placement) | **GET** /api/placements/{scope}/{code} | [EARLY ACCESS] GetPlacement: Get Placement
[**list_placements**](PlacementsApi.md#list_placements) | **GET** /api/placements | [EARLY ACCESS] ListPlacements: List Placements
[**upsert_placements**](PlacementsApi.md#upsert_placements) | **POST** /api/placements | [EARLY ACCESS] UpsertPlacements: Upsert Placement


# **delete_placement**
> DeletedEntityResponse delete_placement(scope, code)

[EARLY ACCESS] DeletePlacement: Delete placement

Delete an placement. Deletion will be valid from the placement's creation datetime.  This means that the placement will no longer exist at any effective datetime from the asAt datetime of deletion.

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
    api_instance = lusid.PlacementsApi(api_client)
    scope = 'scope_example' # str | The placement scope.
    code = 'code_example' # str | The placement's code. This, together with the scope uniquely identifies the placement to delete.

    try:
        # [EARLY ACCESS] DeletePlacement: Delete placement
        api_response = await api_instance.delete_placement(scope, code)
        print("The response of PlacementsApi->delete_placement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementsApi->delete_placement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The placement scope. | 
 **code** | **str**| The placement&#39;s code. This, together with the scope uniquely identifies the placement to delete. | 

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
**200** | The response from deleting an placement. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_placement**
> Placement get_placement(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetPlacement: Get Placement

Fetch a Placement that matches the specified identifier

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
    api_instance = lusid.PlacementsApi(api_client)
    scope = 'scope_example' # str | The scope to which the placement belongs.
    code = 'code_example' # str | The placement's unique identifier.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the placement. Defaults to return the latest version of the placement if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Placement\" domain to decorate onto the placement.              These take the format {domain}/{scope}/{code} e.g. \"Placement/system/Name\". (optional)

    try:
        # [EARLY ACCESS] GetPlacement: Get Placement
        api_response = await api_instance.get_placement(scope, code, as_at=as_at, property_keys=property_keys)
        print("The response of PlacementsApi->get_placement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementsApi->get_placement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the placement belongs. | 
 **code** | **str**| The placement&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the placement. Defaults to return the latest version of the placement if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Placement\&quot; domain to decorate onto the placement.              These take the format {domain}/{scope}/{code} e.g. \&quot;Placement/system/Name\&quot;. | [optional] 

### Return type

[**Placement**](Placement.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The placement matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_placements**
> PagedResourceListOfPlacement list_placements(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListPlacements: List Placements

Fetch the last pre-AsAt date version of each placement in scope (does not fetch the entire history).

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
    api_instance = lusid.PlacementsApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the placement. Defaults to return the latest version of the placement if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing placements from a previous call to list placements.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Placement\" domain to decorate onto each placement.                  These take the format {domain}/{scope}/{code} e.g. \"Placement/system/Name\". (optional)

    try:
        # [EARLY ACCESS] ListPlacements: List Placements
        api_response = await api_instance.list_placements(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        print("The response of PlacementsApi->list_placements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementsApi->list_placements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the placement. Defaults to return the latest version of the placement if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing placements from a previous call to list placements.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Placement\&quot; domain to decorate onto each placement.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Placement/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfPlacement**](PagedResourceListOfPlacement.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Placements in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_placements**
> ResourceListOfPlacement upsert_placements(placement_set_request=placement_set_request)

[EARLY ACCESS] UpsertPlacements: Upsert Placement

Upsert; update existing placements with given ids, or create new placements otherwise.

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
    api_instance = lusid.PlacementsApi(api_client)
    placement_set_request = {"requests":[{"id":{"scope":"MyScope","code":"PLAC00000123"},"blockIds":[{"scope":"MyScope","code":"BLOCK00000123"}],"properties":{"Placement/MyScope/SomePlacementProperty":{"key":"Placement/MyScope/SomePlacementProperty","value":{"labelValue":"XYZ000034567"}}},"instrumentIdentifiers":{"Instrument/default/Currency":"GBP"},"quantity":100,"state":"New","side":"Buy","timeInForce":"GoodTilCancel","type":"Limit","createdDate":"2006-04-11T00:00:00.0000000+00:00","limitPrice":{"amount":12413.33,"currency":"USD"},"stopPrice":{"amount":124335.33,"currency":"USD"},"counterparty":"SomeCounterparty"}]} # PlacementSetRequest | The collection of placement requests. (optional)

    try:
        # [EARLY ACCESS] UpsertPlacements: Upsert Placement
        api_response = await api_instance.upsert_placements(placement_set_request=placement_set_request)
        print("The response of PlacementsApi->upsert_placements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlacementsApi->upsert_placements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_set_request** | [**PlacementSetRequest**](PlacementSetRequest.md)| The collection of placement requests. | [optional] 

### Return type

[**ResourceListOfPlacement**](ResourceListOfPlacement.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of placements. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

