# lusid.InvestmentAccountsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upsert_investment_accounts**](InvestmentAccountsApi.md#upsert_investment_accounts) | **POST** /api/investmentaccounts/$batchUpsert | [EARLY ACCESS] UpsertInvestmentAccounts: Upsert Investment Accounts


# **upsert_investment_accounts**
> UpsertInvestmentAccountsResponse upsert_investment_accounts(success_mode, request_body)

[EARLY ACCESS] UpsertInvestmentAccounts: Upsert Investment Accounts

Creates or updates a collection of Investment Accounts

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InvestmentAccountsApi
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
    api_instance = api_client_factory.build(InvestmentAccountsApi)
    success_mode = 'success_mode_example' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial
    request_body = {"firstExampleRequest":{"identifiers":{"InvestmentAccount/ExternalIdentifier/ExternalIAId":{"key":"InvestmentAccount/ExternalIdentifier/ExternalIAId","value":{"labelValue":"IA_12345678"}},"InvestmentAccount/InternalIdentifier/InternalIAId":{"key":"InvestmentAccount/InternalIdentifier/InternalIAId","value":{"labelValue":"Internal_XHSP2038"}}},"properties":{"InvestmentAccount/Details/Name":{"key":"InvestmentAccount/Details/Name","value":{"labelValue":"John Doe"}},"InvestmentAccount/Details/Country":{"key":"InvestmentAccount/Details/Country","value":{"labelValue":"United Kingdom"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"}},"displayName":"InvestmentAccount1DisplayName","description":"InvestmentAccount1Description","accountType":"Personal","accountHolders":[{"key":"AccountHolder1","identifiers":{"InvestorRecord/ExternalIdentifier/ExternalIRId":{"key":"InvestorRecord/ExternalIdentifier/ExternalIRId","value":{"labelValue":"IR_12345678"}},"InvestorRecord/InternalIdentifier/InternalIRId":{"key":"InvestorRecord/InternalIdentifier/InternalIRId","value":{"labelValue":"Internal_XHSP2038"}}}}],"investmentPortfolios":[]},"secondExampleRequest":{"identifiers":{"InvestmentAccount/ExternalIdentifier/ExternalIAId":{"key":"InvestmentAccount/ExternalIdentifier/ExternalIAId","value":{"labelValue":"IR_22345678"}},"InvestmentAccount/InternalIdentifier/InternalIAId":{"key":"InvestmentAccount/InternalIdentifier/InternalIAId","value":{"labelValue":"Internal_XHSP2039"}}},"properties":{"InvestmentAccount/Details/Name":{"key":"InvestmentAccount/Details/Name","value":{"labelValue":"Jane Doe"}},"InvestmentAccount/Details/Country":{"key":"InvestmentAccount/Details/Country","value":{"labelValue":"Germany"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"}},"displayName":"InvestmentAccount2DisplayName","description":"InvestmentAccount2Description","accountType":"JointMixed","accountHolders":[{"key":"AccountHolder1","identifiers":{"InvestorRecord/ExternalIdentifier/ExternalIRId":{"key":"InvestorRecord/ExternalIdentifier/ExternalIRId","value":{"labelValue":"IR_12345678"}},"InvestorRecord/InternalIdentifier/InternalIRId":{"key":"InvestorRecord/InternalIdentifier/InternalIRId","value":{"labelValue":"Internal_XHSP2038"}}}}],"investmentPortfolios":[]}} # Dict[str, UpsertInvestmentAccountRequest] | A collection of requests to create or update Investment Accounts.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_investment_accounts(success_mode, request_body, opts=opts)

        # [EARLY ACCESS] UpsertInvestmentAccounts: Upsert Investment Accounts
        api_response = api_instance.upsert_investment_accounts(success_mode, request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestmentAccountsApi->upsert_investment_accounts: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | 
 **request_body** | [**Dict[str, UpsertInvestmentAccountRequest]**](UpsertInvestmentAccountRequest.md)| A collection of requests to create or update Investment Accounts. | 

### Return type

[**UpsertInvestmentAccountsResponse**](UpsertInvestmentAccountsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The successfully created or updated Investment Accounts along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

