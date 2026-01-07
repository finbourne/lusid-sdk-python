# lusid.TransactionPortfoliosApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_holdings**](TransactionPortfoliosApi.md#adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings | AdjustHoldings: Adjust holdings
[**batch_adjust_holdings**](TransactionPortfoliosApi.md#batch_adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/$batchAdjust | BatchAdjustHoldings: Batch adjust holdings
[**batch_create_trade_tickets**](TransactionPortfoliosApi.md#batch_create_trade_tickets) | **POST** /api/transactionportfolios/{scope}/{code}/$batchtradetickets | BatchCreateTradeTickets: Batch Create Trade Tickets
[**batch_set_holdings**](TransactionPortfoliosApi.md#batch_set_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/$batchSet | BatchSetHoldings: Batch set holdings
[**batch_upsert_settlement_instructions**](TransactionPortfoliosApi.md#batch_upsert_settlement_instructions) | **POST** /api/transactionportfolios/{scope}/{code}/settlementinstructions/$batchUpsert | [EARLY ACCESS] BatchUpsertSettlementInstructions: Batch Upsert Settlement Instructions.
[**batch_upsert_transactions**](TransactionPortfoliosApi.md#batch_upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$batchUpsert | BatchUpsertTransactions: Batch upsert transactions
[**build_settlement_instructions**](TransactionPortfoliosApi.md#build_settlement_instructions) | **POST** /api/transactionportfolios/{scope}/{code}/settlementinstructions/$build | [EARLY ACCESS] BuildSettlementInstructions: Build Settlement Instructions
[**build_transactions**](TransactionPortfoliosApi.md#build_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$build | BuildTransactions: Build transactions
[**cancel_adjust_holdings**](TransactionPortfoliosApi.md#cancel_adjust_holdings) | **DELETE** /api/transactionportfolios/{scope}/{code}/holdings | CancelAdjustHoldings: Cancel adjust holdings
[**cancel_single_adjust_holding**](TransactionPortfoliosApi.md#cancel_single_adjust_holding) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/$cancelAdjustment | CancelSingleAdjustHolding: Cancel single holding adjustment.
[**cancel_transactions**](TransactionPortfoliosApi.md#cancel_transactions) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions | CancelTransactions: Cancel transactions
[**create_portfolio**](TransactionPortfoliosApi.md#create_portfolio) | **POST** /api/transactionportfolios/{scope} | CreatePortfolio: Create portfolio
[**create_trade_ticket**](TransactionPortfoliosApi.md#create_trade_ticket) | **POST** /api/transactionportfolios/{scope}/{code}/$tradeticket | CreateTradeTicket: Create Trade Ticket
[**delete_custodian_accounts**](TransactionPortfoliosApi.md#delete_custodian_accounts) | **POST** /api/transactionportfolios/{scope}/{code}/custodianaccounts/$delete | DeleteCustodianAccounts: Soft or hard delete multiple custodian accounts
[**delete_properties_from_transaction**](TransactionPortfoliosApi.md#delete_properties_from_transaction) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | DeletePropertiesFromTransaction: Delete properties from transaction
[**delete_settlement_instructions**](TransactionPortfoliosApi.md#delete_settlement_instructions) | **DELETE** /api/transactionportfolios/{scope}/{code}/settlementinstructions | [EARLY ACCESS] DeleteSettlementInstructions: Delete Settlement Instructions.
[**get_a2_b_data**](TransactionPortfoliosApi.md#get_a2_b_data) | **GET** /api/transactionportfolios/{scope}/{code}/a2b | GetA2BData: Get A2B data
[**get_a2_b_movements**](TransactionPortfoliosApi.md#get_a2_b_movements) | **GET** /api/transactionportfolios/{scope}/{code}/a2bmovements | GetA2BMovements: Get an A2B report at the movement level for the given portfolio.
[**get_bucketed_cash_flows**](TransactionPortfoliosApi.md#get_bucketed_cash_flows) | **POST** /api/transactionportfolios/{scope}/{code}/bucketedCashFlows | GetBucketedCashFlows: Get bucketed cash flows from a list of portfolios
[**get_custodian_account**](TransactionPortfoliosApi.md#get_custodian_account) | **GET** /api/transactionportfolios/{scope}/{code}/custodianaccounts/{custodianAccountScope}/{custodianAccountCode} | GetCustodianAccount: Get Custodian Account
[**get_details**](TransactionPortfoliosApi.md#get_details) | **GET** /api/transactionportfolios/{scope}/{code}/details | GetDetails: Get details
[**get_holding_contributors**](TransactionPortfoliosApi.md#get_holding_contributors) | **GET** /api/transactionportfolios/{scope}/{code}/holdings/{holdingId}/contributors | GetHoldingContributors: Get Holdings Contributors
[**get_holdings**](TransactionPortfoliosApi.md#get_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings | GetHoldings: Get holdings
[**get_holdings_adjustment**](TransactionPortfoliosApi.md#get_holdings_adjustment) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | GetHoldingsAdjustment: Get holdings adjustment
[**get_holdings_with_orders**](TransactionPortfoliosApi.md#get_holdings_with_orders) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsWithOrders | GetHoldingsWithOrders: Get holdings with orders
[**get_multiple_holding_contributors**](TransactionPortfoliosApi.md#get_multiple_holding_contributors) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/contributors/$get | GetMultipleHoldingContributors: Get Multiple Holding Contributors
[**get_portfolio_cash_flows**](TransactionPortfoliosApi.md#get_portfolio_cash_flows) | **GET** /api/transactionportfolios/{scope}/{code}/cashflows | GetPortfolioCashFlows: Get portfolio cash flows
[**get_portfolio_cash_ladder**](TransactionPortfoliosApi.md#get_portfolio_cash_ladder) | **GET** /api/transactionportfolios/{scope}/{code}/cashladder | GetPortfolioCashLadder: Get portfolio cash ladder
[**get_portfolio_cash_statement**](TransactionPortfoliosApi.md#get_portfolio_cash_statement) | **GET** /api/transactionportfolios/{scope}/{code}/cashstatement | GetPortfolioCashStatement: Get portfolio cash statement
[**get_transaction_history**](TransactionPortfoliosApi.md#get_transaction_history) | **GET** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/history | GetTransactionHistory: Get the history of a transaction
[**get_transaction_settlement_status**](TransactionPortfoliosApi.md#get_transaction_settlement_status) | **GET** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/settlementstatus | [EARLY ACCESS] GetTransactionSettlementStatus: Gets the Transaction Settlement Status for the requested transaction.
[**get_transactions**](TransactionPortfoliosApi.md#get_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions | GetTransactions: Get transactions
[**get_upsertable_portfolio_cash_flows**](TransactionPortfoliosApi.md#get_upsertable_portfolio_cash_flows) | **GET** /api/transactionportfolios/{scope}/{code}/upsertablecashflows | GetUpsertablePortfolioCashFlows: Get upsertable portfolio cash flows.
[**list_custodian_accounts**](TransactionPortfoliosApi.md#list_custodian_accounts) | **GET** /api/transactionportfolios/{scope}/{code}/custodianaccounts | ListCustodianAccounts: List Custodian Accounts
[**list_holdings_adjustments**](TransactionPortfoliosApi.md#list_holdings_adjustments) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | ListHoldingsAdjustments: List holdings adjustments
[**list_settlement_instructions**](TransactionPortfoliosApi.md#list_settlement_instructions) | **GET** /api/transactionportfolios/{scope}/{code}/settlementinstructions | [EARLY ACCESS] ListSettlementInstructions: List Settlement Instructions.
[**patch_portfolio_details**](TransactionPortfoliosApi.md#patch_portfolio_details) | **PATCH** /api/transactionportfolios/{scope}/{code}/details | PatchPortfolioDetails: Patch portfolio details
[**preview_transaction**](TransactionPortfoliosApi.md#preview_transaction) | **POST** /api/transactionportfolios/{scope}/{code}/previewTransaction | PreviewTransaction: Preview a transaction
[**resolve_instrument**](TransactionPortfoliosApi.md#resolve_instrument) | **POST** /api/transactionportfolios/{scope}/{code}/$resolve | ResolveInstrument: Resolve instrument
[**set_holdings**](TransactionPortfoliosApi.md#set_holdings) | **PUT** /api/transactionportfolios/{scope}/{code}/holdings | SetHoldings: Set holdings
[**upsert_custodian_accounts**](TransactionPortfoliosApi.md#upsert_custodian_accounts) | **POST** /api/transactionportfolios/{scope}/{code}/custodianaccounts | UpsertCustodianAccounts: Upsert Custodian Accounts
[**upsert_custodian_accounts_properties**](TransactionPortfoliosApi.md#upsert_custodian_accounts_properties) | **POST** /api/transactionportfolios/{scope}/{code}/custodianaccounts/{custodianAccountScope}/{custodianAccountCode}/properties/$upsert | UpsertCustodianAccountsProperties: Upsert custodian accounts properties
[**upsert_portfolio_details**](TransactionPortfoliosApi.md#upsert_portfolio_details) | **POST** /api/transactionportfolios/{scope}/{code}/details | UpsertPortfolioDetails: Upsert portfolio details
[**upsert_settlement_instructions**](TransactionPortfoliosApi.md#upsert_settlement_instructions) | **POST** /api/transactionportfolios/{scope}/{code}/settlementinstructions | [EARLY ACCESS] UpsertSettlementInstructions: Upsert Settlement Instructions.
[**upsert_transaction_properties**](TransactionPortfoliosApi.md#upsert_transaction_properties) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | UpsertTransactionProperties: Upsert transaction properties
[**upsert_transactions**](TransactionPortfoliosApi.md#upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions | UpsertTransactions: Upsert transactions


# **adjust_holdings**
> AdjustHolding adjust_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods, override_movement_name=override_movement_name, override_offset_movement_name=override_offset_movement_name)

AdjustHoldings: Adjust holdings

Adjust one or more holdings of the specified transaction portfolio to the provided targets. LUSID will  automatically construct adjustment transactions to ensure that the holdings which have been adjusted are  always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/docs/how-do-i-manually-adjust-or-set-holdings.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holdings should be set to the provided targets.
    adjust_holding_request = [{"instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/ibor/CurrentMarketValue":{"key":"Holding/ibor/CurrentMarketValue","value":{"metricValue":{"value":1000}}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","notionalCost":100,"variationMargin":25,"variationMarginPortfolioCcy":25}],"currency":"GBP","custodianAccountId":{"scope":"CustodianAccountScope","code":"CustodianAccountCode"}}] # List[AdjustHoldingRequest] | The selected set of holdings to adjust to the provided targets for the              transaction portfolio.
    reconciliation_methods = ['reconciliation_methods_example'] # List[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)
    override_movement_name = 'override_movement_name_example' # str | Optional parameter to override movement name for the set holdings. (optional)
    override_offset_movement_name = 'override_offset_movement_name_example' # str | Optional parameter will create an additional offset movement for the set holdings with this new name and transaction type: CarryAsPnl (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.adjust_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods, override_movement_name=override_movement_name, override_offset_movement_name=override_offset_movement_name, opts=opts)

        # AdjustHoldings: Adjust holdings
        api_response = api_instance.adjust_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods, override_movement_name=override_movement_name, override_offset_movement_name=override_offset_movement_name)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->adjust_holdings: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the holdings should be set to the provided targets. | 
 **adjust_holding_request** | [**List[AdjustHoldingRequest]**](AdjustHoldingRequest.md)| The selected set of holdings to adjust to the provided targets for the              transaction portfolio. | 
 **reconciliation_methods** | [**List[str]**](str.md)| Optional parameter for specifying a reconciliation method: e.g. FxForward. | [optional] 
 **override_movement_name** | **str**| Optional parameter to override movement name for the set holdings. | [optional] 
 **override_offset_movement_name** | **str**| Optional parameter will create an additional offset movement for the set holdings with this new name and transaction type: CarryAsPnl | [optional] 

### Return type

[**AdjustHolding**](AdjustHolding.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly adjusted holdings |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **batch_adjust_holdings**
> BatchAdjustHoldingsResponse batch_adjust_holdings(scope, code, success_mode, request_body, reconciliation_methods=reconciliation_methods)

BatchAdjustHoldings: Batch adjust holdings

Adjust one or more holdings of the specified transaction portfolio to the provided targets. LUSID will  automatically construct adjustment transactions to ensure that the holdings which have been adjusted are  always set to the provided targets for the specified effective datetime in each request.                Each request must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each adjustment in the response.    Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio.
    success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial (default to 'Partial')
    request_body = {"AdjustHoldingRequest1":{"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","notionalCost":100,"variationMargin":25,"variationMarginPortfolioCcy":25}],"currency":"GBP"},"AdjustHoldingRequest2":{"effectiveAt":"2019-10-02T00:00:00.0000000+00:00","instrumentIdentifiers":{"Instrument/default/Figi":"CCG000C6K6G9","Instrument/default/Isin":"US00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":50,"cost":{"amount":500,"currency":"USD"},"portfolioCost":500,"price":50,"purchaseDate":"2019-03-05T00:00:00.0000000+00:00","settlementDate":"2019-03-08T00:00:00.0000000+00:00","notionalCost":100,"variationMargin":25,"variationMarginPortfolioCcy":25}],"currency":"GBP"}} # Dict[str, AdjustHoldingForDateRequest] | The selected set of holdings to adjust to the provided targets for the               transaction portfolio.
    reconciliation_methods = ['reconciliation_methods_example'] # List[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.batch_adjust_holdings(scope, code, success_mode, request_body, reconciliation_methods=reconciliation_methods, opts=opts)

        # BatchAdjustHoldings: Batch adjust holdings
        api_response = api_instance.batch_adjust_holdings(scope, code, success_mode, request_body, reconciliation_methods=reconciliation_methods)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->batch_adjust_holdings: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | [default to &#39;Partial&#39;]
 **request_body** | [**Dict[str, AdjustHoldingForDateRequest]**](AdjustHoldingForDateRequest.md)| The selected set of holdings to adjust to the provided targets for the               transaction portfolio. | 
 **reconciliation_methods** | [**List[str]**](str.md)| Optional parameter for specifying a reconciliation method: e.g. FxForward. | [optional] 

### Return type

[**BatchAdjustHoldingsResponse**](BatchAdjustHoldingsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successful AdjustHolding requests along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **batch_create_trade_tickets**
> CreateTradeTicketsResponse batch_create_trade_tickets(scope, code, lusid_trade_ticket)

BatchCreateTradeTickets: Batch Create Trade Tickets

Batch create trade tickets. Each ticket is broadly equivalent to a singular call to upsert an instrument, then a counterparty and finally  a transaction that makes use of the two.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    lusid_trade_ticket = [{"transactionId":"TradeTicket-1111111","transactionType":"OpenTradeTicket","source":"default","transactionDate":"2020-01-01T09:00:00.00Z","settlementDate":"2020-01-01T09:00:00.00Z","totalConsideration":{"amount":1020000,"currency":"GBP"},"units":1000000,"instrumentIdentifiers":{"Instrument/default/ClientInternal":"my-bond"},"instrumentScope":"myScope","instrumentName":"my_bond","instrumentDefinition":{"startDate":"2018-01-01T00:00:00.0000000+00:00","maturityDate":"2019-01-01T00:00:00.0000000+00:00","domAmount":1,"domCcy":"GBP","fgnAmount":-1.5,"fgnCcy":"USD","refSpotRate":1.5,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","bookedAsSpot":false,"instrumentType":"FxForward"},"counterpartyAgreementId":{"scope":"demoScope","code":"myCounterparty"},"tradeTicketType":"LusidTradeTicket"}] # List[LusidTradeTicket] | the trade tickets to create

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.batch_create_trade_tickets(scope, code, lusid_trade_ticket, opts=opts)

        # BatchCreateTradeTickets: Batch Create Trade Tickets
        api_response = api_instance.batch_create_trade_tickets(scope, code, lusid_trade_ticket)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->batch_create_trade_tickets: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **lusid_trade_ticket** | [**List[LusidTradeTicket]**](LusidTradeTicket.md)| the trade tickets to create | 

### Return type

[**CreateTradeTicketsResponse**](CreateTradeTicketsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created trade ticket requests along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **batch_set_holdings**
> BatchAdjustHoldingsResponse batch_set_holdings(scope, code, success_mode, request_body, reconciliation_methods=reconciliation_methods)

BatchSetHoldings: Batch set holdings

Set the holdings of the specified transaction portfolio to the provided targets. LUSID will automatically  construct adjustment transactions to ensure that the entire set of holdings for the transaction portfolio  are always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/docs/how-do-i-manually-adjust-or-set-holdings.                Each request must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each adjustment in the response.    Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio.
    success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial (default to 'Partial')
    request_body = {"AdjustHoldingRequest1":{"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","notionalCost":100,"variationMargin":25,"variationMarginPortfolioCcy":25}],"currency":"GBP"},"AdjustHoldingRequest2":{"effectiveAt":"2019-10-02T00:00:00.0000000+00:00","instrumentIdentifiers":{"Instrument/default/Figi":"CCG000C6K6G9","Instrument/default/Isin":"US00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":50,"cost":{"amount":500,"currency":"USD"},"portfolioCost":500,"price":50,"purchaseDate":"2019-03-05T00:00:00.0000000+00:00","settlementDate":"2019-03-08T00:00:00.0000000+00:00","notionalCost":100,"variationMargin":25,"variationMarginPortfolioCcy":25}],"currency":"GBP"}} # Dict[str, AdjustHoldingForDateRequest] | The selected set of holdings to adjust to the provided targets for the               transaction portfolio.
    reconciliation_methods = ['reconciliation_methods_example'] # List[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.batch_set_holdings(scope, code, success_mode, request_body, reconciliation_methods=reconciliation_methods, opts=opts)

        # BatchSetHoldings: Batch set holdings
        api_response = api_instance.batch_set_holdings(scope, code, success_mode, request_body, reconciliation_methods=reconciliation_methods)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->batch_set_holdings: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | [default to &#39;Partial&#39;]
 **request_body** | [**Dict[str, AdjustHoldingForDateRequest]**](AdjustHoldingForDateRequest.md)| The selected set of holdings to adjust to the provided targets for the               transaction portfolio. | 
 **reconciliation_methods** | [**List[str]**](str.md)| Optional parameter for specifying a reconciliation method: e.g. FxForward. | [optional] 

### Return type

[**BatchAdjustHoldingsResponse**](BatchAdjustHoldingsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successful SetHolding requests along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **batch_upsert_settlement_instructions**
> BatchUpsertTransactionSettlementInstructionResponse batch_upsert_settlement_instructions(scope, code, request_body)

[EARLY ACCESS] BatchUpsertSettlementInstructions: Batch Upsert Settlement Instructions.

Create or update instructions to settle specific transactions.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio.
    request_body = {"request-1":{"settlementInstructionId":"settlementInstructionId","transactionId":"transactionId1","settlementCategory":"CashSettlement","instructionType":"Complete","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"contractualSettlementDate":"2024-01-01T00:00:00.0000000+00:00","actualSettlementDate":"2024-01-01T00:00:00.0000000+00:00","units":10,"subHoldingKeyOverrides":{},"properties":[]},"request-2":{"settlementInstructionId":"settlementInstructionId-2","transactionId":"transactionId2","settlementCategory":"StockSettlement","instructionType":"Complete","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9"},"contractualSettlementDate":"2024-01-02T00:00:00.0000000+00:00","actualSettlementDate":"2024-01-05T00:00:00.0000000+00:00","units":10,"subHoldingKeyOverrides":{},"properties":[]}} # Dict[str, SettlementInstructionRequest] | The definition of the settlement instruction.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.batch_upsert_settlement_instructions(scope, code, request_body, opts=opts)

        # [EARLY ACCESS] BatchUpsertSettlementInstructions: Batch Upsert Settlement Instructions.
        api_response = api_instance.batch_upsert_settlement_instructions(scope, code, request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->batch_upsert_settlement_instructions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. | 
 **request_body** | [**Dict[str, SettlementInstructionRequest]**](SettlementInstructionRequest.md)| The definition of the settlement instruction. | 

### Return type

[**BatchUpsertTransactionSettlementInstructionResponse**](BatchUpsertTransactionSettlementInstructionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created or undated Settlement Instructions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **batch_upsert_transactions**
> BatchUpsertPortfolioTransactionsResponse batch_upsert_transactions(scope, code, success_mode, request_body, preserve_properties=preserve_properties)

BatchUpsertTransactions: Batch upsert transactions

Create or update transactions in the transaction portfolio. A transaction will be updated  if it already exists and created if it does not.    Each request must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each transaction in the response.    Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. (default to 'Partial')
    request_body = {"transactionRequest-1":{"transactionId":"TransactionId-111111","type":"StockIn","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"transactionDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","units":1000,"transactionPrice":{"price":123,"type":"Price"},"totalConsideration":{"amount":123000,"currency":"GBP"},"transactionCurrency":"GBP","properties":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"counterpartyId":"CounterpartyId-118263","source":"","otcConfirmation":{"counterpartyAgreementId":{"scope":"someScope","code":"someCode"}},"orderId":{"scope":"someScope","code":"ORD001"},"allocationId":{"scope":"someScope","code":"ALLOC001"}},"transactionRequest-2":{"transactionId":"TransactionId-222222","type":"StockIn","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000GJ45S5","Instrument/default/Isin":"GB00BFRLS45S"},"transactionDate":"2019-03-05T00:00:00.0000000+00:00","settlementDate":"2019-03-08T00:00:00.0000000+00:00","units":1000,"transactionPrice":{"price":123,"type":"Price"},"totalConsideration":{"amount":123000,"currency":"GBP"},"transactionCurrency":"GBP","properties":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"counterpartyId":"CounterpartyId-141556","source":"","otcConfirmation":{"counterpartyAgreementId":{"scope":"someScope","code":"someCode"}},"orderId":{"scope":"someScope","code":"ORD001"},"allocationId":{"scope":"someScope","code":"ALLOC001"}}} # Dict[str, TransactionRequest] | The payload describing the transactions to be created or updated.
    preserve_properties = True # bool | If set to false, the entire property set will be overwritten by the provided properties. If not specified or set to true, only the properties provided will be updated. (optional) (default to True)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.batch_upsert_transactions(scope, code, success_mode, request_body, preserve_properties=preserve_properties, opts=opts)

        # BatchUpsertTransactions: Batch upsert transactions
        api_response = api_instance.batch_upsert_transactions(scope, code, success_mode, request_body, preserve_properties=preserve_properties)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->batch_upsert_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. | [default to &#39;Partial&#39;]
 **request_body** | [**Dict[str, TransactionRequest]**](TransactionRequest.md)| The payload describing the transactions to be created or updated. | 
 **preserve_properties** | **bool**| If set to false, the entire property set will be overwritten by the provided properties. If not specified or set to true, only the properties provided will be updated. | [optional] [default to True]

### Return type

[**BatchUpsertPortfolioTransactionsResponse**](BatchUpsertPortfolioTransactionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully upserted transaction requests along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **build_settlement_instructions**
> VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery build_settlement_instructions(scope, code, settlement_instruction_query)

[EARLY ACCESS] BuildSettlementInstructions: Build Settlement Instructions

Builds and returns all settlement instructions that have been loaded against this portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # settlement_instruction_query = SettlementInstructionQuery.from_json("")
    # settlement_instruction_query = SettlementInstructionQuery.from_dict({})
    settlement_instruction_query = SettlementInstructionQuery()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.build_settlement_instructions(scope, code, settlement_instruction_query, opts=opts)

        # [EARLY ACCESS] BuildSettlementInstructions: Build Settlement Instructions
        api_response = api_instance.build_settlement_instructions(scope, code, settlement_instruction_query)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->build_settlement_instructions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **settlement_instruction_query** | [**SettlementInstructionQuery**](SettlementInstructionQuery.md)| The queryParameters which control how the settlement instructions are built and returned. | 

### Return type

[**VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery**](VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested settlement instructions from the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **build_transactions**
> VersionedResourceListOfOutputTransaction build_transactions(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)

BuildTransactions: Build transactions

Builds and returns all transactions that affect the holdings of a portfolio over a given interval of  effective time into a set of output transactions. This includes transactions automatically generated by  LUSID such as holding adjustments.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transaction_query_parameters = TransactionQueryParameters.from_json("")
    # transaction_query_parameters = TransactionQueryParameters.from_dict({})
    transaction_query_parameters = TransactionQueryParameters()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to BuildTransactions. (optional)
    data_model_scope = 'data_model_scope_example' # str | The optional scope of a Custom Data Model to use (optional)
    data_model_code = 'data_model_code_example' # str | The optional code of a Custom Data Model to use (optional)
    membership_type = 'membership_type_example' # str | The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.build_transactions(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type, opts=opts)

        # BuildTransactions: Build transactions
        api_response = api_instance.build_transactions(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->build_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_query_parameters** | [**TransactionQueryParameters**](TransactionQueryParameters.md)| The query queryParameters which control how the output transactions are built. | 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Transaction\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to BuildTransactions. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 
 **membership_type** | **str**| The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. | [optional] 

### Return type

[**VersionedResourceListOfOutputTransaction**](VersionedResourceListOfOutputTransaction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions from the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **cancel_adjust_holdings**
> DeletedEntityResponse cancel_adjust_holdings(scope, code, effective_at)

CancelAdjustHoldings: Cancel adjust holdings

Cancel all previous holding adjustments made on the specified transaction portfolio for a specified effective  datetime. This should be used to undo holding adjustments made via set holdings or adjust holdings.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holding adjustments should be undone.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.cancel_adjust_holdings(scope, code, effective_at, opts=opts)

        # CancelAdjustHoldings: Cancel adjust holdings
        api_response = api_instance.cancel_adjust_holdings(scope, code, effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->cancel_adjust_holdings: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the holding adjustments should be undone. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the holding adjustments were cancelled |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **cancel_single_adjust_holding**
> DeletedEntityResponse cancel_single_adjust_holding(scope, code, effective_at, cancel_single_holding_adjustment_request)

CancelSingleAdjustHolding: Cancel single holding adjustment.

Cancel one previously sent holding adjustment without affecting the rest of the adjustment in the previous request on the specified effective datetime.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the previous adjustment was made.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # cancel_single_holding_adjustment_request = CancelSingleHoldingAdjustmentRequest.from_json("")
    # cancel_single_holding_adjustment_request = CancelSingleHoldingAdjustmentRequest.from_dict({})
    cancel_single_holding_adjustment_request = CancelSingleHoldingAdjustmentRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.cancel_single_adjust_holding(scope, code, effective_at, cancel_single_holding_adjustment_request, opts=opts)

        # CancelSingleAdjustHolding: Cancel single holding adjustment.
        api_response = api_instance.cancel_single_adjust_holding(scope, code, effective_at, cancel_single_holding_adjustment_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->cancel_single_adjust_holding: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the previous adjustment was made. | 
 **cancel_single_holding_adjustment_request** | [**CancelSingleHoldingAdjustmentRequest**](CancelSingleHoldingAdjustmentRequest.md)| The selected holding adjustment to be canceled. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the holding adjustment was cancelled |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **cancel_transactions**
> DeletedEntityResponse cancel_transactions(scope, code, transaction_ids)

CancelTransactions: Cancel transactions

Cancel one or more transactions from the transaction portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_ids = ['transaction_ids_example'] # List[str] | The IDs of the transactions to cancel.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.cancel_transactions(scope, code, transaction_ids, opts=opts)

        # CancelTransactions: Cancel transactions
        api_response = api_instance.cancel_transactions(scope, code, transaction_ids)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->cancel_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_ids** | [**List[str]**](str.md)| The IDs of the transactions to cancel. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the transactions were cancelled |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_portfolio**
> Portfolio create_portfolio(scope, create_transaction_portfolio_request)

CreatePortfolio: Create portfolio

Create a transaction portfolio in a particular scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope in which to create the transaction portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_transaction_portfolio_request = CreateTransactionPortfolioRequest.from_json("")
    # create_transaction_portfolio_request = CreateTransactionPortfolioRequest.from_dict({})
    create_transaction_portfolio_request = CreateTransactionPortfolioRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_portfolio(scope, create_transaction_portfolio_request, opts=opts)

        # CreatePortfolio: Create portfolio
        api_response = api_instance.create_portfolio(scope, create_transaction_portfolio_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->create_portfolio: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the transaction portfolio. | 
 **create_transaction_portfolio_request** | [**CreateTransactionPortfolioRequest**](CreateTransactionPortfolioRequest.md)| The definition of the transaction portfolio. | 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly-created transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_trade_ticket**
> LusidTradeTicket create_trade_ticket(scope, code, lusid_trade_ticket=lusid_trade_ticket)

CreateTradeTicket: Create Trade Ticket

Upsert a trade ticket. Broadly equivalent to a singular call to upsert an instrument, then a counterparty and finally  a transaction that makes use of the two. It can be viewed as a utility function or part of a workflow more familiar to users  with OTC systems than flow and equity trading ones.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # lusid_trade_ticket = LusidTradeTicket.from_json("")
    # lusid_trade_ticket = LusidTradeTicket.from_dict({})
    lusid_trade_ticket = LusidTradeTicket()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_trade_ticket(scope, code, lusid_trade_ticket=lusid_trade_ticket, opts=opts)

        # CreateTradeTicket: Create Trade Ticket
        api_response = api_instance.create_trade_ticket(scope, code, lusid_trade_ticket=lusid_trade_ticket)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->create_trade_ticket: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **lusid_trade_ticket** | [**LusidTradeTicket**](LusidTradeTicket.md)| the trade ticket to upsert | [optional] 

### Return type

[**LusidTradeTicket**](LusidTradeTicket.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created trade ticket, possibly populated with created LUID and identifiers if missing on the request. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_custodian_accounts**
> DeleteCustodianAccountsResponse delete_custodian_accounts(scope, code, resource_id, delete_mode=delete_mode)

DeleteCustodianAccounts: Soft or hard delete multiple custodian accounts

Delete one or more custodian accounts from the Transaction Portfolios. Soft deletion marks the custodian account as inactive  While the Hard deletion is deleting the custodian account.  The batch limit per request is 2,000.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolios.
    code = 'code_example' # str | The code of the Transaction Portfolios. Together with the scope this uniquely identifies              the Transaction Portfolios.
    resource_id = [{"scope":"ScopeA","code":"AccountCode1"},{"scope":"ScopeB","code":"AccountCode2"}] # List[ResourceId] | The scope and codes of the custodian accounts to delete.
    delete_mode = 'delete_mode_example' # str | The delete mode to use (defaults to 'Soft'). (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_custodian_accounts(scope, code, resource_id, delete_mode=delete_mode, opts=opts)

        # DeleteCustodianAccounts: Soft or hard delete multiple custodian accounts
        api_response = api_instance.delete_custodian_accounts(scope, code, resource_id, delete_mode=delete_mode)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->delete_custodian_accounts: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolios. | 
 **code** | **str**| The code of the Transaction Portfolios. Together with the scope this uniquely identifies              the Transaction Portfolios. | 
 **resource_id** | [**List[ResourceId]**](ResourceId.md)| The scope and codes of the custodian accounts to delete. | 
 **delete_mode** | **str**| The delete mode to use (defaults to &#39;Soft&#39;). | [optional] 

### Return type

[**DeleteCustodianAccountsResponse**](DeleteCustodianAccountsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the custodian accounts were deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_properties_from_transaction**
> DeletedEntityResponse delete_properties_from_transaction(scope, code, transaction_id, property_keys)

DeletePropertiesFromTransaction: Delete properties from transaction

Delete one or more properties from a single transaction in a transaction portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_id = 'transaction_id_example' # str | The unique ID of the transaction from which to delete properties.
    property_keys = ['property_keys_example'] # List[str] | The property keys of the properties to delete.              These must be from the \"Transaction\" domain and have the format {domain}/{scope}/{code}, for example              \"Transaction/strategy/quantsignal\".

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_properties_from_transaction(scope, code, transaction_id, property_keys, opts=opts)

        # DeletePropertiesFromTransaction: Delete properties from transaction
        api_response = api_instance.delete_properties_from_transaction(scope, code, transaction_id, property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->delete_properties_from_transaction: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique ID of the transaction from which to delete properties. | 
 **property_keys** | [**List[str]**](str.md)| The property keys of the properties to delete.              These must be from the \&quot;Transaction\&quot; domain and have the format {domain}/{scope}/{code}, for example              \&quot;Transaction/strategy/quantsignal\&quot;. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the property was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_settlement_instructions**
> DeletedEntityResponse delete_settlement_instructions(scope, code, settlement_instruction_ids)

[EARLY ACCESS] DeleteSettlementInstructions: Delete Settlement Instructions.

Delete the specified settlement instructions

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies              the portfolio.
    settlement_instruction_ids = ['settlement_instruction_ids_example'] # List[str] | A list of Ids of settlement instructions to be deleted.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_settlement_instructions(scope, code, settlement_instruction_ids, opts=opts)

        # [EARLY ACCESS] DeleteSettlementInstructions: Delete Settlement Instructions.
        api_response = api_instance.delete_settlement_instructions(scope, code, settlement_instruction_ids)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->delete_settlement_instructions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies              the portfolio. | 
 **settlement_instruction_ids** | [**List[str]**](str.md)| A list of Ids of settlement instructions to be deleted. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ids of the deleted settlement instructions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_a2_b_data**
> VersionedResourceListOfA2BDataRecord get_a2_b_data(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)

GetA2BData: Get A2B data

Get an A2B report for the given portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio to retrieve the A2B report for.
    code = 'code_example' # str | The code of the portfolio to retrieve the A2B report for. Together with the scope this              uniquely identifies the portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeId (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_a2_b_data(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter, opts=opts)

        # GetA2BData: Get A2B data
        api_response = api_instance.get_a2_b_data(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_a2_b_data: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to retrieve the A2B report for. | 
 **code** | **str**| The code of the portfolio to retrieve the A2B report for. Together with the scope this              uniquely identifies the portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeId | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**VersionedResourceListOfA2BDataRecord**](VersionedResourceListOfA2BDataRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio A2B data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_a2_b_movements**
> VersionedResourceListOfA2BMovementRecord get_a2_b_movements(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)

GetA2BMovements: Get an A2B report at the movement level for the given portfolio.

Get an A2B report at the movement level for the given portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio to retrieve the A2B movement report for.
    code = 'code_example' # str | The code of the portfolio to retrieve the A2B movement report for. Together with the scope this              uniquely identifies the portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeId (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_a2_b_movements(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter, opts=opts)

        # GetA2BMovements: Get an A2B report at the movement level for the given portfolio.
        api_response = api_instance.get_a2_b_movements(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_a2_b_movements: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to retrieve the A2B movement report for. | 
 **code** | **str**| The code of the portfolio to retrieve the A2B movement report for. Together with the scope this              uniquely identifies the portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeId | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**VersionedResourceListOfA2BMovementRecord**](VersionedResourceListOfA2BMovementRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio A2B movement data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_bucketed_cash_flows**
> BucketedCashFlowResponse get_bucketed_cash_flows(scope, code, bucketed_cash_flow_request=bucketed_cash_flow_request)

GetBucketedCashFlows: Get bucketed cash flows from a list of portfolios

We bucket/aggregate a transaction portfolio's instruments by date or tenor specified in the request.  The cashflows are grouped by both instrumentId and currency.                If you want transactional level cashflow, please use the 'GetUpsertableCashFlows' endpoint.  If you want instrument cashflow, please use the 'GetPortfolioCashFlows' endpoint.  Note that these endpoints do not apply bucketing.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies the portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # bucketed_cash_flow_request = BucketedCashFlowRequest.from_json("")
    # bucketed_cash_flow_request = BucketedCashFlowRequest.from_dict({})
    bucketed_cash_flow_request = BucketedCashFlowRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_bucketed_cash_flows(scope, code, bucketed_cash_flow_request=bucketed_cash_flow_request, opts=opts)

        # GetBucketedCashFlows: Get bucketed cash flows from a list of portfolios
        api_response = api_instance.get_bucketed_cash_flows(scope, code, bucketed_cash_flow_request=bucketed_cash_flow_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_bucketed_cash_flows: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **bucketed_cash_flow_request** | [**BucketedCashFlowRequest**](BucketedCashFlowRequest.md)| Request specifying the bucketing of cashflows | [optional] 

### Return type

[**BucketedCashFlowResponse**](BucketedCashFlowResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio instruments&#39; bucketed cash flow data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_custodian_account**
> CustodianAccount get_custodian_account(scope, code, custodian_account_scope, custodian_account_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

GetCustodianAccount: Get Custodian Account

Retrieve the definition of a particular Custodian Account which is part of a Transaction Portfolios.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolio.
    code = 'code_example' # str | The code of the Transaction Portfolio. Together with the scope this uniquely identifies the Transaction Portfolio.
    custodian_account_scope = 'custodian_account_scope_example' # str | The scope of the Custodian Account.
    custodian_account_code = 'custodian_account_code_example' # str | The code of the Custodian Account.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Custodian Account properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Custodian Account definition. Defaults to returning the latest version of the Custodian Account definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'CustodianAccount' domain to decorate onto the Custodian Account.              These must take the format {domain}/{scope}/{code}, for example 'CustodianAccount/Manager/Id'. If no properties are specified, then no properties will be returned. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_custodian_account(scope, code, custodian_account_scope, custodian_account_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, opts=opts)

        # GetCustodianAccount: Get Custodian Account
        api_response = api_instance.get_custodian_account(scope, code, custodian_account_scope, custodian_account_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_custodian_account: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolio. | 
 **code** | **str**| The code of the Transaction Portfolio. Together with the scope this uniquely identifies the Transaction Portfolio. | 
 **custodian_account_scope** | **str**| The scope of the Custodian Account. | 
 **custodian_account_code** | **str**| The code of the Custodian Account. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Custodian Account properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Custodian Account definition. Defaults to returning the latest version of the Custodian Account definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;CustodianAccount&#39; domain to decorate onto the Custodian Account.              These must take the format {domain}/{scope}/{code}, for example &#39;CustodianAccount/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**CustodianAccount**](CustodianAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Custodian Account definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_details**
> PortfolioDetails get_details(scope, code, effective_at=effective_at, as_at=as_at)

GetDetails: Get details

Get certain details associated with a transaction portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the              scope this uniquely identifies the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to returning the latest version of the details if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_details(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

        # GetDetails: Get details
        api_response = api_instance.get_details(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_details: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the              scope this uniquely identifies the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to returning the latest version of the details if not specified. | [optional] 

### Return type

[**PortfolioDetails**](PortfolioDetails.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_holding_contributors**
> VersionedResourceListOfHoldingContributor get_holding_contributors(scope, code, holding_id, effective_date=effective_date, from_trade_date=from_trade_date, to_trade_date=to_trade_date, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page, timeline_scope=timeline_scope, timeline_code=timeline_code)

GetHoldingContributors: Get Holdings Contributors

Lists all transactions that affect the holdings of a portfolio over a given effective interval. This includes  transactions automatically generated by LUSID such as holding adjustments.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    holding_id = 56 # int | The unique holding identifier
    effective_date = 'effective_date_example' # str | Effective date (optional)
    from_trade_date = 'from_trade_date_example' # str | The from trade date, defaults to first time this holding is opened, lower bound for transactions (optional)
    to_trade_date = 'to_trade_date_example' # str | The to trade date upper bound date, defaults to effectiveDate. upper bound for transactions (optional)
    include_historic = False # bool | If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. (optional) (default to False)
    tax_lot_id = 'tax_lot_id_example' # str | Constrains the Holding Contributors to those which contributed to the specified tax lot. (optional)
    include_unsettled_movements = False # bool | If true, contributing transaction which have not settled yet will also be returned. False by default (optional) (default to False)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. (optional)
    timeline_scope = 'timeline_scope_example' # str | The scope of the timeline used for evaluation. If provided, you must also provide a timelineCode. (optional)
    timeline_code = 'timeline_code_example' # str | The code of the timeline used for evaluation. If provided, you must also provide a timelineScope. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_holding_contributors(scope, code, holding_id, effective_date=effective_date, from_trade_date=from_trade_date, to_trade_date=to_trade_date, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page, timeline_scope=timeline_scope, timeline_code=timeline_code, opts=opts)

        # GetHoldingContributors: Get Holdings Contributors
        api_response = api_instance.get_holding_contributors(scope, code, holding_id, effective_date=effective_date, from_trade_date=from_trade_date, to_trade_date=to_trade_date, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page, timeline_scope=timeline_scope, timeline_code=timeline_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_holding_contributors: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **holding_id** | **int**| The unique holding identifier | 
 **effective_date** | **str**| Effective date | [optional] 
 **from_trade_date** | **str**| The from trade date, defaults to first time this holding is opened, lower bound for transactions | [optional] 
 **to_trade_date** | **str**| The to trade date upper bound date, defaults to effectiveDate. upper bound for transactions | [optional] 
 **include_historic** | **bool**| If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. | [optional] [default to False]
 **tax_lot_id** | **str**| Constrains the Holding Contributors to those which contributed to the specified tax lot. | [optional] 
 **include_unsettled_movements** | **bool**| If true, contributing transaction which have not settled yet will also be returned. False by default | [optional] [default to False]
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. | [optional] 
 **timeline_scope** | **str**| The scope of the timeline used for evaluation. If provided, you must also provide a timelineCode. | [optional] 
 **timeline_code** | **str**| The code of the timeline used for evaluation. If provided, you must also provide a timelineScope. | [optional] 

### Return type

[**VersionedResourceListOfHoldingContributor**](VersionedResourceListOfHoldingContributor.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested holding contributors from the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_holdings**
> VersionedResourceListOfPortfolioHolding get_holdings(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days, timeline_scope=timeline_scope, timeline_code=timeline_code, closed_period_id=closed_period_id)

GetHoldings: Get holdings

Calculate holdings for a transaction portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Holding Type, use \"holdingType eq 'p'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\", \"Holding\", \"Custodian Account\", \"Legal Entity\" or \"Portfolio\" domain to decorate onto              holdings. These must have the format {domain}/{scope}/{code}, for example \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)
    by_taxlots = True # bool | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. (optional)
    include_settlement_events_after_days = 56 # int | Number of days ahead to bring back settlements from, in relation to the specified effectiveAt (optional)
    timeline_scope = 'timeline_scope_example' # str | The scope of the Timeline. (optional)
    timeline_code = 'timeline_code_example' # str | The code of the Timeline. (optional)
    closed_period_id = 'closed_period_id_example' # str | The closed period ID. If this is specified, both timelineScope and timelineCode must be specified. Either closedPeriodId or effectiveAt can be used with a Timeline. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_holdings(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days, timeline_scope=timeline_scope, timeline_code=timeline_code, closed_period_id=closed_period_id, opts=opts)

        # GetHoldings: Get holdings
        api_response = api_instance.get_holdings(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days, timeline_scope=timeline_scope, timeline_code=timeline_code, closed_period_id=closed_period_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_holdings: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Holding Type, use \&quot;holdingType eq &#39;p&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot;, \&quot;Custodian Account\&quot;, \&quot;Legal Entity\&quot; or \&quot;Portfolio\&quot; domain to decorate onto              holdings. These must have the format {domain}/{scope}/{code}, for example \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **by_taxlots** | **bool**| Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. | [optional] 
 **include_settlement_events_after_days** | **int**| Number of days ahead to bring back settlements from, in relation to the specified effectiveAt | [optional] 
 **timeline_scope** | **str**| The scope of the Timeline. | [optional] 
 **timeline_code** | **str**| The code of the Timeline. | [optional] 
 **closed_period_id** | **str**| The closed period ID. If this is specified, both timelineScope and timelineCode must be specified. Either closedPeriodId or effectiveAt can be used with a Timeline. | [optional] 

### Return type

[**VersionedResourceListOfPortfolioHolding**](VersionedResourceListOfPortfolioHolding.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings and version of the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_holdings_adjustment**
> HoldingsAdjustment get_holdings_adjustment(scope, code, effective_at, as_at=as_at, property_keys=property_keys)

GetHoldingsAdjustment: Get holdings adjustment

Get a holdings adjustment made to a transaction portfolio at a specific effective datetime. Note that a  holdings adjustment will only be returned if one exists for the specified effective datetime.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label of the holdings adjustment.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the ‘Instrument' domain to decorate onto holdings adjustments.              These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'.              Note that properties from the 'Holding’ domain are automatically returned. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_holdings_adjustment(scope, code, effective_at, as_at=as_at, property_keys=property_keys, opts=opts)

        # GetHoldingsAdjustment: Get holdings adjustment
        api_response = api_instance.get_holdings_adjustment(scope, code, effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_holdings_adjustment: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label of the holdings adjustment. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the ‘Instrument&#39; domain to decorate onto holdings adjustments.              These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39;.              Note that properties from the &#39;Holding’ domain are automatically returned. | [optional] 

### Return type

[**HoldingsAdjustment**](HoldingsAdjustment.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the requested holdings adjustment |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_holdings_with_orders**
> VersionedResourceListWithWarningsOfPortfolioHolding get_holdings_with_orders(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, include_settlement_events_after_days=include_settlement_events_after_days)

GetHoldingsWithOrders: Get holdings with orders

Get the holdings of a transaction portfolio. Create virtual holdings for any outstanding orders,  and account for order state/fulfillment; that is, treat outstanding orders (and related records) as  if they had been realised at moment of query.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Holding Type, use \"holdingType eq 'p'\"              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\", \"Holding\" or \"Portfolio\" domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)
    by_taxlots = True # bool | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeId (optional)
    include_settlement_events_after_days = 56 # int | Number of days ahead to bring back settlements from, in relation to the specified effectiveAt (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_holdings_with_orders(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, include_settlement_events_after_days=include_settlement_events_after_days, opts=opts)

        # GetHoldingsWithOrders: Get holdings with orders
        api_response = api_instance.get_holdings_with_orders(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, include_settlement_events_after_days=include_settlement_events_after_days)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_holdings_with_orders: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Holding Type, use \&quot;holdingType eq &#39;p&#39;\&quot;              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot; or \&quot;Portfolio\&quot; domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **by_taxlots** | **bool**| Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeId | [optional] 
 **include_settlement_events_after_days** | **int**| Number of days ahead to bring back settlements from, in relation to the specified effectiveAt | [optional] 

### Return type

[**VersionedResourceListWithWarningsOfPortfolioHolding**](VersionedResourceListWithWarningsOfPortfolioHolding.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings and version of the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_multiple_holding_contributors**
> VersionedResourceListOfHoldingContributor get_multiple_holding_contributors(scope, code, holding_ids_request, effective_date=effective_date, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page, timeline_scope=timeline_scope, timeline_code=timeline_code)

GetMultipleHoldingContributors: Get Multiple Holding Contributors

Lists all transactions that affect multiple specified holdings of a portfolio over a given effective interval. This includes  transactions automatically generated by LUSID such as holding adjustments.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # holding_ids_request = HoldingIdsRequest.from_json("")
    # holding_ids_request = HoldingIdsRequest.from_dict({})
    holding_ids_request = HoldingIdsRequest()
    effective_date = 'effective_date_example' # str | Effective date (optional)
    from_transaction_date = 'from_transaction_date_example' # str | The from trade date, defaults to first time this holding is opened, lower bound for transactions (optional)
    to_transaction_date = 'to_transaction_date_example' # str | The to trade date upper bound date, defaults to effectiveDate. upper bound for transactions (optional)
    include_historic = False # bool | If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. (optional) (default to False)
    tax_lot_id = 'tax_lot_id_example' # str | Constrains the Holding Contributors to those which contributed to the specified tax lot. (optional)
    include_unsettled_movements = False # bool | If true, contributing transaction which have not settled yet will also be returned. False by default (optional) (default to False)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. (optional)
    timeline_scope = 'timeline_scope_example' # str | The scope of the timeline used for evaluation. If provided, you must also provide a timelineCode. (optional)
    timeline_code = 'timeline_code_example' # str | The code of the timeline used for evaluation. If provided, you must also provide a timelineScope. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_multiple_holding_contributors(scope, code, holding_ids_request, effective_date=effective_date, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page, timeline_scope=timeline_scope, timeline_code=timeline_code, opts=opts)

        # GetMultipleHoldingContributors: Get Multiple Holding Contributors
        api_response = api_instance.get_multiple_holding_contributors(scope, code, holding_ids_request, effective_date=effective_date, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page, timeline_scope=timeline_scope, timeline_code=timeline_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_multiple_holding_contributors: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **holding_ids_request** | [**HoldingIdsRequest**](HoldingIdsRequest.md)| The array of unique holding identifiers | 
 **effective_date** | **str**| Effective date | [optional] 
 **from_transaction_date** | **str**| The from trade date, defaults to first time this holding is opened, lower bound for transactions | [optional] 
 **to_transaction_date** | **str**| The to trade date upper bound date, defaults to effectiveDate. upper bound for transactions | [optional] 
 **include_historic** | **bool**| If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. | [optional] [default to False]
 **tax_lot_id** | **str**| Constrains the Holding Contributors to those which contributed to the specified tax lot. | [optional] 
 **include_unsettled_movements** | **bool**| If true, contributing transaction which have not settled yet will also be returned. False by default | [optional] [default to False]
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. | [optional] 
 **timeline_scope** | **str**| The scope of the timeline used for evaluation. If provided, you must also provide a timelineCode. | [optional] 
 **timeline_code** | **str**| The code of the timeline used for evaluation. If provided, you must also provide a timelineScope. | [optional] 

### Return type

[**VersionedResourceListOfHoldingContributor**](VersionedResourceListOfHoldingContributor.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested holding contributors for each specified holding from the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_cash_flows**
> ResourceListOfInstrumentCashFlow get_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)

GetPortfolioCashFlows: Get portfolio cash flows

Get the set of cash flows that occur in a window for the transaction portfolio's instruments.                Note that grouping can affect the quantity of information returned; where a holding is an amalgamation of one or more (e.g. cash) instruments, a unique  transaction identifier will not be available. The same may go for diagnostic information (e.g. multiple sources of an aggregate cash amount on a date that is  not split out. Grouping at the transaction and instrument level is recommended for those seeking to attribute individual flows.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this               uniquely identifies the portfolio.
    effective_at = 'effective_at_example' # str | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. (optional)
    window_start = 'window_start_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               There is no lower bound if this is not specified. i.e. it is the minimum date. (optional)
    window_end = 'window_end_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               The upper bound defaults to 'max date' if it is not specified (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the data. Defaults to returning the latest version               of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.               For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)
    exclude_unsettled_trades = False # bool | If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades, opts=opts)

        # GetPortfolioCashFlows: Get portfolio cash flows
        api_response = api_instance.get_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_portfolio_cash_flows: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this               uniquely identifies the portfolio. | 
 **effective_at** | **str**| The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. | [optional] 
 **window_start** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               There is no lower bound if this is not specified. i.e. it is the minimum date. | [optional] 
 **window_end** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               The upper bound defaults to &#39;max date&#39; if it is not specified | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the data. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeID | [optional] 
 **exclude_unsettled_trades** | **bool**| If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. | [optional] [default to False]

### Return type

[**ResourceListOfInstrumentCashFlow**](ResourceListOfInstrumentCashFlow.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio instruments&#39; cash flow data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_cash_ladder**
> ResourceListOfPortfolioCashLadder get_portfolio_cash_ladder(scope, code, from_effective_at, to_effective_at, effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)

GetPortfolioCashLadder: Get portfolio cash ladder

Get a cash ladder for a transaction portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this              uniquely identifies the portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
    effective_at = 'effective_at_example' # str | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to returning the latest version              of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)
    exclude_unsettled_trades = False # bool | If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_cash_ladder(scope, code, from_effective_at, to_effective_at, effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades, opts=opts)

        # GetPortfolioCashLadder: Get portfolio cash ladder
        api_response = api_instance.get_portfolio_cash_ladder(scope, code, from_effective_at, to_effective_at, effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_portfolio_cash_ladder: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this              uniquely identifies the portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | 
 **effective_at** | **str**| The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeID | [optional] 
 **exclude_unsettled_trades** | **bool**| If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. | [optional] [default to False]

### Return type

[**ResourceListOfPortfolioCashLadder**](ResourceListOfPortfolioCashLadder.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio cash-ladder |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_cash_statement**
> ResourceListOfPortfolioCashFlow get_portfolio_cash_statement(scope, code, from_effective_at, to_effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys)

GetPortfolioCashStatement: Get portfolio cash statement

Get a cash statement for a transaction portfolio.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this              uniquely identifies the portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to returning the latest version              of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the cash flows' transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_cash_statement(scope, code, from_effective_at, to_effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, opts=opts)

        # GetPortfolioCashStatement: Get portfolio cash statement
        api_response = api_instance.get_portfolio_cash_statement(scope, code, from_effective_at, to_effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_portfolio_cash_statement: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this              uniquely identifies the portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeID | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Transaction\&quot; domain to decorate onto              the cash flows&#39; transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 

### Return type

[**ResourceListOfPortfolioCashFlow**](ResourceListOfPortfolioCashFlow.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio cash flow data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transaction_history**
> ResourceListOfChangeHistory get_transaction_history(scope, code, transaction_id, as_at=as_at)

GetTransactionHistory: Get the history of a transaction

Get all of the changes that have happened to a transaction.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_id = 'transaction_id_example' # str | The unique ID of the transaction to create or update.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the history of the transaction. Defaults              to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transaction_history(scope, code, transaction_id, as_at=as_at, opts=opts)

        # GetTransactionHistory: Get the history of a transaction
        api_response = api_instance.get_transaction_history(scope, code, transaction_id, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_transaction_history: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique ID of the transaction to create or update. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the history of the transaction. Defaults              to return the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfChangeHistory**](ResourceListOfChangeHistory.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The history of the specified transaction (changes that have been made to it). |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transaction_settlement_status**
> TransactionSettlementStatus get_transaction_settlement_status(scope, code, transaction_id, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetTransactionSettlementStatus: Gets the Transaction Settlement Status for the requested transaction.

Gets the Transaction Settlement Status for the requested transaction.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_id = 'transaction_id_example' # str | The id of the transaction
    effective_at = 'effective_at_example' # str | The effective datetime or cut label for which to get the transaction               settlement status. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to get the transaction settlement status.               Defaults to return the latest status if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transaction_settlement_status(scope, code, transaction_id, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetTransactionSettlementStatus: Gets the Transaction Settlement Status for the requested transaction.
        api_response = api_instance.get_transaction_settlement_status(scope, code, transaction_id, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_transaction_settlement_status: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The id of the transaction | 
 **effective_at** | **str**| The effective datetime or cut label for which to get the transaction               settlement status. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to get the transaction settlement status.               Defaults to return the latest status if not specified. | [optional] 

### Return type

[**TransactionSettlementStatus**](TransactionSettlementStatus.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Transaction Settlement Status for the requested transaction. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transactions**
> VersionedResourceListOfTransaction get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, page=page, limit=limit, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)

GetTransactions: Get transactions

Retrieve all the transactions that occurred during a particular time interval.                If the portfolio is a derived transaction portfolio, the transactions returned are the  union set of all transactions of the parent (and any grandparents, etc.) as well as  those of the derived transaction portfolio itself.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio.
    from_transaction_date = 'from_transaction_date_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no lower bound if this is not specified. (optional)
    to_transaction_date = 'to_transaction_date_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no upper bound if this is not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve transactions. Defaults to returning the latest version               of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression with which to filter the result set.               For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\"               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument', 'Transaction', \"LegalEntity\" or \"CustodianAccount\" domain to decorate onto               transactions. These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name' or               'Transaction/strategy/quantsignal'. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to GetTransactions. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. The current behaviour is               to return all transactions if possible, but this will change to defaulting to 1000 if not specified in the future. It is recommended               to populate this field to enable pagination. (optional)
    show_cancelled_transactions = True # bool | Option to specify whether or not to include cancelled transactions,               including previous versions of transactions which have since been amended.               Defaults to False if not specified. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    data_model_scope = 'data_model_scope_example' # str | The optional scope of a Custom Data Model to use (optional)
    data_model_code = 'data_model_code_example' # str | The optional code of a Custom Data Model to use (optional)
    membership_type = 'membership_type_example' # str | The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, page=page, limit=limit, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type, opts=opts)

        # GetTransactions: Get transactions
        api_response = api_instance.get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, page=page, limit=limit, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio. | 
 **from_transaction_date** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no lower bound if this is not specified. | [optional] 
 **to_transaction_date** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve transactions. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression with which to filter the result set.               For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, \&quot;LegalEntity\&quot; or \&quot;CustodianAccount\&quot; domain to decorate onto               transactions. These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39; or               &#39;Transaction/strategy/quantsignal&#39;. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetTransactions. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. The current behaviour is               to return all transactions if possible, but this will change to defaulting to 1000 if not specified in the future. It is recommended               to populate this field to enable pagination. | [optional] 
 **show_cancelled_transactions** | **bool**| Option to specify whether or not to include cancelled transactions,               including previous versions of transactions which have since been amended.               Defaults to False if not specified. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 
 **membership_type** | **str**| The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. | [optional] 

### Return type

[**VersionedResourceListOfTransaction**](VersionedResourceListOfTransaction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions from the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_upsertable_portfolio_cash_flows**
> ResourceListOfTransaction get_upsertable_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)

GetUpsertablePortfolioCashFlows: Get upsertable portfolio cash flows.

Get the set of cash flows that occur in a window for the given portfolio instruments as a set of upsertable transactions (DTOs).                Note that grouping can affect the quantity of information returned; where a holding is an amalgamation of one or more (e.g. cash) instruments, a unique  transaction identifier will not be available. The same may go for diagnostic information (e.g. multiple sources of an aggregate cash amount on a date that is  not split out. Grouping at the transaction and instrument level is recommended for those seeking to attribute individual flows.                In essence this is identical to the 'GetCashFlows' endpoint but returns the cash flows as a set of transactions suitable for directly putting back into LUSID.  There are a couple of important points:  (1) Internally it can not be fully known where the user wishes to insert these transactions, e.g. portfolio and movement type.      These are therefore defaulted to a sensible option; the user will likely need to change these.  (2) Similarly, knowledge of any properties the user might wish to add to a transaction are unknown and consequently left empty.  (3) The transaction id that is added is simply a concatenation of the original transaction id, instrument id and payment date and direction. The user can happily override this.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this               uniquely identifies the portfolio.
    effective_at = 'effective_at_example' # str | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. (optional)
    window_start = 'window_start_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               There is no lower bound if this is not specified. i.e. uses minimum date-time (optional)
    window_end = 'window_end_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               The upper bound defaults to 'max date' if it is not specified (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version               of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.               For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)
    exclude_unsettled_trades = True # bool | If absent or set to true, unsettled trades will be excluded from the result set. If set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. (optional) (default to True)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_upsertable_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades, opts=opts)

        # GetUpsertablePortfolioCashFlows: Get upsertable portfolio cash flows.
        api_response = api_instance.get_upsertable_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_upsertable_portfolio_cash_flows: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this               uniquely identifies the portfolio. | 
 **effective_at** | **str**| The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. | [optional] 
 **window_start** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               There is no lower bound if this is not specified. i.e. uses minimum date-time | [optional] 
 **window_end** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               The upper bound defaults to &#39;max date&#39; if it is not specified | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeID | [optional] 
 **exclude_unsettled_trades** | **bool**| If absent or set to true, unsettled trades will be excluded from the result set. If set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. | [optional] [default to True]

### Return type

[**ResourceListOfTransaction**](ResourceListOfTransaction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio instruments&#39; cash flow data as a set of upsertable transactions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_custodian_accounts**
> PagedResourceListOfCustodianAccount list_custodian_accounts(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)

ListCustodianAccounts: List Custodian Accounts

List the custodian accounts in a Transaction Portfolios

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolio.
    code = 'code_example' # str | The code of the Transaction Portfolio. Together with the scope this uniquely identifies              the Transaction Portfolios.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties decorated on Custodian Accounts. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing custodian accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Custodian Account type, specify \"code eq '001'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'CustodianAccount' domain to decorate onto the Custodian Account.              These must have the format {domain}/{scope}/{code}, for example 'CustodianAccount/system/Name'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_custodian_accounts(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, opts=opts)

        # ListCustodianAccounts: List Custodian Accounts
        api_response = api_instance.list_custodian_accounts(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->list_custodian_accounts: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolio. | 
 **code** | **str**| The code of the Transaction Portfolio. Together with the scope this uniquely identifies              the Transaction Portfolios. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties decorated on Custodian Accounts. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing custodian accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Custodian Account type, specify \&quot;code eq &#39;001&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;CustodianAccount&#39; domain to decorate onto the Custodian Account.              These must have the format {domain}/{scope}/{code}, for example &#39;CustodianAccount/system/Name&#39;. | [optional] 

### Return type

[**PagedResourceListOfCustodianAccount**](PagedResourceListOfCustodianAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The custodian accounts in the given Transaction Portfolios. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_holdings_adjustments**
> ResourceListOfHoldingsAdjustmentHeader list_holdings_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)

ListHoldingsAdjustments: List holdings adjustments

List the holdings adjustments made to the specified transaction portfolio over a specified interval of effective time.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified. (optional)
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_holdings_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, opts=opts)

        # ListHoldingsAdjustments: List holdings adjustments
        api_response = api_instance.list_holdings_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->list_holdings_adjustments: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified. | [optional] 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified. | [optional] 

### Return type

[**ResourceListOfHoldingsAdjustmentHeader**](ResourceListOfHoldingsAdjustmentHeader.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The record of holdings adjustments made to the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_settlement_instructions**
> VersionedResourceListOfTransactionSettlementInstruction list_settlement_instructions(scope, code, from_date=from_date, to_date=to_date, page=page, limit=limit, filter=filter, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] ListSettlementInstructions: List Settlement Instructions.

Display all the Settlement Instructions for a given Portfolio. The transaction Id filter can be ued to return instructions for an individual transaction.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio to retrieve settlement instructions for.
    code = 'code_example' # str | The code of the portfolio to retrieve settlement instructions for.
    from_date = 'from_date_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve instructions.              There is no lower bound if this is not specified. (optional)
    to_date = 'to_date_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve instructions. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing instructions; this value is returned from the previous call.              If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | The expression to filter out settlement instructions (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the settlement instructions. Defaults to return the latest if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'SettlementInstruction', 'Instrument' or 'Portfolio' domains to decorate onto              settlement instructions. These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name' or 'SettlementInstruction/strategy/quantsignal'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_settlement_instructions(scope, code, from_date=from_date, to_date=to_date, page=page, limit=limit, filter=filter, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] ListSettlementInstructions: List Settlement Instructions.
        api_response = api_instance.list_settlement_instructions(scope, code, from_date=from_date, to_date=to_date, page=page, limit=limit, filter=filter, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->list_settlement_instructions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to retrieve settlement instructions for. | 
 **code** | **str**| The code of the portfolio to retrieve settlement instructions for. | 
 **from_date** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve instructions.              There is no lower bound if this is not specified. | [optional] 
 **to_date** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve instructions. | [optional] 
 **page** | **str**| The pagination token to use to continue listing instructions; this value is returned from the previous call.              If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| The expression to filter out settlement instructions | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the settlement instructions. Defaults to return the latest if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;SettlementInstruction&#39;, &#39;Instrument&#39; or &#39;Portfolio&#39; domains to decorate onto              settlement instructions. These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39; or &#39;SettlementInstruction/strategy/quantsignal&#39;. | [optional] 

### Return type

[**VersionedResourceListOfTransactionSettlementInstruction**](VersionedResourceListOfTransactionSettlementInstruction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested settlement instructions from the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **patch_portfolio_details**
> PortfolioDetails patch_portfolio_details(scope, code, operation, effective_at=effective_at)

PatchPortfolioDetails: Patch portfolio details

Create or update certain details for a particular transaction portfolio.  Note that not all elements of a transaction portfolio definition are  modifiable once it has been created due to the potential implications for data already stored.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: BaseCurrency, AccountingMethod, SubHoldingKeys, AmortisationMethod, TransactionTypeScope, CashGainLossCalculationDate, InstrumentEventConfiguration, AmortisationRuleSetId, TaxRuleSetScope, SettlementConfiguration.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the              scope this uniquely identifies the transaction portfolio.
    operation = [{"value":["Transaction/Client/AccountType"],"path":"/subHoldingKeys","op":"add"},{"value":"GBP","path":"/baseCurrency","op":"add"},{"value":"newscope","path":"/transactiontypescope","op":"add"},{"value":"TransactionDate","path":"/cashGainLossCalculationDate","op":"add"},{"value":["NewTransactionTemplateScope"],"path":"/instrumentEventConfiguration/transactionTemplateScopes","op":"add"},{"value":{"scope":"myRecipeScope","code":"myRecipeCode"},"path":"/instrumentEventConfiguration/recipeId","op":"add"}] # List[Operation] | The patch document.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the updated or inserted details should become valid.              Defaults to the current LUSID system datetime if not specified.              Note that this will affect all bitemporal fields (eg: SettlementConfiguration) in the request (but will not be used for any              perpetual fields). When patching a bitemporal field, the field will be updated from the              effectiveAt onwards and until the end of effective time. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.patch_portfolio_details(scope, code, operation, effective_at=effective_at, opts=opts)

        # PatchPortfolioDetails: Patch portfolio details
        api_response = api_instance.patch_portfolio_details(scope, code, operation, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->patch_portfolio_details: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the              scope this uniquely identifies the transaction portfolio. | 
 **operation** | [**List[Operation]**](Operation.md)| The patch document. | 
 **effective_at** | **str**| The effective datetime or cut label at which the updated or inserted details should become valid.              Defaults to the current LUSID system datetime if not specified.              Note that this will affect all bitemporal fields (eg: SettlementConfiguration) in the request (but will not be used for any              perpetual fields). When patching a bitemporal field, the field will be updated from the              effectiveAt onwards and until the end of effective time. | [optional] 

### Return type

[**PortfolioDetails**](PortfolioDetails.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched details |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **preview_transaction**
> ResourceListOfOutputTransaction preview_transaction(scope, code, transaction_request, property_keys=property_keys, show_cancelled_transactions=show_cancelled_transactions, preserve_properties=preserve_properties, data_model_scope=data_model_scope, data_model_code=data_model_code)

PreviewTransaction: Preview a transaction

Returns the output-transaction(s) - e.g. as returned by BuildTransactions  that would come out of LUSID if the provided TransactionRequest was booked.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transaction_request = TransactionRequest.from_json("")
    # transaction_request = TransactionRequest.from_dict({})
    transaction_request = TransactionRequest()
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\". (optional)
    show_cancelled_transactions = True # bool | Option to specify whether to include previous versions of an amended transaction in the response.              Defaults to False if not specified. (optional)
    preserve_properties = True # bool | If the preview transaction is an amendment to an existing transaction, then setting this to true will carry forward any unmodified properties from the earlier version. (optional)
    data_model_scope = 'data_model_scope_example' # str | The optional scope of a Custom Data Model to use (optional)
    data_model_code = 'data_model_code_example' # str | The optional code of a Custom Data Model to use (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.preview_transaction(scope, code, transaction_request, property_keys=property_keys, show_cancelled_transactions=show_cancelled_transactions, preserve_properties=preserve_properties, data_model_scope=data_model_scope, data_model_code=data_model_code, opts=opts)

        # PreviewTransaction: Preview a transaction
        api_response = api_instance.preview_transaction(scope, code, transaction_request, property_keys=property_keys, show_cancelled_transactions=show_cancelled_transactions, preserve_properties=preserve_properties, data_model_scope=data_model_scope, data_model_code=data_model_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->preview_transaction: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_request** | [**TransactionRequest**](TransactionRequest.md)| The transaction to be previewed. | 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Transaction\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 
 **show_cancelled_transactions** | **bool**| Option to specify whether to include previous versions of an amended transaction in the response.              Defaults to False if not specified. | [optional] 
 **preserve_properties** | **bool**| If the preview transaction is an amendment to an existing transaction, then setting this to true will carry forward any unmodified properties from the earlier version. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 

### Return type

[**ResourceListOfOutputTransaction**](ResourceListOfOutputTransaction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The predicted output relating to the Preview Transaction. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **resolve_instrument**
> UpsertPortfolioTransactionsResponse resolve_instrument(scope, code, instrument_identifier_type, instrument_identifier_value, from_effective_at=from_effective_at, re_resolve=re_resolve, request_body=request_body)

ResolveInstrument: Resolve instrument

Try to resolve the instrument for transaction and holdings for a given instrument identifier and a specified  period of time. Also update the instrument identifiers with the given instrument identifiers collection.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    instrument_identifier_type = 'instrument_identifier_type_example' # str | The instrument identifier type.
    instrument_identifier_value = 'instrument_identifier_value_example' # str | The value for the given instrument identifier.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. (optional)
    re_resolve = False # bool | When set to true, instrument resolution will be attempted for all transactions and holdings for the given identifier and date range.              When set to false (default behaviour), instrument resolution will only be attempted for those transactions and holdings that were previously unresolved. (optional) (default to False)
    request_body = {"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"} # Dict[str, str] | The dictionary with the instrument identifiers to be updated on the             transaction and holdings. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.resolve_instrument(scope, code, instrument_identifier_type, instrument_identifier_value, from_effective_at=from_effective_at, re_resolve=re_resolve, request_body=request_body, opts=opts)

        # ResolveInstrument: Resolve instrument
        api_response = api_instance.resolve_instrument(scope, code, instrument_identifier_type, instrument_identifier_value, from_effective_at=from_effective_at, re_resolve=re_resolve, request_body=request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->resolve_instrument: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **instrument_identifier_type** | **str**| The instrument identifier type. | 
 **instrument_identifier_value** | **str**| The value for the given instrument identifier. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | [optional] 
 **re_resolve** | **bool**| When set to true, instrument resolution will be attempted for all transactions and holdings for the given identifier and date range.              When set to false (default behaviour), instrument resolution will only be attempted for those transactions and holdings that were previously unresolved. | [optional] [default to False]
 **request_body** | [**Dict[str, str]**](str.md)| The dictionary with the instrument identifiers to be updated on the             transaction and holdings. | [optional] 

### Return type

[**UpsertPortfolioTransactionsResponse**](UpsertPortfolioTransactionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly updated or inserted transactions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_holdings**
> AdjustHolding set_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods, override_movement_name=override_movement_name, override_offset_movement_name=override_offset_movement_name)

SetHoldings: Set holdings

Set the holdings of the specified transaction portfolio to the provided targets. LUSID will automatically  construct adjustment transactions to ensure that the entire set of holdings for the transaction portfolio  are always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/docs/how-do-i-manually-adjust-or-set-holdings.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holdings should be set to the provided targets.
    adjust_holding_request = [{"instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/ibor/CurrentMarketValue":{"key":"Holding/ibor/CurrentMarketValue","value":{"metricValue":{"value":1000}}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","notionalCost":100,"variationMargin":25,"variationMarginPortfolioCcy":25}],"currency":"GBP","custodianAccountId":{"scope":"CustodianAccountScope","code":"CustodianAccountCode"}}] # List[AdjustHoldingRequest] | The complete set of target holdings for the transaction portfolio.
    reconciliation_methods = ['reconciliation_methods_example'] # List[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)
    override_movement_name = 'override_movement_name_example' # str | Optional parameter to override movement name for the set holdings. (optional)
    override_offset_movement_name = 'override_offset_movement_name_example' # str | Optional parameter will create an additional offset movement for the set holdings with this new name and transaction type: CarryAsPnl (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods, override_movement_name=override_movement_name, override_offset_movement_name=override_offset_movement_name, opts=opts)

        # SetHoldings: Set holdings
        api_response = api_instance.set_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods, override_movement_name=override_movement_name, override_offset_movement_name=override_offset_movement_name)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->set_holdings: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the holdings should be set to the provided targets. | 
 **adjust_holding_request** | [**List[AdjustHoldingRequest]**](AdjustHoldingRequest.md)| The complete set of target holdings for the transaction portfolio. | 
 **reconciliation_methods** | [**List[str]**](str.md)| Optional parameter for specifying a reconciliation method: e.g. FxForward. | [optional] 
 **override_movement_name** | **str**| Optional parameter to override movement name for the set holdings. | [optional] 
 **override_offset_movement_name** | **str**| Optional parameter will create an additional offset movement for the set holdings with this new name and transaction type: CarryAsPnl | [optional] 

### Return type

[**AdjustHolding**](AdjustHolding.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly set holdings |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_custodian_accounts**
> CustodianAccountsUpsertResponse upsert_custodian_accounts(scope, code, custodian_account_request)

UpsertCustodianAccounts: Upsert Custodian Accounts

Create or update Custodian Accounts in the Transaction Portfolios. A Custodian Account will be updated  if it already exists and created if it does not.  The batch limit per request is 2,000.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolio.
    code = 'code_example' # str | The code of the Transaction Portfolio. Together with the scope this uniquely identifies              the Transaction Portfolios.
    custodian_account_request = [{"scope":"ScopeA","code":"Account1","status":"Active","accountNumber":"10003786BGBP","accountName":"Account1 Sterling","accountingMethod":"FirstInFirstOut","currency":"GBP","properties":{},"custodianIdentifier":{"idTypeScope":"ScopeA","idTypeCode":"LegalEntityCode1","code":"LegalEntityValue1"},"accountType":"Cash"},{"scope":"ScopeB","code":"Account2","status":"Active","accountNumber":"10003786BEUR","accountName":"Account2 Euro","accountingMethod":"FirstInFirstOut","currency":"EUR","properties":{},"custodianIdentifier":{"idTypeScope":"ScopeA","idTypeCode":"LegalEntityCode2","code":"LegalEntityValue2"},"accountType":"Swap"}] # List[CustodianAccountRequest] | A list of Custodian Accounts to be created or updated.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_custodian_accounts(scope, code, custodian_account_request, opts=opts)

        # UpsertCustodianAccounts: Upsert Custodian Accounts
        api_response = api_instance.upsert_custodian_accounts(scope, code, custodian_account_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_custodian_accounts: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolio. | 
 **code** | **str**| The code of the Transaction Portfolio. Together with the scope this uniquely identifies              the Transaction Portfolios. | 
 **custodian_account_request** | [**List[CustodianAccountRequest]**](CustodianAccountRequest.md)| A list of Custodian Accounts to be created or updated. | 

### Return type

[**CustodianAccountsUpsertResponse**](CustodianAccountsUpsertResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly upserted custodian accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_custodian_accounts_properties**
> CustodianAccountProperties upsert_custodian_accounts_properties(scope, code, custodian_account_scope, custodian_account_code, request_body=request_body)

UpsertCustodianAccountsProperties: Upsert custodian accounts properties

Update or insert one or more properties onto a single custodian account. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'CustodianAccount'.                Upserting a property that exists for a Transaction Portfolios, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolios to update or insert the properties onto.
    code = 'code_example' # str | The code of the Transaction Portfolios to update or insert the properties onto. Together with the scope this uniquely identifies the Transaction Portfolios.
    custodian_account_scope = 'custodian_account_scope_example' # str | The scope of the Custodian Account to update or insert the properties onto.
    custodian_account_code = 'custodian_account_code_example' # str | The unique ID of the custodian account to create or update properties for.
    request_body = {"CustodianAccount/MyScope/FundManagerName":{"key":"CustodianAccount/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"CustodianAccount/MyScope/SomeProperty":{"key":"CustodianAccount/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"CustodianAccount/MyScope/AnotherProperty":{"key":"CustodianAccount/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"CustodianAccount/MyScope/ReBalanceInterval":{"key":"CustodianAccount/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be updated or inserted onto the Transaction Portfolio. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"CustodianAccount/Manager/Id\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_custodian_accounts_properties(scope, code, custodian_account_scope, custodian_account_code, request_body=request_body, opts=opts)

        # UpsertCustodianAccountsProperties: Upsert custodian accounts properties
        api_response = api_instance.upsert_custodian_accounts_properties(scope, code, custodian_account_scope, custodian_account_code, request_body=request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_custodian_accounts_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolios to update or insert the properties onto. | 
 **code** | **str**| The code of the Transaction Portfolios to update or insert the properties onto. Together with the scope this uniquely identifies the Transaction Portfolios. | 
 **custodian_account_scope** | **str**| The scope of the Custodian Account to update or insert the properties onto. | 
 **custodian_account_code** | **str**| The unique ID of the custodian account to create or update properties for. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Transaction Portfolio. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;CustodianAccount/Manager/Id\&quot;. | [optional] 

### Return type

[**CustodianAccountProperties**](CustodianAccountProperties.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_portfolio_details**
> PortfolioDetails upsert_portfolio_details(scope, code, create_portfolio_details, effective_at=effective_at)

UpsertPortfolioDetails: Upsert portfolio details

Create or update certain details for a particular transaction portfolio. The details are updated if they already exist, and inserted if they do not.                Note that not all elements of a transaction portfolio definition are  modifiable once it has been created due to the potential implications for data already stored.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the               scope this uniquely identifies the transaction portfolio.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_portfolio_details = CreatePortfolioDetails.from_json("")
    # create_portfolio_details = CreatePortfolioDetails.from_dict({})
    create_portfolio_details = CreatePortfolioDetails()
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the updated or inserted details should become valid.               Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_portfolio_details(scope, code, create_portfolio_details, effective_at=effective_at, opts=opts)

        # UpsertPortfolioDetails: Upsert portfolio details
        api_response = api_instance.upsert_portfolio_details(scope, code, create_portfolio_details, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_portfolio_details: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the               scope this uniquely identifies the transaction portfolio. | 
 **create_portfolio_details** | [**CreatePortfolioDetails**](CreatePortfolioDetails.md)| The details to create or update for the specified transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the updated or inserted details should become valid.               Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**PortfolioDetails**](PortfolioDetails.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly updated or inserted details |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_settlement_instructions**
> ResourceListOfTransactionSettlementInstruction upsert_settlement_instructions(scope, code, settlement_instruction_request)

[EARLY ACCESS] UpsertSettlementInstructions: Upsert Settlement Instructions.

Create or update instructions to settle specific transactions.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio.
    settlement_instruction_request = [{"settlementInstructionId":"settlementInstructionId","transactionId":"transactionId1","settlementCategory":"CashSettlement","instructionType":"Complete","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"contractualSettlementDate":"2024-01-01T00:00:00.0000000+00:00","actualSettlementDate":"2024-01-01T00:00:00.0000000+00:00","units":10,"subHoldingKeyOverrides":{},"properties":[]},{"settlementInstructionId":"settlementInstructionId-2","transactionId":"transactionId2","settlementCategory":"StockSettlement","instructionType":"Complete","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9"},"contractualSettlementDate":"2024-01-02T00:00:00.0000000+00:00","actualSettlementDate":"2024-01-05T00:00:00.0000000+00:00","units":10,"subHoldingKeyOverrides":{},"properties":[]}] # List[SettlementInstructionRequest] | The definition of the settlement instruction.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_settlement_instructions(scope, code, settlement_instruction_request, opts=opts)

        # [EARLY ACCESS] UpsertSettlementInstructions: Upsert Settlement Instructions.
        api_response = api_instance.upsert_settlement_instructions(scope, code, settlement_instruction_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_settlement_instructions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. | 
 **settlement_instruction_request** | [**List[SettlementInstructionRequest]**](SettlementInstructionRequest.md)| The definition of the settlement instruction. | 

### Return type

[**ResourceListOfTransactionSettlementInstruction**](ResourceListOfTransactionSettlementInstruction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created or undated Settlement Instructions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_transaction_properties**
> UpsertTransactionPropertiesResponse upsert_transaction_properties(scope, code, transaction_id, request_body)

UpsertTransactionProperties: Upsert transaction properties

Create or update one or more transaction properties for a single transaction in the transaction portfolio.  Each property will be updated if it already exists and created if it does not.  Both transaction and portfolio must exist at the time when properties are created or updated.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_id = 'transaction_id_example' # str | The unique ID of the transaction to create or update properties for.
    request_body = {"Transaction/MyScope/MyPropertyName":{"key":"Transaction/MyScope/MyPropertyName","value":{"metricValue":{"value":12345.5672,"unit":"Unit"}}},"Transaction/MyScope/MyPropertyName2":{"key":"Transaction/MyScope/MyPropertyName2","value":{"metricValue":{"value":925.3,"unit":"Unit"}}}} # Dict[str, PerpetualProperty] | The properties and their associated values to create or update.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_transaction_properties(scope, code, transaction_id, request_body, opts=opts)

        # UpsertTransactionProperties: Upsert transaction properties
        api_response = api_instance.upsert_transaction_properties(scope, code, transaction_id, request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_transaction_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique ID of the transaction to create or update properties for. | 
 **request_body** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md)| The properties and their associated values to create or update. | 

### Return type

[**UpsertTransactionPropertiesResponse**](UpsertTransactionPropertiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly updated or inserted transaction property |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_transactions**
> UpsertPortfolioTransactionsResponse upsert_transactions(scope, code, transaction_request, preserve_properties=preserve_properties, data_model_scope=data_model_scope, data_model_code=data_model_code)

UpsertTransactions: Upsert transactions

Create or update transactions in the transaction portfolio. A transaction will be updated  if it already exists and created if it does not.  The maximum number of transactions that this method can upsert per request is 10,000.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionPortfoliosApi
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
    api_instance = api_client_factory.build(TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_request = [{"transactionId":"TransactionId-111111","type":"StockIn","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"transactionDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","units":1000,"transactionPrice":{"price":123,"type":"Price"},"totalConsideration":{"amount":123000,"currency":"GBP"},"transactionCurrency":"GBP","properties":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"counterpartyId":"CounterpartyId-118263","source":"","otcConfirmation":{"counterpartyAgreementId":{"scope":"someScope","code":"someCode"}},"orderId":{"scope":"someScope","code":"ORD001"},"allocationId":{"scope":"someScope","code":"ALLOC001"}}] # List[TransactionRequest] | A list of transactions to be created or updated.
    preserve_properties = True # bool | If set to false, the entire property set will be overwritten by the provided properties. If not specified or set to true, only the properties provided will be updated. (optional) (default to True)
    data_model_scope = 'data_model_scope_example' # str | The optional scope of a Custom Data Model to use (optional)
    data_model_code = 'data_model_code_example' # str | The optional code of a Custom Data Model to use (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_transactions(scope, code, transaction_request, preserve_properties=preserve_properties, data_model_scope=data_model_scope, data_model_code=data_model_code, opts=opts)

        # UpsertTransactions: Upsert transactions
        api_response = api_instance.upsert_transactions(scope, code, transaction_request, preserve_properties=preserve_properties, data_model_scope=data_model_scope, data_model_code=data_model_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_request** | [**List[TransactionRequest]**](TransactionRequest.md)| A list of transactions to be created or updated. | 
 **preserve_properties** | **bool**| If set to false, the entire property set will be overwritten by the provided properties. If not specified or set to true, only the properties provided will be updated. | [optional] [default to True]
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 

### Return type

[**UpsertPortfolioTransactionsResponse**](UpsertPortfolioTransactionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly updated or inserted transactions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

