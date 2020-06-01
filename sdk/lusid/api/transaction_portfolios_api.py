# coding: utf-8

"""
    LUSID API

    # Introduction  This page documents the [LUSID APIs](https://www.lusid.com/api/swagger), which allows authorised clients to query and update their data within the LUSID platform.  SDKs to interact with the LUSID APIs are available in the following languages :  * [C#](https://github.com/finbourne/lusid-sdk-csharp) * [Java](https://github.com/finbourne/lusid-sdk-java) * [JavaScript](https://github.com/finbourne/lusid-sdk-js) * [Python](https://github.com/finbourne/lusid-sdk-python)  # Data Model  The LUSID API has a relatively lightweight but extremely powerful data model. One of the goals of LUSID was not to enforce on clients a single rigid data model but rather to provide a flexible foundation onto which clients can map their own data models.  The core entities in LUSID provide a minimal structure and set of relationships, and the data model can be extended using Properties.  The LUSID data model is exposed through the LUSID APIs.  The APIs provide access to both business objects and the meta data used to configure the systems behaviours.   The key business entities are: - * **Portfolios** A portfolio is a container for transactions and holdings (a **Transaction Portfolio**) or constituents (a **Reference Portfolio**). * **Derived Portfolios**. Derived Portfolios allow Portfolios to be created based on other Portfolios, by overriding or adding specific items. * **Holdings** A Holding is a quantity of an Instrument or a balance of cash within a Portfolio.  Holdings can only be adjusted via Transactions. * **Transactions** A Transaction is an economic event that occurs in a Portfolio, causing its holdings to change. * **Corporate Actions** A corporate action is a market event which occurs to an Instrument and thus applies to all portfolios which holding the instrument.  Examples are stock splits or mergers. * **Constituents** A constituent is a record in a Reference Portfolio containing an Instrument and an associated weight. * **Instruments**  An instrument represents a currency, tradable instrument or OTC contract that is attached to a transaction and a holding. * **Properties** All major entities allow additional user defined properties to be associated with them.   For example, a Portfolio manager may be associated with a portfolio.  Meta data includes: - * **Transaction Types** Transactions are booked with a specific transaction type.  The types are client defined and are used to map the Transaction to a series of movements which update the portfolio holdings.  * **Properties Types** Types of user defined properties used within the system.  ## Scope  All data in LUSID is segregated at the client level.  Entities in LUSID are identifiable by a unique code.  Every entity lives within a logical data partition known as a Scope.  Scope is an identity namespace allowing two entities with the same unique code to co-exist within individual address spaces.  For example, prices for equities from different vendors may be uploaded into different scopes such as `client/vendor1` and `client/vendor2`.  A portfolio may then be valued using either of the price sources by referencing the appropriate scope.  LUSID Clients cannot access scopes of other clients.  ## Instruments  LUSID has its own built-in instrument master which you can use to master your own instrument universe.  Every instrument must be created with one or more unique market identifiers, such as [FIGI](https://openfigi.com/). For any non-listed instruments (eg OTCs), you can upload an instrument against a custom ID of your choosing.  In addition, LUSID will allocate each instrument a unique 'LUSID instrument identifier'. The LUSID instrument identifier is what is used when uploading transactions, holdings, prices, etc. The API exposes an `instrument/lookup` endpoint which can be used to lookup these LUSID identifiers using their market identifiers.  Cash can be referenced using the ISO currency code prefixed with \"`CCY_`\" e.g. `CCY_GBP`  ## Instrument Data  Instrument data can be uploaded to the system using the [Instrument Properties](#tag/InstrumentProperties) endpoint.  | Field|Type|Description | | ---|---|--- | | Key|propertykey|The key of the property. This takes the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or 'Transaction/strategy/quantsignal'. | | Value|string|The value of the property. | | EffectiveFrom|datetimeoffset|The effective datetime from which the property is valid. |   ## Transaction Portfolios  Portfolios are the top-level entity containers within LUSID, containing transactions, corporate actions and holdings.    The transactions build up the portfolio holdings on which valuations, analytics profit & loss and risk can be calculated.  Properties can be associated with Portfolios to add in additional data.  Portfolio properties can be changed over time, for example to allow a Portfolio Manager to be linked with a Portfolio.  Additionally, portfolios can be securitised and held by other portfolios, allowing LUSID to perform \"drill-through\" into underlying fund holdings  ### Derived Portfolios  LUSID also allows for a portfolio to be composed of another portfolio via derived portfolios.  A derived portfolio can contain its own transactions and also inherits any transactions from its parent portfolio.  Any changes made to the parent portfolio are automatically reflected in derived portfolio.  Derived portfolios in conjunction with scopes are a powerful construct.  For example, to do pre-trade what-if analysis, a derived portfolio could be created a new namespace linked to the underlying live (parent) portfolio.  Analysis can then be undertaken on the derived portfolio without affecting the live portfolio.  ### Transactions  A transaction represents an economic activity against a Portfolio.  Transactions are processed according to a configuration. This will tell the LUSID engine how to interpret the transaction and correctly update the holdings. LUSID comes with a set of transaction types you can use out of the box, or you can configure your own set(s) of transactions.  For more details see the [LUSID Getting Started Guide for transaction configuration.](https://support.lusid.com/configuring-transaction-types)  | Field|Type|Description | | ---|---|--- | | TransactionId|string|The unique identifier for the transaction. | | Type|string|The type of the transaction e.g. 'Buy', 'Sell'. The transaction type should have been pre-configured via the System Configuration API endpoint. If it hasn't been pre-configured the transaction will still be updated or inserted however you will be unable to generate the resultant holdings for the portfolio that contains this transaction as LUSID does not know how to process it. | | InstrumentIdentifiers|map|A set of instrument identifiers to use to resolve the transaction to a unique instrument. | | TransactionDate|dateorcutlabel|The date of the transaction. | | SettlementDate|dateorcutlabel|The settlement date of the transaction. | | Units|decimal|The number of units transacted in the associated instrument. | | TransactionPrice|transactionprice|The price for each unit of the transacted instrument in the transaction currency. | | TotalConsideration|currencyandamount|The total value of the transaction in the settlement currency. | | ExchangeRate|decimal|The exchange rate between the transaction and settlement currency. For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. | | TransactionCurrency|currency|The transaction currency. | | Properties|map|Set of unique transaction properties and associated values to store with the transaction. Each property must be from the 'Transaction' domain. | | CounterpartyId|string|The identifier for the counterparty of the transaction. | | Source|string|The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. |   From these fields, the following values can be calculated  * **Transaction value in Transaction currency**: TotalConsideration / ExchangeRate  * **Transaction value in Portfolio currency**: Transaction value in Transaction currency * TradeToPortfolioRate  #### Example Transactions  ##### A Common Purchase Example Three example transactions are shown in the table below.   They represent a purchase of USD denominated IBM shares within a Sterling denominated portfolio.   * The first two transactions are for separate buy and fx trades    * Buying 500 IBM shares for $71,480.00    * A spot foreign exchange conversion to fund the IBM purchase. (Buy $71,480.00 for &#163;54,846.60)  * The third transaction is an alternate version of the above trades. Buying 500 IBM shares and settling directly in Sterling.  | Column |  Buy Trade | Fx Trade | Buy Trade with foreign Settlement | | ----- | ----- | ----- | ----- | | TransactionId | FBN00001 | FBN00002 | FBN00003 | | Type | Buy | FxBuy | Buy | | InstrumentIdentifiers | { \"figi\", \"BBG000BLNNH6\" } | { \"CCY\", \"CCY_USD\" } | { \"figi\", \"BBG000BLNNH6\" } | | TransactionDate | 2018-08-02 | 2018-08-02 | 2018-08-02 | | SettlementDate | 2018-08-06 | 2018-08-06 | 2018-08-06 | | Units | 500 | 71480 | 500 | | TransactionPrice | 142.96 | 1 | 142.96 | | TradeCurrency | USD | USD | USD | | ExchangeRate | 1 | 0.7673 | 0.7673 | | TotalConsideration.Amount | 71480.00 | 54846.60 | 54846.60 | | TotalConsideration.Currency | USD | GBP | GBP | | Trade/default/TradeToPortfolioRate&ast; | 0.7673 | 0.7673 | 0.7673 |  [&ast; This is a property field]  ##### A Forward FX Example  LUSID has a flexible transaction modelling system, meaning there are a number of different ways of modelling forward fx trades.  The default LUSID transaction types are FwdFxBuy and FwdFxSell. Using these transaction types, LUSID will generate two holdings for each Forward FX trade, one for each currency in the trade.  An example Forward Fx trade to sell GBP for USD in a JPY-denominated portfolio is shown below:  | Column | Forward 'Sell' Trade | Notes | | ----- | ----- | ---- | | TransactionId | FBN00004 | | | Type | FwdFxSell | | | InstrumentIdentifiers | { \"Instrument/default/Currency\", \"GBP\" } | | | TransactionDate | 2018-08-02 | | | SettlementDate | 2019-02-06 | Six month forward | | Units | 10000.00 | Units of GBP | | TransactionPrice | 1 | | | TradeCurrency | GBP | Currency being sold | | ExchangeRate | 1.3142 | Agreed rate between GBP and USD | | TotalConsideration.Amount | 13142.00 | Amount in the settlement currency, USD | | TotalConsideration.Currency | USD | Settlement currency | | Trade/default/TradeToPortfolioRate | 142.88 | Rate between trade currency, GBP and portfolio base currency, JPY |  Please note that exactly the same economic behaviour could be modelled using the FwdFxBuy Transaction Type with the amounts and rates reversed.  ### Holdings  A holding represents a position in an instrument or cash on a given date.  | Field|Type|Description | | ---|---|--- | | InstrumentUid|string|The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in. | | SubHoldingKeys|map|The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created. | | Properties|map|The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' or 'Holding' domain. | | HoldingType|string|The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | | Units|decimal|The total number of units of the holding. | | SettledUnits|decimal|The total number of settled units of the holding. | | Cost|currencyandamount|The total cost of the holding in the transaction currency. | | CostPortfolioCcy|currencyandamount|The total cost of the holding in the portfolio currency. | | Transaction|transaction|The transaction associated with an unsettled holding. |   ## Corporate Actions  Corporate actions are represented within LUSID in terms of a set of instrument-specific 'transitions'.  These transitions are used to specify the participants of the corporate action, and the effect that the corporate action will have on holdings in those participants.  ### Corporate Action  | Field|Type|Description | | ---|---|--- | | CorporateActionCode|code|The unique identifier of this corporate action | | Description|string|  | | AnnouncementDate|datetimeoffset|The announcement date of the corporate action | | ExDate|datetimeoffset|The ex date of the corporate action | | RecordDate|datetimeoffset|The record date of the corporate action | | PaymentDate|datetimeoffset|The payment date of the corporate action | | Transitions|corporateactiontransition[]|The transitions that result from this corporate action |   ### Transition | Field|Type|Description | | ---|---|--- | | InputTransition|corporateactiontransitioncomponent|Indicating the basis of the corporate action - which security and how many units | | OutputTransitions|corporateactiontransitioncomponent[]|What will be generated relative to the input transition |   ### Example Corporate Action Transitions  #### A Dividend Action Transition  In this example, for each share of IBM, 0.20 units (or 20 pence) of GBP are generated.  | Column |  Input Transition | Output Transition | | ----- | ----- | ----- | | Instrument Identifiers | { \"figi\" : \"BBG000BLNNH6\" } | { \"ccy\" : \"CCY_GBP\" } | | Units Factor | 1 | 0.20 | | Cost Factor | 1 | 0 |  #### A Split Action Transition  In this example, for each share of IBM, we end up with 2 units (2 shares) of IBM, with total value unchanged.  | Column |  Input Transition | Output Transition | | ----- | ----- | ----- | | Instrument Identifiers | { \"figi\" : \"BBG000BLNNH6\" } | { \"figi\" : \"BBG000BLNNH6\" } | | Units Factor | 1 | 2 | | Cost Factor | 1 | 1 |  #### A Spinoff Action Transition  In this example, for each share of IBM, we end up with 1 unit (1 share) of IBM and 3 units (3 shares) of Celestica, with 85% of the value remaining on the IBM share, and 5% in each Celestica share (15% total).  | Column |  Input Transition | Output Transition 1 | Output Transition 2 | | ----- | ----- | ----- | ----- | | Instrument Identifiers | { \"figi\" : \"BBG000BLNNH6\" } | { \"figi\" : \"BBG000BLNNH6\" } | { \"figi\" : \"BBG000HBGRF3\" } | | Units Factor | 1 | 1 | 3 | | Cost Factor | 1 | 0.85 | 0.15 |  ## Reference Portfolios Reference portfolios are portfolios that contain constituents with weights.  They are designed to represent entities such as indices and benchmarks.  ### Constituents | Field|Type|Description | | ---|---|--- | | InstrumentIdentifiers|map|Unique instrument identifiers | | InstrumentUid|string|LUSID's internal unique instrument identifier, resolved from the instrument identifiers | | Currency|decimal|  | | Weight|decimal|  | | FloatingWeight|decimal|  |   ## Portfolio Groups Portfolio groups allow the construction of a hierarchy from portfolios and groups.  Portfolio operations on the group are executed on an aggregated set of portfolios in the hierarchy.   For example:   * Global Portfolios _(group)_   * APAC _(group)_     * Hong Kong _(portfolio)_     * Japan _(portfolio)_   * Europe _(group)_     * France _(portfolio)_     * Germany _(portfolio)_   * UK _(portfolio)_   In this example **Global Portfolios** is a group that consists of an aggregate of **Hong Kong**, **Japan**, **France**, **Germany** and **UK** portfolios.  ## Properties  Properties are key-value pairs that can be applied to any entity within a domain (where a domain is `trade`, `portfolio`, `security` etc).  Properties must be defined before use with a `PropertyDefinition` and can then subsequently be added to entities.   ## Schema  A detailed description of the entities used by the API and parameters for endpoints which take a JSON document can be retrieved via the `schema` endpoint.  ## Meta data  The following headers are returned on all responses from LUSID  | Name | Purpose | | --- | --- | | lusid-meta-duration | Duration of the request | | lusid-meta-success | Whether or not LUSID considered the request to be successful | | lusid-meta-requestId | The unique identifier for the request | | lusid-schema-url | Url of the schema for the data being returned | | lusid-property-schema-url | Url of the schema for any properties |   # Error Codes  | Code|Name|Description | | ---|---|--- | | <a name=\"-10\">-10</a>|Server Configuration Error|  | | <a name=\"-1\">-1</a>|Unknown error|An unexpected error was encountered on our side. | | <a name=\"102\">102</a>|Version Not Found|  | | <a name=\"103\">103</a>|Api Rate Limit Violation|  | | <a name=\"104\">104</a>|Instrument Not Found|  | | <a name=\"105\">105</a>|Property Not Found|  | | <a name=\"106\">106</a>|Portfolio Recursion Depth|  | | <a name=\"108\">108</a>|Group Not Found|  | | <a name=\"109\">109</a>|Portfolio Not Found|  | | <a name=\"110\">110</a>|Property Schema Not Found|  | | <a name=\"111\">111</a>|Portfolio Ancestry Not Found|  | | <a name=\"112\">112</a>|Portfolio With Id Already Exists|  | | <a name=\"113\">113</a>|Orphaned Portfolio|  | | <a name=\"119\">119</a>|Missing Base Claims|  | | <a name=\"121\">121</a>|Property Not Defined|  | | <a name=\"122\">122</a>|Cannot Delete System Property|  | | <a name=\"123\">123</a>|Cannot Modify Immutable Property Field|  | | <a name=\"124\">124</a>|Property Already Exists|  | | <a name=\"125\">125</a>|Invalid Property Life Time|  | | <a name=\"126\">126</a>|Property Constraint Style Excludes Properties|  | | <a name=\"127\">127</a>|Cannot Modify Default Data Type|  | | <a name=\"128\">128</a>|Group Already Exists|  | | <a name=\"129\">129</a>|No Such Data Type|  | | <a name=\"130\">130</a>|Undefined Value For Data Type|  | | <a name=\"131\">131</a>|Unsupported Value Type Defined On Data Type|  | | <a name=\"132\">132</a>|Validation Error|  | | <a name=\"133\">133</a>|Loop Detected In Group Hierarchy|  | | <a name=\"134\">134</a>|Undefined Acceptable Values|  | | <a name=\"135\">135</a>|Sub Group Already Exists|  | | <a name=\"138\">138</a>|Price Source Not Found|  | | <a name=\"139\">139</a>|Analytic Store Not Found|  | | <a name=\"141\">141</a>|Analytic Store Already Exists|  | | <a name=\"143\">143</a>|Client Instrument Already Exists|  | | <a name=\"144\">144</a>|Duplicate In Parameter Set|  | | <a name=\"147\">147</a>|Results Not Found|  | | <a name=\"148\">148</a>|Order Field Not In Result Set|  | | <a name=\"149\">149</a>|Operation Failed|  | | <a name=\"150\">150</a>|Elastic Search Error|  | | <a name=\"151\">151</a>|Invalid Parameter Value|  | | <a name=\"153\">153</a>|Command Processing Failure|  | | <a name=\"154\">154</a>|Entity State Construction Failure|  | | <a name=\"155\">155</a>|Entity Timeline Does Not Exist|  | | <a name=\"156\">156</a>|Event Publish Failure|  | | <a name=\"157\">157</a>|Invalid Request|  | | <a name=\"158\">158</a>|Event Publish Unknown|  | | <a name=\"159\">159</a>|Event Query Failure|  | | <a name=\"160\">160</a>|Blob Did Not Exist|  | | <a name=\"162\">162</a>|Sub System Request Failure|  | | <a name=\"163\">163</a>|Sub System Configuration Failure|  | | <a name=\"165\">165</a>|Failed To Delete|  | | <a name=\"166\">166</a>|Upsert Client Instrument Failure|  | | <a name=\"167\">167</a>|Illegal As At Interval|  | | <a name=\"168\">168</a>|Illegal Bitemporal Query|  | | <a name=\"169\">169</a>|Invalid Alternate Id|  | | <a name=\"170\">170</a>|Cannot Add Source Portfolio Property Explicitly|  | | <a name=\"171\">171</a>|Entity Already Exists In Group|  | | <a name=\"173\">173</a>|Entity With Id Already Exists|  | | <a name=\"174\">174</a>|Derived Portfolio Details Do Not Exist|  | | <a name=\"176\">176</a>|Portfolio With Name Already Exists|  | | <a name=\"177\">177</a>|Invalid Transactions|  | | <a name=\"178\">178</a>|Reference Portfolio Not Found|  | | <a name=\"179\">179</a>|Duplicate Id|  | | <a name=\"180\">180</a>|Command Retrieval Failure|  | | <a name=\"181\">181</a>|Data Filter Application Failure|  | | <a name=\"182\">182</a>|Search Failed|  | | <a name=\"183\">183</a>|Movements Engine Configuration Key Failure|  | | <a name=\"184\">184</a>|Fx Rate Source Not Found|  | | <a name=\"185\">185</a>|Accrual Source Not Found|  | | <a name=\"186\">186</a>|Access Denied|  | | <a name=\"187\">187</a>|Invalid Identity Token|  | | <a name=\"188\">188</a>|Invalid Request Headers|  | | <a name=\"189\">189</a>|Price Not Found|  | | <a name=\"190\">190</a>|Invalid Sub Holding Keys Provided|  | | <a name=\"191\">191</a>|Duplicate Sub Holding Keys Provided|  | | <a name=\"192\">192</a>|Cut Definition Not Found|  | | <a name=\"193\">193</a>|Cut Definition Invalid|  | | <a name=\"194\">194</a>|Time Variant Property Deletion Date Unspecified|  | | <a name=\"195\">195</a>|Perpetual Property Deletion Date Specified|  | | <a name=\"196\">196</a>|Time Variant Property Upsert Date Unspecified|  | | <a name=\"197\">197</a>|Perpetual Property Upsert Date Specified|  | | <a name=\"200\">200</a>|Invalid Unit For Data Type|  | | <a name=\"201\">201</a>|Invalid Type For Data Type|  | | <a name=\"202\">202</a>|Invalid Value For Data Type|  | | <a name=\"203\">203</a>|Unit Not Defined For Data Type|  | | <a name=\"204\">204</a>|Units Not Supported On Data Type|  | | <a name=\"205\">205</a>|Cannot Specify Units On Data Type|  | | <a name=\"206\">206</a>|Unit Schema Inconsistent With Data Type|  | | <a name=\"207\">207</a>|Unit Definition Not Specified|  | | <a name=\"208\">208</a>|Duplicate Unit Definitions Specified|  | | <a name=\"209\">209</a>|Invalid Units Definition|  | | <a name=\"210\">210</a>|Invalid Instrument Identifier Unit|  | | <a name=\"211\">211</a>|Holdings Adjustment Does Not Exist|  | | <a name=\"212\">212</a>|Could Not Build Excel Url|  | | <a name=\"213\">213</a>|Could Not Get Excel Version|  | | <a name=\"214\">214</a>|Instrument By Code Not Found|  | | <a name=\"215\">215</a>|Entity Schema Does Not Exist|  | | <a name=\"216\">216</a>|Feature Not Supported On Portfolio Type|  | | <a name=\"217\">217</a>|Quote Not Found|  | | <a name=\"218\">218</a>|Invalid Quote Identifier|  | | <a name=\"219\">219</a>|Invalid Metric For Data Type|  | | <a name=\"220\">220</a>|Invalid Instrument Definition|  | | <a name=\"221\">221</a>|Instrument Upsert Failure|  | | <a name=\"222\">222</a>|Reference Portfolio Request Not Supported|  | | <a name=\"223\">223</a>|Transaction Portfolio Request Not Supported|  | | <a name=\"224\">224</a>|Invalid Property Value Assignment|  | | <a name=\"230\">230</a>|Transaction Type Not Found|  | | <a name=\"231\">231</a>|Transaction Type Duplication|  | | <a name=\"232\">232</a>|Portfolio Does Not Exist At Given Date|  | | <a name=\"233\">233</a>|Query Parser Failure|  | | <a name=\"234\">234</a>|Duplicate Constituent|  | | <a name=\"235\">235</a>|Unresolved Instrument Constituent|  | | <a name=\"236\">236</a>|Unresolved Instrument In Transition|  | | <a name=\"237\">237</a>|Missing Side Definitions|  | | <a name=\"299\">299</a>|Invalid Recipe|  | | <a name=\"300\">300</a>|Missing Recipe|  | | <a name=\"301\">301</a>|Dependencies|  | | <a name=\"304\">304</a>|Portfolio Preprocess Failure|  | | <a name=\"310\">310</a>|Valuation Engine Failure|  | | <a name=\"311\">311</a>|Task Factory Failure|  | | <a name=\"312\">312</a>|Task Evaluation Failure|  | | <a name=\"313\">313</a>|Task Generation Failure|  | | <a name=\"314\">314</a>|Engine Configuration Failure|  | | <a name=\"315\">315</a>|Model Specification Failure|  | | <a name=\"320\">320</a>|Market Data Key Failure|  | | <a name=\"321\">321</a>|Market Resolver Failure|  | | <a name=\"322\">322</a>|Market Data Failure|  | | <a name=\"330\">330</a>|Curve Failure|  | | <a name=\"331\">331</a>|Volatility Surface Failure|  | | <a name=\"332\">332</a>|Volatility Cube Failure|  | | <a name=\"350\">350</a>|Instrument Failure|  | | <a name=\"351\">351</a>|Cash Flows Failure|  | | <a name=\"352\">352</a>|Reference Data Failure|  | | <a name=\"360\">360</a>|Aggregation Failure|  | | <a name=\"361\">361</a>|Aggregation Measure Failure|  | | <a name=\"370\">370</a>|Result Retrieval Failure|  | | <a name=\"371\">371</a>|Result Processing Failure|  | | <a name=\"372\">372</a>|Vendor Result Processing Failure|  | | <a name=\"373\">373</a>|Vendor Result Mapping Failure|  | | <a name=\"374\">374</a>|Vendor Library Unauthorised|  | | <a name=\"375\">375</a>|Vendor Connectivity Error|  | | <a name=\"376\">376</a>|Vendor Interface Error|  | | <a name=\"377\">377</a>|Vendor Pricing Failure|  | | <a name=\"378\">378</a>|Vendor Translation Failure|  | | <a name=\"379\">379</a>|Vendor Key Mapping Failure|  | | <a name=\"380\">380</a>|Vendor Reflection Failure|  | | <a name=\"390\">390</a>|Attempt To Upsert Duplicate Quotes|  | | <a name=\"391\">391</a>|Corporate Action Source Does Not Exist|  | | <a name=\"392\">392</a>|Corporate Action Source Already Exists|  | | <a name=\"393\">393</a>|Instrument Identifier Already In Use|  | | <a name=\"394\">394</a>|Properties Not Found|  | | <a name=\"395\">395</a>|Batch Operation Aborted|  | | <a name=\"400\">400</a>|Invalid Iso4217 Currency Code|  | | <a name=\"401\">401</a>|Cannot Assign Instrument Identifier To Currency|  | | <a name=\"402\">402</a>|Cannot Assign Currency Identifier To Non Currency|  | | <a name=\"403\">403</a>|Currency Instrument Cannot Be Deleted|  | | <a name=\"404\">404</a>|Currency Instrument Cannot Have Economic Definition|  | | <a name=\"405\">405</a>|Currency Instrument Cannot Have Lookthrough Portfolio|  | | <a name=\"406\">406</a>|Cannot Create Currency Instrument With Multiple Identifiers|  | | <a name=\"407\">407</a>|Specified Currency Is Undefined|  | | <a name=\"410\">410</a>|Index Does Not Exist|  | | <a name=\"411\">411</a>|Sort Field Does Not Exist|  | | <a name=\"413\">413</a>|Negative Pagination Parameters|  | | <a name=\"414\">414</a>|Invalid Search Syntax|  | | <a name=\"415\">415</a>|Filter Execution Timeout|  | | <a name=\"420\">420</a>|Side Definition Inconsistent|  | | <a name=\"450\">450</a>|Invalid Quote Access Metadata Rule|  | | <a name=\"451\">451</a>|Access Metadata Not Found|  | | <a name=\"452\">452</a>|Invalid Access Metadata Identifier|  | | <a name=\"460\">460</a>|Standard Resource Not Found|  | | <a name=\"461\">461</a>|Standard Resource Conflict|  | | <a name=\"601\">601</a>|Person Identifier Already In Use|  | | <a name=\"602\">602</a>|Person Not Found|  | | <a name=\"603\">603</a>|Cannot Set Identifier|  | | <a name=\"617\">617</a>|Invalid Recipe Specification In Request|  | | <a name=\"618\">618</a>|Inline Recipe Deserialisation Failure|  | | <a name=\"619\">619</a>|Identifier Types Not Set For Entity Object|  | | <a name=\"620\">620</a>|Cannot Delete All Client Defined Identifiers|  | | <a name=\"650\">650</a>|The Order requested was not found.|  | | <a name=\"654\">654</a>|The Allocation requested was not found.|  | | <a name=\"655\">655</a>|Cannot build the fx forward target with the given holdings.|  | | <a name=\"656\">656</a>|Group does not contain expected entities.|  | | <a name=\"667\">667</a>|Relation definition already exists|  |   # noqa: E501

    The version of the OpenAPI document: 0.10.1436
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (
    ApiTypeError,
    ApiValueError
)


class TransactionPortfoliosApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def adjust_holdings(self, scope, code, effective_at, holding_adjustments, **kwargs):  # noqa: E501
        """Adjust holdings  # noqa: E501

        Adjust one or more holdings of the specified transaction portfolio to the provided targets. LUSID will  automatically construct adjustment transactions to ensure that the holdings which have been adjusted are  always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/how-do-i-adjust-my-holdings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adjust_holdings(scope, code, effective_at, holding_adjustments, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which the holdings should be set to the provided targets. (required)
        :param list[AdjustHoldingRequest] holding_adjustments: The selected set of holdings to adjust to the provided targets for the              transaction portfolio. (required)
        :param list[str] reconciliation_methods: Optional parameter for specifying a reconciliation method: e.g. FxForward.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AdjustHolding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.adjust_holdings_with_http_info(scope, code, effective_at, holding_adjustments, **kwargs)  # noqa: E501

    def adjust_holdings_with_http_info(self, scope, code, effective_at, holding_adjustments, **kwargs):  # noqa: E501
        """Adjust holdings  # noqa: E501

        Adjust one or more holdings of the specified transaction portfolio to the provided targets. LUSID will  automatically construct adjustment transactions to ensure that the holdings which have been adjusted are  always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/how-do-i-adjust-my-holdings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adjust_holdings_with_http_info(scope, code, effective_at, holding_adjustments, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which the holdings should be set to the provided targets. (required)
        :param list[AdjustHoldingRequest] holding_adjustments: The selected set of holdings to adjust to the provided targets for the              transaction portfolio. (required)
        :param list[str] reconciliation_methods: Optional parameter for specifying a reconciliation method: e.g. FxForward.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AdjustHolding, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at', 'holding_adjustments', 'reconciliation_methods']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adjust_holdings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `adjust_holdings`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `adjust_holdings`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if ('effective_at' not in local_var_params or
                local_var_params['effective_at'] is None):
            raise ApiValueError("Missing the required parameter `effective_at` when calling `adjust_holdings`")  # noqa: E501
        # verify the required parameter 'holding_adjustments' is set
        if ('holding_adjustments' not in local_var_params or
                local_var_params['holding_adjustments'] is None):
            raise ApiValueError("Missing the required parameter `holding_adjustments` when calling `adjust_holdings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'reconciliation_methods' in local_var_params:
            query_params.append(('reconciliationMethods', local_var_params['reconciliation_methods']))  # noqa: E501
            collection_formats['reconciliationMethods'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'holding_adjustments' in local_var_params:
            body_params = local_var_params['holding_adjustments']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/holdings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdjustHolding',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def build_transactions(self, scope, code, query_parameters, **kwargs):  # noqa: E501
        """Build transactions  # noqa: E501

        Builds and returns all transactions that affect the holdings of a portfolio over a given interval of  effective time into a set of output transactions. This includes transactions automatically generated by  LUSID such as holding adjustments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.build_transactions(scope, code, query_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param TransactionQueryParameters query_parameters: The query queryParameters which control how the output transactions are built. (required)
        :param datetime as_at: The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified.
        :param str filter: Expression to filter the result set.              For example, to filter on the Transaction Type, use \"type eq 'Buy'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param list[str] property_keys: A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\".
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: VersionedResourceListOfOutputTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.build_transactions_with_http_info(scope, code, query_parameters, **kwargs)  # noqa: E501

    def build_transactions_with_http_info(self, scope, code, query_parameters, **kwargs):  # noqa: E501
        """Build transactions  # noqa: E501

        Builds and returns all transactions that affect the holdings of a portfolio over a given interval of  effective time into a set of output transactions. This includes transactions automatically generated by  LUSID such as holding adjustments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.build_transactions_with_http_info(scope, code, query_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param TransactionQueryParameters query_parameters: The query queryParameters which control how the output transactions are built. (required)
        :param datetime as_at: The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified.
        :param str filter: Expression to filter the result set.              For example, to filter on the Transaction Type, use \"type eq 'Buy'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param list[str] property_keys: A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\".
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(VersionedResourceListOfOutputTransaction, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'query_parameters', 'as_at', 'filter', 'property_keys']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method build_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `build_transactions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `build_transactions`")  # noqa: E501
        # verify the required parameter 'query_parameters' is set
        if ('query_parameters' not in local_var_params or
                local_var_params['query_parameters'] is None):
            raise ApiValueError("Missing the required parameter `query_parameters` when calling `build_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'property_keys' in local_var_params:
            query_params.append(('propertyKeys', local_var_params['property_keys']))  # noqa: E501
            collection_formats['propertyKeys'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query_parameters' in local_var_params:
            body_params = local_var_params['query_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/transactions/$build', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VersionedResourceListOfOutputTransaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cancel_adjust_holdings(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Cancel adjust holdings  # noqa: E501

        Cancel all previous holding adjustments made on the specified transaction portfolio for a specified effective  datetime. This should be used to undo holding adjustments made via set holdings or adjust holdings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_adjust_holdings(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which the holding adjustments should be undone. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.cancel_adjust_holdings_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501

    def cancel_adjust_holdings_with_http_info(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Cancel adjust holdings  # noqa: E501

        Cancel all previous holding adjustments made on the specified transaction portfolio for a specified effective  datetime. This should be used to undo holding adjustments made via set holdings or adjust holdings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_adjust_holdings_with_http_info(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which the holding adjustments should be undone. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeletedEntityResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_adjust_holdings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `cancel_adjust_holdings`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `cancel_adjust_holdings`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if ('effective_at' not in local_var_params or
                local_var_params['effective_at'] is None):
            raise ApiValueError("Missing the required parameter `effective_at` when calling `cancel_adjust_holdings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/holdings', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeletedEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cancel_executions(self, scope, code, execution_ids, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Cancel executions  # noqa: E501

        Cancel one or more executions which exist in a specified transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_executions(scope, code, execution_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param list[str] execution_ids: The ids of the executions to cancel. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.cancel_executions_with_http_info(scope, code, execution_ids, **kwargs)  # noqa: E501

    def cancel_executions_with_http_info(self, scope, code, execution_ids, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Cancel executions  # noqa: E501

        Cancel one or more executions which exist in a specified transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_executions_with_http_info(scope, code, execution_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param list[str] execution_ids: The ids of the executions to cancel. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeletedEntityResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'execution_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_executions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `cancel_executions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `cancel_executions`")  # noqa: E501
        # verify the required parameter 'execution_ids' is set
        if ('execution_ids' not in local_var_params or
                local_var_params['execution_ids'] is None):
            raise ApiValueError("Missing the required parameter `execution_ids` when calling `cancel_executions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'execution_ids' in local_var_params:
            query_params.append(('executionIds', local_var_params['execution_ids']))  # noqa: E501
            collection_formats['executionIds'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/executions', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeletedEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cancel_transactions(self, scope, code, transaction_ids, **kwargs):  # noqa: E501
        """Cancel transactions  # noqa: E501

        Cancel one or more transactions from the specified transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_transactions(scope, code, transaction_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param list[str] transaction_ids: The ids of the transactions to cancel. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.cancel_transactions_with_http_info(scope, code, transaction_ids, **kwargs)  # noqa: E501

    def cancel_transactions_with_http_info(self, scope, code, transaction_ids, **kwargs):  # noqa: E501
        """Cancel transactions  # noqa: E501

        Cancel one or more transactions from the specified transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_transactions_with_http_info(scope, code, transaction_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param list[str] transaction_ids: The ids of the transactions to cancel. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeletedEntityResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'transaction_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `cancel_transactions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `cancel_transactions`")  # noqa: E501
        # verify the required parameter 'transaction_ids' is set
        if ('transaction_ids' not in local_var_params or
                local_var_params['transaction_ids'] is None):
            raise ApiValueError("Missing the required parameter `transaction_ids` when calling `cancel_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'transaction_ids' in local_var_params:
            query_params.append(('transactionIds', local_var_params['transaction_ids']))  # noqa: E501
            collection_formats['transactionIds'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/transactions', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeletedEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_portfolio(self, scope, transaction_portfolio, **kwargs):  # noqa: E501
        """Create portfolio  # noqa: E501

        Create a transaction portfolio in a specific scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_portfolio(scope, transaction_portfolio, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope that the transaction portfolio will be created in. (required)
        :param CreateTransactionPortfolioRequest transaction_portfolio: The definition and details of the transaction portfolio. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Portfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_portfolio_with_http_info(scope, transaction_portfolio, **kwargs)  # noqa: E501

    def create_portfolio_with_http_info(self, scope, transaction_portfolio, **kwargs):  # noqa: E501
        """Create portfolio  # noqa: E501

        Create a transaction portfolio in a specific scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_portfolio_with_http_info(scope, transaction_portfolio, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope that the transaction portfolio will be created in. (required)
        :param CreateTransactionPortfolioRequest transaction_portfolio: The definition and details of the transaction portfolio. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Portfolio, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'transaction_portfolio']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_portfolio" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `create_portfolio`")  # noqa: E501
        # verify the required parameter 'transaction_portfolio' is set
        if ('transaction_portfolio' not in local_var_params or
                local_var_params['transaction_portfolio'] is None):
            raise ApiValueError("Missing the required parameter `transaction_portfolio` when calling `create_portfolio`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transaction_portfolio' in local_var_params:
            body_params = local_var_params['transaction_portfolio']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Portfolio',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_properties_from_transaction(self, scope, code, transaction_id, property_keys, **kwargs):  # noqa: E501
        """Delete properties from transaction  # noqa: E501

        Delete one or more property values from a single transaction in a transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_properties_from_transaction(scope, code, transaction_id, property_keys, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str transaction_id: The unique id of the transaction to delete the property value from. (required)
        :param list[str] property_keys: The property keys of the properties to delete from the transaction.              This must be from the \"Transaction\" domain and will have the format {domain}/{scope}/{code} e.g.              \"Transaction/strategy/quantsignal\". (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_properties_from_transaction_with_http_info(scope, code, transaction_id, property_keys, **kwargs)  # noqa: E501

    def delete_properties_from_transaction_with_http_info(self, scope, code, transaction_id, property_keys, **kwargs):  # noqa: E501
        """Delete properties from transaction  # noqa: E501

        Delete one or more property values from a single transaction in a transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_properties_from_transaction_with_http_info(scope, code, transaction_id, property_keys, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str transaction_id: The unique id of the transaction to delete the property value from. (required)
        :param list[str] property_keys: The property keys of the properties to delete from the transaction.              This must be from the \"Transaction\" domain and will have the format {domain}/{scope}/{code} e.g.              \"Transaction/strategy/quantsignal\". (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeletedEntityResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'transaction_id', 'property_keys']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_properties_from_transaction" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `delete_properties_from_transaction`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `delete_properties_from_transaction`")  # noqa: E501
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in local_var_params or
                local_var_params['transaction_id'] is None):
            raise ApiValueError("Missing the required parameter `transaction_id` when calling `delete_properties_from_transaction`")  # noqa: E501
        # verify the required parameter 'property_keys' is set
        if ('property_keys' not in local_var_params or
                local_var_params['property_keys'] is None):
            raise ApiValueError("Missing the required parameter `property_keys` when calling `delete_properties_from_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501
        if 'transaction_id' in local_var_params:
            path_params['transactionId'] = local_var_params['transaction_id']  # noqa: E501

        query_params = []
        if 'property_keys' in local_var_params:
            query_params.append(('propertyKeys', local_var_params['property_keys']))  # noqa: E501
            collection_formats['propertyKeys'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeletedEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_details(self, scope, code, **kwargs):  # noqa: E501
        """Get details  # noqa: E501

        Get the details associated with a transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_details(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio to retrieve the details for. (required)
        :param str code: The code of the transaction portfolio to retrieve the details for. Together with the              scope this uniquely identifies the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified.
        :param datetime as_at: The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to return the latest version of the details if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PortfolioDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_details_with_http_info(scope, code, **kwargs)  # noqa: E501

    def get_details_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Get details  # noqa: E501

        Get the details associated with a transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_details_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio to retrieve the details for. (required)
        :param str code: The code of the transaction portfolio to retrieve the details for. Together with the              scope this uniquely identifies the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified.
        :param datetime as_at: The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to return the latest version of the details if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PortfolioDetails, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at', 'as_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `get_details`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `get_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortfolioDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_holdings(self, scope, code, **kwargs):  # noqa: E501
        """Get holdings  # noqa: E501

        Get the holdings of the specified transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_holdings(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified.
        :param datetime as_at: The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified.
        :param str filter: Expression to filter the result set.               For example, to filter on the Holding Type, use \"holdingType eq 'p'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param list[str] property_keys: A list of property keys from the \"Instrument\" or \"Holding\" domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or \"Holding/system/Cost\".
        :param bool by_taxlots: Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: VersionedResourceListOfPortfolioHolding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_holdings_with_http_info(scope, code, **kwargs)  # noqa: E501

    def get_holdings_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Get holdings  # noqa: E501

        Get the holdings of the specified transaction portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_holdings_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified.
        :param datetime as_at: The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified.
        :param str filter: Expression to filter the result set.               For example, to filter on the Holding Type, use \"holdingType eq 'p'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param list[str] property_keys: A list of property keys from the \"Instrument\" or \"Holding\" domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or \"Holding/system/Cost\".
        :param bool by_taxlots: Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(VersionedResourceListOfPortfolioHolding, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at', 'as_at', 'filter', 'property_keys', 'by_taxlots']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_holdings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `get_holdings`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `get_holdings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'property_keys' in local_var_params:
            query_params.append(('propertyKeys', local_var_params['property_keys']))  # noqa: E501
            collection_formats['propertyKeys'] = 'multi'  # noqa: E501
        if 'by_taxlots' in local_var_params:
            query_params.append(('byTaxlots', local_var_params['by_taxlots']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/holdings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VersionedResourceListOfPortfolioHolding',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_holdings_adjustment(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Get holdings adjustment  # noqa: E501

        Get a holdings adjustment made to a transaction portfolio at a specific effective datetime. Note that a  holdings adjustment will only be returned if one exists for the specified effective datetime.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_holdings_adjustment(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label of the holdings adjustment. (required)
        :param datetime as_at: The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: HoldingsAdjustment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_holdings_adjustment_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501

    def get_holdings_adjustment_with_http_info(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Get holdings adjustment  # noqa: E501

        Get a holdings adjustment made to a transaction portfolio at a specific effective datetime. Note that a  holdings adjustment will only be returned if one exists for the specified effective datetime.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_holdings_adjustment_with_http_info(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label of the holdings adjustment. (required)
        :param datetime as_at: The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(HoldingsAdjustment, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at', 'as_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_holdings_adjustment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `get_holdings_adjustment`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `get_holdings_adjustment`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if ('effective_at' not in local_var_params or
                local_var_params['effective_at'] is None):
            raise ApiValueError("Missing the required parameter `effective_at` when calling `get_holdings_adjustment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501
        if 'effective_at' in local_var_params:
            path_params['effectiveAt'] = local_var_params['effective_at']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HoldingsAdjustment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transactions(self, scope, code, **kwargs):  # noqa: E501
        """Get transactions  # noqa: E501

        Get transactions from the specified transaction portfolio over a given interval of effective time.     When the specified portfolio is a derived transaction portfolio, the returned set of transactions is the  union set of all transactions of the parent (and any grandparents etc.) and the specified derived transaction portfolio itself.  The maximum number of transactions that this method can get per request is 2,000.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str from_transaction_date: The lower bound effective datetime or cut label (inclusive) from which to retrieve the transactions.              There is no lower bound if this is not specified.
        :param str to_transaction_date: The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified.
        :param datetime as_at: The asAt datetime at which to retrieve the transactions. Defaults to return the latest version              of each transaction if not specified.
        :param str filter: Expression to filter the result set.               For example, to filter on the Transaction Type, use \"type eq 'Buy'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param list[str] property_keys: A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\".
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: VersionedResourceListOfTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transactions_with_http_info(scope, code, **kwargs)  # noqa: E501

    def get_transactions_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Get transactions  # noqa: E501

        Get transactions from the specified transaction portfolio over a given interval of effective time.     When the specified portfolio is a derived transaction portfolio, the returned set of transactions is the  union set of all transactions of the parent (and any grandparents etc.) and the specified derived transaction portfolio itself.  The maximum number of transactions that this method can get per request is 2,000.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str from_transaction_date: The lower bound effective datetime or cut label (inclusive) from which to retrieve the transactions.              There is no lower bound if this is not specified.
        :param str to_transaction_date: The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified.
        :param datetime as_at: The asAt datetime at which to retrieve the transactions. Defaults to return the latest version              of each transaction if not specified.
        :param str filter: Expression to filter the result set.               For example, to filter on the Transaction Type, use \"type eq 'Buy'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param list[str] property_keys: A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\".
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(VersionedResourceListOfTransaction, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'from_transaction_date', 'to_transaction_date', 'as_at', 'filter', 'property_keys']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `get_transactions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `get_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'from_transaction_date' in local_var_params:
            query_params.append(('fromTransactionDate', local_var_params['from_transaction_date']))  # noqa: E501
        if 'to_transaction_date' in local_var_params:
            query_params.append(('toTransactionDate', local_var_params['to_transaction_date']))  # noqa: E501
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'property_keys' in local_var_params:
            query_params.append(('propertyKeys', local_var_params['property_keys']))  # noqa: E501
            collection_formats['propertyKeys'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VersionedResourceListOfTransaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_holdings_adjustments(self, scope, code, **kwargs):  # noqa: E501
        """List holdings adjustments  # noqa: E501

        List the holdings adjustments made to the specified transaction portfolio over a specified interval of effective time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings_adjustments(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str from_effective_at: The lower bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified.
        :param str to_effective_at: The upper bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified.
        :param datetime as_at: The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResourceListOfHoldingsAdjustmentHeader
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_holdings_adjustments_with_http_info(scope, code, **kwargs)  # noqa: E501

    def list_holdings_adjustments_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """List holdings adjustments  # noqa: E501

        List the holdings adjustments made to the specified transaction portfolio over a specified interval of effective time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings_adjustments_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str from_effective_at: The lower bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified.
        :param str to_effective_at: The upper bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified.
        :param datetime as_at: The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResourceListOfHoldingsAdjustmentHeader, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'from_effective_at', 'to_effective_at', 'as_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_holdings_adjustments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `list_holdings_adjustments`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `list_holdings_adjustments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'from_effective_at' in local_var_params:
            query_params.append(('fromEffectiveAt', local_var_params['from_effective_at']))  # noqa: E501
        if 'to_effective_at' in local_var_params:
            query_params.append(('toEffectiveAt', local_var_params['to_effective_at']))  # noqa: E501
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/holdingsadjustments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceListOfHoldingsAdjustmentHeader',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_holdings(self, scope, code, effective_at, holding_adjustments, **kwargs):  # noqa: E501
        """Set holdings  # noqa: E501

        Set the holdings of the specified transaction portfolio to the provided targets. LUSID will automatically  construct adjustment transactions to ensure that the entire set of holdings for the transaction portfolio  are always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/how-do-i-adjust-my-holdings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_holdings(scope, code, effective_at, holding_adjustments, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which the holdings should be set to the provided targets. (required)
        :param list[AdjustHoldingRequest] holding_adjustments: The complete set of target holdings for the transaction portfolio. (required)
        :param list[str] reconciliation_methods: Optional parameter for specifying a reconciliation method: e.g. FxForward.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AdjustHolding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.set_holdings_with_http_info(scope, code, effective_at, holding_adjustments, **kwargs)  # noqa: E501

    def set_holdings_with_http_info(self, scope, code, effective_at, holding_adjustments, **kwargs):  # noqa: E501
        """Set holdings  # noqa: E501

        Set the holdings of the specified transaction portfolio to the provided targets. LUSID will automatically  construct adjustment transactions to ensure that the entire set of holdings for the transaction portfolio  are always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/how-do-i-adjust-my-holdings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_holdings_with_http_info(scope, code, effective_at, holding_adjustments, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which the holdings should be set to the provided targets. (required)
        :param list[AdjustHoldingRequest] holding_adjustments: The complete set of target holdings for the transaction portfolio. (required)
        :param list[str] reconciliation_methods: Optional parameter for specifying a reconciliation method: e.g. FxForward.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AdjustHolding, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at', 'holding_adjustments', 'reconciliation_methods']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_holdings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `set_holdings`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `set_holdings`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if ('effective_at' not in local_var_params or
                local_var_params['effective_at'] is None):
            raise ApiValueError("Missing the required parameter `effective_at` when calling `set_holdings`")  # noqa: E501
        # verify the required parameter 'holding_adjustments' is set
        if ('holding_adjustments' not in local_var_params or
                local_var_params['holding_adjustments'] is None):
            raise ApiValueError("Missing the required parameter `holding_adjustments` when calling `set_holdings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'reconciliation_methods' in local_var_params:
            query_params.append(('reconciliationMethods', local_var_params['reconciliation_methods']))  # noqa: E501
            collection_formats['reconciliationMethods'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'holding_adjustments' in local_var_params:
            body_params = local_var_params['holding_adjustments']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/holdings', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdjustHolding',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_executions(self, scope, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Upsert executions  # noqa: E501

        Update or insert executions into the specified transaction portfolio. An execution will be updated  if it already exists and inserted if it does not.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_executions(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param list[ExecutionRequest] executions: The executions to update or insert.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UpsertPortfolioExecutionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upsert_executions_with_http_info(scope, code, **kwargs)  # noqa: E501

    def upsert_executions_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Upsert executions  # noqa: E501

        Update or insert executions into the specified transaction portfolio. An execution will be updated  if it already exists and inserted if it does not.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_executions_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param list[ExecutionRequest] executions: The executions to update or insert.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UpsertPortfolioExecutionsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'executions']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_executions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `upsert_executions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `upsert_executions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'executions' in local_var_params:
            body_params = local_var_params['executions']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/executions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpsertPortfolioExecutionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_portfolio_details(self, scope, code, portfolio_details, **kwargs):  # noqa: E501
        """Upsert portfolio details  # noqa: E501

        Update or insert details for the specified transaction portfolio. The details will be updated  if they already exist and inserted if they do not.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_portfolio_details(scope, code, portfolio_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio to update or insert details for. (required)
        :param str code: The code of the transaction portfolio to update or insert details for. Together with the              scope this uniquely identifies the transaction portfolio. (required)
        :param CreatePortfolioDetails portfolio_details: The details to update or insert for the specified transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which the updated or inserted details should become valid.              Defaults to the current LUSID system datetime if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PortfolioDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upsert_portfolio_details_with_http_info(scope, code, portfolio_details, **kwargs)  # noqa: E501

    def upsert_portfolio_details_with_http_info(self, scope, code, portfolio_details, **kwargs):  # noqa: E501
        """Upsert portfolio details  # noqa: E501

        Update or insert details for the specified transaction portfolio. The details will be updated  if they already exist and inserted if they do not.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_portfolio_details_with_http_info(scope, code, portfolio_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio to update or insert details for. (required)
        :param str code: The code of the transaction portfolio to update or insert details for. Together with the              scope this uniquely identifies the transaction portfolio. (required)
        :param CreatePortfolioDetails portfolio_details: The details to update or insert for the specified transaction portfolio. (required)
        :param str effective_at: The effective datetime or cut label at which the updated or inserted details should become valid.              Defaults to the current LUSID system datetime if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PortfolioDetails, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'portfolio_details', 'effective_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_portfolio_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `upsert_portfolio_details`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `upsert_portfolio_details`")  # noqa: E501
        # verify the required parameter 'portfolio_details' is set
        if ('portfolio_details' not in local_var_params or
                local_var_params['portfolio_details'] is None):
            raise ApiValueError("Missing the required parameter `portfolio_details` when calling `upsert_portfolio_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'portfolio_details' in local_var_params:
            body_params = local_var_params['portfolio_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/details', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortfolioDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_transaction_properties(self, scope, code, transaction_id, transaction_properties, **kwargs):  # noqa: E501
        """Upsert transaction properties  # noqa: E501

        Update or insert one or more transaction properties to a single transaction in a transaction portfolio.  Each property will be updated if it already exists and inserted if it does not.  Both transaction and portfolio must exist at the time when properties are updated or inserted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_transaction_properties(scope, code, transaction_id, transaction_properties, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str transaction_id: The unique id of the transaction to update or insert properties against. (required)
        :param dict(str, PerpetualProperty) transaction_properties: The properties with their associated values to update or insert onto the              transaction. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UpsertTransactionPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upsert_transaction_properties_with_http_info(scope, code, transaction_id, transaction_properties, **kwargs)  # noqa: E501

    def upsert_transaction_properties_with_http_info(self, scope, code, transaction_id, transaction_properties, **kwargs):  # noqa: E501
        """Upsert transaction properties  # noqa: E501

        Update or insert one or more transaction properties to a single transaction in a transaction portfolio.  Each property will be updated if it already exists and inserted if it does not.  Both transaction and portfolio must exist at the time when properties are updated or inserted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_transaction_properties_with_http_info(scope, code, transaction_id, transaction_properties, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param str transaction_id: The unique id of the transaction to update or insert properties against. (required)
        :param dict(str, PerpetualProperty) transaction_properties: The properties with their associated values to update or insert onto the              transaction. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UpsertTransactionPropertiesResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'transaction_id', 'transaction_properties']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_transaction_properties" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `upsert_transaction_properties`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `upsert_transaction_properties`")  # noqa: E501
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in local_var_params or
                local_var_params['transaction_id'] is None):
            raise ApiValueError("Missing the required parameter `transaction_id` when calling `upsert_transaction_properties`")  # noqa: E501
        # verify the required parameter 'transaction_properties' is set
        if ('transaction_properties' not in local_var_params or
                local_var_params['transaction_properties'] is None):
            raise ApiValueError("Missing the required parameter `transaction_properties` when calling `upsert_transaction_properties`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501
        if 'transaction_id' in local_var_params:
            path_params['transactionId'] = local_var_params['transaction_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transaction_properties' in local_var_params:
            body_params = local_var_params['transaction_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpsertTransactionPropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_transactions(self, scope, code, transactions, **kwargs):  # noqa: E501
        """Upsert transactions  # noqa: E501

        Update or insert transactions into the specified transaction portfolio. A transaction will be updated  if it already exists and inserted if it does not.  The maximum number of transactions that this method can upsert per request is 10,000.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_transactions(scope, code, transactions, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param list[TransactionRequest] transactions: The transactions to be updated or inserted. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UpsertPortfolioTransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upsert_transactions_with_http_info(scope, code, transactions, **kwargs)  # noqa: E501

    def upsert_transactions_with_http_info(self, scope, code, transactions, **kwargs):  # noqa: E501
        """Upsert transactions  # noqa: E501

        Update or insert transactions into the specified transaction portfolio. A transaction will be updated  if it already exists and inserted if it does not.  The maximum number of transactions that this method can upsert per request is 10,000.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_transactions_with_http_info(scope, code, transactions, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the transaction portfolio. (required)
        :param str code: The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. (required)
        :param list[TransactionRequest] transactions: The transactions to be updated or inserted. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UpsertPortfolioTransactionsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'transactions']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `upsert_transactions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `upsert_transactions`")  # noqa: E501
        # verify the required parameter 'transactions' is set
        if ('transactions' not in local_var_params or
                local_var_params['transactions'] is None):
            raise ApiValueError("Missing the required parameter `transactions` when calling `upsert_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transactions' in local_var_params:
            body_params = local_var_params['transactions']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.10.1436'

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/transactions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpsertPortfolioTransactionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
