# lusid.ComplexMarketDataApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_complex_market_data**](ComplexMarketDataApi.md#delete_complex_market_data) | **POST** /api/complexmarketdata/{scope}/$delete | [EARLY ACCESS] DeleteComplexMarketData: Delete one or more items of complex market data, assuming they are present.
[**get_complex_market_data**](ComplexMarketDataApi.md#get_complex_market_data) | **POST** /api/complexmarketdata/{scope}/$get | [EARLY ACCESS] GetComplexMarketData: Get complex market data
[**list_complex_market_data**](ComplexMarketDataApi.md#list_complex_market_data) | **GET** /api/complexmarketdata | [EXPERIMENTAL] ListComplexMarketData: List the set of ComplexMarketData
[**upsert_complex_market_data**](ComplexMarketDataApi.md#upsert_complex_market_data) | **POST** /api/complexmarketdata/{scope} | UpsertComplexMarketData: Upsert a set of complex market data items. This creates or updates the data in Lusid.


# **delete_complex_market_data**
> AnnulStructuredDataResponse delete_complex_market_data(scope, request_body)

[EARLY ACCESS] DeleteComplexMarketData: Delete one or more items of complex market data, assuming they are present.

Delete one or more specified complex market data items from a single scope. Each item is identified by a unique id which includes  information about its type as well as the exact effective datetime (to the microsecond) at which it entered the system (became valid).                In the request each complex market data item must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each quote in the response.                The response will return both the collection of successfully deleted  complex market data items, as well as those that failed.  For the failures a reason will be provided explaining why the it could not be deleted.                It is important to always check the failed set for any unsuccessful results.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ComplexMarketDataApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ComplexMarketDataApi)
        scope = 'scope_example' # str | The scope of the complex market data to delete.
        request_body = {"first-item":{"provider":"DataScope","priceSource":"Some Bank Plc","lineage":"Swaps Desk Trader A","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","marketAsset":"USDOIS"},"second-item":{"provider":"DataScope","priceSource":"AN.Other Bank Plc","lineage":"Swaps Desk Trader B","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","marketAsset":"RBS"}} # Dict[str, ComplexMarketDataId] | The complex market data Ids to delete, each keyed by a unique correlation id.

        try:
            # [EARLY ACCESS] DeleteComplexMarketData: Delete one or more items of complex market data, assuming they are present.
            api_response = await api_instance.delete_complex_market_data(scope, request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ComplexMarketDataApi->delete_complex_market_data: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the complex market data to delete. | 
 **request_body** | [**Dict[str, ComplexMarketDataId]**](ComplexMarketDataId.md)| The complex market data Ids to delete, each keyed by a unique correlation id. | 

### Return type

[**AnnulStructuredDataResponse**](AnnulStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully deleted ComplexMarketData along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_complex_market_data**
> GetComplexMarketDataResponse get_complex_market_data(scope, request_body, effective_at=effective_at, as_at=as_at, max_age=max_age)

[EARLY ACCESS] GetComplexMarketData: Get complex market data

Get one or more items of complex market data from a single scope.                Each item can be identified by its time invariant complex market data identifier.                For each id LUSID will return the most recent matched item with respect to the provided (or default) effective datetime.                An optional maximum age range window can be specified which defines how far back to look back for data from the specified effective datetime.  LUSID will return the most recent item within this window.                In the request each complex market data id must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each item in the response.                The response will return three collections. One, the successfully retrieved complex market data. Two, those that had a  valid identifier but could not be found. Three, those that failed because LUSID could not construct a valid identifier from the request.                For the ids that failed to resolve or could not be found a reason will be provided explaining why that is the case.                It is important to always check the failed and not found sets for any unsuccessful results.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ComplexMarketDataApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ComplexMarketDataApi)
        scope = 'scope_example' # str | The scope of the complex market data to retrieve.
        request_body = {"first-item":{"provider":"DataScope","priceSource":"Some Bank Plc","lineage":"Swaps Desk Trader A","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","marketAsset":"USDOIS"},"second-item":{"provider":"DataScope","priceSource":"AN.Other Bank Plc","lineage":"Swaps Desk Trader B","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","marketAsset":"RBS"}} # Dict[str, ComplexMarketDataId] | The time invariant set of complex data identifiers to retrieve the data for. These need to be               keyed by a unique correlation id allowing the retrieved item to be identified in the response.
        effective_at = 'effective_at_example' # str | The effective datetime at which to retrieve the complex market data.               Defaults to the current LUSID system datetime if not specified.               Must match the Effective at of each ComplexMarketDataId given in the request body. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the complex market data. Defaults to return the latest version if not specified. (optional)
        max_age = 'max_age_example' # str | The duration of the look back window in an ISO8601 time interval format e.g. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a complex market data item must exist to be retrieved. (optional)

        try:
            # [EARLY ACCESS] GetComplexMarketData: Get complex market data
            api_response = await api_instance.get_complex_market_data(scope, request_body, effective_at=effective_at, as_at=as_at, max_age=max_age)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ComplexMarketDataApi->get_complex_market_data: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the complex market data to retrieve. | 
 **request_body** | [**Dict[str, ComplexMarketDataId]**](ComplexMarketDataId.md)| The time invariant set of complex data identifiers to retrieve the data for. These need to be               keyed by a unique correlation id allowing the retrieved item to be identified in the response. | 
 **effective_at** | **str**| The effective datetime at which to retrieve the complex market data.               Defaults to the current LUSID system datetime if not specified.               Must match the Effective at of each ComplexMarketDataId given in the request body. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the complex market data. Defaults to return the latest version if not specified. | [optional] 
 **max_age** | **str**| The duration of the look back window in an ISO8601 time interval format e.g. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a complex market data item must exist to be retrieved. | [optional] 

### Return type

[**GetComplexMarketDataResponse**](GetComplexMarketDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved complex market data along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_complex_market_data**
> ResourceListOfListComplexMarketDataWithMetaDataResponse list_complex_market_data(as_at=as_at)

[EXPERIMENTAL] ListComplexMarketData: List the set of ComplexMarketData

List the set of ComplexMarketData at the specified date/time,  along with the scope the data was stored in and its identifier in that scope.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ComplexMarketDataApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ComplexMarketDataApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the ComplexMarketData. Defaults to latest if not specified. (optional)

        try:
            # [EXPERIMENTAL] ListComplexMarketData: List the set of ComplexMarketData
            api_response = await api_instance.list_complex_market_data(as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ComplexMarketDataApi->list_complex_market_data: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the ComplexMarketData. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfListComplexMarketDataWithMetaDataResponse**](ResourceListOfListComplexMarketDataWithMetaDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested ComplexMarketData |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_complex_market_data**
> UpsertStructuredDataResponse upsert_complex_market_data(scope, request_body)

UpsertComplexMarketData: Upsert a set of complex market data items. This creates or updates the data in Lusid.

Update or insert one or more complex market data items in a single scope. An item will be updated if it already exists  and inserted if it does not.                In the request each complex market data item must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each complex market data in the response.                The response will return both the collection of successfully updated or inserted complex market data, as well as those that failed.  For the failures a reason will be provided explaining why the item could not be updated or inserted.                It is important to always check the failed set for any unsuccessful results.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ComplexMarketDataApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ComplexMarketDataApi)
        scope = 'scope_example' # str | The scope to use when updating or inserting the complex market data.
        request_body = {"first-item":{"marketDataId":{"provider":"DataScope","priceSource":"Some Bank Plc","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","marketAsset":"USD/USDOIS"},"marketData":{"baseDate":"1970-01-01T00:00:00.0000000+00:00","dates":["1970-01-01T00:00:00.0000000+00:00"],"discountFactors":[1],"lineage":"SomeLineage","marketDataOptions":{"dayCountConvention":"Actual365","frontExtrapolationType":"Linear","backExtrapolationType":"None","marketDataOptionsType":"CurveOptions"},"marketDataType":"DiscountFactorCurveData"}},"second-item":{"marketDataId":{"provider":"Lusid","effectiveAt":"2021-01-20T00:00:00.0000000+00:00","marketAsset":"EUR/USD/FxFwdCurve"},"marketData":{"baseDate":"2021-01-20T00:00:00.0000000+00:00","domCcy":"EUR","fgnCcy":"USD","tenors":["1D","1W","2W","3W","1M","2M","3M","4M","5M","6M","9M","1Y","15M","18M","2Y","3Y"],"pipRates":[0.6375,1.4975,3.0275,4.5625,6.7525,19.5125,27.3225,34.0625,41.5175,49.2025,74.8125,104.9125,141.1925,176.8375,260.1475,453.2625],"lineage":"","marketDataOptions":{"dayCountConvention":"Actual365","frontExtrapolationType":"Flat","backExtrapolationType":"Flat","marketDataOptionsType":"CurveOptions"},"calendars":[],"spotDaysCalculationType":"SingleCalendar","marketDataType":"FxForwardTenorPipsCurveData"}},"third-item":{"marketDataId":{"provider":"Lusid","effectiveAt":"2021-01-20T00:00:00.0000000+00:00","marketAsset":"USD/JPY/FxVol/Ln"},"marketData":{"baseDate":"2021-01-20T00:00:00.0000000+00:00","assetType":"FxVol","lineage":"Some-market-data-provider-or-other","volatility":0.15,"marketDataType":"ConstantVolatilitySurface"}}} # Dict[str, UpsertComplexMarketDataRequest] | The set of complex market data items to update or insert keyed by a unique correlation id.

        try:
            # UpsertComplexMarketData: Upsert a set of complex market data items. This creates or updates the data in Lusid.
            api_response = await api_instance.upsert_complex_market_data(scope, request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ComplexMarketDataApi->upsert_complex_market_data: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the complex market data. | 
 **request_body** | [**Dict[str, UpsertComplexMarketDataRequest]**](UpsertComplexMarketDataRequest.md)| The set of complex market data items to update or insert keyed by a unique correlation id. | 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted ComplexMarketData along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

