# coding: utf-8

"""
    LUSID API

    # Introduction  This page documents the [LUSID APIs](https://api.lusid.com/swagger), which allows authorised clients to query and update their data within the LUSID platform.  SDKs to interact with the LUSID APIs are available in the following languages :  * [C#](https://github.com/finbourne/lusid-sdk-csharp) * [Java](https://github.com/finbourne/lusid-sdk-java) * [JavaScript](https://github.com/finbourne/lusid-sdk-js) * [Python](https://github.com/finbourne/lusid-sdk-python)  # Data Model  The LUSID API has a relatively lightweight but extremely powerful data model. One of the goals of LUSID was not to enforce on clients a single rigid data model but rather to provide a flexible foundation onto which clients can map their own data models.  The core entities in LUSID provide a minimal structure and set of relationships, and the data model can be extended using Properties.  The LUSID data model is exposed through the LUSID APIs.  The APIs provide access to both business objects and the meta data used to configure the systems behaviours.   The key business entities are: - * **Portfolios** A portfolio is a container for transactions and holdings (a **Transaction Portfolio**) or constituents (a **Reference Portfolio**). * **Derived Portfolios**. Derived Portfolios allow Portfolios to be created based on other Portfolios, by overriding or adding specific items. * **Holdings** A Holding is a quantity of an Instrument or a balance of cash within a Portfolio.  Holdings can only be adjusted via Transactions. * **Transactions** A Transaction is an economic event that occurs in a Portfolio, causing its holdings to change. * **Corporate Actions** A corporate action is a market event which occurs to an Instrument and thus applies to all portfolios which holding the instrument.  Examples are stock splits or mergers. * **Constituents** A constituent is a record in a Reference Portfolio containing an Instrument and an associated weight. * **Instruments**  An instrument represents a currency, tradable instrument or OTC contract that is attached to a transaction and a holding. * **Properties** All major entities allow additional user defined properties to be associated with them.   For example, a Portfolio manager may be associated with a portfolio.  Meta data includes: - * **Transaction Types** Transactions are booked with a specific transaction type.  The types are client defined and are used to map the Transaction to a series of movements which update the portfolio holdings.  * **Properties Types** Types of user defined properties used within the system.  ## Scope  All data in LUSID is segregated at the client level.  Entities in LUSID are identifiable by a unique code.  Every entity lives within a logical data partition known as a Scope.  Scope is an identity namespace allowing two entities with the same unique code to co-exist within individual address spaces.  For example, prices for equities from different vendors may be uploaded into different scopes such as `client/vendor1` and `client/vendor2`.  A portfolio may then be valued using either of the price sources by referencing the appropriate scope.  LUSID Clients cannot access scopes of other clients.  ## Instruments  LUSID has its own built-in instrument master which you can use to master your own instrument universe.  Every instrument must be created with one or more unique market identifiers, such as [FIGI](https://openfigi.com/). For any non-listed instruments (eg OTCs), you can upload an instrument against a custom ID of your choosing.  In addition, LUSID will allocate each instrument a unique 'LUSID instrument identifier'. The LUSID instrument identifier is what is used when uploading transactions, holdings, prices, etc. The API exposes an `instrument/lookup` endpoint which can be used to lookup these LUSID identifiers using their market identifiers.  Cash can be referenced using the ISO currency code prefixed with \"`CCY_`\" e.g. `CCY_GBP`  ## Instrument Data  Instrument data can be uploaded to the system using the [Instrument Properties](#tag/InstrumentProperties) endpoint.  | Field|Type|Description | | ---|---|--- | | Key|propertykey|The key of the property. This takes the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or 'Transaction/strategy/quantsignal'. | | Value|string|The value of the property. | | EffectiveFrom|datetimeoffset|The effective datetime from which the property is valid. |   ## Transaction Portfolios  Portfolios are the top-level entity containers within LUSID, containing transactions, corporate actions and holdings.    The transactions build up the portfolio holdings on which valuations, analytics profit & loss and risk can be calculated.  Properties can be associated with Portfolios to add in additional data.  Portfolio properties can be changed over time, for example to allow a Portfolio Manager to be linked with a Portfolio.  Additionally, portfolios can be securitised and held by other portfolios, allowing LUSID to perform \"drill-through\" into underlying fund holdings  ### Derived Portfolios  LUSID also allows for a portfolio to be composed of another portfolio via derived portfolios.  A derived portfolio can contain its own transactions and also inherits any transactions from its parent portfolio.  Any changes made to the parent portfolio are automatically reflected in derived portfolio.  Derived portfolios in conjunction with scopes are a powerful construct.  For example, to do pre-trade what-if analysis, a derived portfolio could be created a new namespace linked to the underlying live (parent) portfolio.  Analysis can then be undertaken on the derived portfolio without affecting the live portfolio.  ### Transactions  A transaction represents an economic activity against a Portfolio.  Transactions are processed according to a configuration. This will tell the LUSID engine how to interpret the transaction and correctly update the holdings. LUSID comes with a set of transaction types you can use out of the box, or you can configure your own set(s) of transactions.  For more details see the [LUSID Getting Started Guide for transaction configuration.](https://support.lusid.com/configuring-transaction-types)  | Field|Type|Description | | ---|---|--- | | TransactionId|string|The unique identifier for the transaction. | | Type|string|The type of the transaction e.g. 'Buy', 'Sell'. The transaction type should have been pre-configured via the System Configuration API endpoint. If it hasn't been pre-configured the transaction will still be updated or inserted however you will be unable to generate the resultant holdings for the portfolio that contains this transaction as LUSID does not know how to process it. | | InstrumentIdentifiers|map|A set of instrument identifiers to use to resolve the transaction to a unique instrument. | | TransactionDate|dateorcutlabel|The date of the transaction. | | SettlementDate|dateorcutlabel|The settlement date of the transaction. | | Units|decimal|The number of units transacted in the associated instrument. | | TransactionPrice|transactionprice|The price for each unit of the transacted instrument in the transaction currency. | | TotalConsideration|currencyandamount|The total value of the transaction in the settlement currency. | | ExchangeRate|decimal|The exchange rate between the transaction and settlement currency. For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. | | TransactionCurrency|currency|The transaction currency. | | Properties|map|Set of unique transaction properties and associated values to store with the transaction. Each property must be from the 'Transaction' domain. | | CounterpartyId|string|The identifier for the counterparty of the transaction. | | Source|string|The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. |   From these fields, the following values can be calculated  * **Transaction value in Transaction currency**: TotalConsideration / ExchangeRate  * **Transaction value in Portfolio currency**: Transaction value in Transaction currency * TradeToPortfolioRate  #### Example Transactions  ##### A Common Purchase Example Three example transactions are shown in the table below.   They represent a purchase of USD denominated IBM shares within a Sterling denominated portfolio.   * The first two transactions are for separate buy and fx trades    * Buying 500 IBM shares for $71,480.00    * A foreign exchange conversion to fund the IBM purchase. (Buy $71,480.00 for &#163;54,846.60)  * The third transaction is an alternate version of the above trades. Buying 500 IBM shares and settling directly in Sterling.  | Column |  Buy Trade | Fx Trade | Buy Trade with foreign Settlement | | ----- | ----- | ----- | ----- | | TransactionId | FBN00001 | FBN00002 | FBN00003 | | Type | Buy | FxBuy | Buy | | InstrumentIdentifiers | { \"figi\", \"BBG000BLNNH6\" } | { \"CCY\", \"CCY_USD\" } | { \"figi\", \"BBG000BLNNH6\" } | | TransactionDate | 2018-08-02 | 2018-08-02 | 2018-08-02 | | SettlementDate | 2018-08-06 | 2018-08-06 | 2018-08-06 | | Units | 500 | 71480 | 500 | | TransactionPrice | 142.96 | 1 | 142.96 | | TradeCurrency | USD | USD | USD | | ExchangeRate | 1 | 0.7673 | 0.7673 | | TotalConsideration.Amount | 71480.00 | 54846.60 | 54846.60 | | TotalConsideration.Currency | USD | GBP | GBP | | Trade/default/TradeToPortfolioRate&ast; | 0.7673 | 0.7673 | 0.7673 |  [&ast; This is a property field]  ##### A Forward FX Example  LUSID has a flexible transaction modelling system, and there are a number of different ways of modelling forward fx trades.  The default LUSID transaction types are FwdFxBuy and FwdFxSell. Other types and behaviours can be configured as required.  Using these transaction types, the holdings query will report two forward positions. One in each currency.   Since an FX trade is an exchange of one currency for another, the following two 6 month forward transactions are equivalent:  | Column |  Forward 'Sell' Trade | Forward 'Buy' Trade | | ----- | ----- | ----- | | TransactionId | FBN00004 | FBN00005 | | Type | FwdFxSell | FwdFxBuy | | InstrumentIdentifiers | { \"CCY\", \"CCY_GBP\" } | { \"CCY\", \"CCY_USD\" } | | TransactionDate | 2018-08-02 | 2018-08-02 | | SettlementDate | 2019-02-06 | 2019-02-06 | | Units | 10000.00 | 13142.00 | | TransactionPrice |1 | 1 | | TradeCurrency | GBP | USD | | ExchangeRate | 1.3142 | 0.760919 | | TotalConsideration.Amount | 13142.00 | 10000.00 | | TotalConsideration.Currency | USD | GBP | | Trade/default/TradeToPortfolioRate | 1.0 | 0.760919 |  ### Holdings  A holding represents a position in an instrument or cash on a given date.  | Field|Type|Description | | ---|---|--- | | InstrumentUid|string|The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in. | | SubHoldingKeys|map|The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created. | | Properties|map|The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' or 'Holding' domain. | | HoldingType|string|The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | | Units|decimal|The total number of units of the holding. | | SettledUnits|decimal|The total number of settled units of the holding. | | Cost|currencyandamount|The total cost of the holding in the transaction currency. | | CostPortfolioCcy|currencyandamount|The total cost of the holding in the portfolio currency. | | Transaction|transaction|The transaction associated with an unsettled holding. |   ## Corporate Actions  Corporate actions are represented within LUSID in terms of a set of instrument-specific 'transitions'.  These transitions are used to specify the participants of the corporate action, and the effect that the corporate action will have on holdings in those participants.  ### Corporate Action  | Field|Type|Description | | ---|---|--- | | CorporateActionCode|code|The unique identifier of this corporate action | | Description|string|  | | AnnouncementDate|datetimeoffset|The announcement date of the corporate action | | ExDate|datetimeoffset|The ex date of the corporate action | | RecordDate|datetimeoffset|The record date of the corporate action | | PaymentDate|datetimeoffset|The payment date of the corporate action | | Transitions|corporateactiontransition[]|The transitions that result from this corporate action |   ### Transition | Field|Type|Description | | ---|---|--- | | InputTransition|corporateactiontransitioncomponent|Indicating the basis of the corporate action - which security and how many units | | OutputTransitions|corporateactiontransitioncomponent[]|What will be generated relative to the input transition |   ### Example Corporate Action Transitions  #### A Dividend Action Transition  In this example, for each share of IBM, 0.20 units (or 20 pence) of GBP are generated.  | Column |  Input Transition | Output Transition | | ----- | ----- | ----- | | Instrument Identifiers | { \"figi\" : \"BBG000BLNNH6\" } | { \"ccy\" : \"CCY_GBP\" } | | Units Factor | 1 | 0.20 | | Cost Factor | 1 | 0 |  #### A Split Action Transition  In this example, for each share of IBM, we end up with 2 units (2 shares) of IBM, with total value unchanged.  | Column |  Input Transition | Output Transition | | ----- | ----- | ----- | | Instrument Identifiers | { \"figi\" : \"BBG000BLNNH6\" } | { \"figi\" : \"BBG000BLNNH6\" } | | Units Factor | 1 | 2 | | Cost Factor | 1 | 1 |  #### A Spinoff Action Transition  In this example, for each share of IBM, we end up with 1 unit (1 share) of IBM and 3 units (3 shares) of Celestica, with 85% of the value remaining on the IBM share, and 5% in each Celestica share (15% total).  | Column |  Input Transition | Output Transition 1 | Output Transition 2 | | ----- | ----- | ----- | ----- | | Instrument Identifiers | { \"figi\" : \"BBG000BLNNH6\" } | { \"figi\" : \"BBG000BLNNH6\" } | { \"figi\" : \"BBG000HBGRF3\" } | | Units Factor | 1 | 1 | 3 | | Cost Factor | 1 | 0.85 | 0.15 |  ## Reference Portfolios Reference portfolios are portfolios that contain constituents with weights.  They are designed to represent entities such as indices and benchmarks.  ### Constituents | Field|Type|Description | | ---|---|--- | | InstrumentIdentifiers|map|Unique instrument identifiers | | InstrumentUid|string|LUSID's internal unique instrument identifier, resolved from the instrument identifiers | | Currency|decimal|  | | Weight|decimal|  | | FloatingWeight|decimal|  |   ## Portfolio Groups Portfolio groups allow the construction of a hierarchy from portfolios and groups.  Portfolio operations on the group are executed on an aggregated set of portfolios in the hierarchy.   For example:   * Global Portfolios _(group)_   * APAC _(group)_     * Hong Kong _(portfolio)_     * Japan _(portfolio)_   * Europe _(group)_     * France _(portfolio)_     * Germany _(portfolio)_   * UK _(portfolio)_   In this example **Global Portfolios** is a group that consists of an aggregate of **Hong Kong**, **Japan**, **France**, **Germany** and **UK** portfolios.  ## Properties  Properties are key-value pairs that can be applied to any entity within a domain (where a domain is `trade`, `portfolio`, `security` etc).  Properties must be defined before use with a `PropertyDefinition` and can then subsequently be added to entities.   ## Schema  A detailed description of the entities used by the API and parameters for endpoints which take a JSON document can be retrieved via the `schema` endpoint.  ## Meta data  The following headers are returned on all responses from LUSID  | Name | Purpose | | --- | --- | | lusid-meta-duration | Duration of the request | | lusid-meta-success | Whether or not LUSID considered the request to be successful | | lusid-meta-requestId | The unique identifier for the request | | lusid-schema-url | Url of the schema for the data being returned | | lusid-property-schema-url | Url of the schema for any properties |   # Error Codes  | Code|Name|Description | | ---|---|--- | | <a name=\"102\">102</a>|VersionNotFound|  | | <a name=\"103\">103</a>|ApiRateLimitViolation|  | | <a name=\"104\">104</a>|InstrumentNotFound|  | | <a name=\"105\">105</a>|PropertyNotFound|  | | <a name=\"106\">106</a>|PortfolioRecursionDepth|  | | <a name=\"108\">108</a>|GroupNotFound|  | | <a name=\"109\">109</a>|PortfolioNotFound|  | | <a name=\"110\">110</a>|PropertySchemaNotFound|  | | <a name=\"111\">111</a>|PortfolioAncestryNotFound|  | | <a name=\"112\">112</a>|PortfolioWithIdAlreadyExists|  | | <a name=\"113\">113</a>|OrphanedPortfolio|  | | <a name=\"119\">119</a>|MissingBaseClaims|  | | <a name=\"121\">121</a>|PropertyNotDefined|  | | <a name=\"122\">122</a>|CannotDeleteSystemProperty|  | | <a name=\"123\">123</a>|CannotModifyImmutablePropertyField|  | | <a name=\"124\">124</a>|PropertyAlreadyExists|  | | <a name=\"125\">125</a>|PropertyConstraintStyleExcludesPropertiesFailure|  | | <a name=\"125\">125</a>|PropertyConstraintStyleExcludesPropertiesFailure|  | | <a name=\"127\">127</a>|CannotModifyDefaultDataType|  | | <a name=\"128\">128</a>|GroupAlreadyExists|  | | <a name=\"129\">129</a>|NoSuchDataType|  | | <a name=\"130\">130</a>|UndefinedValueForDataType|  | | <a name=\"131\">131</a>|UnsupportedValueTypeDefinedOnDataType|  | | <a name=\"132\">132</a>|ValidationError|  | | <a name=\"133\">133</a>|LoopDetectedInGroupHierarchy|  | | <a name=\"134\">134</a>|UndefinedAcceptableValues|  | | <a name=\"135\">135</a>|SubGroupAlreadyExists|  | | <a name=\"138\">138</a>|PriceSourceNotFound|  | | <a name=\"139\">139</a>|AnalyticStoreNotFound|  | | <a name=\"141\">141</a>|AnalyticStoreAlreadyExists|  | | <a name=\"143\">143</a>|ClientInstrumentAlreadyExists|  | | <a name=\"144\">144</a>|DuplicateInParameterSet|  | | <a name=\"147\">147</a>|ResultsNotFound|  | | <a name=\"148\">148</a>|OrderFieldNotInResultSet|  | | <a name=\"149\">149</a>|OperationFailed|  | | <a name=\"150\">150</a>|ElasticSearchError|  | | <a name=\"151\">151</a>|InvalidParameterValue|  | | <a name=\"153\">153</a>|CommandProcessingFailure|  | | <a name=\"154\">154</a>|EntityStateConstructionFailure|  | | <a name=\"155\">155</a>|EntityTimelineDoesNotExist|  | | <a name=\"156\">156</a>|EventPublishFailure|  | | <a name=\"157\">157</a>|InvalidRequestFailure|  | | <a name=\"158\">158</a>|EventPublishUnknown|  | | <a name=\"159\">159</a>|EventQueryFailure|  | | <a name=\"160\">160</a>|BlobDidNotExistFailure|  | | <a name=\"162\">162</a>|SubSystemRequestFailure|  | | <a name=\"163\">163</a>|SubSystemConfigurationFailure|  | | <a name=\"165\">165</a>|FailedToDelete|  | | <a name=\"166\">166</a>|UpsertClientInstrumentFailure|  | | <a name=\"167\">167</a>|IllegalAsAtInterval|  | | <a name=\"168\">168</a>|IllegalBitemporalQuery|  | | <a name=\"169\">169</a>|InvalidAlternateId|  | | <a name=\"170\">170</a>|CannotAddSourcePortfolioPropertyExplicitly|  | | <a name=\"171\">171</a>|EntityAlreadyExistsInGroup|  | | <a name=\"173\">173</a>|EntityWithIdAlreadyExists|  | | <a name=\"174\">174</a>|DerivedPortfolioDetailsDoNotExist|  | | <a name=\"176\">176</a>|PortfolioWithNameAlreadyExists|  | | <a name=\"177\">177</a>|InvalidTransactions|  | | <a name=\"178\">178</a>|ReferencePortfolioNotFound|  | | <a name=\"179\">179</a>|DuplicateIdFailure|  | | <a name=\"180\">180</a>|CommandRetrievalFailure|  | | <a name=\"181\">181</a>|DataFilterApplicationFailure|  | | <a name=\"182\">182</a>|SearchFailed|  | | <a name=\"183\">183</a>|MovementsEngineConfigurationKeyFailure|  | | <a name=\"184\">184</a>|FxRateSourceNotFound|  | | <a name=\"185\">185</a>|AccrualSourceNotFound|  | | <a name=\"186\">186</a>|AccessDenied|  | | <a name=\"187\">187</a>|InvalidIdentityToken|  | | <a name=\"188\">188</a>|InvalidRequestHeaders|  | | <a name=\"189\">189</a>|PriceNotFound|  | | <a name=\"190\">190</a>|InvalidSubHoldingKeysProvided|  | | <a name=\"191\">191</a>|DuplicateSubHoldingKeysProvided|  | | <a name=\"192\">192</a>|CutDefinitionNotFound|  | | <a name=\"193\">193</a>|CutDefinitionInvalid|  | | <a name=\"194\">194</a>|TimeVariantPropertyDeletionDateUnspecified|  | | <a name=\"195\">195</a>|PerpetualPropertyDeletionDateSpecified|  | | <a name=\"196\">196</a>|TimeVariantPropertyUpsertDateUnspecified|  | | <a name=\"197\">197</a>|PerpetualPropertyUpsertDateSpecified|  | | <a name=\"200\">200</a>|InvalidUnitForDataType|  | | <a name=\"201\">201</a>|InvalidTypeForDataType|  | | <a name=\"202\">202</a>|InvalidValueForDataType|  | | <a name=\"203\">203</a>|UnitNotDefinedForDataType|  | | <a name=\"204\">204</a>|UnitsNotSupportedOnDataType|  | | <a name=\"205\">205</a>|CannotSpecifyUnitsOnDataType|  | | <a name=\"206\">206</a>|UnitSchemaInconsistentWithDataType|  | | <a name=\"207\">207</a>|UnitDefinitionNotSpecified|  | | <a name=\"208\">208</a>|DuplicateUnitDefinitionsSpecified|  | | <a name=\"209\">209</a>|InvalidUnitsDefinition|  | | <a name=\"210\">210</a>|InvalidInstrumentIdentifierUnit|  | | <a name=\"211\">211</a>|HoldingsAdjustmentDoesNotExist|  | | <a name=\"212\">212</a>|CouldNotBuildExcelUrl|  | | <a name=\"213\">213</a>|CouldNotGetExcelVersion|  | | <a name=\"214\">214</a>|InstrumentByCodeNotFound|  | | <a name=\"215\">215</a>|EntitySchemaDoesNotExist|  | | <a name=\"216\">216</a>|FeatureNotSupportedOnPortfolioType|  | | <a name=\"217\">217</a>|QuoteNotFoundFailure|  | | <a name=\"218\">218</a>|InvalidQuoteIdentifierFailure|  | | <a name=\"219\">219</a>|InvalidInstrumentDefinition|  | | <a name=\"219\">219</a>|InvalidInstrumentDefinition|  | | <a name=\"221\">221</a>|InstrumentUpsertFailure|  | | <a name=\"222\">222</a>|ReferencePortfolioRequestNotSupported|  | | <a name=\"223\">223</a>|TransactionPortfolioRequestNotSupported|  | | <a name=\"224\">224</a>|InvalidPropertyValueAssignment|  | | <a name=\"230\">230</a>|TransactionTypeNotFound|  | | <a name=\"231\">231</a>|TransactionTypeDuplication|  | | <a name=\"232\">232</a>|PortfolioDoesNotExistAtGivenDate|  | | <a name=\"233\">233</a>|QueryParserFailure|  | | <a name=\"234\">234</a>|DuplicateConstituentFailure|  | | <a name=\"235\">235</a>|UnresolvedInstrumentConstituentFailure|  | | <a name=\"236\">236</a>|UnresolvedInstrumentInTransitionFailure|  | | <a name=\"237\">237</a>|MissingSideDefinitionsFailure|  | | <a name=\"300\">300</a>|MissingRecipeFailure|  | | <a name=\"301\">301</a>|DependenciesFailure|  | | <a name=\"304\">304</a>|PortfolioPreprocessFailure|  | | <a name=\"310\">310</a>|ValuationEngineFailure|  | | <a name=\"311\">311</a>|TaskFactoryFailure|  | | <a name=\"312\">312</a>|TaskEvaluationFailure|  | | <a name=\"313\">313</a>|TaskGenerationFailure|  | | <a name=\"320\">320</a>|MarketDataKeyFailure|  | | <a name=\"321\">321</a>|MarketResolverFailure|  | | <a name=\"322\">322</a>|MarketDataFailure|  | | <a name=\"330\">330</a>|CurveFailure|  | | <a name=\"350\">350</a>|InstrumentFailure|  | | <a name=\"351\">351</a>|CashFlowsFailure|  | | <a name=\"360\">360</a>|AggregationFailure|  | | <a name=\"370\">370</a>|ResultRetrievalFailure|  | | <a name=\"371\">371</a>|VendorPricingFailure|  | | <a name=\"371\">371</a>|VendorPricingFailure|  | | <a name=\"372\">372</a>|VendorResultProcessingFailure|  | | <a name=\"373\">373</a>|VendorResultMappingFailure|  | | <a name=\"374\">374</a>|VendorLibraryUnauthorisedFailure|  | | <a name=\"375\">375</a>|VendorConnectivityError|  | | <a name=\"376\">376</a>|VendorInterfaceError|  | | <a name=\"390\">390</a>|AttemptToUpsertDuplicateQuotes|  | | <a name=\"391\">391</a>|CorporateActionSourceDoesNotExist|  | | <a name=\"392\">392</a>|CorporateActionSourceAlreadyExists|  | | <a name=\"393\">393</a>|InstrumentIdentifierAlreadyInUse|  | | <a name=\"394\">394</a>|PropertiesNotFound|  | | <a name=\"395\">395</a>|BatchOperationAborted|  | | <a name=\"400\">400</a>|InvalidIso4217CurrencyCodeFailure|  | | <a name=\"401\">401</a>|CannotAssignInstrumentIdentifierToCurrencyFailure|  | | <a name=\"402\">402</a>|CannotAssignCurrencyIdentifierToNonCurrency|  | | <a name=\"403\">403</a>|CurrencyInstrumentCannotBeDeleted|  | | <a name=\"404\">404</a>|CurrencyInstrumentCannotHaveEconomicDefinition|  | | <a name=\"405\">405</a>|CurrencyInstrumentCannotHaveLookthroughPortfolio|  | | <a name=\"406\">406</a>|CannotCreateCurrencyInstrumentWithMultipleIdentifiers|  | | <a name=\"410\">410</a>|IndexDoesNotExist|  | | <a name=\"411\">411</a>|SortFieldDoesNotExist|  | | <a name=\"413\">413</a>|NegativePaginationParameters|  | | <a name=\"414\">414</a>|InvalidSearchSyntax|  | | <a name=\"420\">420</a>|SideDefinitionInconsistent|  | | <a name=\"450\">450</a>|InvalidQuoteAccessMetadataRule|  | | <a name=\"451\">451</a>|AccessMetadataNotFound|  | | <a name=\"601\">601</a>|PersonIdentifierAlreadyInUse|  | | <a name=\"602\">602</a>|PersonNotFound|  | | <a name=\"603\">603</a>|CannotSetIdentifier|  | | <a name=\"-10\">-10</a>|ServerConfigurationError|  | | <a name=\"-1\">-1</a>|Unknown error|  |   # noqa: E501

    The version of the OpenAPI document: 0.10.959
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ResourceListOfInstrumentIdTypeDescriptor(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'values': 'list[InstrumentIdTypeDescriptor]',
        'href': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'values': 'values',
        'href': 'href',
        'links': 'links'
    }

    required_map = {
        'values': 'required',
        'href': 'optional',
        'links': 'optional'
    }

    def __init__(self, values=None, href=None, links=None):  # noqa: E501
        """
        ResourceListOfInstrumentIdTypeDescriptor - a model defined in OpenAPI

        :param values:  (required)
        :type values: list[lusid.InstrumentIdTypeDescriptor]
        :param href: 
        :type href: str
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._values = None
        self._href = None
        self._links = None
        self.discriminator = None

        self.values = values
        if href is not None:
            self.href = href
        if links is not None:
            self.links = links

    @property
    def values(self):
        """Gets the values of this ResourceListOfInstrumentIdTypeDescriptor.  # noqa: E501


        :return: The values of this ResourceListOfInstrumentIdTypeDescriptor.  # noqa: E501
        :rtype: list[InstrumentIdTypeDescriptor]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ResourceListOfInstrumentIdTypeDescriptor.


        :param values: The values of this ResourceListOfInstrumentIdTypeDescriptor.  # noqa: E501
        :type: list[InstrumentIdTypeDescriptor]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def href(self):
        """Gets the href of this ResourceListOfInstrumentIdTypeDescriptor.  # noqa: E501


        :return: The href of this ResourceListOfInstrumentIdTypeDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ResourceListOfInstrumentIdTypeDescriptor.


        :param href: The href of this ResourceListOfInstrumentIdTypeDescriptor.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def links(self):
        """Gets the links of this ResourceListOfInstrumentIdTypeDescriptor.  # noqa: E501


        :return: The links of this ResourceListOfInstrumentIdTypeDescriptor.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResourceListOfInstrumentIdTypeDescriptor.


        :param links: The links of this ResourceListOfInstrumentIdTypeDescriptor.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceListOfInstrumentIdTypeDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
