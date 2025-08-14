# lusid.SimplePositionPortfoliosApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_simple_position_portfolio**](SimplePositionPortfoliosApi.md#create_simple_position_portfolio) | **POST** /api/simpleposition/{scope} | [EARLY ACCESS] CreateSimplePositionPortfolio: Create simple position portfolio


# **create_simple_position_portfolio**
> Portfolio create_simple_position_portfolio(scope, create_simple_position_portfolio_request)

[EARLY ACCESS] CreateSimplePositionPortfolio: Create simple position portfolio

Create a simple position portfolio in a particular scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SimplePositionPortfoliosApi
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
    api_instance = api_client_factory.build(SimplePositionPortfoliosApi)
    scope = 'scope_example' # str | The scope in which to create the simple position portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_simple_position_portfolio_request = CreateSimplePositionPortfolioRequest.from_json("")
    # create_simple_position_portfolio_request = CreateSimplePositionPortfolioRequest.from_dict({})
    create_simple_position_portfolio_request = CreateSimplePositionPortfolioRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_simple_position_portfolio(scope, create_simple_position_portfolio_request, opts=opts)

        # [EARLY ACCESS] CreateSimplePositionPortfolio: Create simple position portfolio
        api_response = api_instance.create_simple_position_portfolio(scope, create_simple_position_portfolio_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SimplePositionPortfoliosApi->create_simple_position_portfolio: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the simple position portfolio. | 
 **create_simple_position_portfolio_request** | [**CreateSimplePositionPortfolioRequest**](CreateSimplePositionPortfolioRequest.md)| The definition of the simple position portfolio. | 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created simple position portfolio, with populated id |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

