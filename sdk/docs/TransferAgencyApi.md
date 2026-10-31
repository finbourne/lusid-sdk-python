# lusid.TransferAgencyApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_order_dates**](TransferAgencyApi.md#calculate_order_dates) | **POST** /api/transferagency/orderdates | [EXPERIMENTAL] CalculateOrderDates: Calculate the key dates associated with transfer agency orders
[**cancel_transfer_agency_transactions**](TransferAgencyApi.md#cancel_transfer_agency_transactions) | **POST** /api/transferagency/transactions/cancel | [EXPERIMENTAL] CancelTransferAgencyTransactions: Cancel transfer agency transactions, un-pricing their orders
[**delete_transfer_agency_orders**](TransferAgencyApi.md#delete_transfer_agency_orders) | **POST** /api/transferagency/orders/$delete | [EXPERIMENTAL] DeleteTransferAgencyOrders: Delete transfer agency orders
[**estimate_transfer_agency_orders**](TransferAgencyApi.md#estimate_transfer_agency_orders) | **POST** /api/transferagency/orders/$estimate | [EXPERIMENTAL] EstimateTransferAgencyOrders: Estimate the values of transfer agency orders
[**upsert_external_transfer_agency_orders**](TransferAgencyApi.md#upsert_external_transfer_agency_orders) | **POST** /api/transferagency/orders/$external | [EARLY ACCESS] UpsertExternalTransferAgencyOrders: Load transfer agency orders sent by an external transfer agent
[**upsert_transfer_agency_orders**](TransferAgencyApi.md#upsert_transfer_agency_orders) | **POST** /api/transferagency/orders | [EXPERIMENTAL] UpsertTransferAgencyOrders: Upsert transfer agency orders
[**upsert_transfer_agency_transactions_from_orders**](TransferAgencyApi.md#upsert_transfer_agency_transactions_from_orders) | **POST** /api/transferagency/transactions/$fromOrders | [EXPERIMENTAL] UpsertTransferAgencyTransactionsFromOrders: Upsert transfer agency transactions from transfer agency orders


# **calculate_order_dates**
> CalculateOrderDatesResponse calculate_order_dates(request_body)

[EXPERIMENTAL] CalculateOrderDates: Calculate the key dates associated with transfer agency orders

The response contains both the collection of successfully calculated dates and any failed calculations,  each in the form of a dictionary keyed by the request's keys.  For each failure, a reason is provided. It is important to check the failed set for unsuccessful results.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransferAgencyApi
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
    api_instance = api_client_factory.build(TransferAgencyApi)
    request_body = {"calculation1":{"instrumentIdentifierType":"LusidInstrumentId","instrumentIdentifier":"LUID_00000000","instrumentScope":"MyScope","receivedDate":"2024-10-01T00:00:00.0000000+00:00","transactionCategory":"Subscription"}} # Dict[str, CalculateOrderDatesRequest] | The request containing the dates used for calculation

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.calculate_order_dates(request_body, opts=opts)

        # [EXPERIMENTAL] CalculateOrderDates: Calculate the key dates associated with transfer agency orders
        api_response = api_instance.calculate_order_dates(request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransferAgencyApi->calculate_order_dates: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, CalculateOrderDatesRequest]**](CalculateOrderDatesRequest.md)| The request containing the dates used for calculation | 

### Return type

[**CalculateOrderDatesResponse**](CalculateOrderDatesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully calculated dates and any failed calculations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **cancel_transfer_agency_transactions**
> CancelTransferAgencyTransactionsResponse cancel_transfer_agency_transactions(request_body, success_mode=success_mode)

[EXPERIMENTAL] CancelTransferAgencyTransactions: Cancel transfer agency transactions, un-pricing their orders

Reverses the pricing of a transfer agency order, identified by the security transaction that pricing booked:  cancels that transaction in the investor's portfolio, amends the paired cash transaction back to its  pre-pricing amount, and moves the order from 'Priced' back to 'New'. Both changes are bitemporal, so the  priced state is still visible at an earlier as-at.  A transaction that was never booked, that names no order, that is the cash leg rather than the security leg,  or whose order is not in 'Priced' fails on its own. A leg already cancelled outside this flow is left alone and  the order is still returned to 'New'. A transaction named under two request keys fails the whole request.  The response contains both successfully un-priced orders and any failures, each in the form of a  dictionary keyed by the request's keys. For each failure, a reason is provided. It is important to  check the failed set for unsuccessful results.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransferAgencyApi
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
    api_instance = api_client_factory.build(TransferAgencyApi)
    request_body = {"Transaction1":{"portfolioId":{"scope":"example-scope","code":"investor-portfolio"},"transactionId":"txn-0002"}} # Dict[str, CancelTransferAgencyTransactionRequest] | The security transactions to cancel, keyed by a unique request identifier.
    success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial (optional) (default to 'Partial')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.cancel_transfer_agency_transactions(request_body, success_mode=success_mode, opts=opts)

        # [EXPERIMENTAL] CancelTransferAgencyTransactions: Cancel transfer agency transactions, un-pricing their orders
        api_response = api_instance.cancel_transfer_agency_transactions(request_body, success_mode=success_mode)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransferAgencyApi->cancel_transfer_agency_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, CancelTransferAgencyTransactionRequest]**](CancelTransferAgencyTransactionRequest.md)| The security transactions to cancel, keyed by a unique request identifier. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | [optional] [default to &#39;Partial&#39;]

### Return type

[**CancelTransferAgencyTransactionsResponse**](CancelTransferAgencyTransactionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully un-priced orders and any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_transfer_agency_orders**
> DeleteTransferAgencyOrdersResponse delete_transfer_agency_orders(request_body)

[EXPERIMENTAL] DeleteTransferAgencyOrders: Delete transfer agency orders

Deletes each order supplied, cancelling any cash transaction(s) already booked for it. Only an order in  'New' or 'Pending' can be deleted. A priced order must be un-priced first. An order with no cash transaction  booked against it is deleted successfully and reports no cancelled transactions. Transaction staging rules are not applied to these  cancellations.  The response contains both successfully deleted orders and any failures, each in the form of a  dictionary keyed by the request's keys. For each failure, a reason is provided. It is important to  check the failed set for unsuccessful results.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransferAgencyApi
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
    api_instance = api_client_factory.build(TransferAgencyApi)
    request_body = {"Order1":{"orderId":{"scope":"example-scope","code":"order-1"}}} # Dict[str, DeleteTransferAgencyOrderRequest] | The transfer agency orders to delete, keyed by a unique request identifier.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_transfer_agency_orders(request_body, opts=opts)

        # [EXPERIMENTAL] DeleteTransferAgencyOrders: Delete transfer agency orders
        api_response = api_instance.delete_transfer_agency_orders(request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransferAgencyApi->delete_transfer_agency_orders: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, DeleteTransferAgencyOrderRequest]**](DeleteTransferAgencyOrderRequest.md)| The transfer agency orders to delete, keyed by a unique request identifier. | 

### Return type

[**DeleteTransferAgencyOrdersResponse**](DeleteTransferAgencyOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted orders and any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **estimate_transfer_agency_orders**
> EstimateTransferAgencyOrdersResponse estimate_transfer_agency_orders(request_body)

[EXPERIMENTAL] EstimateTransferAgencyOrders: Estimate the values of transfer agency orders

Estimates the units and the cash each order supplied would move, from the share class's most recent price.  Nothing is written.                An order may be named by its identifier, to estimate it as it stands, or supplied whole, to estimate values  that have not been saved yet. Both forms may appear in the same request. Where an order is supplied whole,  those values are estimated in place of the saved order's.                A switch or a transfer is two orders, and each leg is estimated independently.                The price is reported in the currency the share class is quoted in, which is not necessarily the order's  currency, so it is returned alongside that currency and the rate used.                The response contains both the successful estimates and any failures, each in the form of a dictionary  keyed by the request's keys. A share class with no price available fails only its own orders. It is  important to check the failed set for unsuccessful results.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransferAgencyApi
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
    api_instance = api_client_factory.build(TransferAgencyApi)
    request_body = {"Order1":{"orderId":{"scope":"example-scope","code":"order-1"}},"Order2":{"orderId":{"scope":"example-scope","code":"order-2"},"order":{"portfolioId":{"scope":"example-scope","code":"investor-1"},"instrumentIdentifierType":"LusidInstrumentId","instrumentIdentifier":"LUID_00000000","instrumentScope":"default","transactionCategory":"Subscription","currency":"GBP","amount":10000}}} # Dict[str, EstimateTransferAgencyOrderRequest] | The transfer agency orders to estimate, keyed by a unique request identifier.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.estimate_transfer_agency_orders(request_body, opts=opts)

        # [EXPERIMENTAL] EstimateTransferAgencyOrders: Estimate the values of transfer agency orders
        api_response = api_instance.estimate_transfer_agency_orders(request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransferAgencyApi->estimate_transfer_agency_orders: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, EstimateTransferAgencyOrderRequest]**](EstimateTransferAgencyOrderRequest.md)| The transfer agency orders to estimate, keyed by a unique request identifier. | 

### Return type

[**EstimateTransferAgencyOrdersResponse**](EstimateTransferAgencyOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully estimated orders and any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_external_transfer_agency_orders**
> UpsertExternalTransferAgencyOrdersResponse upsert_external_transfer_agency_orders(request_body)

[EARLY ACCESS] UpsertExternalTransferAgencyOrders: Load transfer agency orders sent by an external transfer agent

Loads the orders a third-party transfer agent dealt for a fund at a dealing point. Each request key names one  set: a fund, a dealing point, the sending source and the orders it dealt, each keyed by the source's own  line id. The orders are written in the fund's scope with the code  `{fundCode}-{source}-{yyyyMMddHHmmss}-{lineId}`, the dealing point written in UTC to the second, in the  External order state, priced at the dealing point, so the fund's External dealing source reads them at that  valuation point. A line whose code would exceed 64 characters is refused.                A set replaces what the same source sent before: every External order of that source for the fund's share  classes at the dealing point that the set does not restate is deleted, and the response names them. Two  sets in one request naming the same fund, source and dealing point are refused after the first.                The fund must list External among its dealing estimate sources. Each line must name a share class of the  fund and exactly one of a positive number of units or a positive amount in a valid currency. A set sent  after its dealing point is loaded and flagged late; one sent exactly at the dealing point is on time.  Whether the set is complete is recorded on each order and is not yet enforced at pricing.                Each order carries the properties `Order/TA/PriceDate` (date), `Order/TA/DealingSource` (string),  `Order/TA/DealingSourceReference` (string), `Order/TA/Complete` (string, `True` or `False`),  `Order/TA/Late` (string, `True` or `False`) and `Order/TA/SentAt` (date). LUSID does not create these  property definitions: define them in the domain, with those data types, before loading, as for the other  transfer agency order properties. A domain missing any of them fails the request with a property-not-defined  error and nothing is written.                Sets are validated independently: a set that fails validation is reported under failures and the others  still load. The sets that pass are then written together in one command, so a reader never sees half a  dealing point, and a refusal at write time fails the whole request and leaves the book as it was. A request  carries at most 200 sets and at most 2000 lines across all of them.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransferAgencyApi
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
    api_instance = api_client_factory.build(TransferAgencyApi)
    request_body = {"Set1":{"fundId":{"scope":"example-scope","code":"fund-1"},"dealingPoint":"2025-06-02T12:00:00.0000000+00:00","source":{"system":"ExampleTA","reference":"BATCH-20250602-001"},"complete":true,"sentAt":"2025-06-02T11:45:00.0000000+00:00","lines":{"line-1":{"instrumentIdentifierType":"ClientInternal","instrumentIdentifier":"FUND-1-CLASS-A","instrumentScope":"example-scope","tradeType":"Subscription","amount":{"value":100000,"currency":"GBP"}},"line-2":{"instrumentIdentifierType":"ClientInternal","instrumentIdentifier":"FUND-1-CLASS-A","instrumentScope":"example-scope","tradeType":"Redemption","units":2500}}}} # Dict[str, UpsertExternalTransferAgencyOrdersRequest] | The sets to load, keyed by a correlation key of the caller's choosing.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_external_transfer_agency_orders(request_body, opts=opts)

        # [EARLY ACCESS] UpsertExternalTransferAgencyOrders: Load transfer agency orders sent by an external transfer agent
        api_response = api_instance.upsert_external_transfer_agency_orders(request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransferAgencyApi->upsert_external_transfer_agency_orders: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, UpsertExternalTransferAgencyOrdersRequest]**](UpsertExternalTransferAgencyOrdersRequest.md)| The sets to load, keyed by a correlation key of the caller&#39;s choosing. | 

### Return type

[**UpsertExternalTransferAgencyOrdersResponse**](UpsertExternalTransferAgencyOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sets loaded and any that failed, keyed by the request key. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_transfer_agency_orders**
> TransferAgencyOrdersResponse upsert_transfer_agency_orders(request_body)

[EXPERIMENTAL] UpsertTransferAgencyOrders: Upsert transfer agency orders

Creates a cash transaction and updates the relevant order for each order supplied. An order must be in  'Pending' or 'New'. An order that already has a cash transaction has that transaction amended  to the order's current amount rather than a second one created.  The response contains both successfully processed orders and any failures, each in the form of a  dictionary keyed by the request's keys. For each failure, a reason is provided. It is important to  check the failed set for unsuccessful results.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransferAgencyApi
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
    api_instance = api_client_factory.build(TransferAgencyApi)
    request_body = {"Order1":{"orderId":{"scope":"example-scope","code":"order-1"}}} # Dict[str, UpsertTransferAgencyOrderRequest] | The transfer agency orders to upsert, keyed by a unique request identifier.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_transfer_agency_orders(request_body, opts=opts)

        # [EXPERIMENTAL] UpsertTransferAgencyOrders: Upsert transfer agency orders
        api_response = api_instance.upsert_transfer_agency_orders(request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransferAgencyApi->upsert_transfer_agency_orders: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, UpsertTransferAgencyOrderRequest]**](UpsertTransferAgencyOrderRequest.md)| The transfer agency orders to upsert, keyed by a unique request identifier. | 

### Return type

[**TransferAgencyOrdersResponse**](TransferAgencyOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed orders and any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_transfer_agency_transactions_from_orders**
> UpsertTransferAgencyTransactionsFromOrdersResponse upsert_transfer_agency_transactions_from_orders(request_body, success_mode=success_mode)

[EXPERIMENTAL] UpsertTransferAgencyTransactionsFromOrders: Upsert transfer agency transactions from transfer agency orders

This endpoint derives transactions from existing transfer agency orders. It does not upsert  caller-supplied ones.  Prices each order supplied, booking the security transaction into the investor's portfolio, amending the  paired cash transaction to the final settlement amount, and moving the order to 'Priced'. Only an order in  'New' can be priced, and the supplied price date must match the price date calculated when the order was  created.  The response contains both successfully priced orders and any failures, each in the form of a  dictionary keyed by the request's keys. For each failure, a reason is provided. It is important to  check the failed set for unsuccessful results.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransferAgencyApi
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
    api_instance = api_client_factory.build(TransferAgencyApi)
    request_body = {"Order1":{"orderId":{"scope":"example-scope","code":"order-1"},"priceDate":"2025-06-02T00:00:00.0000000+00:00"}} # Dict[str, UpsertTransferAgencyTransactionFromOrderRequest] | The transfer agency orders to price, keyed by a unique request identifier.
    success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial (optional) (default to 'Partial')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_transfer_agency_transactions_from_orders(request_body, success_mode=success_mode, opts=opts)

        # [EXPERIMENTAL] UpsertTransferAgencyTransactionsFromOrders: Upsert transfer agency transactions from transfer agency orders
        api_response = api_instance.upsert_transfer_agency_transactions_from_orders(request_body, success_mode=success_mode)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransferAgencyApi->upsert_transfer_agency_transactions_from_orders: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, UpsertTransferAgencyTransactionFromOrderRequest]**](UpsertTransferAgencyTransactionFromOrderRequest.md)| The transfer agency orders to price, keyed by a unique request identifier. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | [optional] [default to &#39;Partial&#39;]

### Return type

[**UpsertTransferAgencyTransactionsFromOrdersResponse**](UpsertTransferAgencyTransactionsFromOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully priced orders and any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

