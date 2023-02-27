# lusid.ReconciliationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reconcile_generic**](ReconciliationsApi.md#reconcile_generic) | **POST** /api/portfolios/$reconcileGeneric | ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are &#39;empty&#39; or null or zero.
[**reconcile_holdings**](ReconciliationsApi.md#reconcile_holdings) | **POST** /api/portfolios/$reconcileholdings | [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
[**reconcile_inline**](ReconciliationsApi.md#reconcile_inline) | **POST** /api/portfolios/$reconcileInline | ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
[**reconcile_valuation**](ReconciliationsApi.md#reconcile_valuation) | **POST** /api/portfolios/$reconcileValuation | ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.


# **reconcile_generic**
> ReconciliationResponse reconcile_generic(reconciliation_request=reconciliation_request)

ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are 'empty' or null or zero.

Perform evaluation of one or two set of holdings (a portfolio of instruments) using one or two (potentially different) configuration recipes.  Produce a breakdown of the resulting differences in evaluation that can be iterated through.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ReconciliationsApi(api_client)
    reconciliation_request = {"left":{"recipeId":{"scope":"MySourceScope","code":"MySourcePortfolioCode"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Sum","options":{}}],"groupBy":["Instrument/default/Name"],"sort":[],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]}},"right":{"recipeId":{"scope":"MyTargetScope","code":"MyTargetPortfolioCode"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Sum","options":{}}],"groupBy":["Instrument/default/Name"],"sort":[],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]}},"leftToRightMapping":[],"comparisonRules":[{"comparisonType":"AbsoluteDifference","tolerance":1.2345,"appliesTo":{"key":"Holding/default/PV","op":"Sum","options":{}},"ruleType":"ReconcileNumericRule"}],"preserveKeys":["Instrument/default/Name"]} # ReconciliationRequest | The specifications of the inputs to the reconciliation (optional)

    try:
        # ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are 'empty' or null or zero.
        api_response = api_instance.reconcile_generic(reconciliation_request=reconciliation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_generic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reconciliation_request** | [**ReconciliationRequest**](ReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ReconciliationResponse**](ReconciliationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_holdings**
> ResourceListOfReconciliationBreak reconcile_holdings(sort_by=sort_by, start=start, limit=limit, filter=filter, portfolios_reconciliation_request=portfolios_reconciliation_request)

[EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings

Reconcile the holdings of two portfolios.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ReconciliationsApi(api_client)
    sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set.              For example, to filter on the left portfolio Code, use \"left.portfolioId.code eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
portfolios_reconciliation_request = {"left":{"portfolioId":{"scope":"MySourceScope","code":"MySourcePortfolioCode"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","asAt":"2018-03-05T00:00:00.0000000+00:00"},"right":{"portfolioId":{"scope":"MyTargetScope","code":"MyTargetPortfolioCode"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","asAt":"2018-03-05T00:00:00.0000000+00:00"},"instrumentPropertyKeys":["Instrument/default/Name"]} # PortfoliosReconciliationRequest | The specifications of the inputs to the reconciliation (optional)

    try:
        # [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
        api_response = api_instance.reconcile_holdings(sort_by=sort_by, start=start, limit=limit, filter=filter, portfolios_reconciliation_request=portfolios_reconciliation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.              For example, to filter on the left portfolio Code, use \&quot;left.portfolioId.code eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **portfolios_reconciliation_request** | [**PortfoliosReconciliationRequest**](PortfoliosReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_inline**
> ListAggregationReconciliation reconcile_inline(inline_valuations_reconciliation_request=inline_valuations_reconciliation_request)

ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.

Perform valuation of one or two set of inline instruments using different one or two configuration recipes. Produce a breakdown of the resulting differences in valuation.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ReconciliationsApi(api_client)
    inline_valuations_reconciliation_request = {"left":{"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Value","options":{}}],"groupBy":["Instrument/default/Name"],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]},"instruments":[{"quantity":10000,"holdingIdentifier":"fx-fwd-GBPUSD","instrument":{"startDate":"2018-03-01T00:00:00.0000000+00:00","maturityDate":"2018-03-30T00:00:00.0000000+00:00","domAmount":100,"domCcy":"GBP","fgnAmount":-150,"fgnCcy":"USD","refSpotRate":1.5,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","instrumentType":"FxForward"}}]},"right":{"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Value","options":{}}],"groupBy":["Instrument/default/Name"],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]},"instruments":[{"quantity":10000,"holdingIdentifier":"fx-fwd-GBPJPY","instrument":{"startDate":"2018-03-01T00:00:00.0000000+00:00","maturityDate":"2018-03-30T00:00:00.0000000+00:00","domAmount":100,"domCcy":"GBP","fgnAmount":-150,"fgnCcy":"JPY","refSpotRate":132,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","instrumentType":"FxForward"}}]},"leftToRightMapping":[],"preserveKeys":[]} # InlineValuationsReconciliationRequest | The specifications of the inputs to the reconciliation (optional)

    try:
        # ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
        api_response = api_instance.reconcile_inline(inline_valuations_reconciliation_request=inline_valuations_reconciliation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_inline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_valuations_reconciliation_request** | [**InlineValuationsReconciliationRequest**](InlineValuationsReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ListAggregationReconciliation**](ListAggregationReconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_valuation**
> ListAggregationReconciliation reconcile_valuation(valuations_reconciliation_request=valuations_reconciliation_request)

ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.

Perform valuation of one or two set of holdings using different one or two configuration recipes. Produce a breakdown of the resulting differences in valuation.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ReconciliationsApi(api_client)
    valuations_reconciliation_request = {"left":{"recipeId":{"scope":"MySourceScope","code":"MySourcePortfolioCode"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Sum","options":{}}],"groupBy":["Instrument/default/Name"],"sort":[],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]}},"right":{"recipeId":{"scope":"MyTargetScope","code":"MyTargetPortfolioCode"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Sum","options":{}}],"groupBy":["Instrument/default/Name"],"sort":[],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]}},"leftToRightMapping":[],"preserveKeys":["Instrument/default/Name"]} # ValuationsReconciliationRequest | The specifications of the inputs to the reconciliation (optional)

    try:
        # ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
        api_response = api_instance.reconcile_valuation(valuations_reconciliation_request=valuations_reconciliation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_valuation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valuations_reconciliation_request** | [**ValuationsReconciliationRequest**](ValuationsReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ListAggregationReconciliation**](ListAggregationReconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

