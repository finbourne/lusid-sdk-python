# lusid.DerivedTransactionPortfoliosApi

All URIs are relative to *http://local-unit-test-server.lusid.com:49585*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_derived_portfolio**](DerivedTransactionPortfoliosApi.md#create_derived_portfolio) | **POST** /api/derivedtransactionportfolios/{scope} | [EARLY ACCESS] CreateDerivedPortfolio: Create derived portfolio
[**delete_derived_portfolio_details**](DerivedTransactionPortfoliosApi.md#delete_derived_portfolio_details) | **DELETE** /api/derivedtransactionportfolios/{scope}/{code}/details | [EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details


# **create_derived_portfolio**
> Portfolio create_derived_portfolio(scope, create_derived_transaction_portfolio_request=create_derived_transaction_portfolio_request)

[EARLY ACCESS] CreateDerivedPortfolio: Create derived portfolio

Create a derived transaction portfolio from a parent transaction portfolio (which may itself be derived).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:49585
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:49585"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:49585"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.DerivedTransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope in which to create the derived transaction portfolio.
create_derived_transaction_portfolio_request = {"displayName":"MyDerivedPortfolioName","description":"Example long form portfolio description","code":"MyDerivedPortfolioCode","parentPortfolioId":{"scope":"MyParentPortfolioScope","code":"MyParentPortfolioCode"},"created":"2018-03-05T00:00:00.0000000+00:00","corporateActionSourceId":{"scope":"MyScope","code":"MyCorporateActionSourceId"},"accountingMethod":"FirstInFirstOut","subHoldingKeys":["Transaction/MyScope/Strategy","Transaction/MyScope/SubAccount"]} # CreateDerivedTransactionPortfolioRequest | The definition of the derived transaction portfolio. (optional)

    try:
        # [EARLY ACCESS] CreateDerivedPortfolio: Create derived portfolio
        api_response = api_instance.create_derived_portfolio(scope, create_derived_transaction_portfolio_request=create_derived_transaction_portfolio_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DerivedTransactionPortfoliosApi->create_derived_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the derived transaction portfolio. | 
 **create_derived_transaction_portfolio_request** | [**CreateDerivedTransactionPortfolioRequest**](CreateDerivedTransactionPortfolioRequest.md)| The definition of the derived transaction portfolio. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created derived portfolio, with populated id |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_derived_portfolio_details**
> DeletedEntityResponse delete_derived_portfolio_details(scope, code, effective_at=effective_at)

[EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details

Delete all the portfolio details for a derived transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:49585
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:49585"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:49585"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.DerivedTransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the derived transaction portfolio.
code = 'code_example' # str | The code of the derived transaction portfolio. Together with the scope this uniquely identifies              the derived transaction portfolio.
effective_at = 'effective_at_example' # str | The effective date of the change. (optional)

    try:
        # [EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details
        api_response = api_instance.delete_derived_portfolio_details(scope, code, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DerivedTransactionPortfoliosApi->delete_derived_portfolio_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the derived transaction portfolio. | 
 **code** | **str**| The code of the derived transaction portfolio. Together with the scope this uniquely identifies              the derived transaction portfolio. | 
 **effective_at** | **str**| The effective date of the change. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

