# lusid.MarketDataFieldConfigurationApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_market_data_field_configuration**](MarketDataFieldConfigurationApi.md#get_market_data_field_configuration) | **GET** /api/marketdata/fieldconfiguration/{marketDataCategory} | [EARLY ACCESS] GetMarketDataFieldConfiguration: Get a Market Data Field Configuration
[**update_market_data_field_configuration**](MarketDataFieldConfigurationApi.md#update_market_data_field_configuration) | **POST** /api/marketdata/fieldconfiguration/{marketDataCategory}/$update | [EARLY ACCESS] UpdateMarketDataFieldConfiguration: Update a Market Data Field Configuration


# **get_market_data_field_configuration**
> MarketDataFieldConfiguration get_market_data_field_configuration(market_data_category, as_at=as_at)

[EARLY ACCESS] GetMarketDataFieldConfiguration: Get a Market Data Field Configuration

Retrieve the market data field configuration for a given market data category.  If the configuration does not yet exist, an empty configuration will be returned.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    MarketDataFieldConfigurationApi
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
    api_instance = api_client_factory.build(MarketDataFieldConfigurationApi)
    market_data_category = 'market_data_category_example' # str | The market data category.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the configuration. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_market_data_field_configuration(market_data_category, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetMarketDataFieldConfiguration: Get a Market Data Field Configuration
        api_response = api_instance.get_market_data_field_configuration(market_data_category, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MarketDataFieldConfigurationApi->get_market_data_field_configuration: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_data_category** | **str**| The market data category. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the configuration. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**MarketDataFieldConfiguration**](MarketDataFieldConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested market data field configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_market_data_field_configuration**
> MarketDataFieldConfiguration update_market_data_field_configuration(market_data_category, update_market_data_field_configuration_request)

[EARLY ACCESS] UpdateMarketDataFieldConfiguration: Update a Market Data Field Configuration

Update the metadata field schema for a market data field configuration.  Allows adding, updating, and removing metadata field definitions.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    MarketDataFieldConfigurationApi
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
    api_instance = api_client_factory.build(MarketDataFieldConfigurationApi)
    market_data_category = 'market_data_category_example' # str | The market data category.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_market_data_field_configuration_request = UpdateMarketDataFieldConfigurationRequest.from_json("")
    # update_market_data_field_configuration_request = UpdateMarketDataFieldConfigurationRequest.from_dict({})
    update_market_data_field_configuration_request = UpdateMarketDataFieldConfigurationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_market_data_field_configuration(market_data_category, update_market_data_field_configuration_request, opts=opts)

        # [EARLY ACCESS] UpdateMarketDataFieldConfiguration: Update a Market Data Field Configuration
        api_response = api_instance.update_market_data_field_configuration(market_data_category, update_market_data_field_configuration_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MarketDataFieldConfigurationApi->update_market_data_field_configuration: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_data_category** | **str**| The market data category. | 
 **update_market_data_field_configuration_request** | [**UpdateMarketDataFieldConfigurationRequest**](UpdateMarketDataFieldConfigurationRequest.md)| The metadata fields to add, update, or remove. | 

### Return type

[**MarketDataFieldConfiguration**](MarketDataFieldConfiguration.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated market data field configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

