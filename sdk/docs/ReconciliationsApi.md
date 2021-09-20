# lusid.ReconciliationsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:35247*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reconcile_holdings**](ReconciliationsApi.md#reconcile_holdings) | **POST** /api/portfolios/$reconcileholdings | [EARLY ACCESS] Reconcile portfolio holdings


# **reconcile_holdings**
> ResourceListOfReconciliationBreak reconcile_holdings(sort_by=sort_by, start=start, limit=limit, filter=filter, portfolios_reconciliation_request=portfolios_reconciliation_request)

[EARLY ACCESS] Reconcile portfolio holdings

Reconcile the holdings of two portfolios.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:35247
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:35247"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:35247"
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
        # [EARLY ACCESS] Reconcile portfolio holdings
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

