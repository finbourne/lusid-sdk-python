# lusid.SubscriptionsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subscription**](SubscriptionsApi.md#delete_subscription) | **DELETE** /api/subscriptions/holdings/{scope}/{code} | [EARLY ACCESS] DeleteSubscription: Delete a Subscription, assuming that it is present.
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /api/subscriptions/holdings/{scope}/{code} | [EARLY ACCESS] GetSubscription: Get Subscription
[**list_subscriptions**](SubscriptionsApi.md#list_subscriptions) | **GET** /api/subscriptions/holdings/{scope} | [EARLY ACCESS] ListSubscriptions: List the set of Subscription definitions
[**upsert_subscription**](SubscriptionsApi.md#upsert_subscription) | **POST** /api/subscriptions/holdings | [EARLY ACCESS] UpsertSubscription: Upsert a Subscription. This creates or updates the subscription definition in LUSID.


# **delete_subscription**
> AnnulSingleStructuredDataResponse delete_subscription(scope, code)

[EARLY ACCESS] DeleteSubscription: Delete a Subscription, assuming that it is present.

Delete the specified Subscription definition from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SubscriptionsApi
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
    api_instance = api_client_factory.build(SubscriptionsApi)
    scope = 'scope_example' # str | The scope of the Subscription to delete.
    code = 'code_example' # str | The Subscription to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_subscription(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteSubscription: Delete a Subscription, assuming that it is present.
        api_response = api_instance.delete_subscription(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SubscriptionsApi->delete_subscription: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Subscription to delete. | 
 **code** | **str**| The Subscription to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_subscription**
> GetSubscriptionResponse get_subscription(scope, code, as_at=as_at)

[EARLY ACCESS] GetSubscription: Get Subscription

Get a Subscription definition from a single scope.                The response will return either the subscription that has been stored, or a failure explaining why the request was unsuccessful.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SubscriptionsApi
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
    api_instance = api_client_factory.build(SubscriptionsApi)
    scope = 'scope_example' # str | The scope of the Subscription to retrieve.
    code = 'code_example' # str | The code of the Subscription to retrieve.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Subscription. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_subscription(scope, code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetSubscription: Get Subscription
        api_response = api_instance.get_subscription(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Subscription to retrieve. | 
 **code** | **str**| The code of the Subscription to retrieve. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Subscription. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetSubscriptionResponse**](GetSubscriptionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Subscription or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_subscriptions**
> PagedResourceListOfGetSubscriptionResponse list_subscriptions(scope, as_at=as_at, filter=filter, limit=limit, page=page)

[EARLY ACCESS] ListSubscriptions: List the set of Subscription definitions

List the set of subscription definitions at the specified date/time and scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SubscriptionsApi
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
    api_instance = api_client_factory.build(SubscriptionsApi)
    scope = 'scope_example' # str | The scope to list subscriptions for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the subscriptions. Defaults to latest if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)
    limit = 56 # int | Maximum number of results to return. Defaults to 100. (optional)
    page = 'page_example' # str | Pagination token from a previous result to fetch the next page. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_subscriptions(scope, as_at=as_at, filter=filter, limit=limit, page=page, opts=opts)

        # [EARLY ACCESS] ListSubscriptions: List the set of Subscription definitions
        api_response = api_instance.list_subscriptions(scope, as_at=as_at, filter=filter, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SubscriptionsApi->list_subscriptions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to list subscriptions for. | 
 **as_at** | **datetime**| The asAt datetime at which to list the subscriptions. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| Maximum number of results to return. Defaults to 100. | [optional] 
 **page** | **str**| Pagination token from a previous result to fetch the next page. | [optional] 

### Return type

[**PagedResourceListOfGetSubscriptionResponse**](PagedResourceListOfGetSubscriptionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested subscriptions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_subscription**
> UpsertSingleStructuredDataResponse upsert_subscription(upsert_subscription_request)

[EARLY ACCESS] UpsertSubscription: Upsert a Subscription. This creates or updates the subscription definition in LUSID.

Update or insert one Subscription definition. An item will be updated if it already exists  and inserted if it does not.                The referenced portfolio (and timeline, when supplied) must exist and be readable by the caller.                The response will return the successfully updated or inserted subscription or failure message if unsuccessful.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SubscriptionsApi
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
    api_instance = api_client_factory.build(SubscriptionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_subscription_request = UpsertSubscriptionRequest.from_json("")
    # upsert_subscription_request = UpsertSubscriptionRequest.from_dict({})
    upsert_subscription_request = UpsertSubscriptionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_subscription(upsert_subscription_request, opts=opts)

        # [EARLY ACCESS] UpsertSubscription: Upsert a Subscription. This creates or updates the subscription definition in LUSID.
        api_response = api_instance.upsert_subscription(upsert_subscription_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SubscriptionsApi->upsert_subscription: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_subscription_request** | [**UpsertSubscriptionRequest**](UpsertSubscriptionRequest.md)| The Subscription to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

