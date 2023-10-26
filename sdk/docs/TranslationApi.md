# lusid.TranslationApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translate_instrument_definitions**](TranslationApi.md#translate_instrument_definitions) | **POST** /api/translation/instrumentdefinitions | [EXPERIMENTAL] TranslateInstrumentDefinitions: Translate instruments
[**translate_trade_tickets**](TranslationApi.md#translate_trade_tickets) | **POST** /api/translation/tradetickets | [EXPERIMENTAL] TranslateTradeTickets: Translate trade ticket


# **translate_instrument_definitions**
> TranslateInstrumentDefinitionsResponse translate_instrument_definitions(translate_instrument_definitions_request)

[EXPERIMENTAL] TranslateInstrumentDefinitions: Translate instruments

Translates one or more instruments into the given target dialect.                In the request each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument.                The response will return both the collection of successfully translated instruments in the target dialect,  as well as those that failed.  For the failures a reason will be provided explaining why the instrument could not be updated or inserted.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.translate_instrument_definitions_request import TranslateInstrumentDefinitionsRequest
from lusid.models.translate_instrument_definitions_response import TranslateInstrumentDefinitionsResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TranslationApi)
    translate_instrument_definitions_request = {"instruments":{"MyFavouriteInstrument":{"instrumentFormat":{"sourceSystem":"someSource","vendor":"someVendor","version":"someVersion"},"content":"{\"InstrumentContentShouldBeGivenAsAJsonString\": \"OrAnXmlString\"}","instrumentType":"ExoticInstrument"},"MyFavouriteLusidInstrument":{"startDate":"2018-01-01T00:00:00.0000000+00:00","maturityDate":"2019-01-01T00:00:00.0000000+00:00","domAmount":1,"domCcy":"GBP","fgnAmount":-1.5,"fgnCcy":"USD","refSpotRate":1.5,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","instrumentType":"FxForward"}},"dialect":"targetDialect"} # TranslateInstrumentDefinitionsRequest | The definitions of the instruments to translate along with the target dialect.

    try:
        # [EXPERIMENTAL] TranslateInstrumentDefinitions: Translate instruments
        api_response = await api_instance.translate_instrument_definitions(translate_instrument_definitions_request)
        print("The response of TranslationApi->translate_instrument_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->translate_instrument_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_instrument_definitions_request** | [**TranslateInstrumentDefinitionsRequest**](TranslateInstrumentDefinitionsRequest.md)| The definitions of the instruments to translate along with the target dialect. | 

### Return type

[**TranslateInstrumentDefinitionsResponse**](TranslateInstrumentDefinitionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully translated instruments along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_trade_tickets**
> TranslateTradeTicketsResponse translate_trade_tickets(translate_trade_ticket_request)

[EXPERIMENTAL] TranslateTradeTickets: Translate trade ticket

Translates one or more trade tickets into the given target dialect.                In the request each trade ticket definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each trade ticket in the response.                The response will return both the collection of successfully translated trade tickets in the target dialect,  as well as those that failed.  For the failures a reason will be provided explaining why the trade ticket could not be updated or inserted.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.translate_trade_ticket_request import TranslateTradeTicketRequest
from lusid.models.translate_trade_tickets_response import TranslateTradeTicketsResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TranslationApi)
    translate_trade_ticket_request = {"tickets":{"MyTicket":{"transactionId":"TradeTicket-1111111","transactionType":"OpenTradeTicket","source":"default","transactionDate":"2020-01-01T09:00:00.00Z","settlementDate":"2020-01-01T09:00:00.00Z","totalConsideration":{"amount":1020000,"currency":"GBP"},"units":1000000,"instrumentIdentifiers":{"Instrument/default/ClientInternal":"my-bond"},"instrumentScope":"myScope","instrumentName":"my_bond","instrumentDefinition":{"startDate":"2018-01-01T00:00:00.0000000+00:00","maturityDate":"2019-01-01T00:00:00.0000000+00:00","domAmount":1,"domCcy":"GBP","fgnAmount":-1.5,"fgnCcy":"USD","refSpotRate":1.5,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","instrumentType":"FxForward"},"counterpartyAgreementId":{"scope":"demoScope","code":"myCounterparty"},"tradeTicketType":"LusidTradeTicket"}},"dialect":"targetDialect"} # TranslateTradeTicketRequest | The definitions of the trade ticket to translate along with the target dialect.

    try:
        # [EXPERIMENTAL] TranslateTradeTickets: Translate trade ticket
        api_response = await api_instance.translate_trade_tickets(translate_trade_ticket_request)
        print("The response of TranslationApi->translate_trade_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->translate_trade_tickets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_trade_ticket_request** | [**TranslateTradeTicketRequest**](TranslateTradeTicketRequest.md)| The definitions of the trade ticket to translate along with the target dialect. | 

### Return type

[**TranslateTradeTicketsResponse**](TranslateTradeTicketsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully translated trade ticket along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

