# lusid.ReferencePortfolioApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reference_portfolio**](ReferencePortfolioApi.md#create_reference_portfolio) | **POST** /api/referenceportfolios/{scope} | [EARLY ACCESS] Create reference portfolio
[**get_reference_portfolio_constituents**](ReferencePortfolioApi.md#get_reference_portfolio_constituents) | **GET** /api/referenceportfolios/{scope}/{code}/constituents | [EARLY ACCESS] Get constituents
[**list_constituents_adjustments**](ReferencePortfolioApi.md#list_constituents_adjustments) | **GET** /api/referenceportfolios/{scope}/{code}/constituentsadjustments | [EARLY ACCESS] Gets constituents adjustments in an interval of effective time.
[**upsert_reference_portfolio_constituents**](ReferencePortfolioApi.md#upsert_reference_portfolio_constituents) | **POST** /api/referenceportfolios/{scope}/{code}/constituents | [EARLY ACCESS] Add constituents


# **create_reference_portfolio**
> Portfolio create_reference_portfolio(scope, reference_portfolio=reference_portfolio)

[EARLY ACCESS] Create reference portfolio

Create a new reference portfolio.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.ReferencePortfolioApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The intended scope of the portfolio
reference_portfolio = lusid.CreateReferencePortfolioRequest() # CreateReferencePortfolioRequest | The portfolio creation request object (optional)

try:
    # [EARLY ACCESS] Create reference portfolio
    api_response = api_instance.create_reference_portfolio(scope, reference_portfolio=reference_portfolio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferencePortfolioApi->create_reference_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The intended scope of the portfolio | 
 **reference_portfolio** | [**CreateReferencePortfolioRequest**](CreateReferencePortfolioRequest.md)| The portfolio creation request object | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
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

[EARLY ACCESS] Get constituents

Get constituents from the specified reference portfolio at an effective time.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.ReferencePortfolioApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the reference portfolio.
code = 'code_example' # str | The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio.
effective_at = 'effective_at_example' # str | The effective date of the constituents to retrieve. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve constituents. Defaults to return the latest version              of each constituent if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" or \"ReferenceHolding\" domain to decorate onto              the constituents. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"ReferenceHolding/strategy/quantsignal\". Defaults to return all available instrument and reference holding properties if not specified. (optional)

try:
    # [EARLY ACCESS] Get constituents
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
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;ReferenceHolding\&quot; domain to decorate onto              the constituents. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;ReferenceHolding/strategy/quantsignal\&quot;. Defaults to return all available instrument and reference holding properties if not specified. | [optional] 

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
> ResourceListOfConstituentsAdjustmentHeader list_constituents_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at_time=as_at_time)

[EARLY ACCESS] Gets constituents adjustments in an interval of effective time.

Specify a time period in which you'd like to see the list of times that adjustments where made to this portfolio

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.ReferencePortfolioApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | Code for the portfolio
from_effective_at = 'from_effective_at_example' # str | Events between this time (inclusive) and the toEffectiveAt are returned. (optional)
to_effective_at = 'to_effective_at_example' # str | Events between this time (inclusive) and the fromEffectiveAt are returned. (optional)
as_at_time = '2013-10-20T19:20:30+01:00' # datetime | The as-at time for which the result is valid. (optional)

try:
    # [EARLY ACCESS] Gets constituents adjustments in an interval of effective time.
    api_response = api_instance.list_constituents_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at_time=as_at_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferencePortfolioApi->list_constituents_adjustments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| Code for the portfolio | 
 **from_effective_at** | **str**| Events between this time (inclusive) and the toEffectiveAt are returned. | [optional] 
 **to_effective_at** | **str**| Events between this time (inclusive) and the fromEffectiveAt are returned. | [optional] 
 **as_at_time** | **datetime**| The as-at time for which the result is valid. | [optional] 

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
> UpsertReferencePortfolioConstituentsResponse upsert_reference_portfolio_constituents(scope, code, constituents=constituents)

[EARLY ACCESS] Add constituents

Add constituents to the specified reference portfolio.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.ReferencePortfolioApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
constituents = lusid.UpsertReferencePortfolioConstituentsRequest() # UpsertReferencePortfolioConstituentsRequest | The constituents to upload to the portfolio (optional)

try:
    # [EARLY ACCESS] Add constituents
    api_response = api_instance.upsert_reference_portfolio_constituents(scope, code, constituents=constituents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferencePortfolioApi->upsert_reference_portfolio_constituents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **constituents** | [**UpsertReferencePortfolioConstituentsRequest**](UpsertReferencePortfolioConstituentsRequest.md)| The constituents to upload to the portfolio | [optional] 

### Return type

[**UpsertReferencePortfolioConstituentsResponse**](UpsertReferencePortfolioConstituentsResponse.md)

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

