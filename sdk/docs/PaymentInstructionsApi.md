# lusid.PaymentInstructionsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_instruction**](PaymentInstructionsApi.md#get_payment_instruction) | **GET** /api/paymentinstructions/{scope}/{code} | [EARLY ACCESS] GetPaymentInstruction: Get Payment Instruction
[**upsert_payment_instructions**](PaymentInstructionsApi.md#upsert_payment_instructions) | **POST** /api/paymentinstructions | [EARLY ACCESS] UpsertPaymentInstructions: Upsert Payment Instructions


# **get_payment_instruction**
> PaymentInstruction get_payment_instruction(scope, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetPaymentInstruction: Get Payment Instruction

Retrieve a single Payment Instruction.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PaymentInstructionsApi
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
    api_instance = api_client_factory.build(PaymentInstructionsApi)
    scope = 'scope_example' # str | The scope of the payment instruction.
    code = 'code_example' # str | The code of the payment instruction.
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"PaymentInstruction\" domain to decorate onto the              payment instruction. These take the format {domain}/{scope}/{code} e.g. \"PaymentInstruction/myScope/myProperty\". (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the payment instruction.              Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the payment instruction. Defaults to return the latest              version of the payment instruction if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_payment_instruction(scope, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetPaymentInstruction: Get Payment Instruction
        api_response = api_instance.get_payment_instruction(scope, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PaymentInstructionsApi->get_payment_instruction: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the payment instruction. | 
 **code** | **str**| The code of the payment instruction. | 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;PaymentInstruction\&quot; domain to decorate onto the              payment instruction. These take the format {domain}/{scope}/{code} e.g. \&quot;PaymentInstruction/myScope/myProperty\&quot;. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the payment instruction.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the payment instruction. Defaults to return the latest              version of the payment instruction if not specified. | [optional] 

### Return type

[**PaymentInstruction**](PaymentInstruction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested payment instruction |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_payment_instructions**
> PaymentInstructionsResponse upsert_payment_instructions(request_body)

[EARLY ACCESS] UpsertPaymentInstructions: Upsert Payment Instructions

Create or update a collection of Payment Instructions.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PaymentInstructionsApi
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
    api_instance = api_client_factory.build(PaymentInstructionsApi)
    request_body = {"paymentInstruction1":{"id":{"scope":"myScope","code":"paymentInstruction1"},"paymentRecordIds":[{"portfolioId":{"scope":"myScope","code":"myPortfolio"},"transactionId":"transaction1","paymentRecordId":"paymentRecord1"}],"currency":"GBP","totalPaymentAmount":1000,"paymentDate":"2024-01-01T00:00:00.0000000+00:00","payorPaymentDetailsReference":{"seriesScope":"myScope","applicableEntity":{"entityType":"Portfolio","entityScope":"myScope","identifierType":"code","identifierScope":"myScope","identifierValue":"LUID_00003D4Q"},"seriesIdentifiers":{"paymentType":"Dividend","currency":"GBP"},"effectiveDate":"2024-01-01T00:00:00.0000000+00:00","asAtDate":"2024-01-01T00:00:00.0000000+00:00"},"payeePaymentDetailsReference":{"seriesScope":"myScope","applicableEntity":{"entityType":"Portfolio","entityScope":"myScope","identifierType":"code","identifierScope":"myScope","identifierValue":"LUID_00003D4R"},"seriesIdentifiers":{"paymentType":"Dividend","currency":"GBP"},"effectiveDate":"2024-01-01T00:00:00.0000000+00:00","asAtDate":"2024-01-01T00:00:00.0000000+00:00"}}} # Dict[str, PaymentInstructionRequest] | A collection of requests to create or update Payment Instructions.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_payment_instructions(request_body, opts=opts)

        # [EARLY ACCESS] UpsertPaymentInstructions: Upsert Payment Instructions
        api_response = api_instance.upsert_payment_instructions(request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PaymentInstructionsApi->upsert_payment_instructions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, PaymentInstructionRequest]**](PaymentInstructionRequest.md)| A collection of requests to create or update Payment Instructions. | 

### Return type

[**PaymentInstructionsResponse**](PaymentInstructionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The successfully created or updated payment instructions along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

