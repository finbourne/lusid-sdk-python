# lusid.ResourceRecordApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_resource_record**](ResourceRecordApi.md#delete_resource_record) | **DELETE** /api/resourcerecords/{scope}/{code}/{resourceId} | [EARLY ACCESS] DeleteResourceRecord: Delete a Resource Record
[**get_resource_record**](ResourceRecordApi.md#get_resource_record) | **GET** /api/resourcerecords/{scope}/{code}/{resourceId} | [EARLY ACCESS] GetResourceRecord: Get a Resource Record
[**list_resource_record_codes**](ResourceRecordApi.md#list_resource_record_codes) | **GET** /api/resourcerecords/{scope} | [EARLY ACCESS] ListResourceRecordCodes: List Resource Records Codes for Scope
[**list_resource_record_scopes**](ResourceRecordApi.md#list_resource_record_scopes) | **GET** /api/resourcerecords | [EARLY ACCESS] ListResourceRecordScopes: List Resource Record Scopes
[**list_resource_records**](ResourceRecordApi.md#list_resource_records) | **GET** /api/resourcerecords/{scope}/{code} | [EARLY ACCESS] ListResourceRecords: List Resource Records
[**upsert_resource_record**](ResourceRecordApi.md#upsert_resource_record) | **POST** /api/resourcerecords | [EARLY ACCESS] UpsertResourceRecord: Upsert a Resource Record


# **delete_resource_record**
> DeletedEntityResponse delete_resource_record(scope, code, resource_id)

[EARLY ACCESS] DeleteResourceRecord: Delete a Resource Record

Delete a resource record.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ResourceRecordApi
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
    api_instance = api_client_factory.build(ResourceRecordApi)
    scope = 'scope_example' # str | The scope of the resource record.
    code = 'code_example' # str | The code of the resource record.
    resource_id = 'resource_id_example' # str | The resource identifier of the resource record.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_resource_record(scope, code, resource_id, opts=opts)

        # [EARLY ACCESS] DeleteResourceRecord: Delete a Resource Record
        api_response = api_instance.delete_resource_record(scope, code, resource_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ResourceRecordApi->delete_resource_record: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the resource record. | 
 **code** | **str**| The code of the resource record. | 
 **resource_id** | **str**| The resource identifier of the resource record. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_resource_record**
> ResourceRecord get_resource_record(scope, code, resource_id, as_at=as_at)

[EARLY ACCESS] GetResourceRecord: Get a Resource Record

Retrieve a resource record by its identifier.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ResourceRecordApi
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
    api_instance = api_client_factory.build(ResourceRecordApi)
    scope = 'scope_example' # str | The scope of the resource record.
    code = 'code_example' # str | The code of the resource record.
    resource_id = 'resource_id_example' # str | The resource identifier of the resource record.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_resource_record(scope, code, resource_id, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetResourceRecord: Get a Resource Record
        api_response = api_instance.get_resource_record(scope, code, resource_id, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ResourceRecordApi->get_resource_record: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the resource record. | 
 **code** | **str**| The code of the resource record. | 
 **resource_id** | **str**| The resource identifier of the resource record. | 
 **as_at** | **datetime**| The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**ResourceRecord**](ResourceRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource record. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_resource_record_codes**
> ResourceListOfString list_resource_record_codes(scope, as_at=as_at, sort_order=sort_order)

[EARLY ACCESS] ListResourceRecordCodes: List Resource Records Codes for Scope

List all resource records matching particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ResourceRecordApi
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
    api_instance = api_client_factory.build(ResourceRecordApi)
    scope = 'scope_example' # str | The scope of the resource record.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. (optional)
    sort_order = 'sort_order_example' # str | Order of the sort - either \"ASC\" or \"DESC\" (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_resource_record_codes(scope, as_at=as_at, sort_order=sort_order, opts=opts)

        # [EARLY ACCESS] ListResourceRecordCodes: List Resource Records Codes for Scope
        api_response = api_instance.list_resource_record_codes(scope, as_at=as_at, sort_order=sort_order)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ResourceRecordApi->list_resource_record_codes: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the resource record. | 
 **as_at** | **datetime**| The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. | [optional] 
 **sort_order** | **str**| Order of the sort - either \&quot;ASC\&quot; or \&quot;DESC\&quot; | [optional] 

### Return type

[**ResourceListOfString**](ResourceListOfString.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource record codes. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_resource_record_scopes**
> ResourceListOfScopeDefinition list_resource_record_scopes(as_at=as_at, page=page, limit=limit)

[EARLY ACCESS] ListResourceRecordScopes: List Resource Record Scopes

List all resource records matching particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ResourceRecordApi
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
    api_instance = api_client_factory.build(ResourceRecordApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing resource records from a previous call. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_resource_record_scopes(as_at=as_at, page=page, limit=limit, opts=opts)

        # [EARLY ACCESS] ListResourceRecordScopes: List Resource Record Scopes
        api_response = api_instance.list_resource_record_scopes(as_at=as_at, page=page, limit=limit)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ResourceRecordApi->list_resource_record_scopes: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing resource records from a previous call. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfScopeDefinition**](ResourceListOfScopeDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource records. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_resource_records**
> PagedResourceListOfResourceRecord list_resource_records(scope, code, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EARLY ACCESS] ListResourceRecords: List Resource Records

List all resource records matching particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ResourceRecordApi
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
    api_instance = api_client_factory.build(ResourceRecordApi)
    scope = 'scope_example' # str | The scope of the resource record.
    code = 'code_example' # str | The code of the resource record.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing resource records from a previous call. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_resource_records(scope, code, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

        # [EARLY ACCESS] ListResourceRecords: List Resource Records
        api_response = api_instance.list_resource_records(scope, code, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ResourceRecordApi->list_resource_records: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the resource record. | 
 **code** | **str**| The code of the resource record. | 
 **as_at** | **datetime**| The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing resource records from a previous call. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**PagedResourceListOfResourceRecord**](PagedResourceListOfResourceRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource records. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_resource_record**
> ResourceRecord upsert_resource_record(upsert_resource_record_request)

[EARLY ACCESS] UpsertResourceRecord: Upsert a Resource Record

Create or update a resource record.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ResourceRecordApi
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
    api_instance = api_client_factory.build(ResourceRecordApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_resource_record_request = UpsertResourceRecordRequest.from_json("")
    # upsert_resource_record_request = UpsertResourceRecordRequest.from_dict({})
    upsert_resource_record_request = UpsertResourceRecordRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_resource_record(upsert_resource_record_request, opts=opts)

        # [EARLY ACCESS] UpsertResourceRecord: Upsert a Resource Record
        api_response = api_instance.upsert_resource_record(upsert_resource_record_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ResourceRecordApi->upsert_resource_record: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_resource_record_request** | [**UpsertResourceRecordRequest**](UpsertResourceRecordRequest.md)| The resource record to upsert. | 

### Return type

[**ResourceRecord**](ResourceRecord.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The upserted resource record. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

