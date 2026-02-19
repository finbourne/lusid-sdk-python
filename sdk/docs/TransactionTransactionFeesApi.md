# lusid.TransactionTransactionFeesApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_fee**](TransactionTransactionFeesApi.md#create_transaction_fee) | **POST** /api/transactions/transactionfees/{scope}/{code} | [EXPERIMENTAL] CreateTransactionFee: Create a TransactionFee
[**delete_transaction_fee**](TransactionTransactionFeesApi.md#delete_transaction_fee) | **DELETE** /api/transactions/transactionfees/{scope}/{code} | [EXPERIMENTAL] DeleteTransactionFee: Delete a TransactionFee
[**get_transaction_fee**](TransactionTransactionFeesApi.md#get_transaction_fee) | **GET** /api/transactions/transactionfees/{scope}/{code} | [EXPERIMENTAL] GetTransactionFee: Get a TransactionFee
[**list_transaction_fees**](TransactionTransactionFeesApi.md#list_transaction_fees) | **GET** /api/transactions/transactionfees | [EXPERIMENTAL] ListTransactionFees: List TransactionFees
[**update_transaction_fee**](TransactionTransactionFeesApi.md#update_transaction_fee) | **PUT** /api/transactions/transactionfees/{scope}/{code} | [EXPERIMENTAL] UpdateTransactionFee: Update a TransactionFee


# **create_transaction_fee**
> TransactionFee create_transaction_fee(scope, code, create_transaction_fee_request, effective_at=effective_at)

[EXPERIMENTAL] CreateTransactionFee: Create a TransactionFee

Create a TransactionFee for the specified scope and code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionTransactionFeesApi
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
    api_instance = api_client_factory.build(TransactionTransactionFeesApi)
    scope = 'scope_example' # str | The scope of the TransactionFee.
    code = 'code_example' # str | The code of the TransactionFee.              Together with the scope this uniquely identifies the TransactionFee.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_transaction_fee_request = CreateTransactionFeeRequest.from_json("")
    # create_transaction_fee_request = CreateTransactionFeeRequest.from_dict({})
    create_transaction_fee_request = CreateTransactionFeeRequest()
    effective_at = 'effective_at_example' # str | The date and time at which the TransactionFee should be effective. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_transaction_fee(scope, code, create_transaction_fee_request, effective_at=effective_at, opts=opts)

        # [EXPERIMENTAL] CreateTransactionFee: Create a TransactionFee
        api_response = api_instance.create_transaction_fee(scope, code, create_transaction_fee_request, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionTransactionFeesApi->create_transaction_fee: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the TransactionFee. | 
 **code** | **str**| The code of the TransactionFee.              Together with the scope this uniquely identifies the TransactionFee. | 
 **create_transaction_fee_request** | [**CreateTransactionFeeRequest**](CreateTransactionFeeRequest.md)| The contents of the TransactionFee. | 
 **effective_at** | **str**| The date and time at which the TransactionFee should be effective. | [optional] 

### Return type

[**TransactionFee**](TransactionFee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created TransactionFee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_transaction_fee**
> DeletedEntityResponse delete_transaction_fee(scope, code)

[EXPERIMENTAL] DeleteTransactionFee: Delete a TransactionFee

Delete a TransactionFee for the specified scope and code. To note, this will be a monotemporal delete, meaning that  the TransactionFee will be deleted for all effective time (including past and future versions of the TransactionFee).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionTransactionFeesApi
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
    api_instance = api_client_factory.build(TransactionTransactionFeesApi)
    scope = 'scope_example' # str | The scope of the TransactionFee.
    code = 'code_example' # str | The code of the specified TransactionFee.              Together with the scope this uniquely identifies the TransactionFee.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_transaction_fee(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteTransactionFee: Delete a TransactionFee
        api_response = api_instance.delete_transaction_fee(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionTransactionFeesApi->delete_transaction_fee: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the TransactionFee. | 
 **code** | **str**| The code of the specified TransactionFee.              Together with the scope this uniquely identifies the TransactionFee. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a TransactionFee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transaction_fee**
> TransactionFee get_transaction_fee(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetTransactionFee: Get a TransactionFee

Get the TransactionFee for the specified scope and code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionTransactionFeesApi
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
    api_instance = api_client_factory.build(TransactionTransactionFeesApi)
    scope = 'scope_example' # str | The scope of the TransactionFee.
    code = 'code_example' # str | The code of the TransactionFee.              Together with the scope this uniquely identifies the TransactionFee.
    effective_at = 'effective_at_example' # str | The date and time at which the query is effective. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the TransactionFees.              Defaults to latest if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | The collection of `PropertyKey`s that we want to decorate on identifies the TransactionFee. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transaction_fee(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] GetTransactionFee: Get a TransactionFee
        api_response = api_instance.get_transaction_fee(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionTransactionFeesApi->get_transaction_fee: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the TransactionFee. | 
 **code** | **str**| The code of the TransactionFee.              Together with the scope this uniquely identifies the TransactionFee. | 
 **effective_at** | **str**| The date and time at which the query is effective. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the TransactionFees.              Defaults to latest if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| The collection of &#x60;PropertyKey&#x60;s that we want to decorate on identifies the TransactionFee. | [optional] 

### Return type

[**TransactionFee**](TransactionFee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The TransactionFee matching the specified scope and code. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_transaction_fees**
> ResourceListOfTransactionFee list_transaction_fees(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListTransactionFees: List TransactionFees

List TransactionFees that match the specified criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionTransactionFeesApi
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
    api_instance = api_client_factory.build(TransactionTransactionFeesApi)
    effective_at = 'effective_at_example' # str | The date and time at which the query is effective. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the TransactionFees.              Defaults to latest if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing TransactionFees from a previous call to list TransactionFees.  This value is returned from the previous call. If a pagination token is provided the filter,  sortBy and asAt field must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Scope, use \"scope eq 'ExampleScope'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | The collection of `PropertyKey`s to filter on (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_transaction_fees(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] ListTransactionFees: List TransactionFees
        api_response = api_instance.list_transaction_fees(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionTransactionFeesApi->list_transaction_fees: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The date and time at which the query is effective. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the TransactionFees.              Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing TransactionFees from a previous call to list TransactionFees.  This value is returned from the previous call. If a pagination token is provided the filter,  sortBy and asAt field must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Scope, use \&quot;scope eq &#39;ExampleScope&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| The collection of &#x60;PropertyKey&#x60;s to filter on | [optional] 

### Return type

[**ResourceListOfTransactionFee**](ResourceListOfTransactionFee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of TransactionFees matching the specified criteria. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_transaction_fee**
> TransactionFee update_transaction_fee(scope, code, update_transaction_fee_request, effective_at=effective_at)

[EXPERIMENTAL] UpdateTransactionFee: Update a TransactionFee

Update a TransactionFee by providing the new contents of the TransactionFee.  The name field and the capitalisation field can not be updated.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionTransactionFeesApi
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
    api_instance = api_client_factory.build(TransactionTransactionFeesApi)
    scope = 'scope_example' # str | The scope of the TransactionFee.
    code = 'code_example' # str | The code of the specified TransactionFee.              Together with the scope this uniquely identifies the TransactionFee.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_transaction_fee_request = UpdateTransactionFeeRequest.from_json("")
    # update_transaction_fee_request = UpdateTransactionFeeRequest.from_dict({})
    update_transaction_fee_request = UpdateTransactionFeeRequest()
    effective_at = 'effective_at_example' # str | The date and time at which the update should take effect.             The updated contents of the TransactionFee. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_transaction_fee(scope, code, update_transaction_fee_request, effective_at=effective_at, opts=opts)

        # [EXPERIMENTAL] UpdateTransactionFee: Update a TransactionFee
        api_response = api_instance.update_transaction_fee(scope, code, update_transaction_fee_request, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionTransactionFeesApi->update_transaction_fee: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the TransactionFee. | 
 **code** | **str**| The code of the specified TransactionFee.              Together with the scope this uniquely identifies the TransactionFee. | 
 **update_transaction_fee_request** | [**UpdateTransactionFeeRequest**](UpdateTransactionFeeRequest.md)| The contents of the TransactionFee. | 
 **effective_at** | **str**| The date and time at which the update should take effect.             The updated contents of the TransactionFee. | [optional] 

### Return type

[**TransactionFee**](TransactionFee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated TransactionFee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

