# lusid.CurrencyGroupsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_currency_group**](CurrencyGroupsApi.md#delete_currency_group) | **DELETE** /api/currencies/groups/{code} | [EXPERIMENTAL] DeleteCurrencyGroup: Delete a currency group.
[**get_currency_group**](CurrencyGroupsApi.md#get_currency_group) | **GET** /api/currencies/groups/{code} | [EXPERIMENTAL] GetCurrencyGroup: Get a currency group.
[**list_currency_groups**](CurrencyGroupsApi.md#list_currency_groups) | **GET** /api/currencies/groups | [EXPERIMENTAL] ListCurrencyGroups: List currency groups.
[**upsert_currency_group**](CurrencyGroupsApi.md#upsert_currency_group) | **POST** /api/currencies/groups | [EXPERIMENTAL] UpsertCurrencyGroup: Upsert a currency group.


# **delete_currency_group**
> DeletedEntityResponse delete_currency_group(code)

[EXPERIMENTAL] DeleteCurrencyGroup: Delete a currency group.

Delete the currency group with the given code. The group's currencies are freed to be claimed  by other currency groups.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CurrencyGroupsApi
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
    api_instance = api_client_factory.build(CurrencyGroupsApi)
    code = 'code_example' # str | The code of the currency group to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_currency_group(code, opts=opts)

        # [EXPERIMENTAL] DeleteCurrencyGroup: Delete a currency group.
        api_response = api_instance.delete_currency_group(code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CurrencyGroupsApi->delete_currency_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the currency group to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_currency_group**
> CurrencyGroupResponse get_currency_group(code, as_at=as_at)

[EXPERIMENTAL] GetCurrencyGroup: Get a currency group.

Get the currency group with the given code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CurrencyGroupsApi
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
    api_instance = api_client_factory.build(CurrencyGroupsApi)
    code = 'code_example' # str | The code of the currency group.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the currency group. Defaults to returning              the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_currency_group(code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetCurrencyGroup: Get a currency group.
        api_response = api_instance.get_currency_group(code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CurrencyGroupsApi->get_currency_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the currency group. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the currency group. Defaults to returning              the latest version if not specified. | [optional] 

### Return type

[**CurrencyGroupResponse**](CurrencyGroupResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested currency group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_currency_groups**
> PagedResourceListOfCurrencyGroupResponse list_currency_groups(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListCurrencyGroups: List currency groups.

List the currency groups defined in the tenant that the caller is entitled to read.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CurrencyGroupsApi
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
    api_instance = api_client_factory.build(CurrencyGroupsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the currency groups. Defaults to returning              the latest version of each currency group if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing currency groups from a previous              call to list currency groups. This value is returned from the previous call. If a pagination token              is provided the filter, sortBy and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. (optional)
    filter = 'filter_example' # str | Expression to filter the results. Filterable fields are the group's code,              displayName and majorUnitCurrency. For example, \"majorUnitCurrency eq 'GBP'\". (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each prefixed with \"+\" for ascending or              \"-\" for descending. Sortable fields are the group's code, displayName and majorUnitCurrency. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_currency_groups(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListCurrencyGroups: List currency groups.
        api_response = api_instance.list_currency_groups(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CurrencyGroupsApi->list_currency_groups: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the currency groups. Defaults to returning              the latest version of each currency group if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing currency groups from a previous              call to list currency groups. This value is returned from the previous call. If a pagination token              is provided the filter, sortBy and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] 
 **filter** | **str**| Expression to filter the results. Filterable fields are the group&#39;s code,              displayName and majorUnitCurrency. For example, \&quot;majorUnitCurrency eq &#39;GBP&#39;\&quot;. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each prefixed with \&quot;+\&quot; for ascending or              \&quot;-\&quot; for descending. Sortable fields are the group&#39;s code, displayName and majorUnitCurrency. | [optional] 

### Return type

[**PagedResourceListOfCurrencyGroupResponse**](PagedResourceListOfCurrencyGroupResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested currency groups. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_currency_group**
> CurrencyGroupResponse upsert_currency_group(upsert_currency_group_request)

[EXPERIMENTAL] UpsertCurrencyGroup: Upsert a currency group.

Create or update a currency group. If a currency group with the same code already exists it is replaced.  A currency may belong to at most one currency group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CurrencyGroupsApi
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
    api_instance = api_client_factory.build(CurrencyGroupsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_currency_group_request = UpsertCurrencyGroupRequest.from_json("")
    # upsert_currency_group_request = UpsertCurrencyGroupRequest.from_dict({})
    upsert_currency_group_request = UpsertCurrencyGroupRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_currency_group(upsert_currency_group_request, opts=opts)

        # [EXPERIMENTAL] UpsertCurrencyGroup: Upsert a currency group.
        api_response = api_instance.upsert_currency_group(upsert_currency_group_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CurrencyGroupsApi->upsert_currency_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_currency_group_request** | [**UpsertCurrencyGroupRequest**](UpsertCurrencyGroupRequest.md)| The currency group to upsert. | 

### Return type

[**CurrencyGroupResponse**](CurrencyGroupResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted currency group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

