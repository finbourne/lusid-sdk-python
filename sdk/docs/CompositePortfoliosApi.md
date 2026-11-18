# lusid.CompositePortfoliosApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_composite_portfolio_membership**](CompositePortfoliosApi.md#change_composite_portfolio_membership) | **POST** /api/compositeportfolios/{scope}/{code}/constituents | [EXPERIMENTAL] ChangeCompositePortfolioMembership: Change composite portfolio membership
[**create_composite_portfolio**](CompositePortfoliosApi.md#create_composite_portfolio) | **POST** /api/compositeportfolios/{scope} | [EXPERIMENTAL] CreateCompositePortfolio: Create composite portfolio


# **change_composite_portfolio_membership**
> PortfolioWithWarnings change_composite_portfolio_membership(scope, code, change_composite_portfolio_membership_request=change_composite_portfolio_membership_request)

[EXPERIMENTAL] ChangeCompositePortfolioMembership: Change composite portfolio membership

Add a constituent to a composite portfolio. The constituent contributes its whole history, so it joins no  later than its own creation date, which is taken when no FromDate is supplied.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CompositePortfoliosApi
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
    api_instance = api_client_factory.build(CompositePortfoliosApi)
    scope = 'scope_example' # str | The scope of the composite portfolio.
    code = 'code_example' # str | The code of the composite portfolio. Together with the scope this uniquely identifies              the composite portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # change_composite_portfolio_membership_request = ChangeCompositePortfolioMembershipRequest.from_json("")
    # change_composite_portfolio_membership_request = ChangeCompositePortfolioMembershipRequest.from_dict({})
    change_composite_portfolio_membership_request = ChangeCompositePortfolioMembershipRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.change_composite_portfolio_membership(scope, code, change_composite_portfolio_membership_request=change_composite_portfolio_membership_request, opts=opts)

        # [EXPERIMENTAL] ChangeCompositePortfolioMembership: Change composite portfolio membership
        api_response = api_instance.change_composite_portfolio_membership(scope, code, change_composite_portfolio_membership_request=change_composite_portfolio_membership_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CompositePortfoliosApi->change_composite_portfolio_membership: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the composite portfolio. | 
 **code** | **str**| The code of the composite portfolio. Together with the scope this uniquely identifies              the composite portfolio. | 
 **change_composite_portfolio_membership_request** | [**ChangeCompositePortfolioMembershipRequest**](ChangeCompositePortfolioMembershipRequest.md)| The membership change to apply. | [optional] 

### Return type

[**PortfolioWithWarnings**](PortfolioWithWarnings.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The composite portfolio with its membership changed, and any warnings about its configuration |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_composite_portfolio**
> PortfolioWithWarnings create_composite_portfolio(scope, create_composite_portfolio_request=create_composite_portfolio_request)

[EXPERIMENTAL] CreateCompositePortfolio: Create composite portfolio

Create a composite portfolio from a set of constituent portfolios. Every constituent must be a transaction  portfolio or a derived transaction portfolio, and must share the base currency of the composite portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CompositePortfoliosApi
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
    api_instance = api_client_factory.build(CompositePortfoliosApi)
    scope = 'scope_example' # str | The scope in which to create the composite portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_composite_portfolio_request = CreateCompositePortfolioRequest.from_json("")
    # create_composite_portfolio_request = CreateCompositePortfolioRequest.from_dict({})
    create_composite_portfolio_request = CreateCompositePortfolioRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_composite_portfolio(scope, create_composite_portfolio_request=create_composite_portfolio_request, opts=opts)

        # [EXPERIMENTAL] CreateCompositePortfolio: Create composite portfolio
        api_response = api_instance.create_composite_portfolio(scope, create_composite_portfolio_request=create_composite_portfolio_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CompositePortfoliosApi->create_composite_portfolio: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the composite portfolio. | 
 **create_composite_portfolio_request** | [**CreateCompositePortfolioRequest**](CreateCompositePortfolioRequest.md)| The definition of the composite portfolio. | [optional] 

### Return type

[**PortfolioWithWarnings**](PortfolioWithWarnings.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created composite portfolio, with populated id, and any warnings about its configuration |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

