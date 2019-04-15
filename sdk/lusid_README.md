# lusid-sdk
# Introduction  This page documents the [LUSID APIs](https://api.lusid.com/swagger), which allows authorised clients to query and update their data within the LUSID platform.  SDKs to interact with the LUSID APIs are available in the following languages :  * [C#](https://github.com/finbourne/lusid-sdk-csharp) * [Java](https://github.com/finbourne/lusid-sdk-java) * [JavaScript](https://github.com/finbourne/lusid-sdk-js) * [Python](https://github.com/finbourne/lusid-sdk-python)  # Data Model  The LUSID API has a relatively lightweight but extremely powerful data model.   One of the goals of LUSID was not to enforce on clients a single rigid data model but rather to provide a flexible foundation onto which clients can streamline their data.   One of the primary tools to extend the data model is through using properties.  Properties can be associated with amongst others: - * Transactions * Instruments * Portfolios   The LUSID data model is exposed through the LUSID APIs.  The APIs provide access to both business objects and the meta data used to configure the systems behaviours.   The key business entities are: - * **Portfolios** A portfolio is the primary container for transactions and holdings.  * **Derived Portfolios** Derived portfolios allow portfolios to be created based on other portfolios, by overriding or overlaying specific items * **Holdings** A holding is a position account for a instrument within a portfolio.  Holdings can only be adjusted via transactions. * **Transactions** A Transaction is a source of transactions used to manipulate holdings.  * **Corporate Actions** A corporate action is a market event which occurs to a instrument, for example a stock split * **Instruments**  A instrument represents a currency, tradable instrument or OTC contract that is attached to a transaction and a holding. * **Properties** Several entities allow additional user defined properties to be associated with them.   For example, a Portfolio manager may be associated with a portfolio  Meta data includes: - * **Transaction Types** Transactions are booked with a specific transaction type.  The types are client defined and are used to map the Transaction to a series of movements which update the portfolio holdings.  * **Properties Types** Types of user defined properties used within the system.  This section describes the data model that LUSID exposes via the APIs.  ## Scope  All data in LUSID is segregated at the client level.  Entities in LUSID are identifiable by a unique code.  Every entity lives within a logical data partition known as a Scope.  Scope is an identity namespace allowing two entities with the same unique code to co-exist within individual address spaces.  For example, prices for equities from different vendors may be uploaded into different scopes such as `client/vendor1` and `client/vendor2`.  A portfolio may then be valued using either of the price sources by referencing the appropriate scope.  LUSID Clients cannot access scopes of other clients.  ## Schema  A detailed description of the entities used by the API and parameters for endpoints which take a JSON document can be retrieved via the `schema` endpoint.  ## Instruments  LUSID has its own built-in instrument master which you can use to master your own instrument universe.  Every instrument must be created with one or more unique market identifiers, such as [FIGI](https://openfigi.com/) or RIC code. For any non-listed instruments (eg OTCs), you can upload an instrument against a custom ID of your choosing.  In addition, LUSID will allocate each instrument a unique 'LUSID instrument identifier'. The LUSID instrument identifier is what is used when uploading transactions, holdings, prices, etc. The API exposes an `instrument/lookup` endpoint which can be used to lookup these LUSID identifiers using their market identifiers.  Cash can be referenced using the ISO currency code prefixed with \"`CCY_`\" e.g. `CCY_GBP`  ## Instrument Prices (Analytics)  Instrument prices are stored in LUSID's Analytics Store  | Field|Type|Description | | ---|---|--- | | InstrumentUid|string|Unique instrument identifier | | Value|decimal|Value of the analytic, eg price | | Denomination|string|Underlying unit of the analytic, eg currency, EPS etc. |   ## Instrument Data  Instrument data can be uploaded to the system using the [Instrument Properties](#tag/InstrumentProperties) endpoint.  | Field|Type|Description | | ---|---|--- |   ## Portfolios  Portfolios are the top-level entity containers within LUSID, containing transactions, corporate actions and holdings.    The transactions build up the portfolio holdings on which valuations, analytics profit & loss and risk can be calculated.     Properties can be associated with Portfolios to add in additional model data.  Portfolio properties can be changed over time as well.  For example, to allow a Portfolio Manager to be linked with a Portfolio.  Additionally, portfolios can be securitised and held by other portfolios, allowing LUSID to perform \"drill-through\" into underlying fund holdings  ### Reference Portfolios Reference portfolios are portfolios that contain only weights, as opposed to transactions, and are designed to represent entities such as indices.  ### Derived Portfolios  LUSID also allows for a portfolio to be composed of another portfolio via derived portfolios.  A derived portfolio can contain its own transactions and also inherits any transactions from its parent portfolio.  Any changes made to the parent portfolio are automatically reflected in derived portfolio.  Derived portfolios in conjunction with scopes are a powerful construct.  For example, to do pre-trade what-if analysis, a derived portfolio could be created a new namespace linked to the underlying live (parent) portfolio.  Analysis can then be undertaken on the derived portfolio without affecting the live portfolio.  ### Portfolio Groups Portfolio groups allow the construction of a hierarchy from portfolios and groups.  Portfolio operations on the group are executed on an aggregated set of portfolios in the hierarchy.   For example:   * Global Portfolios _(group)_   * APAC _(group)_     * Hong Kong _(portfolio)_     * Japan _(portfolio)_   * Europe _(group)_     * France _(portfolio)_     * Germany _(portfolio)_   * UK _(portfolio)_   In this example **Global Portfolios** is a group that consists of an aggregate of **Hong Kong**, **Japan**, **France**, **Germany** and **UK** portfolios.  ### Movements Engine The Movements engine sits on top of the immutable event store and is used to manage the relationship between input trading actions and their associated portfolio holdings.     The movements engine reads in the following entity types:- * Posting Transactions * Applying Corporate Actions  * Holding Adjustments  These are converted to one or more movements and used by the movements engine to calculate holdings.  At the same time it also calculates running balances, and realised P&L.  The outputs from the movements engine are holdings and transactions.  ## Transactions  A transaction represents an economic activity against a Portfolio.  Transactions are processed according to a configuration. This will tell the LUSID engine how to interpret the transaction and correctly update the holdings. LUSID comes with a set of transaction types you can use out of the box, or you can configure your own set(s) of transactions.  For more details see the [LUSID Getting Started Guide for transaction configuration.](https://support.finbourne.com/hc/en-us/articles/360016737511-Configuring-Transaction-Types)  | Field|Type|Description | | ---|---|--- | | TransactionId|string|Unique transaction identifier | | Type|string|LUSID transaction type code - Buy, Sell, StockIn, StockOut, etc | | InstrumentIdentifiers|IReadOnlyDictionary`2|Unique instrument identifiers. | | InstrumentUid|string|Unique instrument identifier | | TransactionDate|datetime|Transaction date | | SettlementDate|datetime|Settlement date | | Units|decimal|Quantity of transaction in units of the instrument | | TransactionPrice|tradeprice|Execution price for the transaction | | TotalConsideration|currencyandamount|Total value of the transaction in settlement currency | | ExchangeRate|decimal|Rate between transaction and settle currency | | TransactionCurrency|currency|Transaction currency | | CounterpartyId|string|Counterparty identifier | | Source|string|Where this transaction came from | | NettingSet|string|  |   From these fields, the following values can be calculated  * **Transaction value in Transaction currency**: TotalConsideration / ExchangeRate  * **Transaction value in Portfolio currency**: Transaction value in Transaction currency * TradeToPortfolioRate  ### Example Transactions  #### A Common Purchase Example Three example transactions are shown in the table below.   They represent a purchase of USD denominated IBM shares within a Sterling denominated portfolio.   * The first two transactions are for separate buy and fx trades    * Buying 500 IBM shares for $71,480.00    * A foreign exchange conversion to fund the IBM purchase. (Buy $71,480.00 for &#163;54,846.60)  * The third transaction is an alternate version of the above trades. Buying 500 IBM shares and settling directly in Sterling.  | Column |  Buy Trade | Fx Trade | Buy Trade with foreign Settlement | | ----- | ----- | ----- | ----- | | TransactionId | FBN00001 | FBN00002 | FBN00003 | | Type | Buy | FxBuy | Buy | | InstrumentUid | FIGI_BBG000BLNNH6 | CCY_USD | FIGI_BBG000BLNNH6 | | TransactionDate | 2018-08-02 | 2018-08-02 | 2018-08-02 | | SettlementDate | 2018-08-06 | 2018-08-06 | 2018-08-06 | | Units | 500 | 71480 | 500 | | TransactionPrice | 142.96 | 1 | 142.96 | | TradeCurrency | USD | USD | USD | | ExchangeRate | 1 | 0.7673 | 0.7673 | | TotalConsideration.Amount | 71480.00 | 54846.60 | 54846.60 | | TotalConsideration.Currency | USD | GBP | GBP | | Trade/default/TradeToPortfolioRate&ast; | 0.7673 | 0.7673 | 0.7673 |  [&ast; This is a property field]  #### A Forward FX Example  LUSID has a flexible transaction modelling system, and there are a number of different ways of modelling forward fx trades.  The default LUSID transaction types are FwdFxBuy and FwdFxSell. Other types and behaviours can be configured as required.  Using these transaction types, the holdings query will report two forward positions. One in each currency.   Since an FX trade is an exchange of one currency for another, the following two 6 month forward transactions are equivalent:  | Column |  Forward 'Sell' Trade | Forward 'Buy' Trade | | ----- | ----- | ----- | | TransactionId | FBN00004 | FBN00005 | | Type | FwdFxSell | FwdFxBuy | | InstrumentUid | CCY_GBP | CCY_USD | | TransactionDate | 2018-08-02 | 2018-08-02 | | SettlementDate | 2019-02-06 | 2019-02-06 | | Units | 10000.00 | 13142.00 | | TransactionPrice |1 | 1 | | TradeCurrency | GBP | USD | | ExchangeRate | 1.3142 | 0.760919 | | TotalConsideration.Amount | 13142.00 | 10000.00 | | TotalConsideration.Currency | USD | GBP | | Trade/default/TradeToPortfolioRate | 1.0 | 0.760919 |  ## Holdings  A holding represents a position in a instrument or cash on a given date.  | Field|Type|Description | | ---|---|--- | | InstrumentUid|string|Unique instrument identifier | | HoldingType|string|Type of holding, eg Position, Balance, CashCommitment, Receivable, ForwardFX | | Units|decimal|Quantity of holding | | SettledUnits|decimal|Settled quantity of holding | | Cost|currencyandamount|Book cost of holding in transaction currency | | CostPortfolioCcy|currencyandamount|Book cost of holding in portfolio currency | | Transaction|Transaction|If this is commitment-type holding, the transaction behind it |   ## Corporate Actions  Corporate actions are represented within LUSID in terms of a set of instrument-specific 'transitions'.  These transitions are used to specify the participants of the corporate action, and the effect that the corporate action will have on holdings in those participants.  *Corporate action*  | Field|Type|Description | | ---|---|--- | | SourceId|id|  | | CorporateActionCode|code|  | | AnnouncementDate|datetime|  | | ExDate|datetime|  | | RecordDate|datetime|  | | PaymentDate|datetime|  |    *Transition*  | Field|Type|Description | | ---|---|--- |   ## Property  Properties are key-value pairs that can be applied to any entity within a domain (where a domain is `trade`, `portfolio`, `security` etc).  Properties must be defined before use with a `PropertyDefinition` and can then subsequently be added to entities.  # Schemas  The following headers are returned on all responses from LUSID  | Name | Purpose | | --- | --- | | lusid-meta-duration | Duration of the request | | lusid-meta-success | Whether or not LUSID considered the request to be successful | | lusid-meta-requestId | The unique identifier for the request | | lusid-schema-url | Url of the schema for the data being returned | | lusid-property-schema-url | Url of the schema for any properties |   # Error Codes  | Code|Name|Description | | ---|---|--- | | <a name=\"102\">102</a>|VersionNotFound|  | | <a name=\"104\">104</a>|InstrumentNotFound|  | | <a name=\"105\">105</a>|PropertyNotFound|  | | <a name=\"106\">106</a>|PortfolioRecursionDepth|  | | <a name=\"108\">108</a>|GroupNotFound|  | | <a name=\"109\">109</a>|PortfolioNotFound|  | | <a name=\"110\">110</a>|PropertySchemaNotFound|  | | <a name=\"111\">111</a>|PortfolioAncestryNotFound|  | | <a name=\"112\">112</a>|PortfolioWithIdAlreadyExists|  | | <a name=\"113\">113</a>|OrphanedPortfolio|  | | <a name=\"119\">119</a>|MissingBaseClaims|  | | <a name=\"121\">121</a>|PropertyNotDefined|  | | <a name=\"122\">122</a>|CannotDeleteSystemProperty|  | | <a name=\"123\">123</a>|CannotModifyImmutablePropertyField|  | | <a name=\"124\">124</a>|PropertyAlreadyExists|  | | <a name=\"125\">125</a>|InvalidPropertyLifeTime|  | | <a name=\"127\">127</a>|CannotModifyDefaultDataType|  | | <a name=\"128\">128</a>|GroupAlreadyExists|  | | <a name=\"129\">129</a>|NoSuchDataType|  | | <a name=\"132\">132</a>|ValidationError|  | | <a name=\"133\">133</a>|LoopDetectedInGroupHierarchy|  | | <a name=\"135\">135</a>|SubGroupAlreadyExists|  | | <a name=\"138\">138</a>|PriceSourceNotFound|  | | <a name=\"139\">139</a>|AnalyticStoreNotFound|  | | <a name=\"141\">141</a>|AnalyticStoreAlreadyExists|  | | <a name=\"143\">143</a>|ClientInstrumentAlreadyExists|  | | <a name=\"144\">144</a>|DuplicateInParameterSet|  | | <a name=\"147\">147</a>|ResultsNotFound|  | | <a name=\"148\">148</a>|OrderFieldNotInResultSet|  | | <a name=\"149\">149</a>|OperationFailed|  | | <a name=\"150\">150</a>|ElasticSearchError|  | | <a name=\"151\">151</a>|InvalidParameterValue|  | | <a name=\"153\">153</a>|CommandProcessingFailure|  | | <a name=\"154\">154</a>|EntityStateConstructionFailure|  | | <a name=\"155\">155</a>|EntityTimelineDoesNotExist|  | | <a name=\"156\">156</a>|EventPublishFailure|  | | <a name=\"157\">157</a>|InvalidRequestFailure|  | | <a name=\"158\">158</a>|EventPublishUnknown|  | | <a name=\"159\">159</a>|EventQueryFailure|  | | <a name=\"160\">160</a>|BlobDidNotExistFailure|  | | <a name=\"162\">162</a>|SubSystemRequestFailure|  | | <a name=\"163\">163</a>|SubSystemConfigurationFailure|  | | <a name=\"165\">165</a>|FailedToDelete|  | | <a name=\"166\">166</a>|UpsertClientInstrumentFailure|  | | <a name=\"167\">167</a>|IllegalAsAtInterval|  | | <a name=\"168\">168</a>|IllegalBitemporalQuery|  | | <a name=\"169\">169</a>|InvalidAlternateId|  | | <a name=\"170\">170</a>|CannotAddSourcePortfolioPropertyExplicitly|  | | <a name=\"171\">171</a>|EntityAlreadyExistsInGroup|  | | <a name=\"173\">173</a>|EntityWithIdAlreadyExists|  | | <a name=\"174\">174</a>|DerivedPortfolioDetailsDoNotExist|  | | <a name=\"176\">176</a>|PortfolioWithNameAlreadyExists|  | | <a name=\"177\">177</a>|InvalidTransactions|  | | <a name=\"178\">178</a>|ReferencePortfolioNotFound|  | | <a name=\"179\">179</a>|DuplicateIdFailure|  | | <a name=\"180\">180</a>|CommandRetrievalFailure|  | | <a name=\"181\">181</a>|DataFilterApplicationFailure|  | | <a name=\"182\">182</a>|SearchFailed|  | | <a name=\"183\">183</a>|MovementsEngineConfigurationKeyFailure|  | | <a name=\"184\">184</a>|FxRateSourceNotFound|  | | <a name=\"185\">185</a>|AccrualSourceNotFound|  | | <a name=\"186\">186</a>|EntitlementsFailure|  | | <a name=\"187\">187</a>|InvalidIdentityToken|  | | <a name=\"188\">188</a>|InvalidRequestHeaders|  | | <a name=\"189\">189</a>|PriceNotFound|  | | <a name=\"190\">190</a>|InvalidSubHoldingKeysProvided|  | | <a name=\"191\">191</a>|DuplicateSubHoldingKeysProvided|  | | <a name=\"192\">192</a>|CutDefinitionNotFound|  | | <a name=\"193\">193</a>|CutDefinitionInvalid|  | | <a name=\"200\">200</a>|InvalidUnitForDataType|  | | <a name=\"201\">201</a>|InvalidTypeForDataType|  | | <a name=\"202\">202</a>|InvalidValueForDataType|  | | <a name=\"203\">203</a>|UnitNotDefinedForDataType|  | | <a name=\"204\">204</a>|UnitsNotSupportedOnDataType|  | | <a name=\"205\">205</a>|CannotSpecifyUnitsOnDataType|  | | <a name=\"206\">206</a>|UnitSchemaInconsistentWithDataType|  | | <a name=\"207\">207</a>|UnitDefinitionNotSpecified|  | | <a name=\"208\">208</a>|DuplicateUnitDefinitionsSpecified|  | | <a name=\"209\">209</a>|InvalidUnitsDefinition|  | | <a name=\"210\">210</a>|InvalidInstrumentIdentifierUnit|  | | <a name=\"211\">211</a>|HoldingsAdjustmentDoesNotExist|  | | <a name=\"212\">212</a>|CouldNotBuildExcelUrl|  | | <a name=\"213\">213</a>|CouldNotGetExcelVersion|  | | <a name=\"214\">214</a>|InstrumentByCodeNotFound|  | | <a name=\"215\">215</a>|EntitySchemaDoesNotExist|  | | <a name=\"216\">216</a>|FeatureNotSupportedOnPortfolioType|  | | <a name=\"217\">217</a>|QuoteNotFoundFailure|  | | <a name=\"219\">219</a>|InvalidInstrumentDefinition|  | | <a name=\"221\">221</a>|InstrumentUpsertFailure|  | | <a name=\"222\">222</a>|ReferencePortfolioRequestNotSupported|  | | <a name=\"223\">223</a>|TransactionPortfolioRequestNotSupported|  | | <a name=\"224\">224</a>|InvalidPropertyValueAssignment|  | | <a name=\"230\">230</a>|TransactionTypeNotFound|  | | <a name=\"231\">231</a>|TransactionTypeDuplication|  | | <a name=\"232\">232</a>|PortfolioDoesNotExistAtGivenDate|  | | <a name=\"233\">233</a>|QueryParserFailure|  | | <a name=\"234\">234</a>|DuplicateConstituentFailure|  | | <a name=\"235\">235</a>|UnresolvedInstrumentConstituentFailure|  | | <a name=\"236\">236</a>|UnresolvedInstrumentInTransitionFailure|  | | <a name=\"300\">300</a>|MissingRecipeFailure|  | | <a name=\"301\">301</a>|DependenciesFailure|  | | <a name=\"304\">304</a>|PortfolioPreprocessFailure|  | | <a name=\"310\">310</a>|ValuationEngineFailure|  | | <a name=\"311\">311</a>|TaskFactoryFailure|  | | <a name=\"312\">312</a>|TaskEvaluationFailure|  | | <a name=\"350\">350</a>|InstrumentFailure|  | | <a name=\"351\">351</a>|CashFlowsFailure|  | | <a name=\"370\">370</a>|ResultRetrievalFailure|  | | <a name=\"371\">371</a>|ResultProcessingFailure|  | | <a name=\"372\">372</a>|VendorResultProcessingFailure|  | | <a name=\"373\">373</a>|CannotSupplyTimesWithPortfoliosQuery|  | | <a name=\"374\">374</a>|AttemptToUpsertDuplicateQuotes|  | | <a name=\"375\">375</a>|CorporateActionSourceDoesNotExist|  | | <a name=\"376\">376</a>|InstrumentIdentifierAlreadyInUse|  | | <a name=\"377\">377</a>|PortfolioInInvalidState|  | | <a name=\"378\">378</a>|GroupInInvalidState|  | | <a name=\"379\">379</a>|CorporateActionSourceInInvalidState|  | | <a name=\"380\">380</a>|LookThroughPortfolioInInvalidState|  | | <a name=\"381\">381</a>|InstrumentInInvalidState|  | | <a name=\"382\">382</a>|PropertyDefinitionInInvalidState|  | | <a name=\"-10\">-10</a>|ServerConfigurationError|  | | <a name=\"-1\">-1</a>|Unknown error|  | 

The `lusid` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.10.9
- Package version: 0.10.9
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.finbourne.com](https://www.finbourne.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.15
* six >= 1.10
* certifi
* python-dateutil

## Getting Started

In your own code, to use this library to connect and interact with lusid-sdk,
you can run the following:

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
aggregation_request = lusid.AggregationRequest() # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # Aggregate data in a portfolio group
    api_response = api_instance.get_aggregation_by_group(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_aggregation_by_group: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AggregationApi* | [**get_aggregation_by_group**](lusid/docs/AggregationApi.md#get_aggregation_by_group) | **POST** /api/portfoliogroups/{scope}/{code}/$aggregate | Aggregate data in a portfolio group
*AggregationApi* | [**get_aggregation_by_portfolio**](lusid/docs/AggregationApi.md#get_aggregation_by_portfolio) | **POST** /api/portfolios/{scope}/{code}/$aggregate | Aggregate data in a portfolio
*AggregationApi* | [**get_aggregation_by_result_set**](lusid/docs/AggregationApi.md#get_aggregation_by_result_set) | **POST** /api/results/{scope}/{resultsKey}/$aggregate | Aggregate using result data
*AggregationApi* | [**get_nested_aggregation_by_group**](lusid/docs/AggregationApi.md#get_nested_aggregation_by_group) | **POST** /api/portfoliogroups/{scope}/{code}/$aggregatenested | Aggregate data in a portfolio group, as nested
*AnalyticsStoresApi* | [**create_analytic_store**](lusid/docs/AnalyticsStoresApi.md#create_analytic_store) | **POST** /api/analytics | Create analytic store
*AnalyticsStoresApi* | [**delete_analytic_store**](lusid/docs/AnalyticsStoresApi.md#delete_analytic_store) | **DELETE** /api/analytics/{scope}/{year}/{month}/{day} | Delete analytic store
*AnalyticsStoresApi* | [**get_analytic_store**](lusid/docs/AnalyticsStoresApi.md#get_analytic_store) | **GET** /api/analytics/{scope}/{year}/{month}/{day} | Get analytic store
*AnalyticsStoresApi* | [**list_analytic_stores**](lusid/docs/AnalyticsStoresApi.md#list_analytic_stores) | **GET** /api/analytics | List analytic stores
*AnalyticsStoresApi* | [**set_analytics**](lusid/docs/AnalyticsStoresApi.md#set_analytics) | **PUT** /api/analytics/{scope}/{year}/{month}/{day}/prices | Set analytic data
*ApplicationMetadataApi* | [**get_excel_addin**](lusid/docs/ApplicationMetadataApi.md#get_excel_addin) | **GET** /api/metadata/downloads/exceladdin | Download Excel Addin
*ApplicationMetadataApi* | [**get_excel_download_url**](lusid/docs/ApplicationMetadataApi.md#get_excel_download_url) | **GET** /api/metadata/downloads/excel | Get Excel download url
*ApplicationMetadataApi* | [**get_lusid_versions**](lusid/docs/ApplicationMetadataApi.md#get_lusid_versions) | **GET** /api/metadata/versions | Get LUSID versions
*CorporateActionSourcesApi* | [**batch_upsert_corporate_actions**](lusid/docs/CorporateActionSourcesApi.md#batch_upsert_corporate_actions) | **POST** /api/corporateactionsources/{scope}/{code}/corporateactions | Upsert corporate actions
*CorporateActionSourcesApi* | [**create_corporate_action_source**](lusid/docs/CorporateActionSourcesApi.md#create_corporate_action_source) | **POST** /api/corporateactionsources | Create Corporate Action Source
*CorporateActionSourcesApi* | [**delete_corporate_action_source**](lusid/docs/CorporateActionSourcesApi.md#delete_corporate_action_source) | **DELETE** /api/corporateactionsources/{scope}/{code} | Delete a corporate action source
*CorporateActionSourcesApi* | [**get_corporate_actions**](lusid/docs/CorporateActionSourcesApi.md#get_corporate_actions) | **GET** /api/corporateactionsources/{scope}/{code}/corporateactions | Get corporate actions
*CorporateActionSourcesApi* | [**list_corporate_action_sources**](lusid/docs/CorporateActionSourcesApi.md#list_corporate_action_sources) | **GET** /api/corporateactionsources | Get corporate action sources
*DataTypesApi* | [**create_data_type**](lusid/docs/DataTypesApi.md#create_data_type) | **POST** /api/datatypes | Create data type definition
*DataTypesApi* | [**get_data_type**](lusid/docs/DataTypesApi.md#get_data_type) | **GET** /api/datatypes/{scope}/{code} | Get data type definition
*DataTypesApi* | [**get_units_from_data_type**](lusid/docs/DataTypesApi.md#get_units_from_data_type) | **GET** /api/datatypes/{scope}/{code}/units | Get units from data type
*DataTypesApi* | [**list_data_types**](lusid/docs/DataTypesApi.md#list_data_types) | **GET** /api/datatypes/{scope} | List data types
*DataTypesApi* | [**update_data_type**](lusid/docs/DataTypesApi.md#update_data_type) | **PUT** /api/datatypes/{scope}/{code} | Update data type definition
*DerivedTransactionPortfoliosApi* | [**create_derived_portfolio**](lusid/docs/DerivedTransactionPortfoliosApi.md#create_derived_portfolio) | **POST** /api/derivedtransactionportfolios/{scope} | Create derived transaction portfolio
*DerivedTransactionPortfoliosApi* | [**delete_derived_portfolio_details**](lusid/docs/DerivedTransactionPortfoliosApi.md#delete_derived_portfolio_details) | **DELETE** /api/derivedtransactionportfolios/{scope}/{code}/details | Delete portfolio details
*InstrumentsApi* | [**delete_instrument**](lusid/docs/InstrumentsApi.md#delete_instrument) | **DELETE** /api/instruments/{identifierType}/{identifier} | Delete instrument
*InstrumentsApi* | [**get_instrument**](lusid/docs/InstrumentsApi.md#get_instrument) | **GET** /api/instruments/{identifierType}/{identifier} | Get instrument definition
*InstrumentsApi* | [**get_instrument_identifiers**](lusid/docs/InstrumentsApi.md#get_instrument_identifiers) | **GET** /api/instruments/identifiers | Get allowable instrument identifiers
*InstrumentsApi* | [**get_instruments**](lusid/docs/InstrumentsApi.md#get_instruments) | **POST** /api/instruments/$get | Get instrument definition
*InstrumentsApi* | [**list_instruments**](lusid/docs/InstrumentsApi.md#list_instruments) | **GET** /api/instruments | Get all of the currently mastered instruments in LUSID
*InstrumentsApi* | [**update_instrument_identifier**](lusid/docs/InstrumentsApi.md#update_instrument_identifier) | **POST** /api/instruments/{identifierType}/{identifier} | Update instrument identifier
*InstrumentsApi* | [**upsert_instruments**](lusid/docs/InstrumentsApi.md#upsert_instruments) | **POST** /api/instruments | Upsert instruments
*InstrumentsApi* | [**upsert_instruments_properties**](lusid/docs/InstrumentsApi.md#upsert_instruments_properties) | **POST** /api/instruments/$upsertproperties | Upsert instrument properties
*LoginApi* | [**get_saml_identity_provider_id**](lusid/docs/LoginApi.md#get_saml_identity_provider_id) | **GET** /api/login/saml/{domain} | Get SAML Identity Provider
*PortfolioGroupsApi* | [**add_portfolio_to_group**](lusid/docs/PortfolioGroupsApi.md#add_portfolio_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/portfolios | Add portfolio to group
*PortfolioGroupsApi* | [**add_sub_group_to_group**](lusid/docs/PortfolioGroupsApi.md#add_sub_group_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/subgroups | Add group to group
*PortfolioGroupsApi* | [**create_portfolio_group**](lusid/docs/PortfolioGroupsApi.md#create_portfolio_group) | **POST** /api/portfoliogroups/{scope} | Create group
*PortfolioGroupsApi* | [**delete_portfolio_from_group**](lusid/docs/PortfolioGroupsApi.md#delete_portfolio_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode} | Remove portfolio from group
*PortfolioGroupsApi* | [**delete_portfolio_group**](lusid/docs/PortfolioGroupsApi.md#delete_portfolio_group) | **DELETE** /api/portfoliogroups/{scope}/{code} | Delete group
*PortfolioGroupsApi* | [**delete_sub_group_from_group**](lusid/docs/PortfolioGroupsApi.md#delete_sub_group_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode} | Remove group from group
*PortfolioGroupsApi* | [**get_portfolio_group**](lusid/docs/PortfolioGroupsApi.md#get_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code} | Get portfolio group
*PortfolioGroupsApi* | [**get_portfolio_group_commands**](lusid/docs/PortfolioGroupsApi.md#get_portfolio_group_commands) | **GET** /api/portfoliogroups/{scope}/{code}/commands | Get commands
*PortfolioGroupsApi* | [**get_portfolio_group_expansion**](lusid/docs/PortfolioGroupsApi.md#get_portfolio_group_expansion) | **GET** /api/portfoliogroups/{scope}/{code}/expansion | Get a full expansion of a portfolio group
*PortfolioGroupsApi* | [**list_portfolio_groups**](lusid/docs/PortfolioGroupsApi.md#list_portfolio_groups) | **GET** /api/portfoliogroups/{scope} | List groups in scope
*PortfolioGroupsApi* | [**update_portfolio_group**](lusid/docs/PortfolioGroupsApi.md#update_portfolio_group) | **PUT** /api/portfoliogroups/{scope}/{code} | Update group
*PortfoliosApi* | [**delete_portfolio**](lusid/docs/PortfoliosApi.md#delete_portfolio) | **DELETE** /api/portfolios/{scope}/{code} | Delete portfolio
*PortfoliosApi* | [**delete_portfolio_properties**](lusid/docs/PortfoliosApi.md#delete_portfolio_properties) | **DELETE** /api/portfolios/{scope}/{code}/properties | Delete portfolio properties
*PortfoliosApi* | [**get_portfolio**](lusid/docs/PortfoliosApi.md#get_portfolio) | **GET** /api/portfolios/{scope}/{code} | Get portfolio definition
*PortfoliosApi* | [**get_portfolio_commands**](lusid/docs/PortfoliosApi.md#get_portfolio_commands) | **GET** /api/portfolios/{scope}/{code}/commands | Get commands
*PortfoliosApi* | [**get_portfolio_properties**](lusid/docs/PortfoliosApi.md#get_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties | Get portfolio properties
*PortfoliosApi* | [**list_portfolios**](lusid/docs/PortfoliosApi.md#list_portfolios) | **GET** /api/portfolios | List portfolios
*PortfoliosApi* | [**list_portfolios_for_scope**](lusid/docs/PortfoliosApi.md#list_portfolios_for_scope) | **GET** /api/portfolios/{scope} | List portfolios for scope
*PortfoliosApi* | [**update_portfolio**](lusid/docs/PortfoliosApi.md#update_portfolio) | **PUT** /api/portfolios/{scope}/{code} | Update portfolio definition
*PortfoliosApi* | [**upsert_portfolio_properties**](lusid/docs/PortfoliosApi.md#upsert_portfolio_properties) | **POST** /api/portfolios/{scope}/{code}/properties | Upsert properties
*PropertyDefinitionsApi* | [**create_property_definition**](lusid/docs/PropertyDefinitionsApi.md#create_property_definition) | **POST** /api/propertydefinitions | Define a new property
*PropertyDefinitionsApi* | [**delete_property_definition**](lusid/docs/PropertyDefinitionsApi.md#delete_property_definition) | **DELETE** /api/propertydefinitions/{domain}/{scope}/{code} | Delete property definition
*PropertyDefinitionsApi* | [**get_multiple_property_definitions**](lusid/docs/PropertyDefinitionsApi.md#get_multiple_property_definitions) | **GET** /api/propertydefinitions | Get multiple property definitions
*PropertyDefinitionsApi* | [**get_property_definition**](lusid/docs/PropertyDefinitionsApi.md#get_property_definition) | **GET** /api/propertydefinitions/{domain}/{scope}/{code} | Get property definition
*PropertyDefinitionsApi* | [**update_property_definition**](lusid/docs/PropertyDefinitionsApi.md#update_property_definition) | **PUT** /api/propertydefinitions/{domain}/{scope}/{code} | Update the definition of the specified existing property
*QuotesApi* | [**delete_quotes**](lusid/docs/QuotesApi.md#delete_quotes) | **POST** /api/quotes/{scope}/$delete | Delete a quote
*QuotesApi* | [**get_quotes**](lusid/docs/QuotesApi.md#get_quotes) | **POST** /api/quotes/{scope}/$get | Get quotes
*QuotesApi* | [**upsert_quotes**](lusid/docs/QuotesApi.md#upsert_quotes) | **POST** /api/quotes/{scope} | Upsert quotes
*ReconciliationsApi* | [**reconcile_holdings**](lusid/docs/ReconciliationsApi.md#reconcile_holdings) | **POST** /api/portfolios/$reconcileholdings | Reconcile portfolio holdings
*ReconciliationsApi* | [**reconcile_valuation**](lusid/docs/ReconciliationsApi.md#reconcile_valuation) | **POST** /api/portfolios/$reconcileValuation | Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
*ReferencePortfolioApi* | [**create_reference_portfolio**](lusid/docs/ReferencePortfolioApi.md#create_reference_portfolio) | **POST** /api/referenceportfolios/{scope} | Create reference portfolio
*ReferencePortfolioApi* | [**get_reference_portfolio_constituents**](lusid/docs/ReferencePortfolioApi.md#get_reference_portfolio_constituents) | **GET** /api/referenceportfolios/{scope}/{code}/constituents | Get constituents
*ReferencePortfolioApi* | [**list_constituents_adjustments**](lusid/docs/ReferencePortfolioApi.md#list_constituents_adjustments) | **GET** /api/referenceportfolios/{scope}/{code}/constituentsadjustments | Gets constituents adjustments in an interval of effective time.
*ReferencePortfolioApi* | [**upsert_reference_portfolio_constituents**](lusid/docs/ReferencePortfolioApi.md#upsert_reference_portfolio_constituents) | **POST** /api/referenceportfolios/{scope}/{code}/constituents | Add constituents
*ResultsApi* | [**get_results**](lusid/docs/ResultsApi.md#get_results) | **GET** /api/results/{scope}/{key}/{date} | Get results
*ResultsApi* | [**upsert_results**](lusid/docs/ResultsApi.md#upsert_results) | **POST** /api/results/{scope}/{key}/{date} | Upsert results
*SchemasApi* | [**get_entity_schema**](lusid/docs/SchemasApi.md#get_entity_schema) | **GET** /api/schemas/entities/{entity} | Get schema
*SchemasApi* | [**get_property_schema**](lusid/docs/SchemasApi.md#get_property_schema) | **GET** /api/schemas/properties | Get property schema
*SchemasApi* | [**get_value_types**](lusid/docs/SchemasApi.md#get_value_types) | **GET** /api/schemas/types | Get value types
*SchemasApi* | [**list_entities**](lusid/docs/SchemasApi.md#list_entities) | **GET** /api/schemas/entities | List entities
*ScopesApi* | [**list_scopes**](lusid/docs/ScopesApi.md#list_scopes) | **GET** /api/scopes | List scopes
*SearchApi* | [**instruments_search**](lusid/docs/SearchApi.md#instruments_search) | **POST** /api/search/instruments | Search instruments
*SearchApi* | [**portfolio_groups_search**](lusid/docs/SearchApi.md#portfolio_groups_search) | **POST** /api/search/portfoliogroups | Search portfolio groups
*SearchApi* | [**portfolios_search**](lusid/docs/SearchApi.md#portfolios_search) | **POST** /api/search/portfolios | Search portfolios
*SearchApi* | [**properties_search**](lusid/docs/SearchApi.md#properties_search) | **POST** /api/search/propertydefinitions | Search property definitions
*SystemConfigurationApi* | [**create_configuration_transaction_type**](lusid/docs/SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/systemconfiguration/transactiontypes | Create transaction type
*SystemConfigurationApi* | [**list_configuration_transaction_types**](lusid/docs/SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/systemconfiguration/transactiontypes | List transaction types
*SystemConfigurationApi* | [**set_configuration_transaction_types**](lusid/docs/SystemConfigurationApi.md#set_configuration_transaction_types) | **PUT** /api/systemconfiguration/transactiontypes | Set transaction types
*TransactionPortfoliosApi* | [**add_transaction_property**](lusid/docs/TransactionPortfoliosApi.md#add_transaction_property) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | Add transaction properties
*TransactionPortfoliosApi* | [**adjust_holdings**](lusid/docs/TransactionPortfoliosApi.md#adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt} | Adjust holdings
*TransactionPortfoliosApi* | [**build_transactions**](lusid/docs/TransactionPortfoliosApi.md#build_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$build | Build output transactions
*TransactionPortfoliosApi* | [**cancel_adjust_holdings**](lusid/docs/TransactionPortfoliosApi.md#cancel_adjust_holdings) | **DELETE** /api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt} | Cancel holdings adjustments
*TransactionPortfoliosApi* | [**create_portfolio**](lusid/docs/TransactionPortfoliosApi.md#create_portfolio) | **POST** /api/transactionportfolios/{scope} | Create transaction portfolio
*TransactionPortfoliosApi* | [**delete_executions**](lusid/docs/TransactionPortfoliosApi.md#delete_executions) | **DELETE** /api/transactionportfolios/{scope}/{code}/executions | Delete executions
*TransactionPortfoliosApi* | [**delete_property_from_transaction**](lusid/docs/TransactionPortfoliosApi.md#delete_property_from_transaction) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | Delete transaction property
*TransactionPortfoliosApi* | [**delete_transactions**](lusid/docs/TransactionPortfoliosApi.md#delete_transactions) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions | Delete transactions
*TransactionPortfoliosApi* | [**get_details**](lusid/docs/TransactionPortfoliosApi.md#get_details) | **GET** /api/transactionportfolios/{scope}/{code}/details | Get portfolio details
*TransactionPortfoliosApi* | [**get_holdings**](lusid/docs/TransactionPortfoliosApi.md#get_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings | Get holdings
*TransactionPortfoliosApi* | [**get_holdings_adjustment**](lusid/docs/TransactionPortfoliosApi.md#get_holdings_adjustment) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | Get holding adjustment
*TransactionPortfoliosApi* | [**get_transactions**](lusid/docs/TransactionPortfoliosApi.md#get_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions | Get transactions
*TransactionPortfoliosApi* | [**list_holdings_adjustments**](lusid/docs/TransactionPortfoliosApi.md#list_holdings_adjustments) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | List holdings adjustments
*TransactionPortfoliosApi* | [**set_holdings**](lusid/docs/TransactionPortfoliosApi.md#set_holdings) | **PUT** /api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt} | Set all holdings on a transaction portfolio
*TransactionPortfoliosApi* | [**upsert_executions**](lusid/docs/TransactionPortfoliosApi.md#upsert_executions) | **POST** /api/transactionportfolios/{scope}/{code}/executions | Upsert executions
*TransactionPortfoliosApi* | [**upsert_portfolio_details**](lusid/docs/TransactionPortfoliosApi.md#upsert_portfolio_details) | **POST** /api/transactionportfolios/{scope}/{code}/details | Upsert details
*TransactionPortfoliosApi* | [**upsert_transactions**](lusid/docs/TransactionPortfoliosApi.md#upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions | Upsert transactions into the specified transaction portfolio


## Documentation For Models

 - [AddTransactionPropertyResponse](lusid/docs/AddTransactionPropertyResponse.md)
 - [AdjustHolding](lusid/docs/AdjustHolding.md)
 - [AdjustHoldingRequest](lusid/docs/AdjustHoldingRequest.md)
 - [AggregateSpec](lusid/docs/AggregateSpec.md)
 - [AggregationContext](lusid/docs/AggregationContext.md)
 - [AggregationOptions](lusid/docs/AggregationOptions.md)
 - [AggregationRequest](lusid/docs/AggregationRequest.md)
 - [AggregationResponseNode](lusid/docs/AggregationResponseNode.md)
 - [AnalyticStore](lusid/docs/AnalyticStore.md)
 - [AnalyticStoreKey](lusid/docs/AnalyticStoreKey.md)
 - [CompletePortfolio](lusid/docs/CompletePortfolio.md)
 - [ConfigurationRecipe](lusid/docs/ConfigurationRecipe.md)
 - [ConstituentsAdjustmentHeader](lusid/docs/ConstituentsAdjustmentHeader.md)
 - [CorporateAction](lusid/docs/CorporateAction.md)
 - [CorporateActionSource](lusid/docs/CorporateActionSource.md)
 - [CorporateActionTransition](lusid/docs/CorporateActionTransition.md)
 - [CorporateActionTransitionComponent](lusid/docs/CorporateActionTransitionComponent.md)
 - [CorporateActionTransitionComponentRequest](lusid/docs/CorporateActionTransitionComponentRequest.md)
 - [CorporateActionTransitionRequest](lusid/docs/CorporateActionTransitionRequest.md)
 - [CreateAnalyticStoreRequest](lusid/docs/CreateAnalyticStoreRequest.md)
 - [CreateCorporateAction](lusid/docs/CreateCorporateAction.md)
 - [CreateCorporateActionSourceRequest](lusid/docs/CreateCorporateActionSourceRequest.md)
 - [CreateDataTypeRequest](lusid/docs/CreateDataTypeRequest.md)
 - [CreateDerivedTransactionPortfolioRequest](lusid/docs/CreateDerivedTransactionPortfolioRequest.md)
 - [CreatePortfolioDetails](lusid/docs/CreatePortfolioDetails.md)
 - [CreatePortfolioGroupRequest](lusid/docs/CreatePortfolioGroupRequest.md)
 - [CreatePropertyDefinitionRequest](lusid/docs/CreatePropertyDefinitionRequest.md)
 - [CreateReferencePortfolioRequest](lusid/docs/CreateReferencePortfolioRequest.md)
 - [CreateResults](lusid/docs/CreateResults.md)
 - [CreateTransactionPortfolioRequest](lusid/docs/CreateTransactionPortfolioRequest.md)
 - [CreateUnitDefinition](lusid/docs/CreateUnitDefinition.md)
 - [CurrencyAndAmount](lusid/docs/CurrencyAndAmount.md)
 - [DataType](lusid/docs/DataType.md)
 - [DeleteInstrumentPropertyRequest](lusid/docs/DeleteInstrumentPropertyRequest.md)
 - [DeleteInstrumentResponse](lusid/docs/DeleteInstrumentResponse.md)
 - [DeleteQuoteRequest](lusid/docs/DeleteQuoteRequest.md)
 - [DeleteQuotesResponse](lusid/docs/DeleteQuotesResponse.md)
 - [DeletedEntityResponse](lusid/docs/DeletedEntityResponse.md)
 - [ErrorDetail](lusid/docs/ErrorDetail.md)
 - [ErrorDetailBase](lusid/docs/ErrorDetailBase.md)
 - [ErrorResponse](lusid/docs/ErrorResponse.md)
 - [ExecutionRequest](lusid/docs/ExecutionRequest.md)
 - [ExpandedGroup](lusid/docs/ExpandedGroup.md)
 - [FieldSchema](lusid/docs/FieldSchema.md)
 - [FileResponse](lusid/docs/FileResponse.md)
 - [GetInstrumentsResponse](lusid/docs/GetInstrumentsResponse.md)
 - [GetQuotesResponse](lusid/docs/GetQuotesResponse.md)
 - [GetReferencePortfolioConstituentsResponse](lusid/docs/GetReferencePortfolioConstituentsResponse.md)
 - [HoldingAdjustment](lusid/docs/HoldingAdjustment.md)
 - [HoldingsAdjustment](lusid/docs/HoldingsAdjustment.md)
 - [HoldingsAdjustmentHeader](lusid/docs/HoldingsAdjustmentHeader.md)
 - [IUnitDefinitionDto](lusid/docs/IUnitDefinitionDto.md)
 - [Instrument](lusid/docs/Instrument.md)
 - [InstrumentAnalytic](lusid/docs/InstrumentAnalytic.md)
 - [InstrumentDefinition](lusid/docs/InstrumentDefinition.md)
 - [InstrumentEconomicDefinition](lusid/docs/InstrumentEconomicDefinition.md)
 - [InstrumentIdTypeDescriptor](lusid/docs/InstrumentIdTypeDescriptor.md)
 - [InstrumentIdValue](lusid/docs/InstrumentIdValue.md)
 - [InstrumentMatch](lusid/docs/InstrumentMatch.md)
 - [InstrumentProperty](lusid/docs/InstrumentProperty.md)
 - [InstrumentSearchProperty](lusid/docs/InstrumentSearchProperty.md)
 - [Link](lusid/docs/Link.md)
 - [ListAggregationResponse](lusid/docs/ListAggregationResponse.md)
 - [MarketContext](lusid/docs/MarketContext.md)
 - [MarketContextSuppliers](lusid/docs/MarketContextSuppliers.md)
 - [MarketDataKeyRule](lusid/docs/MarketDataKeyRule.md)
 - [MarketOptions](lusid/docs/MarketOptions.md)
 - [MetricValue](lusid/docs/MetricValue.md)
 - [ModelProperty](lusid/docs/ModelProperty.md)
 - [ModelSelection](lusid/docs/ModelSelection.md)
 - [NestedAggregationResponse](lusid/docs/NestedAggregationResponse.md)
 - [OutputTransaction](lusid/docs/OutputTransaction.md)
 - [PerpetualProperty](lusid/docs/PerpetualProperty.md)
 - [PerpetualPropertyValue](lusid/docs/PerpetualPropertyValue.md)
 - [Portfolio](lusid/docs/Portfolio.md)
 - [PortfolioDetails](lusid/docs/PortfolioDetails.md)
 - [PortfolioGroup](lusid/docs/PortfolioGroup.md)
 - [PortfolioHolding](lusid/docs/PortfolioHolding.md)
 - [PortfolioProperties](lusid/docs/PortfolioProperties.md)
 - [PortfolioReconciliationRequest](lusid/docs/PortfolioReconciliationRequest.md)
 - [PortfolioSearchResult](lusid/docs/PortfolioSearchResult.md)
 - [PortfoliosReconciliationRequest](lusid/docs/PortfoliosReconciliationRequest.md)
 - [PricingContext](lusid/docs/PricingContext.md)
 - [PricingOptions](lusid/docs/PricingOptions.md)
 - [ProcessedCommand](lusid/docs/ProcessedCommand.md)
 - [PropertyDefinition](lusid/docs/PropertyDefinition.md)
 - [PropertyFilter](lusid/docs/PropertyFilter.md)
 - [PropertySchema](lusid/docs/PropertySchema.md)
 - [PropertyValue](lusid/docs/PropertyValue.md)
 - [Quote](lusid/docs/Quote.md)
 - [QuoteId](lusid/docs/QuoteId.md)
 - [RealisedGainLoss](lusid/docs/RealisedGainLoss.md)
 - [ReconciliationBreak](lusid/docs/ReconciliationBreak.md)
 - [ReferencePortfolioConstituent](lusid/docs/ReferencePortfolioConstituent.md)
 - [ReferencePortfolioConstituentRequest](lusid/docs/ReferencePortfolioConstituentRequest.md)
 - [ResourceId](lusid/docs/ResourceId.md)
 - [ResourceListOfAnalyticStoreKey](lusid/docs/ResourceListOfAnalyticStoreKey.md)
 - [ResourceListOfConstituentsAdjustmentHeader](lusid/docs/ResourceListOfConstituentsAdjustmentHeader.md)
 - [ResourceListOfCorporateAction](lusid/docs/ResourceListOfCorporateAction.md)
 - [ResourceListOfCorporateActionSource](lusid/docs/ResourceListOfCorporateActionSource.md)
 - [ResourceListOfDataType](lusid/docs/ResourceListOfDataType.md)
 - [ResourceListOfHoldingsAdjustmentHeader](lusid/docs/ResourceListOfHoldingsAdjustmentHeader.md)
 - [ResourceListOfIUnitDefinitionDto](lusid/docs/ResourceListOfIUnitDefinitionDto.md)
 - [ResourceListOfInstrument](lusid/docs/ResourceListOfInstrument.md)
 - [ResourceListOfInstrumentIdTypeDescriptor](lusid/docs/ResourceListOfInstrumentIdTypeDescriptor.md)
 - [ResourceListOfPortfolio](lusid/docs/ResourceListOfPortfolio.md)
 - [ResourceListOfPortfolioGroup](lusid/docs/ResourceListOfPortfolioGroup.md)
 - [ResourceListOfPortfolioSearchResult](lusid/docs/ResourceListOfPortfolioSearchResult.md)
 - [ResourceListOfProcessedCommand](lusid/docs/ResourceListOfProcessedCommand.md)
 - [ResourceListOfPropertyDefinition](lusid/docs/ResourceListOfPropertyDefinition.md)
 - [ResourceListOfReconciliationBreak](lusid/docs/ResourceListOfReconciliationBreak.md)
 - [ResourceListOfScopeDefinition](lusid/docs/ResourceListOfScopeDefinition.md)
 - [ResourceListOfString](lusid/docs/ResourceListOfString.md)
 - [ResourceListOfTransactionConfigurationData](lusid/docs/ResourceListOfTransactionConfigurationData.md)
 - [ResourceListOfValueType](lusid/docs/ResourceListOfValueType.md)
 - [ResultDataSchema](lusid/docs/ResultDataSchema.md)
 - [Results](lusid/docs/Results.md)
 - [Schema](lusid/docs/Schema.md)
 - [ScopeDefinition](lusid/docs/ScopeDefinition.md)
 - [Stream](lusid/docs/Stream.md)
 - [TargetTaxLot](lusid/docs/TargetTaxLot.md)
 - [TargetTaxLotRequest](lusid/docs/TargetTaxLotRequest.md)
 - [Transaction](lusid/docs/Transaction.md)
 - [TransactionConfigurationData](lusid/docs/TransactionConfigurationData.md)
 - [TransactionConfigurationDataRequest](lusid/docs/TransactionConfigurationDataRequest.md)
 - [TransactionConfigurationMovementData](lusid/docs/TransactionConfigurationMovementData.md)
 - [TransactionConfigurationMovementDataRequest](lusid/docs/TransactionConfigurationMovementDataRequest.md)
 - [TransactionConfigurationTypeAlias](lusid/docs/TransactionConfigurationTypeAlias.md)
 - [TransactionPrice](lusid/docs/TransactionPrice.md)
 - [TransactionPropertyMapping](lusid/docs/TransactionPropertyMapping.md)
 - [TransactionPropertyMappingRequest](lusid/docs/TransactionPropertyMappingRequest.md)
 - [TransactionQueryParameters](lusid/docs/TransactionQueryParameters.md)
 - [TransactionRequest](lusid/docs/TransactionRequest.md)
 - [UpdateDataTypeRequest](lusid/docs/UpdateDataTypeRequest.md)
 - [UpdateInstrumentIdentifierRequest](lusid/docs/UpdateInstrumentIdentifierRequest.md)
 - [UpdatePortfolioGroupRequest](lusid/docs/UpdatePortfolioGroupRequest.md)
 - [UpdatePortfolioRequest](lusid/docs/UpdatePortfolioRequest.md)
 - [UpdatePropertyDefinitionRequest](lusid/docs/UpdatePropertyDefinitionRequest.md)
 - [UpsertCorporateActionsResponse](lusid/docs/UpsertCorporateActionsResponse.md)
 - [UpsertInstrumentPropertiesResponse](lusid/docs/UpsertInstrumentPropertiesResponse.md)
 - [UpsertInstrumentPropertyRequest](lusid/docs/UpsertInstrumentPropertyRequest.md)
 - [UpsertInstrumentsResponse](lusid/docs/UpsertInstrumentsResponse.md)
 - [UpsertPortfolioExecutionsResponse](lusid/docs/UpsertPortfolioExecutionsResponse.md)
 - [UpsertPortfolioTransactionsResponse](lusid/docs/UpsertPortfolioTransactionsResponse.md)
 - [UpsertQuoteRequest](lusid/docs/UpsertQuoteRequest.md)
 - [UpsertQuotesResponse](lusid/docs/UpsertQuotesResponse.md)
 - [UpsertReferencePortfolioConstituentsRequest](lusid/docs/UpsertReferencePortfolioConstituentsRequest.md)
 - [UpsertReferencePortfolioConstituentsResponse](lusid/docs/UpsertReferencePortfolioConstituentsResponse.md)
 - [User](lusid/docs/User.md)
 - [ValuationReconciliationRequest](lusid/docs/ValuationReconciliationRequest.md)
 - [ValuationsReconciliationRequest](lusid/docs/ValuationsReconciliationRequest.md)
 - [VendorModelRule](lusid/docs/VendorModelRule.md)
 - [Version](lusid/docs/Version.md)
 - [VersionSummaryDto](lusid/docs/VersionSummaryDto.md)
 - [VersionedResourceListOfOutputTransaction](lusid/docs/VersionedResourceListOfOutputTransaction.md)
 - [VersionedResourceListOfPortfolioHolding](lusid/docs/VersionedResourceListOfPortfolioHolding.md)
 - [VersionedResourceListOfTransaction](lusid/docs/VersionedResourceListOfTransaction.md)


## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://lusid.okta.com/oauth2/aus5a0xgh5ZSUqwkN2p6/v1/authorize
- **Scopes**: N/A


## Author

info@finbourne.com


