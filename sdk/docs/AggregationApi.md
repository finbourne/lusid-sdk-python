# lusid.AggregationApi

All URIs are relative to *http://local-unit-test-server.lusid.com:63021*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_valuation**](AggregationApi.md#get_valuation) | **POST** /api/aggregation/$valuation | GetValuation: Perform valuation for a list of portfolios and/or portfolio groups
[**get_valuation_of_weighted_instruments**](AggregationApi.md#get_valuation_of_weighted_instruments) | **POST** /api/aggregation/$valuationinlined | GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio


# **get_valuation**
> ListAggregationResponse get_valuation(valuation_request=valuation_request)

GetValuation: Perform valuation for a list of portfolios and/or portfolio groups

Perform valuation on specified list of portfolio and/or portfolio groups for a set of dates.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:63021
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:63021"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:63021"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AggregationApi(api_client)
    valuation_request = {"recipeId":{"scope":"MyRecipeScope","code":"default"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value"},{"key":"Holding/default/PV","op":"Value"}],"groupBy":["Instrument/default/Name"],"sort":[{"key":"Instrument/default/RIC","sortOrder":"Ascending"}],"reportCurrency":"USD","equipWithSubtotals":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]}} # ValuationRequest | The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics (optional)

    try:
        # GetValuation: Perform valuation for a list of portfolios and/or portfolio groups
        api_response = api_instance.get_valuation(valuation_request=valuation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AggregationApi->get_valuation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valuation_request** | [**ValuationRequest**](ValuationRequest.md)| The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_valuation_of_weighted_instruments**
> ListAggregationResponse get_valuation_of_weighted_instruments(inline_valuation_request=inline_valuation_request)

GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio

Perform valuation on the portfolio that is defined by the weighted set of instruments passed to the request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:63021
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:63021"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:63021"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AggregationApi(api_client)
    inline_valuation_request = {"recipeId":{"scope":"MyRecipeScope","code":"default"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value"},{"key":"Holding/default/PV","op":"Value"}],"groupBy":["Instrument/default/Name"],"reportCurrency":"USD","equipWithSubtotals":false,"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]},"instruments":[{"quantity":10000,"holdingIdentifier":"my-holding-on-some-date","instrument":{"startDate":"2018-03-05T00:00:00.0000000+00:00","maturityDate":"2018-04-04T00:00:00.0000000+00:00","domAmount":100,"domCcy":"GBP","fgnAmount":-150,"fgnCcy":"USD","refSpotRate":1.5,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","instrumentType":"FxForward"}}]} # InlineValuationRequest | The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics (optional)

    try:
        # GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio
        api_response = api_instance.get_valuation_of_weighted_instruments(inline_valuation_request=inline_valuation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AggregationApi->get_valuation_of_weighted_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_valuation_request** | [**InlineValuationRequest**](InlineValuationRequest.md)| The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

