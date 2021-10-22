# lusid.ReferencePortfolioApi

All URIs are relative to *http://local-unit-test-server.lusid.com:31220*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reference_portfolio**](ReferencePortfolioApi.md#create_reference_portfolio) | **POST** /api/referenceportfolios/{scope} | CreateReferencePortfolio: Create reference portfolio
[**get_reference_portfolio_constituents**](ReferencePortfolioApi.md#get_reference_portfolio_constituents) | **GET** /api/referenceportfolios/{scope}/{code}/constituents | GetReferencePortfolioConstituents: Get reference portfolio constituents
[**list_constituents_adjustments**](ReferencePortfolioApi.md#list_constituents_adjustments) | **GET** /api/referenceportfolios/{scope}/{code}/constituentsadjustments | ListConstituentsAdjustments: List constituents adjustments
[**upsert_reference_portfolio_constituents**](ReferencePortfolioApi.md#upsert_reference_portfolio_constituents) | **POST** /api/referenceportfolios/{scope}/{code}/constituents | UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents


# **create_reference_portfolio**
> Portfolio create_reference_portfolio(scope, create_reference_portfolio_request)

CreateReferencePortfolio: Create reference portfolio

Create a reference portfolio in a particular scope.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:31220
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:31220"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:31220"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ReferencePortfolioApi(api_client)
    scope = 'scope_example' # str | The scope in which to create the reference portfolio.
create_reference_portfolio_request = {"displayName":"MyPortfolioName","description":"Description of my portfolio","code":"MyPortfolioCode","created":"2018-03-05T00:00:00.0000000+00:00","properties":{}} # CreateReferencePortfolioRequest | The definition of the reference portfolio.

    try:
        # CreateReferencePortfolio: Create reference portfolio
        api_response = api_instance.create_reference_portfolio(scope, create_reference_portfolio_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReferencePortfolioApi->create_reference_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the reference portfolio. | 
 **create_reference_portfolio_request** | [**CreateReferencePortfolioRequest**](CreateReferencePortfolioRequest.md)| The definition of the reference portfolio. | 

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
**201** | The created reference portfolio, with populated id |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_portfolio_constituents**
> GetReferencePortfolioConstituentsResponse get_reference_portfolio_constituents(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

GetReferencePortfolioConstituents: Get reference portfolio constituents

Get constituents from a reference portfolio at a particular effective time.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:31220
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:31220"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:31220"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ReferencePortfolioApi(api_client)
    scope = 'scope_example' # str | The scope of the reference portfolio.
code = 'code_example' # str | The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio.
effective_at = 'effective_at_example' # str | The effective date of the constituents to retrieve. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve constituents. Defaults to return the latest version              of each constituent if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'Instrument' or 'ReferenceHolding' domain to decorate onto              constituents. These take the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or              'ReferenceHolding/strategy/quantsignal'. Defaults to return all available instrument and reference holding properties if not specified. (optional)

    try:
        # GetReferencePortfolioConstituents: Get reference portfolio constituents
        api_response = api_instance.get_reference_portfolio_constituents(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReferencePortfolioApi->get_reference_portfolio_constituents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | 
 **effective_at** | **str**| The effective date of the constituents to retrieve. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve constituents. Defaults to return the latest version              of each constituent if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;Instrument&#39; or &#39;ReferenceHolding&#39; domain to decorate onto              constituents. These take the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or              &#39;ReferenceHolding/strategy/quantsignal&#39;. Defaults to return all available instrument and reference holding properties if not specified. | [optional] 

### Return type

[**GetReferencePortfolioConstituentsResponse**](GetReferencePortfolioConstituentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reference portfolio constituents |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_constituents_adjustments**
> ResourceListOfConstituentsAdjustmentHeader list_constituents_adjustments(scope, code, from_effective_at, to_effective_at, as_at_time=as_at_time)

ListConstituentsAdjustments: List constituents adjustments

List adjustments made to constituents in a reference portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:31220
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:31220"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:31220"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ReferencePortfolioApi(api_client)
    scope = 'scope_example' # str | The scope of the reference portfolio.
code = 'code_example' # str | The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio.
from_effective_at = 'from_effective_at_example' # str | Events between this time (inclusive) and the toEffectiveAt are returned.
to_effective_at = 'to_effective_at_example' # str | Events between this time (inclusive) and the fromEffectiveAt are returned.
as_at_time = '2013-10-20T19:20:30+01:00' # datetime | The asAt time for which the result is valid. (optional)

    try:
        # ListConstituentsAdjustments: List constituents adjustments
        api_response = api_instance.list_constituents_adjustments(scope, code, from_effective_at, to_effective_at, as_at_time=as_at_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReferencePortfolioApi->list_constituents_adjustments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | 
 **from_effective_at** | **str**| Events between this time (inclusive) and the toEffectiveAt are returned. | 
 **to_effective_at** | **str**| Events between this time (inclusive) and the fromEffectiveAt are returned. | 
 **as_at_time** | **datetime**| The asAt time for which the result is valid. | [optional] 

### Return type

[**ResourceListOfConstituentsAdjustmentHeader**](ResourceListOfConstituentsAdjustmentHeader.md)

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

# **upsert_reference_portfolio_constituents**
> UpsertReferencePortfolioConstituentsResponse upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request)

UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents

Add constituents to a reference portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:31220
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:31220"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:31220"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ReferencePortfolioApi(api_client)
    scope = 'scope_example' # str | The scope of the reference portfolio.
code = 'code_example' # str | The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio.
upsert_reference_portfolio_constituents_request = {"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","weightType":"Periodical","periodType":"Quarterly","periodCount":2,"constituents":[{"instrumentIdentifiers":{"instrument/default/Figi":"BBG0077GZM13","instrument/default/Isin":"GB00BH4HKS39"},"properties":{"portfolio/MyScope/MyPropertyKey":{"key":"Portfolio/MyScope/MyPropertyKey","value":{"metricValue":{"value":12345.5672,"unit":"Unit"}}}},"weight":100,"currency":"GBP"},{"instrumentIdentifiers":{"instrument/default/Figi":"BBG0077H2WN1","instrument/default/Isin":"US0378331005"},"properties":{},"weight":50,"currency":"USD"}]} # UpsertReferencePortfolioConstituentsRequest | The constituents to upload to the reference portfolio.

    try:
        # UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents
        api_response = api_instance.upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReferencePortfolioApi->upsert_reference_portfolio_constituents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | 
 **upsert_reference_portfolio_constituents_request** | [**UpsertReferencePortfolioConstituentsRequest**](UpsertReferencePortfolioConstituentsRequest.md)| The constituents to upload to the reference portfolio. | 

### Return type

[**UpsertReferencePortfolioConstituentsResponse**](UpsertReferencePortfolioConstituentsResponse.md)

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

