# lusid.TransfersApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transfer**](TransfersApi.md#create_transfer) | **POST** /api/transfers | [EXPERIMENTAL] CreateTransfer: Create a transfer.
[**delete_transfer**](TransfersApi.md#delete_transfer) | **DELETE** /api/transfers/{scope}/{code} | [EXPERIMENTAL] DeleteTransfer: Delete a transfer.
[**get_transfer**](TransfersApi.md#get_transfer) | **POST** /api/transfers/$get | [EXPERIMENTAL] GetTransfer: Get a transfer


# **create_transfer**
> CreateTransferResponse create_transfer(create_transfer_request)

[EXPERIMENTAL] CreateTransfer: Create a transfer.

Move a position between two portfolios, exchange one instrument for another within a portfolio, or do  both at once.  The outgoing and incoming transaction legs and the Transfer entity recording them are written as a single  atomic operation: if any part of the request is rejected, nothing is written.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransfersApi
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
    api_instance = api_client_factory.build(TransfersApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_transfer_request = CreateTransferRequest.from_json("")
    # create_transfer_request = CreateTransferRequest.from_dict({})
    create_transfer_request = CreateTransferRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_transfer(create_transfer_request, opts=opts)

        # [EXPERIMENTAL] CreateTransfer: Create a transfer.
        api_response = api_instance.create_transfer(create_transfer_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransfersApi->create_transfer: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transfer_request** | [**CreateTransferRequest**](CreateTransferRequest.md)| The transfer to create. | 

### Return type

[**CreateTransferResponse**](CreateTransferResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The transfer that was created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_transfer**
> DeletedEntityResponse delete_transfer(scope, code, portfolio_scope_out, portfolio_code_out, portfolio_scope_in, portfolio_code_in)

[EXPERIMENTAL] DeleteTransfer: Delete a transfer.

Delete the Transfer entity recording a transfer and cancel the transaction legs it still has, as a single  atomic operation: if any part of the request is rejected, nothing is changed. A leg that has already gone is  skipped, so a transfer with no legs left can still be deleted to clear the record.                A transfer is identified by its scope, its code and both of its portfolios, so all four are required. Where  no transfer matches all four, the request is reported as not found.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransfersApi
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
    api_instance = api_client_factory.build(TransfersApi)
    scope = 'scope_example' # str | The scope of the transfer.
    code = 'code_example' # str | The code of the transfer. Together with the scope and both portfolios this uniquely               identifies the transfer.
    portfolio_scope_out = 'portfolio_scope_out_example' # str | The scope of the portfolio the outgoing leg is booked in.
    portfolio_code_out = 'portfolio_code_out_example' # str | The code of the portfolio the outgoing leg is booked in.
    portfolio_scope_in = 'portfolio_scope_in_example' # str | The scope of the portfolio the incoming leg is booked in.
    portfolio_code_in = 'portfolio_code_in_example' # str | The code of the portfolio the incoming leg is booked in. Equal to               portfolioCodeOut for a switch between instruments within one portfolio.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_transfer(scope, code, portfolio_scope_out, portfolio_code_out, portfolio_scope_in, portfolio_code_in, opts=opts)

        # [EXPERIMENTAL] DeleteTransfer: Delete a transfer.
        api_response = api_instance.delete_transfer(scope, code, portfolio_scope_out, portfolio_code_out, portfolio_scope_in, portfolio_code_in)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransfersApi->delete_transfer: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transfer. | 
 **code** | **str**| The code of the transfer. Together with the scope and both portfolios this uniquely               identifies the transfer. | 
 **portfolio_scope_out** | **str**| The scope of the portfolio the outgoing leg is booked in. | 
 **portfolio_code_out** | **str**| The code of the portfolio the outgoing leg is booked in. | 
 **portfolio_scope_in** | **str**| The scope of the portfolio the incoming leg is booked in. | 
 **portfolio_code_in** | **str**| The code of the portfolio the incoming leg is booked in. Equal to               portfolioCodeOut for a switch between instruments within one portfolio. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asAt the deletion landed at. |  -  |
**400** | The details of the input related failure |  -  |
**404** | No transfer with the given scope, code and portfolios. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transfer**
> GetTransferResponse get_transfer(get_transfer_request, as_at=as_at)

[EXPERIMENTAL] GetTransfer: Get a transfer

Retrieve a transfer and both of the transactions it booked.  A transfer is identified by its scope, its code and both of its portfolios, so all four are supplied in  the request body rather than in the path.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransfersApi
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
    api_instance = api_client_factory.build(TransfersApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # get_transfer_request = GetTransferRequest.from_json("")
    # get_transfer_request = GetTransferRequest.from_dict({})
    get_transfer_request = GetTransferRequest()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transfer. Defaults to latest              version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transfer(get_transfer_request, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetTransfer: Get a transfer
        api_response = api_instance.get_transfer(get_transfer_request, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransfersApi->get_transfer: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_transfer_request** | [**GetTransferRequest**](GetTransferRequest.md)| The transfer to retrieve. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transfer. Defaults to latest              version if not specified. | [optional] 

### Return type

[**GetTransferResponse**](GetTransferResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transfer and both of its transactions. |  -  |
**400** | The details of the input related failure |  -  |
**404** | No transfer exists with the requested scope, code and portfolios. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

