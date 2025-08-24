# lusid.DerivedTransactionPortfoliosApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_derived_portfolio**](DerivedTransactionPortfoliosApi.md#create_derived_portfolio) | **POST** /api/derivedtransactionportfolios/{scope} | CreateDerivedPortfolio: Create derived portfolio
[**delete_derived_portfolio_details**](DerivedTransactionPortfoliosApi.md#delete_derived_portfolio_details) | **DELETE** /api/derivedtransactionportfolios/{scope}/{code}/details | [EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details


# **create_derived_portfolio**
> Portfolio create_derived_portfolio(scope, create_derived_transaction_portfolio_request=create_derived_transaction_portfolio_request)

CreateDerivedPortfolio: Create derived portfolio

Create a derived transaction portfolio from a parent transaction portfolio (which may itself be derived).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DerivedTransactionPortfoliosApi
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
    api_instance = api_client_factory.build(DerivedTransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope in which to create the derived transaction portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_derived_transaction_portfolio_request = CreateDerivedTransactionPortfolioRequest.from_json("")
    # create_derived_transaction_portfolio_request = CreateDerivedTransactionPortfolioRequest.from_dict({})
    create_derived_transaction_portfolio_request = CreateDerivedTransactionPortfolioRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_derived_portfolio(scope, create_derived_transaction_portfolio_request=create_derived_transaction_portfolio_request, opts=opts)

        # CreateDerivedPortfolio: Create derived portfolio
        api_response = api_instance.create_derived_portfolio(scope, create_derived_transaction_portfolio_request=create_derived_transaction_portfolio_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DerivedTransactionPortfoliosApi->create_derived_portfolio: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the derived transaction portfolio. | 
 **create_derived_transaction_portfolio_request** | [**CreateDerivedTransactionPortfolioRequest**](CreateDerivedTransactionPortfolioRequest.md)| The definition of the derived transaction portfolio. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created derived portfolio, with populated id |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_derived_portfolio_details**
> DeletedEntityResponse delete_derived_portfolio_details(scope, code, effective_at=effective_at)

[EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details

Delete all the portfolio details for a derived transaction portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DerivedTransactionPortfoliosApi
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
    api_instance = api_client_factory.build(DerivedTransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the derived transaction portfolio.
    code = 'code_example' # str | The code of the derived transaction portfolio. Together with the scope this uniquely identifies              the derived transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective date of the change. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_derived_portfolio_details(scope, code, effective_at=effective_at, opts=opts)

        # [EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details
        api_response = api_instance.delete_derived_portfolio_details(scope, code, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DerivedTransactionPortfoliosApi->delete_derived_portfolio_details: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the derived transaction portfolio. | 
 **code** | **str**| The code of the derived transaction portfolio. Together with the scope this uniquely identifies              the derived transaction portfolio. | 
 **effective_at** | **str**| The effective date of the change. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

