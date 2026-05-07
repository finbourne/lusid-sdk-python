# lusid.TransactionFeeTypesApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_fee_type**](TransactionFeeTypesApi.md#create_transaction_fee_type) | **POST** /api/transactions/transactionfeetypes/{scope}/{code} | [EXPERIMENTAL] CreateTransactionFeeType: Create a transaction fee type
[**delete_transaction_fee_type**](TransactionFeeTypesApi.md#delete_transaction_fee_type) | **DELETE** /api/transactions/transactionfeetypes/{scope}/{code} | [EXPERIMENTAL] DeleteTransactionFeeType: Delete a transaction fee type
[**get_transaction_fee_type**](TransactionFeeTypesApi.md#get_transaction_fee_type) | **GET** /api/transactions/transactionfeetypes/{scope}/{code} | [EXPERIMENTAL] GetTransactionFeeType: Get a transaction fee type
[**list_transaction_fee_types**](TransactionFeeTypesApi.md#list_transaction_fee_types) | **GET** /api/transactions/transactionfeetypes | [EXPERIMENTAL] ListTransactionFeeTypes: List transaction fee types
[**update_transaction_fee_type**](TransactionFeeTypesApi.md#update_transaction_fee_type) | **PUT** /api/transactions/transactionfeetypes/{scope}/{code} | [EXPERIMENTAL] UpdateTransactionFeeType: Update a transaction fee type


# **create_transaction_fee_type**
> TransactionFeeType create_transaction_fee_type(scope, code, create_transaction_fee_type_request)

[EXPERIMENTAL] CreateTransactionFeeType: Create a transaction fee type

Create a transaction fee type for the specified scope and code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionFeeTypesApi
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
    api_instance = api_client_factory.build(TransactionFeeTypesApi)
    scope = 'scope_example' # str | The scope of the transaction fee type.
    code = 'code_example' # str | The code of the transaction fee type.              Together with the scope this uniquely identifies the transaction fee type.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_transaction_fee_type_request = CreateTransactionFeeTypeRequest.from_json("")
    # create_transaction_fee_type_request = CreateTransactionFeeTypeRequest.from_dict({})
    create_transaction_fee_type_request = CreateTransactionFeeTypeRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_transaction_fee_type(scope, code, create_transaction_fee_type_request, opts=opts)

        # [EXPERIMENTAL] CreateTransactionFeeType: Create a transaction fee type
        api_response = api_instance.create_transaction_fee_type(scope, code, create_transaction_fee_type_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionFeeTypesApi->create_transaction_fee_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction fee type. | 
 **code** | **str**| The code of the transaction fee type.              Together with the scope this uniquely identifies the transaction fee type. | 
 **create_transaction_fee_type_request** | [**CreateTransactionFeeTypeRequest**](CreateTransactionFeeTypeRequest.md)| The contents of the transaction fee type. | 

### Return type

[**TransactionFeeType**](TransactionFeeType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created transaction fee type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_transaction_fee_type**
> DeletedEntityResponse delete_transaction_fee_type(scope, code)

[EXPERIMENTAL] DeleteTransactionFeeType: Delete a transaction fee type

Delete a transaction fee type for the specified scope and code. To note, this will be a monotemporal delete, meaning that  the transaction fee type will be deleted for all effective time (including past and future versions of the transaction fee type).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionFeeTypesApi
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
    api_instance = api_client_factory.build(TransactionFeeTypesApi)
    scope = 'scope_example' # str | The scope of the transaction fee type.
    code = 'code_example' # str | The code of the specified transaction fee type.              Together with the scope this uniquely identifies the transaction fee type.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_transaction_fee_type(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteTransactionFeeType: Delete a transaction fee type
        api_response = api_instance.delete_transaction_fee_type(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionFeeTypesApi->delete_transaction_fee_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction fee type. | 
 **code** | **str**| The code of the specified transaction fee type.              Together with the scope this uniquely identifies the transaction fee type. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a transaction fee type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transaction_fee_type**
> TransactionFeeType get_transaction_fee_type(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetTransactionFeeType: Get a transaction fee type

Get the transaction fee type for the specified scope and code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionFeeTypesApi
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
    api_instance = api_client_factory.build(TransactionFeeTypesApi)
    scope = 'scope_example' # str | The scope of the transaction fee type.
    code = 'code_example' # str | The code of the transaction fee type.              Together with the scope this uniquely identifies the transaction fee type.
    effective_at = 'effective_at_example' # str | The effective datetime at which to retrieve the transaction fee type properties.              Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction fee types.              Defaults to latest if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | The collection of `PropertyKey`s that we want to decorate on the transaction fee type. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transaction_fee_type(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] GetTransactionFeeType: Get a transaction fee type
        api_response = api_instance.get_transaction_fee_type(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionFeeTypesApi->get_transaction_fee_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction fee type. | 
 **code** | **str**| The code of the transaction fee type.              Together with the scope this uniquely identifies the transaction fee type. | 
 **effective_at** | **str**| The effective datetime at which to retrieve the transaction fee type properties.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction fee types.              Defaults to latest if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| The collection of &#x60;PropertyKey&#x60;s that we want to decorate on the transaction fee type. | [optional] 

### Return type

[**TransactionFeeType**](TransactionFeeType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction fee type matching the specified scope and code. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_transaction_fee_types**
> ResourceListOfTransactionFeeType list_transaction_fee_types(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListTransactionFeeTypes: List transaction fee types

List transaction fee types that match the specified criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionFeeTypesApi
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
    api_instance = api_client_factory.build(TransactionFeeTypesApi)
    effective_at = 'effective_at_example' # str | The effective datetime at which to retrieve transaction fee type properties.              Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction fee types.              Defaults to latest if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transaction fee types from a previous call to list transaction fee types.  This value is returned from the previous call. If a pagination token is provided the filter,  sortBy, effectiveAt and asAt field must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Scope, use \"scope eq 'ExampleScope'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | The collection of `PropertyKey`s to filter on (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_transaction_fee_types(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] ListTransactionFeeTypes: List transaction fee types
        api_response = api_instance.list_transaction_fee_types(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionFeeTypesApi->list_transaction_fee_types: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime at which to retrieve transaction fee type properties.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction fee types.              Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transaction fee types from a previous call to list transaction fee types.  This value is returned from the previous call. If a pagination token is provided the filter,  sortBy, effectiveAt and asAt field must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Scope, use \&quot;scope eq &#39;ExampleScope&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| The collection of &#x60;PropertyKey&#x60;s to filter on | [optional] 

### Return type

[**ResourceListOfTransactionFeeType**](ResourceListOfTransactionFeeType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of transaction fee types matching the specified criteria. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_transaction_fee_type**
> TransactionFeeType update_transaction_fee_type(scope, code, update_transaction_fee_type_request)

[EXPERIMENTAL] UpdateTransactionFeeType: Update a transaction fee type

Update a transaction fee type by providing the new contents of the transaction fee type.  The displayName field cannot be updated.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionFeeTypesApi
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
    api_instance = api_client_factory.build(TransactionFeeTypesApi)
    scope = 'scope_example' # str | The scope of the transaction fee type.
    code = 'code_example' # str | The code of the specified transaction fee type.              Together with the scope this uniquely identifies the transaction fee type.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_transaction_fee_type_request = UpdateTransactionFeeTypeRequest.from_json("")
    # update_transaction_fee_type_request = UpdateTransactionFeeTypeRequest.from_dict({})
    update_transaction_fee_type_request = UpdateTransactionFeeTypeRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_transaction_fee_type(scope, code, update_transaction_fee_type_request, opts=opts)

        # [EXPERIMENTAL] UpdateTransactionFeeType: Update a transaction fee type
        api_response = api_instance.update_transaction_fee_type(scope, code, update_transaction_fee_type_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionFeeTypesApi->update_transaction_fee_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction fee type. | 
 **code** | **str**| The code of the specified transaction fee type.              Together with the scope this uniquely identifies the transaction fee type. | 
 **update_transaction_fee_type_request** | [**UpdateTransactionFeeTypeRequest**](UpdateTransactionFeeTypeRequest.md)| The updated contents of the transaction fee type. | 

### Return type

[**TransactionFeeType**](TransactionFeeType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated transaction fee type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

