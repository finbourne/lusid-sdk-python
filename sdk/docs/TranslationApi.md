# lusid.TranslationApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translate_instrument_definitions**](TranslationApi.md#translate_instrument_definitions) | **POST** /api/translation/instrumentdefinitions | [EXPERIMENTAL] TranslateInstrumentDefinitions: Translate instruments
[**translate_trade_tickets**](TranslationApi.md#translate_trade_tickets) | **POST** /api/translation/tradetickets | [EXPERIMENTAL] TranslateTradeTickets: Translate trade ticket


# **translate_instrument_definitions**
> TranslateInstrumentDefinitionsResponse translate_instrument_definitions(translate_instrument_definitions_request)

[EXPERIMENTAL] TranslateInstrumentDefinitions: Translate instruments

Translates one or more instruments into the given target dialect.              In the request each instrument definition should be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.              Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument.              The response will return both the collection of successfully translated instruments in the target dialect, as well as those that failed. For the failures a reason will be provided explaining why the instrument could not be updated or inserted.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TranslationApi
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
    api_instance = api_client_factory.build(TranslationApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # translate_instrument_definitions_request = TranslateInstrumentDefinitionsRequest.from_json("")
    # translate_instrument_definitions_request = TranslateInstrumentDefinitionsRequest.from_dict({})
    translate_instrument_definitions_request = TranslateInstrumentDefinitionsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.translate_instrument_definitions(translate_instrument_definitions_request, opts=opts)

        # [EXPERIMENTAL] TranslateInstrumentDefinitions: Translate instruments
        api_response = api_instance.translate_instrument_definitions(translate_instrument_definitions_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TranslationApi->translate_instrument_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_instrument_definitions_request** | [**TranslateInstrumentDefinitionsRequest**](TranslateInstrumentDefinitionsRequest.md)| The definitions of the instruments to translate along with the target dialect. | 

### Return type

[**TranslateInstrumentDefinitionsResponse**](TranslateInstrumentDefinitionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully translated instruments along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **translate_trade_tickets**
> TranslateTradeTicketsResponse translate_trade_tickets(translate_trade_ticket_request)

[EXPERIMENTAL] TranslateTradeTickets: Translate trade ticket

Translates one or more trade tickets into the given target dialect.              In the request each trade ticket definition should be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID. It serves only as a way to easily identify each trade ticket in the response.              The response will return both the collection of successfully translated trade tickets in the target dialect, as well as those that failed. For the failures a reason will be provided explaining why the trade ticket could not be updated or inserted.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TranslationApi
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
    api_instance = api_client_factory.build(TranslationApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # translate_trade_ticket_request = TranslateTradeTicketRequest.from_json("")
    # translate_trade_ticket_request = TranslateTradeTicketRequest.from_dict({})
    translate_trade_ticket_request = TranslateTradeTicketRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.translate_trade_tickets(translate_trade_ticket_request, opts=opts)

        # [EXPERIMENTAL] TranslateTradeTickets: Translate trade ticket
        api_response = api_instance.translate_trade_tickets(translate_trade_ticket_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TranslationApi->translate_trade_tickets: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_trade_ticket_request** | [**TranslateTradeTicketRequest**](TranslateTradeTicketRequest.md)| The definitions of the trade ticket to translate along with the target dialect. | 

### Return type

[**TranslateTradeTicketsResponse**](TranslateTradeTicketsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully translated trade ticket along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

