# lusid.SettlementActivityApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_settlement_activity**](SettlementActivityApi.md#query_settlement_activity) | **POST** /api/settlementactivities/$query | [EARLY ACCESS] QuerySettlementActivity: Query Settlement Activity


# **query_settlement_activity**
> ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery query_settlement_activity(settlement_activity_query)

[EARLY ACCESS] QuerySettlementActivity: Query Settlement Activity

Queries settlement activity (Expected and Settled) for the specified portfolios and/or portfolio groups.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SettlementActivityApi
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
    api_instance = api_client_factory.build(SettlementActivityApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # settlement_activity_query = SettlementActivityQuery.from_json("")
    # settlement_activity_query = SettlementActivityQuery.from_dict({})
    settlement_activity_query = SettlementActivityQuery()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.query_settlement_activity(settlement_activity_query, opts=opts)

        # [EARLY ACCESS] QuerySettlementActivity: Query Settlement Activity
        api_response = api_instance.query_settlement_activity(settlement_activity_query)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SettlementActivityApi->query_settlement_activity: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_activity_query** | [**SettlementActivityQuery**](SettlementActivityQuery.md)| The query parameters controlling which settlement activity is returned. | 

### Return type

[**ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery**](ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested settlement activity for the specified portfolios and portfolio groups |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

