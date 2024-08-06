# lusid.AggregationApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_configuration_recipe**](AggregationApi.md#generate_configuration_recipe) | **POST** /api/aggregation/{scope}/{code}/$generateconfigurationrecipe | [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
[**get_queryable_keys**](AggregationApi.md#get_queryable_keys) | **GET** /api/results/queryable/keys | GetQueryableKeys: Query the set of supported \&quot;addresses\&quot; that can be queried from the aggregation endpoint.
[**get_valuation**](AggregationApi.md#get_valuation) | **POST** /api/aggregation/$valuation | GetValuation: Perform valuation for a list of portfolios and/or portfolio groups
[**get_valuation_of_weighted_instruments**](AggregationApi.md#get_valuation_of_weighted_instruments) | **POST** /api/aggregation/$valuationinlined | GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio


# **generate_configuration_recipe**
> ConfigurationRecipe generate_configuration_recipe(scope, code, create_recipe_request=create_recipe_request)

[EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.

Given a set of scopes, a portfolio Id and a basic recipe, this endpoint generates a configuration recipe with relevant rules that can value the instruments in the portfolio.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    AggregationApi
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
        api_instance = api_client_factory.build(AggregationApi)
        scope = 'scope_example' # str | The scope of the portfolio
        code = 'code_example' # str | The code of the portfolio

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_recipe_request = CreateRecipeRequest()
        # create_recipe_request = CreateRecipeRequest.from_json("")
        create_recipe_request = CreateRecipeRequest.from_dict({"recipeCreationMarketDataScopes":["MyScope"],"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00"}) # CreateRecipeRequest | The request specifying the parameters to generating the recipe (optional)

        try:
            # [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
            api_response = await api_instance.generate_configuration_recipe(scope, code, create_recipe_request=create_recipe_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AggregationApi->generate_configuration_recipe: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **create_recipe_request** | [**CreateRecipeRequest**](CreateRecipeRequest.md)| The request specifying the parameters to generating the recipe | [optional] 

### Return type

[**ConfigurationRecipe**](ConfigurationRecipe.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_queryable_keys**
> ResourceListOfAggregationQuery get_queryable_keys(page=page, limit=limit, filter=filter)

GetQueryableKeys: Query the set of supported \"addresses\" that can be queried from the aggregation endpoint.

When a request is made for aggregation, the user needs to know what keys can be passed to it for queryable data. This endpoint allows to queries to provide the set of keys,  what they are and what they return.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    AggregationApi
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
        api_instance = api_client_factory.build(AggregationApi)
        page = 'page_example' # str | The pagination token to use to continue listing queryable keys from a previous call to list queryable keys.              This value is returned from the previous call. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # GetQueryableKeys: Query the set of supported \"addresses\" that can be queried from the aggregation endpoint.
            api_response = await api_instance.get_queryable_keys(page=page, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AggregationApi->get_queryable_keys: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing queryable keys from a previous call to list queryable keys.              This value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfAggregationQuery**](ResourceListOfAggregationQuery.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation**
> ListAggregationResponse get_valuation(valuation_request=valuation_request)

GetValuation: Perform valuation for a list of portfolios and/or portfolio groups

Perform valuation on specified list of portfolio and/or portfolio groups for a set of dates.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    AggregationApi
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
        api_instance = api_client_factory.build(AggregationApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # valuation_request = ValuationRequest()
        # valuation_request = ValuationRequest.from_json("")
        valuation_request = ValuationRequest.from_dict({"recipeId":{"scope":"MyRecipeScope","code":"default"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Valuation/PV","op":"Value","options":{}}],"groupBy":["Instrument/default/Name"],"sort":[{"key":"Instrument/default/RIC","sortOrder":"Ascending"}],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"None","holidayCalendars":[],"valuationDateTimes":[],"businessDayConvention":"F"}}) # ValuationRequest | The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics (optional)

        try:
            # GetValuation: Perform valuation for a list of portfolios and/or portfolio groups
            api_response = await api_instance.get_valuation(valuation_request=valuation_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AggregationApi->get_valuation: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valuation_request** | [**ValuationRequest**](ValuationRequest.md)| The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation_of_weighted_instruments**
> ListAggregationResponse get_valuation_of_weighted_instruments(inline_valuation_request=inline_valuation_request)

GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio

Perform valuation on the portfolio that is defined by the weighted set of instruments passed to the request.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    AggregationApi
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
        api_instance = api_client_factory.build(AggregationApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # inline_valuation_request = InlineValuationRequest()
        # inline_valuation_request = InlineValuationRequest.from_json("")
        inline_valuation_request = InlineValuationRequest.from_dict({"recipeId":{"scope":"MyRecipeScope","code":"default"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Valuation/PV","op":"Value","options":{}}],"groupBy":["Instrument/default/Name"],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"None","holidayCalendars":[],"valuationDateTimes":[],"businessDayConvention":"F"},"instruments":[{"quantity":10000,"holdingIdentifier":"my-holding-on-some-date","instrument":{"startDate":"2018-03-05T00:00:00.0000000+00:00","maturityDate":"2018-04-04T00:00:00.0000000+00:00","domAmount":100,"domCcy":"GBP","fgnAmount":-150,"fgnCcy":"USD","refSpotRate":1.5,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","bookedAsSpot":false,"instrumentType":"FxForward"},"inLineLookupIdentifiers":{}}]}) # InlineValuationRequest | The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics (optional)

        try:
            # GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio
            api_response = await api_instance.get_valuation_of_weighted_instruments(inline_valuation_request=inline_valuation_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AggregationApi->get_valuation_of_weighted_instruments: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_valuation_request** | [**InlineValuationRequest**](InlineValuationRequest.md)| The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

