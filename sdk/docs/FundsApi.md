# lusid.FundsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_estimate_valuation_point**](FundsApi.md#accept_estimate_valuation_point) | **POST** /api/funds/{scope}/{code}/valuationpoints/$acceptestimate | [EARLY ACCESS] AcceptEstimateValuationPoint: Accepts an Estimate Valuation Point.
[**accrue_carry**](FundsApi.md#accrue_carry) | **POST** /api/funds/{scope}/{code}/carry/$accrue | [EARLY ACCESS] AccrueCarry: [EXPERIMENTAL] AccrueCarry: Accrue carried interest to the Fund&#39;s partners.
[**add_allocation_groups**](FundsApi.md#add_allocation_groups) | **POST** /api/funds/{scope}/{code}/allocationgroups | [EARLY ACCESS] AddAllocationGroups: Add Allocation Groups to a Fund.
[**add_series**](FundsApi.md#add_series) | **POST** /api/funds/{scope}/{code}/series | [EARLY ACCESS] AddSeries: Add Series to a Fund.
[**calculate_management_fees**](FundsApi.md#calculate_management_fees) | **POST** /api/funds/{scope}/{code}/fees/$calculate | [EARLY ACCESS] CalculateManagementFees: [EXPERIMENTAL] CalculateManagementFees: Calculate the management fee per partner for a period.
[**create_facility**](FundsApi.md#create_facility) | **POST** /api/funds/{scope}/{code}/facilities | [EXPERIMENTAL] CreateFacility: [EXPERIMENTAL] CreateFacility: Create a Facility.
[**create_fee**](FundsApi.md#create_fee) | **POST** /api/funds/{scope}/{code}/fees | [EARLY ACCESS] CreateFee: Create a Fee.
[**create_fund**](FundsApi.md#create_fund) | **POST** /api/funds/{scope} | [EARLY ACCESS] CreateFund: Create a Fund.
[**create_fund_v2**](FundsApi.md#create_fund_v2) | **POST** /api/funds/v2/{scope} | [EARLY ACCESS] CreateFundV2: Create a Fund V2 (Preview).
[**create_valuation_point**](FundsApi.md#create_valuation_point) | **POST** /api/funds/{scope}/{code}/valuationpoints/$create | [EARLY ACCESS] CreateValuationPoint: Create a Valuation Point.
[**deactivate_nav_types**](FundsApi.md#deactivate_nav_types) | **POST** /api/funds/{scope}/{code}/deactivateNavTypes | [EARLY ACCESS] DeactivateNavTypes: Deactivate NAV types on a Fund.
[**delete_bookmark**](FundsApi.md#delete_bookmark) | **DELETE** /api/funds/{scope}/{code}/bookmarks/{bookmarkCode} | [EARLY ACCESS] DeleteBookmark: Delete a Bookmark.
[**delete_facility**](FundsApi.md#delete_facility) | **DELETE** /api/funds/{scope}/{code}/facilities/{facilityCode} | [EXPERIMENTAL] DeleteFacility: [EXPERIMENTAL] DeleteFacility: Delete a Facility.
[**delete_fee**](FundsApi.md#delete_fee) | **DELETE** /api/funds/{scope}/{code}/fees/{feeCode} | [EARLY ACCESS] DeleteFee: Delete a Fee.
[**delete_fund**](FundsApi.md#delete_fund) | **DELETE** /api/funds/{scope}/{code} | [EARLY ACCESS] DeleteFund: Delete a Fund.
[**delete_nav_activity_adjustments**](FundsApi.md#delete_nav_activity_adjustments) | **POST** /api/funds/{scope}/{code}/navAdjustment/$delete | [EARLY ACCESS] DeleteNavActivityAdjustments: Delete Nav activity adjustments.
[**delete_series**](FundsApi.md#delete_series) | **DELETE** /api/funds/{scope}/{code}/shareclasses/{shareClassCode}/series/{seriesIdentifier} | [EARLY ACCESS] DeleteSeries: [EARLY ACCESS] DeleteSeries: Remove a Series from a Share Class of a Fund.
[**delete_valuation_point**](FundsApi.md#delete_valuation_point) | **DELETE** /api/funds/{scope}/{code}/valuationpoints/{diaryEntryCode} | [EARLY ACCESS] DeleteValuationPoint: Delete a Valuation Point.
[**diff_partner_statement**](FundsApi.md#diff_partner_statement) | **GET** /api/funds/{scope}/{code}/partners/{investorRecordId}/statements/{statementId}/$diff | [EARLY ACCESS] DiffPartnerStatement: [EXPERIMENTAL] DiffPartnerStatement: Compare two of a partner&#39;s statements.
[**finalise_candidate_valuation_point**](FundsApi.md#finalise_candidate_valuation_point) | **POST** /api/funds/{scope}/{code}/valuationpoints/$finalisecandidate | [EARLY ACCESS] FinaliseCandidateValuationPoint: Finalise a Candidate Valuation Point.
[**get_a2_b_data_for_fund**](FundsApi.md#get_a2_b_data_for_fund) | **POST** /api/funds/{scope}/{code}/valuationpoints/a2b/$query | [EARLY ACCESS] GetA2BDataForFund: Get A2B data for a Fund.
[**get_a2_b_movements_for_fund**](FundsApi.md#get_a2_b_movements_for_fund) | **POST** /api/funds/{scope}/{code}/valuationpoints/a2bmovements/$query | [EARLY ACCESS] GetA2BMovementsForFund: Get A2B movements for transaction portfolios in a Fund.
[**get_facility**](FundsApi.md#get_facility) | **GET** /api/funds/{scope}/{code}/facilities/{facilityCode} | [EXPERIMENTAL] GetFacility: [EXPERIMENTAL] GetFacility: Get a Facility for a specified Fund.
[**get_fee**](FundsApi.md#get_fee) | **GET** /api/funds/{scope}/{code}/fees/{feeCode} | [EARLY ACCESS] GetFee: Get a Fee for a specified Fund.
[**get_fee_properties**](FundsApi.md#get_fee_properties) | **GET** /api/funds/{scope}/{code}/fees/{feeCode}/properties | [EARLY ACCESS] GetFeeProperties: Get Fee properties.
[**get_fund**](FundsApi.md#get_fund) | **GET** /api/funds/{scope}/{code} | [EARLY ACCESS] GetFund: Get a Fund.
[**get_fund_performance**](FundsApi.md#get_fund_performance) | **GET** /api/funds/{scope}/{code}/performance | [EARLY ACCESS] GetFundPerformance: [EARLY ACCESS] GetFundPerformance: Get a fund&#39;s performance measures over all its partners.
[**get_fund_properties**](FundsApi.md#get_fund_properties) | **GET** /api/funds/{scope}/{code}/properties | [EARLY ACCESS] GetFundProperties: Get Fund properties.
[**get_holding_contributors_for_fund**](FundsApi.md#get_holding_contributors_for_fund) | **POST** /api/funds/{scope}/{code}/holdings/{holdingId}/contributors | [EARLY ACCESS] GetHoldingContributorsForFund: Get holdings contributors for transaction portfolios in a Fund.
[**get_holdings_for_fund**](FundsApi.md#get_holdings_for_fund) | **POST** /api/funds/{scope}/{code}/$holdings | [EARLY ACCESS] GetHoldingsForFund: Get holdings for transaction portfolios in a Fund.
[**get_partner_capital_account**](FundsApi.md#get_partner_capital_account) | **GET** /api/funds/{scope}/{code}/partners/{irScope}/{irCode}/capitalaccount | [EARLY ACCESS] GetPartnerCapitalAccount: [EARLY ACCESS] GetPartnerCapitalAccount: Get a partner&#39;s capital account statement.
[**get_partner_performance**](FundsApi.md#get_partner_performance) | **GET** /api/funds/{scope}/{code}/partners/{irScope}/{irCode}/performance | [EARLY ACCESS] GetPartnerPerformance: [EARLY ACCESS] GetPartnerPerformance: Get a partner&#39;s performance measures.
[**get_partner_unfunded_reconciliation**](FundsApi.md#get_partner_unfunded_reconciliation) | **GET** /api/funds/{scope}/{code}/partners/{investorRecordId}/unfundedreconciliation | [EARLY ACCESS] GetPartnerUnfundedReconciliation: [EARLY ACCESS] GetPartnerUnfundedReconciliation: Get a partner&#39;s unfunded commitment statement.
[**get_partners**](FundsApi.md#get_partners) | **GET** /api/funds/{scope}/{code}/partners | [EARLY ACCESS] GetPartners: [EARLY ACCESS] GetPartners: Get the partners of a partnership fund.
[**get_partnership_config_pack**](FundsApi.md#get_partnership_config_pack) | **GET** /api/funds/{scope}/{code}/partnershipaccounting/configpack | [EARLY ACCESS] GetPartnershipConfigPack: [EXPERIMENTAL] GetPartnershipConfigPack: Get the partnership configuration pack of a Fund.
[**get_series**](FundsApi.md#get_series) | **GET** /api/funds/{scope}/{code}/series | [EARLY ACCESS] GetSeries: [EARLY ACCESS] GetSeries: List the Series of a Fund.
[**get_valuation_for_fund**](FundsApi.md#get_valuation_for_fund) | **POST** /api/funds/{scope}/{code}/$valuation | [EARLY ACCESS] GetValuationForFund: Perform valuation for a Fund.
[**get_valuation_point_data**](FundsApi.md#get_valuation_point_data) | **POST** /api/funds/{scope}/{code}/valuationpoints/$query | [EARLY ACCESS] GetValuationPointData: Get Valuation Point Data for a Fund.
[**get_valuation_point_journal_entry_lines**](FundsApi.md#get_valuation_point_journal_entry_lines) | **POST** /api/funds/{scope}/{code}/valuationpoints/journalentrylines/$query | [EARLY ACCESS] GetValuationPointJournalEntryLines: Get the Journal Entry Lines for the given Fund.
[**get_valuation_point_pnl_summary**](FundsApi.md#get_valuation_point_pnl_summary) | **POST** /api/funds/{scope}/{code}/valuationpoints/pnlsummary/$query | [EARLY ACCESS] GetValuationPointPnlSummary: Get a PnL summary for the given Valuation Point in the Fund.
[**get_valuation_point_quotes**](FundsApi.md#get_valuation_point_quotes) | **POST** /api/funds/{scope}/{code}/valuationpoints/quotes/$query | [EARLY ACCESS] GetValuationPointQuotes: Get the Quotes for the given Fund and Valuation Point.
[**get_valuation_point_transactions**](FundsApi.md#get_valuation_point_transactions) | **POST** /api/funds/{scope}/{code}/valuationpoints/transactions/$query | [EARLY ACCESS] GetValuationPointTransactions: Get the Transactions for the given Fund.
[**get_valuation_point_trial_balance**](FundsApi.md#get_valuation_point_trial_balance) | **POST** /api/funds/{scope}/{code}/valuationpoints/trialbalance/$query | [EARLY ACCESS] GetValuationPointTrialBalance: Get Trial Balance for the given Fund.
[**get_valuation_point_unsettled_transactions**](FundsApi.md#get_valuation_point_unsettled_transactions) | **POST** /api/funds/{scope}/{code}/valuationpoints/unsettledtransactions/$query | [EARLY ACCESS] GetValuationPointUnsettledTransactions: Get Unsettled Transactions for the given Fund.
[**list_facilities**](FundsApi.md#list_facilities) | **GET** /api/funds/{scope}/{code}/facilities | [EXPERIMENTAL] ListFacilities: [EXPERIMENTAL] ListFacilities: List Facilities for a specified Fund.
[**list_fees**](FundsApi.md#list_fees) | **GET** /api/funds/{scope}/{code}/fees | [EARLY ACCESS] ListFees: List Fees for a specified Fund.
[**list_fund_calendar**](FundsApi.md#list_fund_calendar) | **GET** /api/funds/{scope}/{code}/calendar | [EARLY ACCESS] ListFundCalendar: List Fund Calendar.
[**list_fund_calendar_entries**](FundsApi.md#list_fund_calendar_entries) | **GET** /api/funds/{scope}/{code}/calendars | [EARLY ACCESS] ListFundCalendarEntries: List Fund Calendar Entries.
[**list_funds**](FundsApi.md#list_funds) | **GET** /api/funds | [EARLY ACCESS] ListFunds: List Funds.
[**list_nav_activity_adjustments**](FundsApi.md#list_nav_activity_adjustments) | **GET** /api/funds/{scope}/{code}/navAdjustment | [EARLY ACCESS] ListNavActivityAdjustments: List NAV adjustment activities applied to a valuation point
[**list_partner_capital_accounts**](FundsApi.md#list_partner_capital_accounts) | **GET** /api/funds/{scope}/{code}/capitalaccounts | [EARLY ACCESS] ListPartnerCapitalAccounts: [EARLY ACCESS] ListPartnerCapitalAccounts: List the capital account statements of a fund&#39;s partners.
[**list_partner_statements**](FundsApi.md#list_partner_statements) | **GET** /api/funds/{scope}/{code}/partners/{investorRecordId}/statements | [EARLY ACCESS] ListPartnerStatements: [EXPERIMENTAL] ListPartnerStatements: List the statements produced for a partner.
[**list_valuation_point_complex_market_data**](FundsApi.md#list_valuation_point_complex_market_data) | **POST** /api/funds/{scope}/{code}/valuationpoints/complexmarketdata/$query | [EARLY ACCESS] ListValuationPointComplexMarketData: List the Complex Market Data for the given Fund and Valuation Point.
[**list_valuation_point_instruments**](FundsApi.md#list_valuation_point_instruments) | **GET** /api/funds/{scope}/{code}/valuationpoints/instruments/$query | [EARLY ACCESS] ListValuationPointInstruments: List Instruments inside a valuation point
[**list_valuation_point_overview**](FundsApi.md#list_valuation_point_overview) | **GET** /api/funds/{scope}/{code}/valuationPointOverview | [EARLY ACCESS] ListValuationPointOverview: List Valuation Points Overview for a given Fund.
[**patch_fee**](FundsApi.md#patch_fee) | **PATCH** /api/funds/{scope}/{code}/fees/{feeCode} | [EARLY ACCESS] PatchFee: Patch Fee.
[**patch_fund**](FundsApi.md#patch_fund) | **PATCH** /api/funds/{scope}/{code} | [EARLY ACCESS] PatchFund: Patch a Fund.
[**produce_partner_statement**](FundsApi.md#produce_partner_statement) | **POST** /api/funds/{scope}/{code}/partners/{investorRecordId}/statements | [EARLY ACCESS] ProducePartnerStatement: [EXPERIMENTAL] ProducePartnerStatement: Produce a partner&#39;s capital statement for a period.
[**query_cash_statement**](FundsApi.md#query_cash_statement) | **POST** /api/funds/{scope}/{code}/valuationpoints/cashstatement/$query | [DEPRECATED] QueryCashStatement: [DEPRECATED] QueryCashStatement: Query cash statement for a Fund valuation point.
[**query_cash_statement_local_currency**](FundsApi.md#query_cash_statement_local_currency) | **POST** /api/funds/{scope}/{code}/valuationpoints/cashstatementlocalcurrency/$query | [EARLY ACCESS] QueryCashStatementLocalCurrency: [EXPERIMENTAL] QueryCashStatementLocalCurrency: Query the local-currency cash statement for a Fund valuation point.
[**revert_valuation_point_to_estimate**](FundsApi.md#revert_valuation_point_to_estimate) | **POST** /api/funds/{scope}/{code}/valuationpoints/$reverttoestimate | [EARLY ACCESS] RevertValuationPointToEstimate: Reverts a Final Valuation Point to Estimate.
[**run_partner_allocations**](FundsApi.md#run_partner_allocations) | **POST** /api/funds/{scope}/{code}/partnerallocations/$run | [EARLY ACCESS] RunPartnerAllocations: [EXPERIMENTAL] RunPartnerAllocations: Allocate a period&#39;s income to the Fund&#39;s partners.
[**set_share_class_instruments**](FundsApi.md#set_share_class_instruments) | **PUT** /api/funds/{scope}/{code}/shareclasses | [EARLY ACCESS] SetShareClassInstruments: Set the ShareClass Instruments on a Fund.
[**update_valuation_point**](FundsApi.md#update_valuation_point) | **PUT** /api/funds/{scope}/{code}/valuationpoints | [EARLY ACCESS] UpdateValuationPoint: Update a Valuation Point.
[**upsert_bookmark**](FundsApi.md#upsert_bookmark) | **POST** /api/funds/{scope}/{code}/bookmarks | [EARLY ACCESS] UpsertBookmark: Upsert a bookmark.
[**upsert_diary_entry_type_valuation_point**](FundsApi.md#upsert_diary_entry_type_valuation_point) | **POST** /api/funds/{scope}/{code}/valuationpoints | [EARLY ACCESS] UpsertDiaryEntryTypeValuationPoint: Upsert a Valuation Point.
[**upsert_fee_properties**](FundsApi.md#upsert_fee_properties) | **POST** /api/funds/{scope}/{code}/fees/{feeCode}/properties/$upsert | [EARLY ACCESS] UpsertFeeProperties: Upsert Fee properties.
[**upsert_fund_properties**](FundsApi.md#upsert_fund_properties) | **POST** /api/funds/{scope}/{code}/properties/$upsert | [EARLY ACCESS] UpsertFundProperties: Upsert Fund properties.
[**upsert_nav_activity_adjustments**](FundsApi.md#upsert_nav_activity_adjustments) | **POST** /api/funds/{scope}/{code}/navAdjustment | [EARLY ACCESS] UpsertNavActivityAdjustments: Upsert NAV adjustment activities to a valuation point


# **accept_estimate_valuation_point**
> AcceptEstimateValuationPointResponse accept_estimate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)

[EARLY ACCESS] AcceptEstimateValuationPoint: Accepts an Estimate Valuation Point.

Accepts the specified estimate Valuation Point.  Should the Valuation Point differ since the Valuation Point was last run, both Valuation Points will be returned and status will be marked as 'Candidate',  otherwise it will be marked as 'Final'.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_request = ValuationPointDataRequest.from_json("")
    # valuation_point_data_request = ValuationPointDataRequest.from_dict({})
    valuation_point_data_request = ValuationPointDataRequest()
    nav_type_code = 'nav_type_code_example' # str | When provided, accepts the Valuation Point of the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.accept_estimate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] AcceptEstimateValuationPoint: Accepts an Estimate Valuation Point.
        api_response = api_instance.accept_estimate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->accept_estimate_valuation_point: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_request** | [**ValuationPointDataRequest**](ValuationPointDataRequest.md)| The valuationPointDataRequest which contains the Diary Entry code for the Estimate Valuation Point to move to Candidate or Final state. | 
 **nav_type_code** | **str**| When provided, accepts the Valuation Point of the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**AcceptEstimateValuationPointResponse**](AcceptEstimateValuationPointResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Accepted Estimate point and status after being Accepted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **accrue_carry**
> CarryAccrualResult accrue_carry(scope, code, carry_accrual_request, as_at=as_at)

[EARLY ACCESS] AccrueCarry: [EXPERIMENTAL] AccrueCarry: Accrue carried interest to the Fund's partners.

Take the carry each partner has earned to the period end, as the waterfall states it, and book the movement  against what is already accrued on the books.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # carry_accrual_request = CarryAccrualRequest.from_json("")
    # carry_accrual_request = CarryAccrualRequest.from_dict({})
    carry_accrual_request = CarryAccrualRequest()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.accrue_carry(scope, code, carry_accrual_request, as_at=as_at, opts=opts)

        # [EARLY ACCESS] AccrueCarry: [EXPERIMENTAL] AccrueCarry: Accrue carried interest to the Fund's partners.
        api_response = api_instance.accrue_carry(scope, code, carry_accrual_request, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->accrue_carry: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **carry_accrual_request** | [**CarryAccrualRequest**](CarryAccrualRequest.md)| The carry to accrue. | 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**CarryAccrualResult**](CarryAccrualResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The carry accrual movement per partner. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **add_allocation_groups**
> Fund add_allocation_groups(scope, code, allocation_group_definition)

[EARLY ACCESS] AddAllocationGroups: Add Allocation Groups to a Fund.

Add the given Allocation Group definitions to the Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    allocation_group_definition = [{"classes":[{"shareClassShortCode":"ScA","apportionmentFactor":0.6},{"shareClassShortCode":"ScB","apportionmentFactor":0.4}],"name":"Allocation Group 1","shareClassShortCode":"ScA"}] # List[AllocationGroupDefinition] | The definitions of the Allocation Groups to add to the Fund.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_allocation_groups(scope, code, allocation_group_definition, opts=opts)

        # [EARLY ACCESS] AddAllocationGroups: Add Allocation Groups to a Fund.
        api_response = api_instance.add_allocation_groups(scope, code, allocation_group_definition)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->add_allocation_groups: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **allocation_group_definition** | [**List[AllocationGroupDefinition]**](AllocationGroupDefinition.md)| The definitions of the Allocation Groups to add to the Fund. | 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund with the added Allocation Groups. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **add_series**
> Fund add_series(scope, code, series_definition_request)

[EARLY ACCESS] AddSeries: Add Series to a Fund.

Add the given Series definitions to the specified Share Classes of the Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    series_definition_request = [{"shareClassCode":"ShareClass1","seriesDefinitions":[{"seriesIdentifier":"Series1","seriesType":"Lead","launchDate":"2024-01-01T00:00:00.0000000+00:00","launchPriceType":"Manual","domCcy":"GBP","properties":{}}]}] # List[SeriesDefinitionRequest] | The definitions of the Series to add.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_series(scope, code, series_definition_request, opts=opts)

        # [EARLY ACCESS] AddSeries: Add Series to a Fund.
        api_response = api_instance.add_series(scope, code, series_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->add_series: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **series_definition_request** | [**List[SeriesDefinitionRequest]**](SeriesDefinitionRequest.md)| The definitions of the Series to add. | 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund with the added Series. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **calculate_management_fees**
> ManagementFeeResult calculate_management_fees(scope, code, management_fee_request, as_at=as_at)

[EARLY ACCESS] CalculateManagementFees: [EXPERIMENTAL] CalculateManagementFees: Calculate the management fee per partner for a period.

Charge the Fund's management fee on each partner's capital base for the period, net of any fee income offsets,  and book the net fee unless the request asks only for the calculation.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # management_fee_request = ManagementFeeRequest.from_json("")
    # management_fee_request = ManagementFeeRequest.from_dict({})
    management_fee_request = ManagementFeeRequest()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.calculate_management_fees(scope, code, management_fee_request, as_at=as_at, opts=opts)

        # [EARLY ACCESS] CalculateManagementFees: [EXPERIMENTAL] CalculateManagementFees: Calculate the management fee per partner for a period.
        api_response = api_instance.calculate_management_fees(scope, code, management_fee_request, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->calculate_management_fees: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **management_fee_request** | [**ManagementFeeRequest**](ManagementFeeRequest.md)| The fee period, basis and offsets. | 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**ManagementFeeResult**](ManagementFeeResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The management fee per partner. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_facility**
> Facility create_facility(scope, code, facility_request)

[EXPERIMENTAL] CreateFacility: [EXPERIMENTAL] CreateFacility: Create a Facility.

Create the given Facility against a Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # facility_request = FacilityRequest.from_json("")
    # facility_request = FacilityRequest.from_dict({})
    facility_request = FacilityRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_facility(scope, code, facility_request, opts=opts)

        # [EXPERIMENTAL] CreateFacility: [EXPERIMENTAL] CreateFacility: Create a Facility.
        api_response = api_instance.create_facility(scope, code, facility_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->create_facility: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **facility_request** | [**FacilityRequest**](FacilityRequest.md)| The Facility to create. | 

### Return type

[**Facility**](Facility.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Facility. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_fee**
> Fee create_fee(scope, code, fee_request, nav_type_code=nav_type_code)

[EARLY ACCESS] CreateFee: Create a Fee.

Create the given Fee.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # fee_request = FeeRequest.from_json("")
    # fee_request = FeeRequest.from_dict({})
    fee_request = FeeRequest()
    nav_type_code = 'nav_type_code_example' # str | When provided, creates the Fee against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_fee(scope, code, fee_request, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] CreateFee: Create a Fee.
        api_response = api_instance.create_fee(scope, code, fee_request, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->create_fee: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_request** | [**FeeRequest**](FeeRequest.md)| The Fee to create. | 
 **nav_type_code** | **str**| When provided, creates the Fee against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**Fee**](Fee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_fund**
> Fund create_fund(scope, fund_request)

[EARLY ACCESS] CreateFund: Create a Fund.

Create the given Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # fund_request = FundRequest.from_json("")
    # fund_request = FundRequest.from_dict({})
    fund_request = FundRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_fund(scope, fund_request, opts=opts)

        # [EARLY ACCESS] CreateFund: Create a Fund.
        api_response = api_instance.create_fund(scope, fund_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->create_fund: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **fund_request** | [**FundRequest**](FundRequest.md)| The definition of the Fund. | 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_fund_v2**
> Fund create_fund_v2(scope, fund_definition_request)

[EARLY ACCESS] CreateFundV2: Create a Fund V2 (Preview).

Create the given V2 Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # fund_definition_request = FundDefinitionRequest.from_json("")
    # fund_definition_request = FundDefinitionRequest.from_dict({})
    fund_definition_request = FundDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_fund_v2(scope, fund_definition_request, opts=opts)

        # [EARLY ACCESS] CreateFundV2: Create a Fund V2 (Preview).
        api_response = api_instance.create_fund_v2(scope, fund_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->create_fund_v2: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **fund_definition_request** | [**FundDefinitionRequest**](FundDefinitionRequest.md)| The definition of the Fund. | 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_valuation_point**
> ValuationPoint create_valuation_point(scope, code, create_valuation_point_request, nav_type_code=nav_type_code)

[EARLY ACCESS] CreateValuationPoint: Create a Valuation Point.

Insert the estimate Valuation Point.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_valuation_point_request = CreateValuationPointRequest.from_json("")
    # create_valuation_point_request = CreateValuationPointRequest.from_dict({})
    create_valuation_point_request = CreateValuationPointRequest()
    nav_type_code = 'nav_type_code_example' # str | When provided, creates the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_valuation_point(scope, code, create_valuation_point_request, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] CreateValuationPoint: Create a Valuation Point.
        api_response = api_instance.create_valuation_point(scope, code, create_valuation_point_request, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->create_valuation_point: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **create_valuation_point_request** | [**CreateValuationPointRequest**](CreateValuationPointRequest.md)| The Valuation Point Estimate definition to create. | 
 **nav_type_code** | **str**| When provided, creates the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPoint**](ValuationPoint.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created estimated Valuation Point |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **deactivate_nav_types**
> Fund deactivate_nav_types(scope, code, request_body, delete_mode=delete_mode)

[EARLY ACCESS] DeactivateNavTypes: Deactivate NAV types on a Fund.

Deactivate the given NAV types on the Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    request_body = ["NavTypeCode1","NavTypeCode2"] # List[str] | The codes of the nav types to be deactivated.
    delete_mode = 'delete_mode_example' # str | The delete mode to use. Default value: Soft. Available values: Soft, Hard. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.deactivate_nav_types(scope, code, request_body, delete_mode=delete_mode, opts=opts)

        # [EARLY ACCESS] DeactivateNavTypes: Deactivate NAV types on a Fund.
        api_response = api_instance.deactivate_nav_types(scope, code, request_body, delete_mode=delete_mode)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->deactivate_nav_types: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **request_body** | [**List[str]**](str.md)| The codes of the nav types to be deactivated. | 
 **delete_mode** | **str**| The delete mode to use. Default value: Soft. Available values: Soft, Hard. | [optional] 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund with the specified NAV types deactivated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_bookmark**
> DeletedEntityResponse delete_bookmark(scope, code, bookmark_code, nav_type_code=nav_type_code)

[EARLY ACCESS] DeleteBookmark: Delete a Bookmark.

Deletes the given Bookmark.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    bookmark_code = 'bookmark_code_example' # str | The bookmark code for the bookmark to be deleted.
    nav_type_code = 'nav_type_code_example' # str | When provided, deletes the Bookmark against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_bookmark(scope, code, bookmark_code, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] DeleteBookmark: Delete a Bookmark.
        api_response = api_instance.delete_bookmark(scope, code, bookmark_code, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->delete_bookmark: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **bookmark_code** | **str**| The bookmark code for the bookmark to be deleted. | 
 **nav_type_code** | **str**| When provided, deletes the Bookmark against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Bookmark was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_facility**
> DeletedEntityResponse delete_facility(scope, code, facility_code)

[EXPERIMENTAL] DeleteFacility: [EXPERIMENTAL] DeleteFacility: Delete a Facility.

Delete the given Facility.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    facility_code = 'facility_code_example' # str | The code of the Facility to be deleted.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_facility(scope, code, facility_code, opts=opts)

        # [EXPERIMENTAL] DeleteFacility: [EXPERIMENTAL] DeleteFacility: Delete a Facility.
        api_response = api_instance.delete_facility(scope, code, facility_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->delete_facility: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **facility_code** | **str**| The code of the Facility to be deleted. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Facility was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_fee**
> DeletedEntityResponse delete_fee(scope, code, fee_code)

[EARLY ACCESS] DeleteFee: Delete a Fee.

Delete the given Fee.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    fee_code = 'fee_code_example' # str | The code of the Fee to be deleted.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_fee(scope, code, fee_code, opts=opts)

        # [EARLY ACCESS] DeleteFee: Delete a Fee.
        api_response = api_instance.delete_fee(scope, code, fee_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->delete_fee: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_code** | **str**| The code of the Fee to be deleted. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Fee was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_fund**
> DeletedEntityResponse delete_fund(scope, code)

[EARLY ACCESS] DeleteFund: Delete a Fund.

Delete the given Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund to be deleted.
    code = 'code_example' # str | The code of the Fund to be deleted. Together with the scope this uniquely identifies the Fund.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_fund(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteFund: Delete a Fund.
        api_response = api_instance.delete_fund(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->delete_fund: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund to be deleted. | 
 **code** | **str**| The code of the Fund to be deleted. Together with the scope this uniquely identifies the Fund. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Fund was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_nav_activity_adjustments**
> DeletedEntityResponse delete_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment_response, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)

[EARLY ACCESS] DeleteNavActivityAdjustments: Delete Nav activity adjustments.

Delete Nav activity adjustments on a Valuation Point.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope is the unique identifier for the given Fund.
    valuation_point_code = 'valuation_point_code_example' # str | The valuation point Code to delete the adjustment from
    nav_activity_adjustment_response = [{"navActivityAdjustmentSource":"Undefined","asAt":"2024-01-01T00:00:00.0000000+00:00","portfolioScope":"portfolioScope1","portfolioCode":"portfolioCode1","transactionId":"transactionId1","navActivityAdjustmentType":"PortfolioTransactionAdjustment"}] # List[NavActivityAdjustmentResponse] | The request describing the Nav activity adjustments to delete from a specific valuation point and nav type
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    valuation_point_code_variant = 'valuation_point_code_variant_example' # str | The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment_response, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant, opts=opts)

        # [EARLY ACCESS] DeleteNavActivityAdjustments: Delete Nav activity adjustments.
        api_response = api_instance.delete_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment_response, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->delete_nav_activity_adjustments: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | 
 **valuation_point_code** | **str**| The valuation point Code to delete the adjustment from | 
 **nav_activity_adjustment_response** | [**List[NavActivityAdjustmentResponse]**](NavActivityAdjustmentResponse.md)| The request describing the Nav activity adjustments to delete from a specific valuation point and nav type | 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Nav activity adjustments were deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_series**
> DeletedEntityResponse delete_series(scope, code, share_class_code, series_identifier)

[EARLY ACCESS] DeleteSeries: [EARLY ACCESS] DeleteSeries: Remove a Series from a Share Class of a Fund.

Removes the Series from the Share Class. A Series that still has units in issue cannot be removed.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    share_class_code = 'share_class_code_example' # str | The short code of the Share Class the Series belongs to.
    series_identifier = 'series_identifier_example' # str | The identifier of the Series to remove.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_series(scope, code, share_class_code, series_identifier, opts=opts)

        # [EARLY ACCESS] DeleteSeries: [EARLY ACCESS] DeleteSeries: Remove a Series from a Share Class of a Fund.
        api_response = api_instance.delete_series(scope, code, share_class_code, series_identifier)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->delete_series: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **share_class_code** | **str**| The short code of the Share Class the Series belongs to. | 
 **series_identifier** | **str**| The identifier of the Series to remove. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Series was removed. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_valuation_point**
> DeletedEntityResponse delete_valuation_point(scope, code, diary_entry_code, diary_entry_code_variant=diary_entry_code_variant, nav_type_code=nav_type_code)

[EARLY ACCESS] DeleteValuationPoint: Delete a Valuation Point.

Deletes the given Valuation Point.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    diary_entry_code = 'diary_entry_code_example' # str | The diary entry code for the valuation Point to be deleted.
    diary_entry_code_variant = 'diary_entry_code_variant_example' # str | The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. This is working only for the Estimates. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, deletes the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_valuation_point(scope, code, diary_entry_code, diary_entry_code_variant=diary_entry_code_variant, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] DeleteValuationPoint: Delete a Valuation Point.
        api_response = api_instance.delete_valuation_point(scope, code, diary_entry_code, diary_entry_code_variant=diary_entry_code_variant, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->delete_valuation_point: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **diary_entry_code** | **str**| The diary entry code for the valuation Point to be deleted. | 
 **diary_entry_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. This is working only for the Estimates. | [optional] 
 **nav_type_code** | **str**| When provided, deletes the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Valuation Point was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **diff_partner_statement**
> PartnerStatementDiff diff_partner_statement(scope, code, investor_record_id, statement_id, against)

[EARLY ACCESS] DiffPartnerStatement: [EXPERIMENTAL] DiffPartnerStatement: Compare two of a partner's statements.

Compare a partner's statement against another produced for the same partner, figure by figure.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    investor_record_id = 'investor_record_id_example' # str | The investor record the statements are for.
    statement_id = 'statement_id_example' # str | The identifier of the statement to compare.
    against = 'against_example' # str | The identifier of the statement to compare against.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.diff_partner_statement(scope, code, investor_record_id, statement_id, against, opts=opts)

        # [EARLY ACCESS] DiffPartnerStatement: [EXPERIMENTAL] DiffPartnerStatement: Compare two of a partner's statements.
        api_response = api_instance.diff_partner_statement(scope, code, investor_record_id, statement_id, against)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->diff_partner_statement: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **investor_record_id** | **str**| The investor record the statements are for. | 
 **statement_id** | **str**| The identifier of the statement to compare. | 
 **against** | **str**| The identifier of the statement to compare against. | 

### Return type

[**PartnerStatementDiff**](PartnerStatementDiff.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The figures that differ between the two statements. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **finalise_candidate_valuation_point**
> ValuationPointDataResponse finalise_candidate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)

[EARLY ACCESS] FinaliseCandidateValuationPoint: Finalise a Candidate Valuation Point.

Moves a 'Candidate' status Valuation Point to status 'Final'.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_request = ValuationPointDataRequest.from_json("")
    # valuation_point_data_request = ValuationPointDataRequest.from_dict({})
    valuation_point_data_request = ValuationPointDataRequest()
    nav_type_code = 'nav_type_code_example' # str | When provided, finalises the Valuation Point of the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.finalise_candidate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] FinaliseCandidateValuationPoint: Finalise a Candidate Valuation Point.
        api_response = api_instance.finalise_candidate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->finalise_candidate_valuation_point: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_request** | [**ValuationPointDataRequest**](ValuationPointDataRequest.md)| The details of the Valuation Point to mark as final. | 
 **nav_type_code** | **str**| When provided, finalises the Valuation Point of the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointDataResponse**](ValuationPointDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Valuation Point response as a result of it be marked as Final. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_a2_b_data_for_fund**
> VersionedResourceListOfFundA2BDataRecord get_a2_b_data_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys)

[EARLY ACCESS] GetA2BDataForFund: Get A2B data for a Fund.

Get the A2B data for transaction portfolios in a specified Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to resolve the fund and the timeline. Defaults              to return the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" domain to decorate onto              the A2B data. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_a2_b_data_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] GetA2BDataForFund: Get A2B data for a Fund.
        api_response = api_instance.get_a2_b_data_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_a2_b_data_for_fund: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the A2B data. This includes start and end dates. | 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to resolve the fund and the timeline. Defaults              to return the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the A2B data. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 

### Return type

[**VersionedResourceListOfFundA2BDataRecord**](VersionedResourceListOfFundA2BDataRecord.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The A2B data for transaction portfolios in a Fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_a2_b_movements_for_fund**
> VersionedResourceListOfFundA2BMovementRecord get_a2_b_movements_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys)

[EARLY ACCESS] GetA2BMovementsForFund: Get A2B movements for transaction portfolios in a Fund.

Get the A2B movement records of transaction portfolios in a specified Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to resolve the fund and the timeline. Defaults              to return the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" domain to decorate onto              the A2B movements. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_a2_b_movements_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] GetA2BMovementsForFund: Get A2B movements for transaction portfolios in a Fund.
        api_response = api_instance.get_a2_b_movements_for_fund(scope, code, valuation_point_data_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_a2_b_movements_for_fund: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the A2B movements. This includes start and end dates. | 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to resolve the fund and the timeline. Defaults              to return the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the A2B movements. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 

### Return type

[**VersionedResourceListOfFundA2BMovementRecord**](VersionedResourceListOfFundA2BMovementRecord.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The A2B movement records of transaction portfolios for a Fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_facility**
> Facility get_facility(scope, code, facility_code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetFacility: [EXPERIMENTAL] GetFacility: Get a Facility for a specified Fund.

Retrieve a Facility for a specified Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    facility_code = 'facility_code_example' # str | The code of the Facility.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Facility. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Facility. Defaults to returning the latest version of the Facility if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_facility(scope, code, facility_code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetFacility: [EXPERIMENTAL] GetFacility: Get a Facility for a specified Fund.
        api_response = api_instance.get_facility(scope, code, facility_code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_facility: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **facility_code** | **str**| The code of the Facility. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Facility. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Facility. Defaults to returning the latest version of the Facility if not specified. | [optional] 

### Return type

[**Facility**](Facility.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Facility definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_fee**
> Fee get_fee(scope, code, fee_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetFee: Get a Fee for a specified Fund.

Retrieve a fee for a specified Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    fee_code = 'fee_code_example' # str | The code of the Fee.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Fee properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Fee. Defaults to returning the latest version of the Fee if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Fee' domain to decorate onto the Fee.              These must take the format {domain}/{scope}/{code}, for example 'Fee/Account/Id'. If no properties are specified, then no properties will be returned. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_fee(scope, code, fee_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] GetFee: Get a Fee for a specified Fund.
        api_response = api_instance.get_fee(scope, code, fee_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_fee: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_code** | **str**| The code of the Fee. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Fee properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fee. Defaults to returning the latest version of the Fee if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fee&#39; domain to decorate onto the Fee.              These must take the format {domain}/{scope}/{code}, for example &#39;Fee/Account/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Fee**](Fee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fee definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_fee_properties**
> FeeProperties get_fee_properties(scope, code, fee_code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetFeeProperties: Get Fee properties.

Get all the properties of a single fee.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    fee_code = 'fee_code_example' # str | The code of the Fee to get the properties for.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the Fee's properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Fee's properties. Defaults to return the latest version of each property if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_fee_properties(scope, code, fee_code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetFeeProperties: Get Fee properties.
        api_response = api_instance.get_fee_properties(scope, code, fee_code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_fee_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_code** | **str**| The code of the Fee to get the properties for. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Fee&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fee&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**FeeProperties**](FeeProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified fee |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_fund**
> Fund get_fund(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetFund: Get a Fund.

Retrieve the definition of a particular Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Fund properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Fund' domain to decorate onto the Fund.              These must take the format {domain}/{scope}/{code}, for example 'Fund/Manager/Id'. If no properties are specified, then no properties will be returned. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_fund(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] GetFund: Get a Fund.
        api_response = api_instance.get_fund(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_fund: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Fund properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fund&#39; domain to decorate onto the Fund.              These must take the format {domain}/{scope}/{code}, for example &#39;Fund/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_fund_performance**
> PartnerPerformance get_fund_performance(scope, code, nav_type_code=nav_type_code, as_at=as_at)

[EARLY ACCESS] GetFundPerformance: [EARLY ACCESS] GetFundPerformance: Get a fund's performance measures over all its partners.

The fund's PIC, DPI, RVPI, TVPI and net IRR built from the capital activity of every partner on the  register, open or closed, with the same optional with- and without-facility views as the partner read.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    nav_type_code = 'nav_type_code_example' # str | The NAV type to read the register and ledger under. Defaults to the fund's primary NAV type. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_fund_performance(scope, code, nav_type_code=nav_type_code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetFundPerformance: [EARLY ACCESS] GetFundPerformance: Get a fund's performance measures over all its partners.
        api_response = api_instance.get_fund_performance(scope, code, nav_type_code=nav_type_code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_fund_performance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **nav_type_code** | **str**| The NAV type to read the register and ledger under. Defaults to the fund&#39;s primary NAV type. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**PartnerPerformance**](PartnerPerformance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fund&#39;s performance measures over all its partners. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_fund_properties**
> FundProperties get_fund_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetFundProperties: Get Fund properties.

Get all the properties of a single fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund to list the properties for.
    code = 'code_example' # str | The code of the Fund to list the properties for. Together with the scope this uniquely identifies the Fund.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the Fund's properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Fund's properties. Defaults to return the latest version of each property if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_fund_properties(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetFundProperties: Get Fund properties.
        api_response = api_instance.get_fund_properties(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_fund_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund to list the properties for. | 
 **code** | **str**| The code of the Fund to list the properties for. Together with the scope this uniquely identifies the Fund. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Fund&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fund&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**FundProperties**](FundProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_holding_contributors_for_fund**
> VersionedResourceListOfHoldingContributor get_holding_contributors_for_fund(scope, code, holding_id, valuation_point_data_query_parameters, nav_type_code=nav_type_code, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page)

[EARLY ACCESS] GetHoldingContributorsForFund: Get holdings contributors for transaction portfolios in a Fund.

Get the holdings of transaction portfolios in a specified Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    holding_id = 56 # int | The unique holding identifier

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    include_historic = False # bool | If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. (optional) (default to False)
    tax_lot_id = 'tax_lot_id_example' # str | Constrains the Holding Contributors to those which contributed to the specified tax lot. (optional)
    include_unsettled_movements = False # bool | If true, contributing transaction which have not settled yet will also be returned. False by default (optional) (default to False)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_holding_contributors_for_fund(scope, code, holding_id, valuation_point_data_query_parameters, nav_type_code=nav_type_code, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page, opts=opts)

        # [EARLY ACCESS] GetHoldingContributorsForFund: Get holdings contributors for transaction portfolios in a Fund.
        api_response = api_instance.get_holding_contributors_for_fund(scope, code, holding_id, valuation_point_data_query_parameters, nav_type_code=nav_type_code, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_holding_contributors_for_fund: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **holding_id** | **int**| The unique holding identifier | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the holdings.This can be a date, valuationPoint or a bookmark. | 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **include_historic** | **bool**| If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. | [optional] [default to False]
 **tax_lot_id** | **str**| Constrains the Holding Contributors to those which contributed to the specified tax lot. | [optional] 
 **include_unsettled_movements** | **bool**| If true, contributing transaction which have not settled yet will also be returned. False by default | [optional] [default to False]
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. | [optional] 

### Return type

[**VersionedResourceListOfHoldingContributor**](VersionedResourceListOfHoldingContributor.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested holding contributors from the specified Fund and NavType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_holdings_for_fund**
> VersionedResourceListOfPortfolioHolding get_holdings_for_fund(scope, code, single_valuation_point_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)

[EARLY ACCESS] GetHoldingsForFund: Get holdings for transaction portfolios in a Fund.

Get the holdings of transaction portfolios in a specified Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # single_valuation_point_query_parameters = SingleValuationPointQueryParameters.from_json("")
    # single_valuation_point_query_parameters = SingleValuationPointQueryParameters.from_dict({})
    single_valuation_point_query_parameters = SingleValuationPointQueryParameters()
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of transaction portfolios in the Fund. Defaults              to return the latest version of the holdings if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\", \"Holding\" or \"Portfolio\",\"CustodianAccount\" or \"LegalEntity\" domain to decorate onto domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)
    by_taxlots = True # bool | Whether to expand the holdings to return the underlying tax-lots. Defaults to False. (optional)
    include_settlement_events_after_days = 56 # int | Number of days ahead to bring back settlements from, in relation to the specified effectiveAt. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_holdings_for_fund(scope, code, single_valuation_point_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days, opts=opts)

        # [EARLY ACCESS] GetHoldingsForFund: Get holdings for transaction portfolios in a Fund.
        api_response = api_instance.get_holdings_for_fund(scope, code, single_valuation_point_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_holdings_for_fund: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **single_valuation_point_query_parameters** | [**SingleValuationPointQueryParameters**](SingleValuationPointQueryParameters.md)| The arguments to use for querying the holdings. | 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of transaction portfolios in the Fund. Defaults              to return the latest version of the holdings if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot; or \&quot;Portfolio\&quot;,\&quot;CustodianAccount\&quot; or \&quot;LegalEntity\&quot; domain to decorate onto domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **by_taxlots** | **bool**| Whether to expand the holdings to return the underlying tax-lots. Defaults to False. | [optional] 
 **include_settlement_events_after_days** | **int**| Number of days ahead to bring back settlements from, in relation to the specified effectiveAt. | [optional] 

### Return type

[**VersionedResourceListOfPortfolioHolding**](VersionedResourceListOfPortfolioHolding.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings of transaction portfolios for a Fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_partner_capital_account**
> PartnerCapitalAccount get_partner_capital_account(scope, code, ir_scope, ir_code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at)

[EARLY ACCESS] GetPartnerCapitalAccount: [EARLY ACCESS] GetPartnerCapitalAccount: Get a partner's capital account statement.

One partner's capital account over a period, rolled from beginning capital through contributions,  distributions, transfers, allocated income, fees, gains and carried interest to ending capital, with  quarter-, year- and inception-to-date columns. The memo block carries the commitment position. The  statement is an estimate until a final valuation point covers the period end.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    ir_scope = 'ir_scope_example' # str | The scope of the partner's investor record.
    ir_code = 'ir_code_example' # str | The code of the partner's investor record.
    period_start = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime the statement period opens at. Defaults to the start of the quarter containing the period end. (optional)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime the statement period closes at. Defaults to the current LUSID system datetime. (optional)
    nav_type_code = 'nav_type_code_example' # str | The NAV type to read the register and ledger under. Defaults to the fund's primary NAV type. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_partner_capital_account(scope, code, ir_scope, ir_code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetPartnerCapitalAccount: [EARLY ACCESS] GetPartnerCapitalAccount: Get a partner's capital account statement.
        api_response = api_instance.get_partner_capital_account(scope, code, ir_scope, ir_code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_partner_capital_account: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **ir_scope** | **str**| The scope of the partner&#39;s investor record. | 
 **ir_code** | **str**| The code of the partner&#39;s investor record. | 
 **period_start** | **datetime**| The effective datetime the statement period opens at. Defaults to the start of the quarter containing the period end. | [optional] 
 **period_end** | **datetime**| The effective datetime the statement period closes at. Defaults to the current LUSID system datetime. | [optional] 
 **nav_type_code** | **str**| The NAV type to read the register and ledger under. Defaults to the fund&#39;s primary NAV type. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**PartnerCapitalAccount**](PartnerCapitalAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partner&#39;s capital account statement over the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_partner_performance**
> PartnerPerformance get_partner_performance(scope, code, ir_scope, ir_code, nav_type_code=nav_type_code, as_at=as_at)

[EARLY ACCESS] GetPartnerPerformance: [EARLY ACCESS] GetPartnerPerformance: Get a partner's performance measures.

One partner's paid-in to committed (PIC), distributions to paid-in (DPI), residual value to paid-in (RVPI),  total value to paid-in (TVPI) and net IRR, together with the dated cash flows the IRR was solved from.  Where any of the partner's events were financed by a subscription facility, the measures are also given  with and without the facility, the latter re-dating facility-funded calls to the deal funding date.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    ir_scope = 'ir_scope_example' # str | The scope of the partner's investor record.
    ir_code = 'ir_code_example' # str | The code of the partner's investor record.
    nav_type_code = 'nav_type_code_example' # str | The NAV type to read the register and ledger under. Defaults to the fund's primary NAV type. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_partner_performance(scope, code, ir_scope, ir_code, nav_type_code=nav_type_code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetPartnerPerformance: [EARLY ACCESS] GetPartnerPerformance: Get a partner's performance measures.
        api_response = api_instance.get_partner_performance(scope, code, ir_scope, ir_code, nav_type_code=nav_type_code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_partner_performance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **ir_scope** | **str**| The scope of the partner&#39;s investor record. | 
 **ir_code** | **str**| The code of the partner&#39;s investor record. | 
 **nav_type_code** | **str**| The NAV type to read the register and ledger under. Defaults to the fund&#39;s primary NAV type. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**PartnerPerformance**](PartnerPerformance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partner&#39;s performance measures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_partner_unfunded_reconciliation**
> FundPartnerUnfundedReconciliation get_partner_unfunded_reconciliation(scope, code, investor_record_id, var_from, to=to, as_at=as_at)

[EARLY ACCESS] GetPartnerUnfundedReconciliation: [EARLY ACCESS] GetPartnerUnfundedReconciliation: Get a partner's unfunded commitment statement.

Reconciles one partner's unfunded commitment over a period: the register's opening unfunded, less capital  called inside the commitment, plus recallable distributions, less recallable distributions that expired,  plus or minus commitment changes and transfers, gives the closing unfunded, which is checked against the  register's unfunded at the close. Every booked allocation to the partner in the period is listed with the  ILPA transaction type it is reported under.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    investor_record_id = 'investor_record_id_example' # str | The investor record of the partner.
    var_from = 'var_from_example' # str | The effective datetime or cut label the statement opens at.
    to = 'to_example' # str | The effective datetime or cut label the statement closes at. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the register and the booked events. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_partner_unfunded_reconciliation(scope, code, investor_record_id, var_from, to=to, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetPartnerUnfundedReconciliation: [EARLY ACCESS] GetPartnerUnfundedReconciliation: Get a partner's unfunded commitment statement.
        api_response = api_instance.get_partner_unfunded_reconciliation(scope, code, investor_record_id, var_from, to=to, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_partner_unfunded_reconciliation: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **investor_record_id** | **str**| The investor record of the partner. | 
 **var_from** | **str**| The effective datetime or cut label the statement opens at. | 
 **to** | **str**| The effective datetime or cut label the statement closes at. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the register and the booked events. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**FundPartnerUnfundedReconciliation**](FundPartnerUnfundedReconciliation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partner&#39;s unfunded commitment statement over the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_partners**
> PagedResourceListOfFundPartner get_partners(scope, code, effective_at=effective_at, as_at=as_at, include_closed=include_closed, page=page, limit=limit)

[EARLY ACCESS] GetPartners: [EARLY ACCESS] GetPartners: Get the partners of a partnership fund.

Lists the register lines of a partnership-accounting fund with each partner's capital balances at the  requested effective date, together with totals across the whole register. Committed capital is totalled per  commitment currency, and each line's share of commitments is of the total in its own currency; amounts in  different currencies are never added together.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to read the register. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the register. Defaults to returning the latest version if not specified. (optional)
    include_closed = True # bool | Whether to include register lines with no remaining commitment or funded capital. Defaults to false. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing partners; this value is returned from the previous call.              If a pagination token is provided, the effectiveAt and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_partners(scope, code, effective_at=effective_at, as_at=as_at, include_closed=include_closed, page=page, limit=limit, opts=opts)

        # [EARLY ACCESS] GetPartners: [EARLY ACCESS] GetPartners: Get the partners of a partnership fund.
        api_response = api_instance.get_partners(scope, code, effective_at=effective_at, as_at=as_at, include_closed=include_closed, page=page, limit=limit)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_partners: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **effective_at** | **str**| The effective datetime or cut label at which to read the register. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the register. Defaults to returning the latest version if not specified. | [optional] 
 **include_closed** | **bool**| Whether to include register lines with no remaining commitment or funded capital. Defaults to false. | [optional] 
 **page** | **str**| The pagination token to use to continue listing partners; this value is returned from the previous call.              If a pagination token is provided, the effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 

### Return type

[**PagedResourceListOfFundPartner**](PagedResourceListOfFundPartner.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partners of the requested Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_partnership_config_pack**
> PartnershipConfigPack get_partnership_config_pack(scope, code, as_at=as_at)

[EARLY ACCESS] GetPartnershipConfigPack: [EXPERIMENTAL] GetPartnershipConfigPack: Get the partnership configuration pack of a Fund.

Resolve the partnership configuration pack the Fund's configuration names: the partnership transaction types,  the accounts partner capital is posted to and the rules that move each type between them.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the pack. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_partnership_config_pack(scope, code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetPartnershipConfigPack: [EXPERIMENTAL] GetPartnershipConfigPack: Get the partnership configuration pack of a Fund.
        api_response = api_instance.get_partnership_config_pack(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_partnership_config_pack: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the pack. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**PartnershipConfigPack**](PartnershipConfigPack.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partnership configuration pack the Fund runs on. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_series**
> ResourceListOfSeries get_series(scope, code, share_class_code=share_class_code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetSeries: [EARLY ACCESS] GetSeries: List the Series of a Fund.

Lists the Series defined on the Share Classes of the Fund, optionally restricted to a single Share Class.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    share_class_code = 'share_class_code_example' # str | Optionally, the short code of the Share Class whose Series to list. Defaults to all Share Classes. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to read the Fund. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the Fund. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_series(scope, code, share_class_code=share_class_code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetSeries: [EARLY ACCESS] GetSeries: List the Series of a Fund.
        api_response = api_instance.get_series(scope, code, share_class_code=share_class_code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_series: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **share_class_code** | **str**| Optionally, the short code of the Share Class whose Series to list. Defaults to all Share Classes. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to read the Fund. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfSeries**](ResourceListOfSeries.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Series of the requested Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation_for_fund**
> ListAggregationResponse get_valuation_for_fund(scope, code, nav_type_code=nav_type_code, fund_valuation_request=fund_valuation_request)

[EARLY ACCESS] GetValuationForFund: Perform valuation for a Fund.

Perform valuation on a specified Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # fund_valuation_request = FundValuationRequest.from_json("")
    # fund_valuation_request = FundValuationRequest.from_dict({})
    fund_valuation_request = FundValuationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_valuation_for_fund(scope, code, nav_type_code=nav_type_code, fund_valuation_request=fund_valuation_request, opts=opts)

        # [EARLY ACCESS] GetValuationForFund: Perform valuation for a Fund.
        api_response = api_instance.get_valuation_for_fund(scope, code, nav_type_code=nav_type_code, fund_valuation_request=fund_valuation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_valuation_for_fund: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **fund_valuation_request** | [**FundValuationRequest**](FundValuationRequest.md)| The request specifying the dates (or DiaryEntry) on which to calculate a set of valuation metrics. | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

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

# **get_valuation_point_data**
> ValuationPointDataResponse get_valuation_point_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, nav_type_code=nav_type_code)

[EARLY ACCESS] GetValuationPointData: Get Valuation Point Data for a Fund.

Retrieves the Valuation Point data between given dates or Valuation Point codes.  The endpoint will internally extract all 'Assets' and 'Liabilities' from the Fund's Trial balance to produce a GAV.  Start date will be assumed from the last 'official' ValuationPoint and EndDate will be as provided.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_valuation_point_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] GetValuationPointData: Get Valuation Point Data for a Fund.
        api_response = api_instance.get_valuation_point_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_valuation_point_data: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the Valuation Point data. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointDataResponse**](ValuationPointDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Valuation Point data for the Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation_point_journal_entry_lines**
> ValuationPointResourceListOfFundJournalEntryLine get_valuation_point_journal_entry_lines(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, bucket_set_code=bucket_set_code)

[EARLY ACCESS] GetValuationPointJournalEntryLines: Get the Journal Entry Lines for the given Fund.

Gets the Journal Entry Lines for the given Valuation Point for a Fund.                The Journal Entry Lines have been generated from transactions, translated via posting rules and used in the valuation point.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    general_ledger_profile_code = 'general_ledger_profile_code_example' # str | The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve Journal Entry Lines. Defaults to returning the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Journal Entry Lines from a previous call to GetValuationPointJournalEntryLines. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument', 'Transaction', 'Portfolio', 'Account', 'LegalEntity' or 'CustodianAccount'               domain to decorate onto the Journal Entry Lines. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    bucket_set_code = 'bucket_set_code_example' # str | When provided, each line's bucketMemberships report only this bucket set's classification of it.               Otherwise, every bucket set covering the NAV Type is reported. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_valuation_point_journal_entry_lines(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, bucket_set_code=bucket_set_code, opts=opts)

        # [EARLY ACCESS] GetValuationPointJournalEntryLines: Get the Journal Entry Lines for the given Fund.
        api_response = api_instance.get_valuation_point_journal_entry_lines(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, bucket_set_code=bucket_set_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_valuation_point_journal_entry_lines: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the Journal Entry Lines. | 
 **general_ledger_profile_code** | **str**| The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve Journal Entry Lines. Defaults to returning the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Journal Entry Lines from a previous call to GetValuationPointJournalEntryLines. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;               domain to decorate onto the Journal Entry Lines. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **bucket_set_code** | **str**| When provided, each line&#39;s bucketMemberships report only this bucket set&#39;s classification of it.               Otherwise, every bucket set covering the NAV Type is reported. | [optional] 

### Return type

[**ValuationPointResourceListOfFundJournalEntryLine**](ValuationPointResourceListOfFundJournalEntryLine.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Journal Entry Lines for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation_point_pnl_summary**
> ValuationPointResourceListOfPnlJournalEntryLine get_valuation_point_pnl_summary(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, nav_type_code=nav_type_code)

[EARLY ACCESS] GetValuationPointPnlSummary: Get a PnL summary for the given Valuation Point in the Fund.

Gets the PnL Summary lines from the Journal Entry Lines produced when calculating the Valuation Point.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    general_ledger_profile_code = 'general_ledger_profile_code_example' # str | The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve PnL summary. Defaults to returning the latest version              of each transaction if not specified. (optional)
    filter = 'filter_example' # str | \"Expression to filter the result set.\" (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing results from a previous call to GetValuationPointPnlSummary. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_valuation_point_pnl_summary(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] GetValuationPointPnlSummary: Get a PnL summary for the given Valuation Point in the Fund.
        api_response = api_instance.get_valuation_point_pnl_summary(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_valuation_point_pnl_summary: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for generating the PnL summary. | 
 **general_ledger_profile_code** | **str**| The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve PnL summary. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| \&quot;Expression to filter the result set.\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing results from a previous call to GetValuationPointPnlSummary. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointResourceListOfPnlJournalEntryLine**](ValuationPointResourceListOfPnlJournalEntryLine.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested PnL summary for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation_point_quotes**
> ValuationPointResourceListOfAccountedQuote get_valuation_point_quotes(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code)

[EARLY ACCESS] GetValuationPointQuotes: Get the Quotes for the given Fund and Valuation Point.

Gets all quotes within the effective date range of the specified Valuation Point for a Fund,  including any quotes added via a Complex Close (Post-Close Activity).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve quotes. Defaults to returning the latest version              of each quote if not specified. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing quotes from a previous call to GetValuationPointQuotes. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_valuation_point_quotes(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] GetValuationPointQuotes: Get the Quotes for the given Fund and Valuation Point.
        api_response = api_instance.get_valuation_point_quotes(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_valuation_point_quotes: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the quotes. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve quotes. Defaults to returning the latest version              of each quote if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing quotes from a previous call to GetValuationPointQuotes. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointResourceListOfAccountedQuote**](ValuationPointResourceListOfAccountedQuote.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested quotes for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation_point_transactions**
> ValuationPointResourceListOfAccountedTransaction get_valuation_point_transactions(scope, code, valuation_point_data_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, data_model_scope=data_model_scope, data_model_code=data_model_code, show_cancelled_transactions=show_cancelled_transactions, membership_type=membership_type, return_excluded_transactions=return_excluded_transactions)

[EARLY ACCESS] GetValuationPointTransactions: Get the Transactions for the given Fund.

Gets the Transactions for the given Valuation Point for a Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve transactions. Defaults to returning the latest version              of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to GetValuationPointTransactions. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument', 'Transaction', 'Portfolio', 'Account', 'LegalEntity' or 'CustodianAccount'              domain to decorate onto the transactions. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    data_model_scope = 'data_model_scope_example' # str | The optional scope of a Custom Data Model to use (optional)
    data_model_code = 'data_model_code_example' # str | The optional code of a Custom Data Model to use (optional)
    show_cancelled_transactions = True # bool | Option to specify whether or not to include cancelled transactions,              including previous versions of transactions which have since been amended.              Defaults to False if not specified. (optional)
    membership_type = 'membership_type_example' # str | The membership types of the specified Custom Data Model to return. Default value: Member. Available values: All, Member, Candidate. (optional)
    return_excluded_transactions = True # bool | Option to specify whether or not to include transactions excluded by the              NavType's TransactionExclusionFilter. Defaults to False if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_valuation_point_transactions(scope, code, valuation_point_data_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, data_model_scope=data_model_scope, data_model_code=data_model_code, show_cancelled_transactions=show_cancelled_transactions, membership_type=membership_type, return_excluded_transactions=return_excluded_transactions, opts=opts)

        # [EARLY ACCESS] GetValuationPointTransactions: Get the Transactions for the given Fund.
        api_response = api_instance.get_valuation_point_transactions(scope, code, valuation_point_data_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, data_model_scope=data_model_scope, data_model_code=data_model_code, show_cancelled_transactions=show_cancelled_transactions, membership_type=membership_type, return_excluded_transactions=return_excluded_transactions)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_valuation_point_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the transactions. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve transactions. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetValuationPointTransactions. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;              domain to decorate onto the transactions. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 
 **show_cancelled_transactions** | **bool**| Option to specify whether or not to include cancelled transactions,              including previous versions of transactions which have since been amended.              Defaults to False if not specified. | [optional] 
 **membership_type** | **str**| The membership types of the specified Custom Data Model to return. Default value: Member. Available values: All, Member, Candidate. | [optional] 
 **return_excluded_transactions** | **bool**| Option to specify whether or not to include transactions excluded by the              NavType&#39;s TransactionExclusionFilter. Defaults to False if not specified. | [optional] 

### Return type

[**ValuationPointResourceListOfAccountedTransaction**](ValuationPointResourceListOfAccountedTransaction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation_point_trial_balance**
> ValuationPointResourceListOfTrialBalance get_valuation_point_trial_balance(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, exclude_cleardown_module=exclude_cleardown_module)

[EARLY ACCESS] GetValuationPointTrialBalance: Get Trial Balance for the given Fund.

Gets the Trial Balance for the given Valuation Point for a Fund.                The Trial Balance has been generated from transactions, translated via Posting Rules  and aggregated based on a General Ledger Profile (where specified).                Supplying the X-LUSID-SuppressImbalanceValidation header suppresses the imbalance check.  Any caller with access to this endpoint may use it; it is not role-restricted.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    general_ledger_profile_code = 'general_ledger_profile_code_example' # str | The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Trial Balance.               Defaults to returning the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results by.               For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this number.               Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Trial Balances.               This token is returned from the previous call.               If a pagination token is provided, the filter, effectiveAt and asAt fields               must not have changed since the original request. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument', 'Transaction', 'Portfolio', 'Account', 'LegalEntity' or 'CustodianAccount'               domain to decorate onto the TrialBalance. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    exclude_cleardown_module = False # bool | If this is set to true, no Cleardown Module will be applied to the Trial Balance. Defaults to false. (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_valuation_point_trial_balance(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, exclude_cleardown_module=exclude_cleardown_module, opts=opts)

        # [EARLY ACCESS] GetValuationPointTrialBalance: Get Trial Balance for the given Fund.
        api_response = api_instance.get_valuation_point_trial_balance(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, exclude_cleardown_module=exclude_cleardown_module)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_valuation_point_trial_balance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for generating the Trial Balance. | 
 **general_ledger_profile_code** | **str**| The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Trial Balance.               Defaults to returning the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results by.               For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this number.               Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Trial Balances.               This token is returned from the previous call.               If a pagination token is provided, the filter, effectiveAt and asAt fields               must not have changed since the original request. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;               domain to decorate onto the TrialBalance. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **exclude_cleardown_module** | **bool**| If this is set to true, no Cleardown Module will be applied to the Trial Balance. Defaults to false. | [optional] [default to False]

### Return type

[**ValuationPointResourceListOfTrialBalance**](ValuationPointResourceListOfTrialBalance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Trial Balance for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation_point_unsettled_transactions**
> ValuationPointResourceListOfUnsettledTransaction get_valuation_point_unsettled_transactions(scope, code, single_valuation_point_query_parameters, as_at=as_at, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, filter=filter)

[EARLY ACCESS] GetValuationPointUnsettledTransactions: Get Unsettled Transactions for the given Fund.

Gets all transactions that remain unsettled as at the specified Valuation Point for a Fund,  looking back from inception. Settlement status is point-in-time: post-cutoff settlement  activity does not alter the result.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # single_valuation_point_query_parameters = SingleValuationPointQueryParameters.from_json("")
    # single_valuation_point_query_parameters = SingleValuationPointQueryParameters.from_dict({})
    single_valuation_point_query_parameters = SingleValuationPointQueryParameters()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the report. Defaults to latest. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing from a previous call. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument', 'Transaction', 'Portfolio', or 'Account'              domain to decorate onto the transactions. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_valuation_point_unsettled_transactions(scope, code, single_valuation_point_query_parameters, as_at=as_at, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, filter=filter, opts=opts)

        # [EARLY ACCESS] GetValuationPointUnsettledTransactions: Get Unsettled Transactions for the given Fund.
        api_response = api_instance.get_valuation_point_unsettled_transactions(scope, code, single_valuation_point_query_parameters, as_at=as_at, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->get_valuation_point_unsettled_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **single_valuation_point_query_parameters** | [**SingleValuationPointQueryParameters**](SingleValuationPointQueryParameters.md)| The arguments to use for querying the unsettled transactions. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the report. Defaults to latest. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing from a previous call. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, or &#39;Account&#39;              domain to decorate onto the transactions. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ValuationPointResourceListOfUnsettledTransaction**](ValuationPointResourceListOfUnsettledTransaction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The unsettled transactions for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_facilities**
> PagedResourceListOfFacility list_facilities(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListFacilities: [EXPERIMENTAL] ListFacilities: List Facilities for a specified Fund.

List all the Facilities matching a particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the Facilities. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Facilities. Defaults to returning the latest version of each Facility if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing facilities; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the lender, specify \"lender eq 'Bank'\". For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_facilities(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListFacilities: [EXPERIMENTAL] ListFacilities: List Facilities for a specified Fund.
        api_response = api_instance.list_facilities(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_facilities: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Facilities. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Facilities. Defaults to returning the latest version of each Facility if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing facilities; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the lender, specify \&quot;lender eq &#39;Bank&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfFacility**](PagedResourceListOfFacility.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Facilities. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_fees**
> PagedResourceListOfFee list_fees(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EARLY ACCESS] ListFees: List Fees for a specified Fund.

List all the Fees matching a particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the Fees. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Fees. Defaults to returning the latest version of each Fee if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing fees; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the treatment, specify \"treatment eq 'Monthly'\". For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Fee' domain to decorate onto each Fee.              These must take the format {domain}/{scope}/{code}, for example 'Fee/Account/Id'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_fees(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] ListFees: List Fees for a specified Fund.
        api_response = api_instance.list_fees(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_fees: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Fees. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fees. Defaults to returning the latest version of each Fee if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing fees; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the treatment, specify \&quot;treatment eq &#39;Monthly&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fee&#39; domain to decorate onto each Fee.              These must take the format {domain}/{scope}/{code}, for example &#39;Fee/Account/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFee**](PagedResourceListOfFee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fees. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_fund_calendar**
> PagedResourceListOfFundCalendarEntry list_fund_calendar(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EARLY ACCESS] ListFundCalendar: List Fund Calendar.

List all the Calendar Entries associated with the Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Calendar. Defaults to returning the latest version of each Calendar Entry if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Calendar Entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'ClosedPeriod' domain to decorate onto each item. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_fund_calendar(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] ListFundCalendar: List Fund Calendar.
        api_response = api_instance.list_fund_calendar(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_fund_calendar: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **as_at** | **datetime**| The asAt datetime at which to list the Calendar. Defaults to returning the latest version of each Calendar Entry if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Calendar Entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;ClosedPeriod&#39; domain to decorate onto each item. | [optional] 

### Return type

[**PagedResourceListOfFundCalendarEntry**](PagedResourceListOfFundCalendarEntry.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund Calendar Entries. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_fund_calendar_entries**
> PagedResourceListOfFundCalendarEntries list_fund_calendar_entries(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EARLY ACCESS] ListFundCalendarEntries: List Fund Calendar Entries.

List all the Calendar Entries associated with the Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Calendar. Defaults to returning the latest version of each Calendar Entry if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Calendar Entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'DiaryEntry' domain to decorate onto each item. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_fund_calendar_entries(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] ListFundCalendarEntries: List Fund Calendar Entries.
        api_response = api_instance.list_fund_calendar_entries(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_fund_calendar_entries: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **as_at** | **datetime**| The asAt datetime at which to list the Calendar. Defaults to returning the latest version of each Calendar Entry if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Calendar Entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;DiaryEntry&#39; domain to decorate onto each item. | [optional] 

### Return type

[**PagedResourceListOfFundCalendarEntries**](PagedResourceListOfFundCalendarEntries.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund Calendar Entries. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_funds**
> PagedResourceListOfFund list_funds(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EARLY ACCESS] ListFunds: List Funds.

List all the Funds matching particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the Funds. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Funds. Defaults to returning the latest version of each Fund if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Funds; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Fund code, specify \"id.Code eq 'Fund1'\". For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Fund' domain to decorate onto each Fund.              These must take the format {domain}/{scope}/{code}, for example 'Fund/Manager/Id'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_funds(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] ListFunds: List Funds.
        api_response = api_instance.list_funds(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_funds: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Funds. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Funds. Defaults to returning the latest version of each Fund if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Funds; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Fund code, specify \&quot;id.Code eq &#39;Fund1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fund&#39; domain to decorate onto each Fund.              These must take the format {domain}/{scope}/{code}, for example &#39;Fund/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFund**](PagedResourceListOfFund.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Funds. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_nav_activity_adjustments**
> ResourceListOfNavActivityAdjustmentResponse list_nav_activity_adjustments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, valuation_point_code_variant=valuation_point_code_variant)

[EARLY ACCESS] ListNavActivityAdjustments: List NAV adjustment activities applied to a valuation point

Lists the NAV adjustment activities applied to the specified valuation point for a Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope is the unique identifier for the given Fund.
    valuation_point_code = 'valuation_point_code_example' # str | Fetch all NAV adjustment activities for this valuation point.
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Nav activity adjustments. Defaults to returning the latest version of each adjustment if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Nav activity adjustments; this              value is returned from the previous call. If a pagination token is provided, the filter,              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    valuation_point_code_variant = 'valuation_point_code_variant_example' # str | The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_nav_activity_adjustments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, valuation_point_code_variant=valuation_point_code_variant, opts=opts)

        # [EARLY ACCESS] ListNavActivityAdjustments: List NAV adjustment activities applied to a valuation point
        api_response = api_instance.list_nav_activity_adjustments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, valuation_point_code_variant=valuation_point_code_variant)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_nav_activity_adjustments: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | 
 **valuation_point_code** | **str**| Fetch all NAV adjustment activities for this valuation point. | 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Nav activity adjustments. Defaults to returning the latest version of each adjustment if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Nav activity adjustments; this              value is returned from the previous call. If a pagination token is provided, the filter,              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

[**ResourceListOfNavActivityAdjustmentResponse**](ResourceListOfNavActivityAdjustmentResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested NAV activity adjustments for the specific valuation point and Nav type for the Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_partner_capital_accounts**
> PagedResourceListOfPartnerCapitalAccount list_partner_capital_accounts(scope, code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit)

[EARLY ACCESS] ListPartnerCapitalAccounts: [EARLY ACCESS] ListPartnerCapitalAccounts: List the capital account statements of a fund's partners.

The capital account statement of every open partner on the fund's register over a period, paged in  register order.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    period_start = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime the statement period opens at. Defaults to the start of the quarter containing the period end. (optional)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime the statement period closes at. Defaults to the current LUSID system datetime. (optional)
    nav_type_code = 'nav_type_code_example' # str | The NAV type to read the register and ledger under. Defaults to the fund's primary NAV type. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing statements from a previous call. This value is returned from the previous call. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_partner_capital_accounts(scope, code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, opts=opts)

        # [EARLY ACCESS] ListPartnerCapitalAccounts: [EARLY ACCESS] ListPartnerCapitalAccounts: List the capital account statements of a fund's partners.
        api_response = api_instance.list_partner_capital_accounts(scope, code, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_partner_capital_accounts: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **period_start** | **datetime**| The effective datetime the statement period opens at. Defaults to the start of the quarter containing the period end. | [optional] 
 **period_end** | **datetime**| The effective datetime the statement period closes at. Defaults to the current LUSID system datetime. | [optional] 
 **nav_type_code** | **str**| The NAV type to read the register and ledger under. Defaults to the fund&#39;s primary NAV type. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the fund. Defaults to returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing statements from a previous call. This value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 

### Return type

[**PagedResourceListOfPartnerCapitalAccount**](PagedResourceListOfPartnerCapitalAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The capital account statements of the fund&#39;s partners over the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_partner_statements**
> ResourceListOfPartnerStatement list_partner_statements(scope, code, investor_record_id)

[EARLY ACCESS] ListPartnerStatements: [EXPERIMENTAL] ListPartnerStatements: List the statements produced for a partner.

List every statement produced for the partner on this Fund, most recent first.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    investor_record_id = 'investor_record_id_example' # str | The investor record the statements are for.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_partner_statements(scope, code, investor_record_id, opts=opts)

        # [EARLY ACCESS] ListPartnerStatements: [EXPERIMENTAL] ListPartnerStatements: List the statements produced for a partner.
        api_response = api_instance.list_partner_statements(scope, code, investor_record_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_partner_statements: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **investor_record_id** | **str**| The investor record the statements are for. | 

### Return type

[**ResourceListOfPartnerStatement**](ResourceListOfPartnerStatement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The statements produced for the partner. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_valuation_point_complex_market_data**
> ValuationPointResourceListOfAccountedComplexMarketData list_valuation_point_complex_market_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code)

[EARLY ACCESS] ListValuationPointComplexMarketData: List the Complex Market Data for the given Fund and Valuation Point.

Lists all complex market data within the effective date range of the specified Valuation Point for a Fund,  including any items added via a Complex Close (Post-Close Activity).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_json("")
    # valuation_point_data_query_parameters = ValuationPointDataQueryParameters.from_dict({})
    valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve complex market data. Defaults to returning the latest version              of each item if not specified. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing complex market data from a previous call to ListValuationPointComplexMarketData. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_valuation_point_complex_market_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] ListValuationPointComplexMarketData: List the Complex Market Data for the given Fund and Valuation Point.
        api_response = api_instance.list_valuation_point_complex_market_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, limit=limit, page=page, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_valuation_point_complex_market_data: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the complex market data. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve complex market data. Defaults to returning the latest version              of each item if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing complex market data from a previous call to ListValuationPointComplexMarketData. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointResourceListOfAccountedComplexMarketData**](ValuationPointResourceListOfAccountedComplexMarketData.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested complex market data for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_valuation_point_instruments**
> PagedResourceListOfValuationPointInstrument list_valuation_point_instruments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, instrument_property_keys=instrument_property_keys, valuation_point_code_variant=valuation_point_code_variant)

[EARLY ACCESS] ListValuationPointInstruments: List Instruments inside a valuation point

Lists the Instruments linked to Transactions within a Valuation Point for a Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope is the unique identifier for the given Fund.
    valuation_point_code = 'valuation_point_code_example' # str | Fetch all instruments for this valuation point.
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the instruments. Defaults to returning the latest version of each instrument if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing instruments; this              value is returned from the previous call. If a pagination token is provided, the filter,              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    instrument_property_keys = ['instrument_property_keys_example'] # List[str] | A list of property keys from the 'Instrument' domain to decorate onto              instruments, or from any domain that supports relationships to decorate onto related entities.              These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'. (optional)
    valuation_point_code_variant = 'valuation_point_code_variant_example' # str | The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_valuation_point_instruments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, instrument_property_keys=instrument_property_keys, valuation_point_code_variant=valuation_point_code_variant, opts=opts)

        # [EARLY ACCESS] ListValuationPointInstruments: List Instruments inside a valuation point
        api_response = api_instance.list_valuation_point_instruments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, instrument_property_keys=instrument_property_keys, valuation_point_code_variant=valuation_point_code_variant)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_valuation_point_instruments: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | 
 **valuation_point_code** | **str**| Fetch all instruments for this valuation point. | 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the instruments. Defaults to returning the latest version of each instrument if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing instruments; this              value is returned from the previous call. If a pagination token is provided, the filter,              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **instrument_property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39; domain to decorate onto              instruments, or from any domain that supports relationships to decorate onto related entities.              These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39;. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

[**PagedResourceListOfValuationPointInstrument**](PagedResourceListOfValuationPointInstrument.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The instruments held at the specified valuation point for the Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_valuation_point_overview**
> PagedResourceListOfValuationPointOverview list_valuation_point_overview(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, nav_type_code=nav_type_code)

[EARLY ACCESS] ListValuationPointOverview: List Valuation Points Overview for a given Fund.

List the overview of all the Valuation Points that match the given criteria for a given Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the Valuation Points. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Valuation Points. Defaults to returning the latest version of each Valuation Point if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Valuation Points; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results by.              For example, to filter on the NAV, specify \"NAV gt 300\". For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'DiaryEntry' domain to decorate onto each ValuationPoint.              These must take the format {domain}/{scope}/{code}, for example 'DiaryEntry/ValuationPoint/Id'. (optional)
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_valuation_point_overview(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] ListValuationPointOverview: List Valuation Points Overview for a given Fund.
        api_response = api_instance.list_valuation_point_overview(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->list_valuation_point_overview: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Valuation Points. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Valuation Points. Defaults to returning the latest version of each Valuation Point if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Valuation Points; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results by.              For example, to filter on the NAV, specify \&quot;NAV gt 300\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;DiaryEntry&#39; domain to decorate onto each ValuationPoint.              These must take the format {domain}/{scope}/{code}, for example &#39;DiaryEntry/ValuationPoint/Id&#39;. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**PagedResourceListOfValuationPointOverview**](PagedResourceListOfValuationPointOverview.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The overviews of the requested Valuation Points. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **patch_fee**
> Fee patch_fee(scope, code, fee_code, operation)

[EARLY ACCESS] PatchFee: Patch Fee.

Create or update certain fields for a particular Fee.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: EndDate, ShareClasses.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    fee_code = 'fee_code_example' # str | The code of the Fee.
    operation = [{"value":"2027-12-31T00:00:00.0000000+00:00","path":"/endDate","op":"add"}] # List[Operation] | The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.patch_fee(scope, code, fee_code, operation, opts=opts)

        # [EARLY ACCESS] PatchFee: Patch Fee.
        api_response = api_instance.patch_fee(scope, code, fee_code, operation)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->patch_fee: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_code** | **str**| The code of the Fee. | 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | 

### Return type

[**Fee**](Fee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched Fee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **patch_fund**
> Fund patch_fund(scope, code, operation, effective_at=effective_at)

[EARLY ACCESS] PatchFund: Patch a Fund.

Update fields on a Fund.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: DisplayName, Description, BaseCurrency, PortfolioIds, FundConfigurationId, ShareClassInstruments, Type, InceptionDate, DecimalPlaces, PrimaryNavType, AdditionalNavTypes, AborId, YearEndDate, PricingMethodology, ReportingPrices, WhtParameters, ShareClasses.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    operation = [{"value":"UpdatedFundName","path":"/displayName","op":"add"},{"path":"/description","op":"remove"},{"value":{"scope":"myFundConfigScope","code":"myFundConfigCode"},"path":"/fundConfigurationId","op":"add"},{"value":{"scope":"myAborScope","code":"myAborCode"},"path":"/aborId","op":"add"},{"value":["shareClassScope"],"path":"/shareClassInstrumentScopes","op":"add"},{"value":{"instrumentIdentifiers":{"Instrument/default/ClientInternal":"shareClass526"},"launchPrice":2.5,"launchDate":"2024-02-01T00:00:00.0000000+00:00"},"path":"/shareClassInstruments/-","op":"add"},{"value":"Standalone","path":"/type","op":"add"},{"value":"2024-01-01","path":"/inceptionDate","op":"add"},{"value":2,"path":"/decimalPlaces","op":"add"},{"value":{"day":24,"month":12},"path":"/yearEndDate","op":"add"}] # List[Operation] | The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label from which the patch applies. If not specified, the patch applies for all time.              Only DisplayName and Description can be patched with an effectiveAt, and the Fund is returned as at that datetime.              A value patched with an effectiveAt stays in force from that datetime. A later patch of the same field without an effectiveAt              changes it only before that datetime; to change it from that datetime, patch it again with the same effectiveAt. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.patch_fund(scope, code, operation, effective_at=effective_at, opts=opts)

        # [EARLY ACCESS] PatchFund: Patch a Fund.
        api_response = api_instance.patch_fund(scope, code, operation, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->patch_fund: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | 
 **effective_at** | **str**| The effective datetime or cut label from which the patch applies. If not specified, the patch applies for all time.              Only DisplayName and Description can be patched with an effectiveAt, and the Fund is returned as at that datetime.              A value patched with an effectiveAt stays in force from that datetime. A later patch of the same field without an effectiveAt              changes it only before that datetime; to change it from that datetime, patch it again with the same effectiveAt. | [optional] 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **produce_partner_statement**
> PartnerStatement produce_partner_statement(scope, code, investor_record_id, partner_statement_request, as_at=as_at)

[EARLY ACCESS] ProducePartnerStatement: [EXPERIMENTAL] ProducePartnerStatement: Produce a partner's capital statement for a period.

Produce the capital account statement of one partner for the period: opening capital, contributions,  distributions, allocated income, carry and fees, and closing capital. The statement is kept so later  statements for the same period can be compared against it.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    investor_record_id = 'investor_record_id_example' # str | The investor record the statement is for.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # partner_statement_request = PartnerStatementRequest.from_json("")
    # partner_statement_request = PartnerStatementRequest.from_dict({})
    partner_statement_request = PartnerStatementRequest()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.produce_partner_statement(scope, code, investor_record_id, partner_statement_request, as_at=as_at, opts=opts)

        # [EARLY ACCESS] ProducePartnerStatement: [EXPERIMENTAL] ProducePartnerStatement: Produce a partner's capital statement for a period.
        api_response = api_instance.produce_partner_statement(scope, code, investor_record_id, partner_statement_request, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->produce_partner_statement: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **investor_record_id** | **str**| The investor record the statement is for. | 
 **partner_statement_request** | [**PartnerStatementRequest**](PartnerStatementRequest.md)| The statement period. | 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**PartnerStatement**](PartnerStatement.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The partner&#39;s statement for the period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **query_cash_statement**
> ValuationPointResourceListOfFundCashStatementRow query_cash_statement(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)

[DEPRECATED] QueryCashStatement: [DEPRECATED] QueryCashStatement: Query cash statement for a Fund valuation point.

Deprecated: use QueryCashStatementLocalCurrency instead. Returns settled cash movements with  running balance, cost basis, average FX rate, and realised FX PnL for the specified Fund  valuation point period. The cash statement is derived from Journal Entry Lines filtered to  settled cash (HoldType='B', SourceType=LusidTransaction). Use the DisplayMode parameter on the  request body to choose between ShowReversal (full reversal/TrueUp detail) and Consolidated  (collapses reversals into AvgRateCorrection rows).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_fund_cash_statement_parameters = QueryFundCashStatementParameters.from_json("")
    # query_fund_cash_statement_parameters = QueryFundCashStatementParameters.from_dict({})
    query_fund_cash_statement_parameters = QueryFundCashStatementParameters()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the cash statement. Defaults to the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to get the next page of results. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys to decorate onto the cash statement rows. (optional)
    nav_type_code = 'nav_type_code_example' # str | The code of the NAV type to use. Defaults to the primary NAV type if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.query_cash_statement(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, opts=opts)

        # [DEPRECATED] QueryCashStatement: [DEPRECATED] QueryCashStatement: Query cash statement for a Fund valuation point.
        api_response = api_instance.query_cash_statement(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->query_cash_statement: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **query_fund_cash_statement_parameters** | [**QueryFundCashStatementParameters**](QueryFundCashStatementParameters.md)| The query parameters specifying the diary entry period and display mode. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the cash statement. Defaults to the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to get the next page of results. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys to decorate onto the cash statement rows. | [optional] 
 **nav_type_code** | **str**| The code of the NAV type to use. Defaults to the primary NAV type if not specified. | [optional] 

### Return type

[**ValuationPointResourceListOfFundCashStatementRow**](ValuationPointResourceListOfFundCashStatementRow.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cash statement for the specified Fund valuation point. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **query_cash_statement_local_currency**
> ValuationPointResourceListOfFundCashStatementLocalCurrency query_cash_statement_local_currency(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)

[EARLY ACCESS] QueryCashStatementLocalCurrency: [EXPERIMENTAL] QueryCashStatementLocalCurrency: Query the local-currency cash statement for a Fund valuation point.

Returns settled cash movements with a running balance in local currency for the specified Fund  valuation point period. The cash statement is derived from Journal Entry Lines filtered to  settled cash (HoldType='B', SourceType=LusidTransaction). Use the DisplayMode parameter on the  request body to choose between ShowReversal (full reversal/TrueUp detail) and Consolidated  (collapses system-generated zero-net reversal/TrueUp pairs into SystemCorrection rows). Base  currency columns are out of scope for this variant and are not returned.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_fund_cash_statement_parameters = QueryFundCashStatementParameters.from_json("")
    # query_fund_cash_statement_parameters = QueryFundCashStatementParameters.from_dict({})
    query_fund_cash_statement_parameters = QueryFundCashStatementParameters()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the cash statement. Defaults to the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to get the next page of results. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys to decorate onto the cash statement rows. (optional)
    nav_type_code = 'nav_type_code_example' # str | The code of the NAV type to use. Defaults to the primary NAV type if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.query_cash_statement_local_currency(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] QueryCashStatementLocalCurrency: [EXPERIMENTAL] QueryCashStatementLocalCurrency: Query the local-currency cash statement for a Fund valuation point.
        api_response = api_instance.query_cash_statement_local_currency(scope, code, query_fund_cash_statement_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->query_cash_statement_local_currency: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **query_fund_cash_statement_parameters** | [**QueryFundCashStatementParameters**](QueryFundCashStatementParameters.md)| The query parameters specifying the diary entry period and display mode. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the cash statement. Defaults to the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to get the next page of results. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys to decorate onto the cash statement rows. | [optional] 
 **nav_type_code** | **str**| The code of the NAV type to use. Defaults to the primary NAV type if not specified. | [optional] 

### Return type

[**ValuationPointResourceListOfFundCashStatementLocalCurrency**](ValuationPointResourceListOfFundCashStatementLocalCurrency.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The local-currency cash statement for the specified Fund valuation point. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **revert_valuation_point_to_estimate**
> RevertValuationPointResponse revert_valuation_point_to_estimate(scope, code, revert_valuation_point_data_request, nav_type_code=nav_type_code)

[EARLY ACCESS] RevertValuationPointToEstimate: Reverts a Final Valuation Point to Estimate.

Moves a 'Final' status Valuation Point to status 'Estimate'.  Returns the reverted Valuation Point alongside every variant that  finalising it had rejected.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # revert_valuation_point_data_request = RevertValuationPointDataRequest.from_json("")
    # revert_valuation_point_data_request = RevertValuationPointDataRequest.from_dict({})
    revert_valuation_point_data_request = RevertValuationPointDataRequest()
    nav_type_code = 'nav_type_code_example' # str | When provided, sets the status of the Valuation Point of the specified NAV Type to be Estimate.              Otherwise, the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.revert_valuation_point_to_estimate(scope, code, revert_valuation_point_data_request, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] RevertValuationPointToEstimate: Reverts a Final Valuation Point to Estimate.
        api_response = api_instance.revert_valuation_point_to_estimate(scope, code, revert_valuation_point_data_request, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->revert_valuation_point_to_estimate: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **revert_valuation_point_data_request** | [**RevertValuationPointDataRequest**](RevertValuationPointDataRequest.md)| The revertValuationPointRequest which contains the Diary Entry code for the Final Valuation Point to move to Estimate status. | 
 **nav_type_code** | **str**| When provided, sets the status of the Valuation Point of the specified NAV Type to be Estimate.              Otherwise, the Primary NAV Type will be used. | [optional] 

### Return type

[**RevertValuationPointResponse**](RevertValuationPointResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reverted Estimate Valuation Point, with every variant resurrected by the revert |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **run_partner_allocations**
> PartnerAllocationRunResult run_partner_allocations(scope, code, partner_allocation_run_request, as_at=as_at)

[EARLY ACCESS] RunPartnerAllocations: [EXPERIMENTAL] RunPartnerAllocations: Allocate a period's income to the Fund's partners.

Share the Fund's income, gains and expenses for the period across the partners on its register, pool by pool,  and book the allocation unless the run is a dry run.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # partner_allocation_run_request = PartnerAllocationRunRequest.from_json("")
    # partner_allocation_run_request = PartnerAllocationRunRequest.from_dict({})
    partner_allocation_run_request = PartnerAllocationRunRequest()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.run_partner_allocations(scope, code, partner_allocation_run_request, as_at=as_at, opts=opts)

        # [EARLY ACCESS] RunPartnerAllocations: [EXPERIMENTAL] RunPartnerAllocations: Allocate a period's income to the Fund's partners.
        api_response = api_instance.run_partner_allocations(scope, code, partner_allocation_run_request, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->run_partner_allocations: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **partner_allocation_run_request** | [**PartnerAllocationRunRequest**](PartnerAllocationRunRequest.md)| The period to allocate and how. | 
 **as_at** | **datetime**| The asAt datetime at which to read the Fund. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**PartnerAllocationRunResult**](PartnerAllocationRunResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The allocation of the period to the partners. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_share_class_instruments**
> Fund set_share_class_instruments(scope, code, set_share_class_instruments_request)

[EARLY ACCESS] SetShareClassInstruments: Set the ShareClass Instruments on a Fund.

Update the ShareClass Instruments on an existing Fund with the set of instruments provided.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # set_share_class_instruments_request = SetShareClassInstrumentsRequest.from_json("")
    # set_share_class_instruments_request = SetShareClassInstrumentsRequest.from_dict({})
    set_share_class_instruments_request = SetShareClassInstrumentsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_share_class_instruments(scope, code, set_share_class_instruments_request, opts=opts)

        # [EARLY ACCESS] SetShareClassInstruments: Set the ShareClass Instruments on a Fund.
        api_response = api_instance.set_share_class_instruments(scope, code, set_share_class_instruments_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->set_share_class_instruments: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **set_share_class_instruments_request** | [**SetShareClassInstrumentsRequest**](SetShareClassInstrumentsRequest.md)| The scopes and instrument identifiers for the instruments to be set. | 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_valuation_point**
> ValuationPoint update_valuation_point(scope, code, update_valuation_point_request, nav_type_code=nav_type_code)

[EARLY ACCESS] UpdateValuationPoint: Update a Valuation Point.

Updates an existing Valuation Point.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_valuation_point_request = UpdateValuationPointRequest.from_json("")
    # update_valuation_point_request = UpdateValuationPointRequest.from_dict({})
    update_valuation_point_request = UpdateValuationPointRequest()
    nav_type_code = 'nav_type_code_example' # str | When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_valuation_point(scope, code, update_valuation_point_request, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] UpdateValuationPoint: Update a Valuation Point.
        api_response = api_instance.update_valuation_point(scope, code, update_valuation_point_request, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->update_valuation_point: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **update_valuation_point_request** | [**UpdateValuationPointRequest**](UpdateValuationPointRequest.md)| The Valuation Point Estimate definition to upsert. | 
 **nav_type_code** | **str**| When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPoint**](ValuationPoint.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated estimated Valuation Point |  -  |
**400** | The details of the input related failure |  -  |
**404** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_bookmark**
> FundCalendarEntry upsert_bookmark(scope, code, upsert_fund_bookmark_request, nav_type_code=nav_type_code)

[EARLY ACCESS] UpsertBookmark: Upsert a bookmark.

This method will update or upsert a Bookmark for the Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_fund_bookmark_request = UpsertFundBookmarkRequest.from_json("")
    # upsert_fund_bookmark_request = UpsertFundBookmarkRequest.from_dict({})
    upsert_fund_bookmark_request = UpsertFundBookmarkRequest()
    nav_type_code = 'nav_type_code_example' # str | When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_bookmark(scope, code, upsert_fund_bookmark_request, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] UpsertBookmark: Upsert a bookmark.
        api_response = api_instance.upsert_bookmark(scope, code, upsert_fund_bookmark_request, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->upsert_bookmark: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **upsert_fund_bookmark_request** | [**UpsertFundBookmarkRequest**](UpsertFundBookmarkRequest.md)| The bookmark definition to upsert. | 
 **nav_type_code** | **str**| When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**FundCalendarEntry**](FundCalendarEntry.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted Bookmark |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_diary_entry_type_valuation_point**
> DiaryEntry upsert_diary_entry_type_valuation_point(scope, code, upsert_valuation_point_request, nav_type_code=nav_type_code)

[EARLY ACCESS] UpsertDiaryEntryTypeValuationPoint: Upsert a Valuation Point.

Insert the estimate Valuation Point.                If the Valuation Point does not exist, this method will create it in estimate state.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_valuation_point_request = UpsertValuationPointRequest.from_json("")
    # upsert_valuation_point_request = UpsertValuationPointRequest.from_dict({})
    upsert_valuation_point_request = UpsertValuationPointRequest()
    nav_type_code = 'nav_type_code_example' # str | When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_diary_entry_type_valuation_point(scope, code, upsert_valuation_point_request, nav_type_code=nav_type_code, opts=opts)

        # [EARLY ACCESS] UpsertDiaryEntryTypeValuationPoint: Upsert a Valuation Point.
        api_response = api_instance.upsert_diary_entry_type_valuation_point(scope, code, upsert_valuation_point_request, nav_type_code=nav_type_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->upsert_diary_entry_type_valuation_point: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **upsert_valuation_point_request** | [**UpsertValuationPointRequest**](UpsertValuationPointRequest.md)| The Valuation Point Estimate definition to upsert. | 
 **nav_type_code** | **str**| When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**DiaryEntry**](DiaryEntry.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted estimated Valuation Point |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_fee_properties**
> FeeProperties upsert_fee_properties(scope, code, fee_code, request_body=request_body)

[EARLY ACCESS] UpsertFeeProperties: Upsert Fee properties.

Update or insert one or more properties onto a single Fee. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Fee'.                Upserting a property that exists for an Fee, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    fee_code = 'fee_code_example' # str | The code of the Fee to update or insert the properties onto.
    request_body = {"Fee/MyScope/FundManagerName":{"key":"Fee/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Fee/MyScope/SomeProperty":{"key":"Fee/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Fee/MyScope/AnotherProperty":{"key":"Fee/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Fee/MyScope/ReBalanceInterval":{"key":"Fee/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be updated or inserted onto the Fee. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"Fee/Manager/Id\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_fee_properties(scope, code, fee_code, request_body=request_body, opts=opts)

        # [EARLY ACCESS] UpsertFeeProperties: Upsert Fee properties.
        api_response = api_instance.upsert_fee_properties(scope, code, fee_code, request_body=request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->upsert_fee_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_code** | **str**| The code of the Fee to update or insert the properties onto. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Fee. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Fee/Manager/Id\&quot;. | [optional] 

### Return type

[**FeeProperties**](FeeProperties.md)

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

# **upsert_fund_properties**
> FundProperties upsert_fund_properties(scope, code, request_body=request_body)

[EARLY ACCESS] UpsertFundProperties: Upsert Fund properties.

Update or insert one or more properties onto a single Fund. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Fund'.                Upserting a property that exists for an Fund, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    request_body = {"Fund/MyScope/FundManagerName":{"key":"Fund/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Fund/MyScope/SomeProperty":{"key":"Fund/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Fund/MyScope/AnotherProperty":{"key":"Fund/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Fund/MyScope/ReBalanceInterval":{"key":"Fund/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be updated or inserted onto the Fund. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"Fund/Manager/Id\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_fund_properties(scope, code, request_body=request_body, opts=opts)

        # [EARLY ACCESS] UpsertFundProperties: Upsert Fund properties.
        api_response = api_instance.upsert_fund_properties(scope, code, request_body=request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->upsert_fund_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Fund. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Fund/Manager/Id\&quot;. | [optional] 

### Return type

[**FundProperties**](FundProperties.md)

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

# **upsert_nav_activity_adjustments**
> datetime upsert_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)

[EARLY ACCESS] UpsertNavActivityAdjustments: Upsert NAV adjustment activities to a valuation point

Upserts the NAV adjustment activities to the specified valuation point for a Fund.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundsApi
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
    api_instance = api_client_factory.build(FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope is the unique identifier for the given Fund.
    valuation_point_code = 'valuation_point_code_example' # str | The valuation point Code to apply the adjustment to
    nav_activity_adjustment = [{"asAt":"2024-01-01T00:00:00.0000000+00:00","portfolioScope":"portfolioScope1","portfolioCode":"portfolioCode1","transactionId":"transactionId1","navActivityAdjustmentType":"PortfolioTransaction"}] # List[NavActivityAdjustment] | The request describing the Nav activity adjustments to apply to a specific valuation point and nav type
    nav_type_code = 'nav_type_code_example' # str | When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. (optional)
    valuation_point_code_variant = 'valuation_point_code_variant_example' # str | The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant, opts=opts)

        # [EARLY ACCESS] UpsertNavActivityAdjustments: Upsert NAV adjustment activities to a valuation point
        api_response = api_instance.upsert_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundsApi->upsert_nav_activity_adjustments: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | 
 **valuation_point_code** | **str**| The valuation point Code to apply the adjustment to | 
 **nav_activity_adjustment** | [**List[NavActivityAdjustment]**](NavActivityAdjustment.md)| The request describing the Nav activity adjustments to apply to a specific valuation point and nav type | 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

**datetime**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The date and time of the successfully applied Nav Activity Adjustments. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

