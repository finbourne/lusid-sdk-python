# lusid.DerivedTransactionPortfoliosApi

All URIs are relative to *http://localhost:43406*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_derived_portfolio**](DerivedTransactionPortfoliosApi.md#create_derived_portfolio) | **POST** /api/derivedtransactionportfolios/{scope} | [EARLY ACCESS] Create derived transaction portfolio
[**delete_derived_portfolio_details**](DerivedTransactionPortfoliosApi.md#delete_derived_portfolio_details) | **DELETE** /api/derivedtransactionportfolios/{scope}/{code}/details | [EARLY ACCESS] Delete portfolio details


# **create_derived_portfolio**
> Portfolio create_derived_portfolio(scope, create_derived_transaction_portfolio_request=create_derived_transaction_portfolio_request)

[EARLY ACCESS] Create derived transaction portfolio

Creates a transaction portfolio that derives from an existing transaction portfolio. In a derived portfolio, parts of the portfolio can either be specific to this portfolio, or can be inherited from a \"parent\". Different parts of the portfolio (e.g. transactions or properties) are combined in different ways. The portfolio details are either overridden in entirety, or not at all. The same is true for properties. Transactions on a derived portfolio are merged with its parent portfolio's transactions. If the parent portfolio is itself a derived portfolio, transactions from that parent are also merged (and that parent's portfolio's, if it is also a derived portfolio, and so on).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:43406
configuration.host = "http://localhost:43406"
# Create an instance of the API class
api_instance = lusid.DerivedTransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope into which to create the new derived portfolio
create_derived_transaction_portfolio_request = {"displayName":"MyDerivedPortfolioName","description":"Example long form portfolio description","code":"MyDerivedPortfolioCode","parentPortfolioId":{"scope":"MyParentPortfolioScope","code":"MyParentPortfolioCode"},"created":"2018-03-05T00:00:00.0000000+00:00","corporateActionSourceId":{"scope":"MyScope","code":"MyCorporateActionSourceId"},"accountingMethod":"FirstInFirstOut","subHoldingKeys":["Transaction/MyScope/Strategy","Transaction/MyScope/SubAccount"]} # CreateDerivedTransactionPortfolioRequest | The root object of the new derived portfolio, containing a populated reference portfolio id and reference scope (optional)

try:
    # [EARLY ACCESS] Create derived transaction portfolio
    api_response = api_instance.create_derived_portfolio(scope, create_derived_transaction_portfolio_request=create_derived_transaction_portfolio_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedTransactionPortfoliosApi->create_derived_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope into which to create the new derived portfolio | 
 **create_derived_transaction_portfolio_request** | [**CreateDerivedTransactionPortfolioRequest**](CreateDerivedTransactionPortfolioRequest.md)| The root object of the new derived portfolio, containing a populated reference portfolio id and reference scope | [optional] 

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

[EARLY ACCESS] Delete portfolio details

Deletes the portfolio details for the specified derived transaction portfolio

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:43406
configuration.host = "http://localhost:43406"
# Create an instance of the API class
api_instance = lusid.DerivedTransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = 'effective_at_example' # str | The effective date of the change (optional)

try:
    # [EARLY ACCESS] Delete portfolio details
    api_response = api_instance.delete_derived_portfolio_details(scope, code, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedTransactionPortfoliosApi->delete_derived_portfolio_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **str**| The effective date of the change | [optional] 

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

