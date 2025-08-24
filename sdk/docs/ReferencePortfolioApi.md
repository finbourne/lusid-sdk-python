# lusid.ReferencePortfolioApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reference_portfolio**](ReferencePortfolioApi.md#create_reference_portfolio) | **POST** /api/referenceportfolios/{scope} | CreateReferencePortfolio: Create reference portfolio
[**get_reference_portfolio_constituents**](ReferencePortfolioApi.md#get_reference_portfolio_constituents) | **GET** /api/referenceportfolios/{scope}/{code}/constituents | GetReferencePortfolioConstituents: Get reference portfolio constituents
[**list_constituents_adjustments**](ReferencePortfolioApi.md#list_constituents_adjustments) | **GET** /api/referenceportfolios/{scope}/{code}/constituentsadjustments | ListConstituentsAdjustments: List constituents adjustments
[**upsert_reference_portfolio_constituent_properties**](ReferencePortfolioApi.md#upsert_reference_portfolio_constituent_properties) | **POST** /api/referenceportfolios/{scope}/{code}/constituents/properties | [EARLY ACCESS] UpsertReferencePortfolioConstituentProperties: Upsert constituent properties
[**upsert_reference_portfolio_constituents**](ReferencePortfolioApi.md#upsert_reference_portfolio_constituents) | **POST** /api/referenceportfolios/{scope}/{code}/constituents | UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents


# **create_reference_portfolio**
> Portfolio create_reference_portfolio(scope, create_reference_portfolio_request)

CreateReferencePortfolio: Create reference portfolio

Create a reference portfolio in a particular scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReferencePortfolioApi
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
    api_instance = api_client_factory.build(ReferencePortfolioApi)
    scope = 'scope_example' # str | The scope in which to create the reference portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_reference_portfolio_request = CreateReferencePortfolioRequest.from_json("")
    # create_reference_portfolio_request = CreateReferencePortfolioRequest.from_dict({})
    create_reference_portfolio_request = CreateReferencePortfolioRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_reference_portfolio(scope, create_reference_portfolio_request, opts=opts)

        # CreateReferencePortfolio: Create reference portfolio
        api_response = api_instance.create_reference_portfolio(scope, create_reference_portfolio_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReferencePortfolioApi->create_reference_portfolio: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the reference portfolio. | 
 **create_reference_portfolio_request** | [**CreateReferencePortfolioRequest**](CreateReferencePortfolioRequest.md)| The definition of the reference portfolio. | 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created reference portfolio, with populated id |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_reference_portfolio_constituents**
> GetReferencePortfolioConstituentsResponse get_reference_portfolio_constituents(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

GetReferencePortfolioConstituents: Get reference portfolio constituents

Get constituents from a reference portfolio at a particular effective time.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReferencePortfolioApi
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
    api_instance = api_client_factory.build(ReferencePortfolioApi)
    scope = 'scope_example' # str | The scope of the reference portfolio.
    code = 'code_example' # str | The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio.
    effective_at = 'effective_at_example' # str | The effective date of the constituents to retrieve. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve constituents. Defaults to return the latest version              of each constituent if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument' or 'ReferenceHolding' domain to decorate onto              constituents. These take the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or              'ReferenceHolding/strategy/quantsignal'. Defaults to return all available instrument and reference holding properties if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_reference_portfolio_constituents(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, opts=opts)

        # GetReferencePortfolioConstituents: Get reference portfolio constituents
        api_response = api_instance.get_reference_portfolio_constituents(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReferencePortfolioApi->get_reference_portfolio_constituents: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | 
 **effective_at** | **str**| The effective date of the constituents to retrieve. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve constituents. Defaults to return the latest version              of each constituent if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39; or &#39;ReferenceHolding&#39; domain to decorate onto              constituents. These take the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or              &#39;ReferenceHolding/strategy/quantsignal&#39;. Defaults to return all available instrument and reference holding properties if not specified. | [optional] 

### Return type

[**GetReferencePortfolioConstituentsResponse**](GetReferencePortfolioConstituentsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reference portfolio constituents |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_constituents_adjustments**
> ResourceListOfConstituentsAdjustmentHeader list_constituents_adjustments(scope, code, from_effective_at, to_effective_at, as_at_time=as_at_time)

ListConstituentsAdjustments: List constituents adjustments

List adjustments made to constituents in a reference portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReferencePortfolioApi
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
    api_instance = api_client_factory.build(ReferencePortfolioApi)
    scope = 'scope_example' # str | The scope of the reference portfolio.
    code = 'code_example' # str | The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio.
    from_effective_at = 'from_effective_at_example' # str | Events between this time (inclusive) and the toEffectiveAt are returned.
    to_effective_at = 'to_effective_at_example' # str | Events between this time (inclusive) and the fromEffectiveAt are returned.
    as_at_time = '2013-10-20T19:20:30+01:00' # datetime | The asAt time for which the result is valid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_constituents_adjustments(scope, code, from_effective_at, to_effective_at, as_at_time=as_at_time, opts=opts)

        # ListConstituentsAdjustments: List constituents adjustments
        api_response = api_instance.list_constituents_adjustments(scope, code, from_effective_at, to_effective_at, as_at_time=as_at_time)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReferencePortfolioApi->list_constituents_adjustments: %s\n" % e)

main()
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_reference_portfolio_constituent_properties**
> UpsertReferencePortfolioConstituentPropertiesResponse upsert_reference_portfolio_constituent_properties(scope, code, upsert_reference_portfolio_constituent_properties_request)

[EARLY ACCESS] UpsertReferencePortfolioConstituentProperties: Upsert constituent properties

Create or update one or more constituent properties for a single constituent in the reference portfolio.  Each property will be updated if it already exists, created if it does not and deleted if value is null.  Both constituent and portfolio must exist at the time when properties are created or updated.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReferencePortfolioApi
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
    api_instance = api_client_factory.build(ReferencePortfolioApi)
    scope = 'scope_example' # str | The scope of the reference portfolio.
    code = 'code_example' # str | The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_reference_portfolio_constituent_properties_request = UpsertReferencePortfolioConstituentPropertiesRequest.from_json("")
    # upsert_reference_portfolio_constituent_properties_request = UpsertReferencePortfolioConstituentPropertiesRequest.from_dict({})
    upsert_reference_portfolio_constituent_properties_request = UpsertReferencePortfolioConstituentPropertiesRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_reference_portfolio_constituent_properties(scope, code, upsert_reference_portfolio_constituent_properties_request, opts=opts)

        # [EARLY ACCESS] UpsertReferencePortfolioConstituentProperties: Upsert constituent properties
        api_response = api_instance.upsert_reference_portfolio_constituent_properties(scope, code, upsert_reference_portfolio_constituent_properties_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReferencePortfolioApi->upsert_reference_portfolio_constituent_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | 
 **upsert_reference_portfolio_constituent_properties_request** | [**UpsertReferencePortfolioConstituentPropertiesRequest**](UpsertReferencePortfolioConstituentPropertiesRequest.md)| The request to modify properties for the constituent. | 

### Return type

[**UpsertReferencePortfolioConstituentPropertiesResponse**](UpsertReferencePortfolioConstituentPropertiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_reference_portfolio_constituents**
> UpsertReferencePortfolioConstituentsResponse upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request)

UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents

Add constituents to a reference portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReferencePortfolioApi
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
    api_instance = api_client_factory.build(ReferencePortfolioApi)
    scope = 'scope_example' # str | The scope of the reference portfolio.
    code = 'code_example' # str | The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_reference_portfolio_constituents_request = UpsertReferencePortfolioConstituentsRequest.from_json("")
    # upsert_reference_portfolio_constituents_request = UpsertReferencePortfolioConstituentsRequest.from_dict({})
    upsert_reference_portfolio_constituents_request = UpsertReferencePortfolioConstituentsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request, opts=opts)

        # UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents
        api_response = api_instance.upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReferencePortfolioApi->upsert_reference_portfolio_constituents: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | 
 **upsert_reference_portfolio_constituents_request** | [**UpsertReferencePortfolioConstituentsRequest**](UpsertReferencePortfolioConstituentsRequest.md)| The constituents to upload to the reference portfolio. | 

### Return type

[**UpsertReferencePortfolioConstituentsResponse**](UpsertReferencePortfolioConstituentsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

