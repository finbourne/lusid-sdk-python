# lusid.PlacementsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_placement**](PlacementsApi.md#delete_placement) | **DELETE** /api/placements/{scope}/{code} | [EARLY ACCESS] DeletePlacement: Delete placement
[**get_placement**](PlacementsApi.md#get_placement) | **GET** /api/placements/{scope}/{code} | [EARLY ACCESS] GetPlacement: Get Placement
[**list_placements**](PlacementsApi.md#list_placements) | **GET** /api/placements | [EARLY ACCESS] ListPlacements: List Placements
[**upsert_placements**](PlacementsApi.md#upsert_placements) | **POST** /api/placements | [EARLY ACCESS] UpsertPlacements: Upsert Placement


# **delete_placement**
> DeletedEntityResponse delete_placement(scope, code)

[EARLY ACCESS] DeletePlacement: Delete placement

Delete an placement. Deletion will be valid from the placement's creation datetime. This means that the placement will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PlacementsApi
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
    api_instance = api_client_factory.build(PlacementsApi)
    scope = 'scope_example' # str | The placement scope.
    code = 'code_example' # str | The placement's code. This, together with the scope uniquely identifies the placement to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_placement(scope, code, opts=opts)

        # [EARLY ACCESS] DeletePlacement: Delete placement
        api_response = api_instance.delete_placement(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PlacementsApi->delete_placement: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The placement scope. | 
 **code** | **str**| The placement&#39;s code. This, together with the scope uniquely identifies the placement to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting an placement. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_placement**
> Placement get_placement(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetPlacement: Get Placement

Fetch a Placement that matches the specified identifier

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PlacementsApi
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
    api_instance = api_client_factory.build(PlacementsApi)
    scope = 'scope_example' # str | The scope to which the placement belongs.
    code = 'code_example' # str | The placement's unique identifier.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the placement. Defaults to return the latest version of the placement if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Placement\" domain to decorate onto the placement.  If none are given, all applied properties are returned.             These take the format {domain}/{scope}/{code} e.g. \"Placement/system/Name\". Property keys from the instrument domain can also be decorated             onto the placement, e.g. \"Instrument/default/Isin\". These are only decorated if requested. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_placement(scope, code, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] GetPlacement: Get Placement
        api_response = api_instance.get_placement(scope, code, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PlacementsApi->get_placement: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the placement belongs. | 
 **code** | **str**| The placement&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the placement. Defaults to return the latest version of the placement if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Placement\&quot; domain to decorate onto the placement.  If none are given, all applied properties are returned.             These take the format {domain}/{scope}/{code} e.g. \&quot;Placement/system/Name\&quot;. Property keys from the instrument domain can also be decorated             onto the placement, e.g. \&quot;Instrument/default/Isin\&quot;. These are only decorated if requested. | [optional] 

### Return type

[**Placement**](Placement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The placement matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_placements**
> PagedResourceListOfPlacement list_placements(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListPlacements: List Placements

Fetch the last pre-AsAt date version of each placement in scope (does not fetch the entire history).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PlacementsApi
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
    api_instance = api_client_factory.build(PlacementsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the placement. Defaults to return the latest version of the placement if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing placements from a previous call to list placements.             This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields             must not have changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:             https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Placement\" domain to decorate onto each placement.                 These take the format {domain}/{scope}/{code} e.g. \"Placement/system/Name\".                 All properties, except derived properties, are returned by default, without specifying here. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_placements(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] ListPlacements: List Placements
        api_response = api_instance.list_placements(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PlacementsApi->list_placements: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the placement. Defaults to return the latest version of the placement if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing placements from a previous call to list placements.             This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields             must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:             https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Placement\&quot; domain to decorate onto each placement.                 These take the format {domain}/{scope}/{code} e.g. \&quot;Placement/system/Name\&quot;.                 All properties, except derived properties, are returned by default, without specifying here. | [optional] 

### Return type

[**PagedResourceListOfPlacement**](PagedResourceListOfPlacement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Placements in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_placements**
> ResourceListOfPlacement upsert_placements(placement_set_request=placement_set_request)

[EARLY ACCESS] UpsertPlacements: Upsert Placement

Upsert; update existing placements with given ids, or create new placements otherwise.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PlacementsApi
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
    api_instance = api_client_factory.build(PlacementsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # placement_set_request = PlacementSetRequest.from_json("")
    # placement_set_request = PlacementSetRequest.from_dict({})
    placement_set_request = PlacementSetRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_placements(placement_set_request=placement_set_request, opts=opts)

        # [EARLY ACCESS] UpsertPlacements: Upsert Placement
        api_response = api_instance.upsert_placements(placement_set_request=placement_set_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PlacementsApi->upsert_placements: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_set_request** | [**PlacementSetRequest**](PlacementSetRequest.md)| The collection of placement requests. | [optional] 

### Return type

[**ResourceListOfPlacement**](ResourceListOfPlacement.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of placements. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

