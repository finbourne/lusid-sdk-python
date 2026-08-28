# lusid.TransfersApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transfer**](TransfersApi.md#create_transfer) | **POST** /api/transfers | [EXPERIMENTAL] CreateTransfer: Create a transfer.


# **create_transfer**
> CreateTransferResponse create_transfer(create_transfer_request)

[EXPERIMENTAL] CreateTransfer: Create a transfer.

Move a position between two portfolios, exchange one instrument for another within a portfolio, or do  both at once.                The outgoing and incoming transaction legs and the Transfer entity recording them are written as a single  atomic operation: if any part of the request is rejected, nothing is written.

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

