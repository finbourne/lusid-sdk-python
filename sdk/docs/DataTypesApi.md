# lusid.DataTypesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_type**](DataTypesApi.md#create_data_type) | **POST** /api/datatypes | [EARLY ACCESS] CreateDataType: Create data type definition
[**delete_data_type**](DataTypesApi.md#delete_data_type) | **DELETE** /api/datatypes/{scope}/{code} | DeleteDataType: Delete a data type definition.
[**get_data_type**](DataTypesApi.md#get_data_type) | **GET** /api/datatypes/{scope}/{code} | GetDataType: Get data type definition
[**get_units_from_data_type**](DataTypesApi.md#get_units_from_data_type) | **GET** /api/datatypes/{scope}/{code}/units | [EARLY ACCESS] GetUnitsFromDataType: Get units from data type
[**list_data_type_summaries**](DataTypesApi.md#list_data_type_summaries) | **GET** /api/datatypes | [EARLY ACCESS] ListDataTypeSummaries: List all data type summaries, without the reference data
[**list_data_types**](DataTypesApi.md#list_data_types) | **GET** /api/datatypes/{scope} | ListDataTypes: List data types
[**update_data_type**](DataTypesApi.md#update_data_type) | **PUT** /api/datatypes/{scope}/{code} | [EARLY ACCESS] UpdateDataType: Update data type definition
[**update_reference_data**](DataTypesApi.md#update_reference_data) | **PUT** /api/datatypes/{scope}/{code}/referencedata | [EARLY ACCESS] UpdateReferenceData: Update all reference data on a data type, includes the reference values, the field definitions, field values
[**update_reference_values**](DataTypesApi.md#update_reference_values) | **PUT** /api/datatypes/{scope}/{code}/referencedatavalues | [EARLY ACCESS] UpdateReferenceValues: Update reference data on a data type


# **create_data_type**
> DataType create_data_type(create_data_type_request=create_data_type_request)

[EARLY ACCESS] CreateDataType: Create data type definition

Create a new data type definition    Data types cannot be created in either the \"default\" or \"system\" scopes.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DataTypesApi
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
    api_instance = api_client_factory.build(DataTypesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_data_type_request = CreateDataTypeRequest.from_json("")
    # create_data_type_request = CreateDataTypeRequest.from_dict({})
    create_data_type_request = CreateDataTypeRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_data_type(create_data_type_request=create_data_type_request, opts=opts)

        # [EARLY ACCESS] CreateDataType: Create data type definition
        api_response = api_instance.create_data_type(create_data_type_request=create_data_type_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DataTypesApi->create_data_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_data_type_request** | [**CreateDataTypeRequest**](CreateDataTypeRequest.md)| The definition of the new data type | [optional] 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_data_type**
> DeletedEntityResponse delete_data_type(scope, code)

DeleteDataType: Delete a data type definition.

Delete an existing data type definition.    Data types cannot be deleted in either the \"default\" or \"system\" scopes, scopes beginning with \"LUSID-\",  or data types that are in use on a property definition.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DataTypesApi
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
    api_instance = api_client_factory.build(DataTypesApi)
    scope = 'scope_example' # str | The scope of the data type
    code = 'code_example' # str | The code of the data type

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_data_type(scope, code, opts=opts)

        # DeleteDataType: Delete a data type definition.
        api_response = api_instance.delete_data_type(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DataTypesApi->delete_data_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | 
 **code** | **str**| The code of the data type | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_data_type**
> DataType get_data_type(scope, code, as_at=as_at)

GetDataType: Get data type definition

Get the definition of a specified data type

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DataTypesApi
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
    api_instance = api_client_factory.build(DataTypesApi)
    scope = 'scope_example' # str | The scope of the data type
    code = 'code_example' # str | The code of the data type
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the data type definition. Defaults to              return the latest version of the instrument definition if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_data_type(scope, code, as_at=as_at, opts=opts)

        # GetDataType: Get data type definition
        api_response = api_instance.get_data_type(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DataTypesApi->get_data_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | 
 **code** | **str**| The code of the data type | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the data type definition. Defaults to              return the latest version of the instrument definition if not specified. | [optional] 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_units_from_data_type**
> ResourceListOfIUnitDefinitionDto get_units_from_data_type(scope, code, units=units, filter=filter, as_at=as_at)

[EARLY ACCESS] GetUnitsFromDataType: Get units from data type

Get the definitions of the specified units associated bound to a specific data type

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DataTypesApi
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
    api_instance = api_client_factory.build(DataTypesApi)
    scope = 'scope_example' # str | The scope of the data type
    code = 'code_example' # str | The code of the data type
    units = ['units_example'] # List[str] | One or more unit identifiers for which the definition is being requested (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set.               For example, to filter on the Schema, use \"schema eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The as at of the requested data type (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_units_from_data_type(scope, code, units=units, filter=filter, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetUnitsFromDataType: Get units from data type
        api_response = api_instance.get_units_from_data_type(scope, code, units=units, filter=filter, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DataTypesApi->get_units_from_data_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | 
 **code** | **str**| The code of the data type | 
 **units** | [**List[str]**](str.md)| One or more unit identifiers for which the definition is being requested | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.               For example, to filter on the Schema, use \&quot;schema eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **as_at** | **datetime**| Optional. The as at of the requested data type | [optional] 

### Return type

[**ResourceListOfIUnitDefinitionDto**](ResourceListOfIUnitDefinitionDto.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_data_type_summaries**
> PagedResourceListOfDataTypeSummary list_data_type_summaries(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListDataTypeSummaries: List all data type summaries, without the reference data

List all data type summaries

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DataTypesApi
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
    api_instance = api_client_factory.build(DataTypesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the data type summaries. Defaults to returning the latest version               of each summary if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing data type summaries. This  value is returned from the previous call. If a pagination token is provided, the filter, sortBy  and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set.                For example, to filter on the Scope, use \"id.scope eq 'myscope'\", to filter on Schema, use \"schema eq 'string'\",               to filter on AcceptableValues use \"acceptableValues any (~ eq 'value')\"               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_data_type_summaries(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EARLY ACCESS] ListDataTypeSummaries: List all data type summaries, without the reference data
        api_response = api_instance.list_data_type_summaries(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DataTypesApi->list_data_type_summaries: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the data type summaries. Defaults to returning the latest version               of each summary if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing data type summaries. This  value is returned from the previous call. If a pagination token is provided, the filter, sortBy  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.                For example, to filter on the Scope, use \&quot;id.scope eq &#39;myscope&#39;\&quot;, to filter on Schema, use \&quot;schema eq &#39;string&#39;\&quot;,               to filter on AcceptableValues use \&quot;acceptableValues any (~ eq &#39;value&#39;)\&quot;               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfDataTypeSummary**](PagedResourceListOfDataTypeSummary.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_data_types**
> ResourceListOfDataType list_data_types(scope, as_at=as_at, include_system=include_system, sort_by=sort_by, limit=limit, filter=filter)

ListDataTypes: List data types

List all data types in a specified scope

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DataTypesApi
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
    api_instance = api_client_factory.build(DataTypesApi)
    scope = 'scope_example' # str | The requested scope of the data types
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The as at of the requested data types (optional)
    include_system = True # bool | Whether to additionally include those data types in the \"system\" scope (optional)
    sort_by = ['sort_by_example'] # List[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set.              For example, to filter on the Display Name, use \"displayName eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_data_types(scope, as_at=as_at, include_system=include_system, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

        # ListDataTypes: List data types
        api_response = api_instance.list_data_types(scope, as_at=as_at, include_system=include_system, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DataTypesApi->list_data_types: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The requested scope of the data types | 
 **as_at** | **datetime**| The as at of the requested data types | [optional] 
 **include_system** | **bool**| Whether to additionally include those data types in the \&quot;system\&quot; scope | [optional] 
 **sort_by** | [**List[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.              For example, to filter on the Display Name, use \&quot;displayName eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfDataType**](ResourceListOfDataType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_data_type**
> DataType update_data_type(scope, code, update_data_type_request)

[EARLY ACCESS] UpdateDataType: Update data type definition

Update the definition of the specified existing data type    Not all elements within a data type definition are modifiable due to the potential implications for data  already stored against the types

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DataTypesApi
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
    api_instance = api_client_factory.build(DataTypesApi)
    scope = 'scope_example' # str | The scope of the data type
    code = 'code_example' # str | The code of the data type

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_data_type_request = UpdateDataTypeRequest.from_json("")
    # update_data_type_request = UpdateDataTypeRequest.from_dict({})
    update_data_type_request = UpdateDataTypeRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_data_type(scope, code, update_data_type_request, opts=opts)

        # [EARLY ACCESS] UpdateDataType: Update data type definition
        api_response = api_instance.update_data_type(scope, code, update_data_type_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DataTypesApi->update_data_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | 
 **code** | **str**| The code of the data type | 
 **update_data_type_request** | [**UpdateDataTypeRequest**](UpdateDataTypeRequest.md)| The updated definition of the data type | 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_reference_data**
> DataType update_reference_data(scope, code, update_reference_data_request)

[EARLY ACCESS] UpdateReferenceData: Update all reference data on a data type, includes the reference values, the field definitions, field values

Replaces the whole set of reference data

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DataTypesApi
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
    api_instance = api_client_factory.build(DataTypesApi)
    scope = 'scope_example' # str | The scope of the data type
    code = 'code_example' # str | The code of the data type

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_reference_data_request = UpdateReferenceDataRequest.from_json("")
    # update_reference_data_request = UpdateReferenceDataRequest.from_dict({})
    update_reference_data_request = UpdateReferenceDataRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_reference_data(scope, code, update_reference_data_request, opts=opts)

        # [EARLY ACCESS] UpdateReferenceData: Update all reference data on a data type, includes the reference values, the field definitions, field values
        api_response = api_instance.update_reference_data(scope, code, update_reference_data_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DataTypesApi->update_reference_data: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | 
 **code** | **str**| The code of the data type | 
 **update_reference_data_request** | [**UpdateReferenceDataRequest**](UpdateReferenceDataRequest.md)| The updated reference data | 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_reference_values**
> DataType update_reference_values(scope, code, field_value)

[EARLY ACCESS] UpdateReferenceValues: Update reference data on a data type

Replaces the whole set of reference values

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DataTypesApi
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
    api_instance = api_client_factory.build(DataTypesApi)
    scope = 'scope_example' # str | The scope of the data type
    code = 'code_example' # str | The code of the data type
    field_value = [{"value":"FRA","fields":{"english_short_name":"France","continent":"Europe"},"numericFields":{"population_in_millions":68}},{"value":"DEU","fields":{"english_short_name":"Germany","continent":"Europe"},"numericFields":{"population_in_millions":84}}] # List[FieldValue] | The updated reference values

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_reference_values(scope, code, field_value, opts=opts)

        # [EARLY ACCESS] UpdateReferenceValues: Update reference data on a data type
        api_response = api_instance.update_reference_values(scope, code, field_value)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DataTypesApi->update_reference_values: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | 
 **code** | **str**| The code of the data type | 
 **field_value** | [**List[FieldValue]**](FieldValue.md)| The updated reference values | 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

