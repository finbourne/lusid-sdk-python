# lusid.AddressKeyAliasApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_address_key_alias**](AddressKeyAliasApi.md#delete_address_key_alias) | **DELETE** /api/addresskeyaliases/{scope}/{code} | [EXPERIMENTAL] DeleteAddressKeyAlias: Delete an Address Key Alias, assuming that it is present.
[**get_address_key_alias**](AddressKeyAliasApi.md#get_address_key_alias) | **GET** /api/addresskeyaliases/{scope}/{code} | [EXPERIMENTAL] GetAddressKeyAlias: Get Address Key Alias
[**list_address_key_aliases**](AddressKeyAliasApi.md#list_address_key_aliases) | **GET** /api/addresskeyaliases/{scope} | [EXPERIMENTAL] ListAddressKeyAliases: List the set of Address Key Aliases
[**upsert_address_key_alias**](AddressKeyAliasApi.md#upsert_address_key_alias) | **POST** /api/addresskeyaliases | [EXPERIMENTAL] UpsertAddressKeyAlias: Upsert an Address Key Alias. This creates or updates the alias in LUSID.


# **delete_address_key_alias**
> AnnulSingleStructuredDataResponse delete_address_key_alias(scope, code)

[EXPERIMENTAL] DeleteAddressKeyAlias: Delete an Address Key Alias, assuming that it is present.

Delete the specified Address Key Alias from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AddressKeyAliasApi
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
    api_instance = api_client_factory.build(AddressKeyAliasApi)
    scope = 'scope_example' # str | The scope of the Address Key Alias to delete.
    code = 'code_example' # str | The Address Key Alias to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_address_key_alias(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteAddressKeyAlias: Delete an Address Key Alias, assuming that it is present.
        api_response = api_instance.delete_address_key_alias(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AddressKeyAliasApi->delete_address_key_alias: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Address Key Alias to delete. | 
 **code** | **str**| The Address Key Alias to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_address_key_alias**
> GetAddressKeyAliasResponse get_address_key_alias(scope, code, as_at=as_at)

[EXPERIMENTAL] GetAddressKeyAlias: Get Address Key Alias

Get an Address Key Alias from a single scope.                The response will return either the alias that has been stored, or a failure explaining why the request was unsuccessful.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AddressKeyAliasApi
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
    api_instance = api_client_factory.build(AddressKeyAliasApi)
    scope = 'scope_example' # str | The scope of the Address Key Alias to retrieve.
    code = 'code_example' # str | The code of the alias to retrieve.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the alias. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_address_key_alias(scope, code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetAddressKeyAlias: Get Address Key Alias
        api_response = api_instance.get_address_key_alias(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AddressKeyAliasApi->get_address_key_alias: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Address Key Alias to retrieve. | 
 **code** | **str**| The code of the alias to retrieve. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the alias. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetAddressKeyAliasResponse**](GetAddressKeyAliasResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Address Key Alias or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_address_key_aliases**
> PagedResourceListOfGetAddressKeyAliasResponse list_address_key_aliases(scope, as_at=as_at, filter=filter, limit=limit, page=page)

[EXPERIMENTAL] ListAddressKeyAliases: List the set of Address Key Aliases

List the set of address key aliases at the specified date/time and scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AddressKeyAliasApi
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
    api_instance = api_client_factory.build(AddressKeyAliasApi)
    scope = 'scope_example' # str | The scope to list aliases for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the aliases. Defaults to latest if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)
    limit = 56 # int | Maximum number of results to return. Defaults to 100. (optional)
    page = 'page_example' # str | Pagination token from a previous result to fetch the next page. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_address_key_aliases(scope, as_at=as_at, filter=filter, limit=limit, page=page, opts=opts)

        # [EXPERIMENTAL] ListAddressKeyAliases: List the set of Address Key Aliases
        api_response = api_instance.list_address_key_aliases(scope, as_at=as_at, filter=filter, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AddressKeyAliasApi->list_address_key_aliases: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to list aliases for. | 
 **as_at** | **datetime**| The asAt datetime at which to list the aliases. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| Maximum number of results to return. Defaults to 100. | [optional] 
 **page** | **str**| Pagination token from a previous result to fetch the next page. | [optional] 

### Return type

[**PagedResourceListOfGetAddressKeyAliasResponse**](PagedResourceListOfGetAddressKeyAliasResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested address key aliases |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_address_key_alias**
> UpsertSingleStructuredDataResponse upsert_address_key_alias(upsert_address_key_alias_request)

[EXPERIMENTAL] UpsertAddressKeyAlias: Upsert an Address Key Alias. This creates or updates the alias in LUSID.

Update or insert one Address Key Alias. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted alias or failure message if unsuccessful.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AddressKeyAliasApi
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
    api_instance = api_client_factory.build(AddressKeyAliasApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_address_key_alias_request = UpsertAddressKeyAliasRequest.from_json("")
    # upsert_address_key_alias_request = UpsertAddressKeyAliasRequest.from_dict({})
    upsert_address_key_alias_request = UpsertAddressKeyAliasRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_address_key_alias(upsert_address_key_alias_request, opts=opts)

        # [EXPERIMENTAL] UpsertAddressKeyAlias: Upsert an Address Key Alias. This creates or updates the alias in LUSID.
        api_response = api_instance.upsert_address_key_alias(upsert_address_key_alias_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AddressKeyAliasApi->upsert_address_key_alias: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_address_key_alias_request** | [**UpsertAddressKeyAliasRequest**](UpsertAddressKeyAliasRequest.md)| The Address Key Alias to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

