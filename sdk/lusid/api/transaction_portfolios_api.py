# coding: utf-8

"""
    LUSID API

    # Introduction  This page documents the [LUSID APIs](https://api.lusid.com/swagger), which allows authorised clients to query and update their data within the LUSID platform.  SDKs to interact with the LUSID APIs are available in the following languages :  * [C#](https://github.com/finbourne/lusid-sdk-csharp) * [Java](https://github.com/finbourne/lusid-sdk-java) * [JavaScript](https://github.com/finbourne/lusid-sdk-js) * [Python](https://github.com/finbourne/lusid-sdk-python)  # Data Model  The LUSID API has a relatively lightweight but extremely powerful data model.   One of the goals of LUSID was not to enforce on clients a single rigid data model but rather to provide a flexible foundation onto which clients can streamline their data.   One of the primary tools to extend the data model is through using properties.  Properties can be associated with amongst others: - * Transactions * Instruments * Portfolios   The LUSID data model is exposed through the LUSID APIs.  The APIs provide access to both business objects and the meta data used to configure the systems behaviours.   The key business entities are: - * **Portfolios** A portfolio is the primary container for transactions and holdings.  * **Derived Portfolios** Derived portfolios allow portfolios to be created based on other portfolios, by overriding or overlaying specific items * **Holdings** A holding is a position account for a instrument within a portfolio.  Holdings can only be adjusted via transactions. * **Transactions** A Transaction is a source of transactions used to manipulate holdings.  * **Corporate Actions** A corporate action is a market event which occurs to a instrument, for example a stock split * **Instruments**  A instrument represents a currency, tradable instrument or OTC contract that is attached to a transaction and a holding. * **Properties** Several entities allow additional user defined properties to be associated with them.   For example, a Portfolio manager may be associated with a portfolio  Meta data includes: - * **Transaction Types** Transactions are booked with a specific transaction type.  The types are client defined and are used to map the Transaction to a series of movements which update the portfolio holdings.  * **Properties Types** Types of user defined properties used within the system.  This section describes the data model that LUSID exposes via the APIs.  ## Scope  All data in LUSID is segregated at the client level.  Entities in LUSID are identifiable by a unique code.  Every entity lives within a logical data partition known as a Scope.  Scope is an identity namespace allowing two entities with the same unique code to co-exist within individual address spaces.  For example, prices for equities from different vendors may be uploaded into different scopes such as `client/vendor1` and `client/vendor2`.  A portfolio may then be valued using either of the price sources by referencing the appropriate scope.  LUSID Clients cannot access scopes of other clients.  ## Schema  A detailed description of the entities used by the API and parameters for endpoints which take a JSON document can be retrieved via the `schema` endpoint.  ## Instruments  LUSID has its own built-in instrument master which you can use to master your own instrument universe.  Every instrument must be created with one or more unique market identifiers, such as [FIGI](https://openfigi.com/) or RIC code. For any non-listed instruments (eg OTCs), you can upload an instrument against a custom ID of your choosing.  In addition, LUSID will allocate each instrument a unique 'LUSID instrument identifier'. The LUSID instrument identifier is what is used when uploading transactions, holdings, prices, etc. The API exposes an `instrument/lookup` endpoint which can be used to lookup these LUSID identifiers using their market identifiers.  Cash can be referenced using the ISO currency code prefixed with \"`CCY_`\" e.g. `CCY_GBP`  ## Instrument Prices (Analytics)  Instrument prices are stored in LUSID's Analytics Store  | Field|Type|Description | | ---|---|--- | | InstrumentUid|string|Unique instrument identifier | | Value|decimal|Value of the analytic, eg price | | Denomination|string|Underlying unit of the analytic, eg currency, EPS etc. |   ## Instrument Data  Instrument data can be uploaded to the system using the [Instrument Properties](#tag/InstrumentProperties) endpoint.  | Field|Type|Description | | ---|---|--- |   ## Portfolios  Portfolios are the top-level entity containers within LUSID, containing transactions, corporate actions and holdings.    The transactions build up the portfolio holdings on which valuations, analytics profit & loss and risk can be calculated.     Properties can be associated with Portfolios to add in additional model data.  Portfolio properties can be changed over time as well.  For example, to allow a Portfolio Manager to be linked with a Portfolio.  Additionally, portfolios can be securitised and held by other portfolios, allowing LUSID to perform \"drill-through\" into underlying fund holdings  ### Reference Portfolios Reference portfolios are portfolios that contain only weights, as opposed to transactions, and are designed to represent entities such as indices.  ### Derived Portfolios  LUSID also allows for a portfolio to be composed of another portfolio via derived portfolios.  A derived portfolio can contain its own transactions and also inherits any transactions from its parent portfolio.  Any changes made to the parent portfolio are automatically reflected in derived portfolio.  Derived portfolios in conjunction with scopes are a powerful construct.  For example, to do pre-trade what-if analysis, a derived portfolio could be created a new namespace linked to the underlying live (parent) portfolio.  Analysis can then be undertaken on the derived portfolio without affecting the live portfolio.  ### Portfolio Groups Portfolio groups allow the construction of a hierarchy from portfolios and groups.  Portfolio operations on the group are executed on an aggregated set of portfolios in the hierarchy.   For example:   * Global Portfolios _(group)_   * APAC _(group)_     * Hong Kong _(portfolio)_     * Japan _(portfolio)_   * Europe _(group)_     * France _(portfolio)_     * Germany _(portfolio)_   * UK _(portfolio)_   In this example **Global Portfolios** is a group that consists of an aggregate of **Hong Kong**, **Japan**, **France**, **Germany** and **UK** portfolios.  ### Movements Engine The Movements engine sits on top of the immutable event store and is used to manage the relationship between input trading actions and their associated portfolio holdings.     The movements engine reads in the following entity types:- * Posting Transactions * Applying Corporate Actions  * Holding Adjustments  These are converted to one or more movements and used by the movements engine to calculate holdings.  At the same time it also calculates running balances, and realised P&L.  The outputs from the movements engine are holdings and transactions.  ## Transactions  A transaction represents an economic activity against a Portfolio.  Transactions are processed according to a configuration. This will tell the LUSID engine how to interpret the transaction and correctly update the holdings. LUSID comes with a set of transaction types you can use out of the box, or you can configure your own set(s) of transactions.  For more details see the [LUSID Getting Started Guide for transaction configuration.](https://support.finbourne.com/hc/en-us/articles/360016737511-Configuring-Transaction-Types)  | Field|Type|Description | | ---|---|--- | | TransactionId|string|Unique transaction identifier | | Type|string|LUSID transaction type code - Buy, Sell, StockIn, StockOut, etc | | InstrumentIdentifiers|IReadOnlyDictionary`2|Unique instrument identifiers. | | InstrumentUid|string|Unique instrument identifier | | TransactionDate|datetime|Transaction date | | SettlementDate|datetime|Settlement date | | Units|decimal|Quantity of transaction in units of the instrument | | TransactionPrice|tradeprice|Execution price for the transaction | | TotalConsideration|currencyandamount|Total value of the transaction in settlement currency | | ExchangeRate|decimal|Rate between transaction and settle currency | | TransactionCurrency|currency|Transaction currency | | CounterpartyId|string|Counterparty identifier | | Source|string|Where this transaction came from | | NettingSet|string|  |   From these fields, the following values can be calculated  * **Transaction value in Transaction currency**: TotalConsideration / ExchangeRate  * **Transaction value in Portfolio currency**: Transaction value in Transaction currency * TradeToPortfolioRate  ### Example Transactions  #### A Common Purchase Example Three example transactions are shown in the table below.   They represent a purchase of USD denominated IBM shares within a Sterling denominated portfolio.   * The first two transactions are for separate buy and fx trades    * Buying 500 IBM shares for $71,480.00    * A foreign exchange conversion to fund the IBM purchase. (Buy $71,480.00 for &#163;54,846.60)  * The third transaction is an alternate version of the above trades. Buying 500 IBM shares and settling directly in Sterling.  | Column |  Buy Trade | Fx Trade | Buy Trade with foreign Settlement | | ----- | ----- | ----- | ----- | | TransactionId | FBN00001 | FBN00002 | FBN00003 | | Type | Buy | FxBuy | Buy | | InstrumentUid | FIGI_BBG000BLNNH6 | CCY_USD | FIGI_BBG000BLNNH6 | | TransactionDate | 2018-08-02 | 2018-08-02 | 2018-08-02 | | SettlementDate | 2018-08-06 | 2018-08-06 | 2018-08-06 | | Units | 500 | 71480 | 500 | | TransactionPrice | 142.96 | 1 | 142.96 | | TradeCurrency | USD | USD | USD | | ExchangeRate | 1 | 0.7673 | 0.7673 | | TotalConsideration.Amount | 71480.00 | 54846.60 | 54846.60 | | TotalConsideration.Currency | USD | GBP | GBP | | Trade/default/TradeToPortfolioRate&ast; | 0.7673 | 0.7673 | 0.7673 |  [&ast; This is a property field]  #### A Forward FX Example  LUSID has a flexible transaction modelling system, and there are a number of different ways of modelling forward fx trades.  The default LUSID transaction types are FwdFxBuy and FwdFxSell. Other types and behaviours can be configured as required.  Using these transaction types, the holdings query will report two forward positions. One in each currency.   Since an FX trade is an exchange of one currency for another, the following two 6 month forward transactions are equivalent:  | Column |  Forward 'Sell' Trade | Forward 'Buy' Trade | | ----- | ----- | ----- | | TransactionId | FBN00004 | FBN00005 | | Type | FwdFxSell | FwdFxBuy | | InstrumentUid | CCY_GBP | CCY_USD | | TransactionDate | 2018-08-02 | 2018-08-02 | | SettlementDate | 2019-02-06 | 2019-02-06 | | Units | 10000.00 | 13142.00 | | TransactionPrice |1 | 1 | | TradeCurrency | GBP | USD | | ExchangeRate | 1.3142 | 0.760919 | | TotalConsideration.Amount | 13142.00 | 10000.00 | | TotalConsideration.Currency | USD | GBP | | Trade/default/TradeToPortfolioRate | 1.0 | 0.760919 |  ## Holdings  A holding represents a position in a instrument or cash on a given date.  | Field|Type|Description | | ---|---|--- | | InstrumentUid|string|Unique instrument identifier | | HoldingType|string|Type of holding, eg Position, Balance, CashCommitment, Receivable, ForwardFX | | Units|decimal|Quantity of holding | | SettledUnits|decimal|Settled quantity of holding | | Cost|currencyandamount|Book cost of holding in transaction currency | | CostPortfolioCcy|currencyandamount|Book cost of holding in portfolio currency | | Transaction|Transaction|If this is commitment-type holding, the transaction behind it |   ## Corporate Actions  Corporate actions are represented within LUSID in terms of a set of instrument-specific 'transitions'.  These transitions are used to specify the participants of the corporate action, and the effect that the corporate action will have on holdings in those participants.  *Corporate action*  | Field|Type|Description | | ---|---|--- | | SourceId|id|  | | CorporateActionCode|code|  | | AnnouncementDate|datetime|  | | ExDate|datetime|  | | RecordDate|datetime|  | | PaymentDate|datetime|  |    *Transition*  | Field|Type|Description | | ---|---|--- |   ## Property  Properties are key-value pairs that can be applied to any entity within a domain (where a domain is `trade`, `portfolio`, `security` etc).  Properties must be defined before use with a `PropertyDefinition` and can then subsequently be added to entities.  # Schemas  The following headers are returned on all responses from LUSID  | Name | Purpose | | --- | --- | | lusid-meta-duration | Duration of the request | | lusid-meta-success | Whether or not LUSID considered the request to be successful | | lusid-meta-requestId | The unique identifier for the request | | lusid-schema-url | Url of the schema for the data being returned | | lusid-property-schema-url | Url of the schema for any properties |   # Error Codes  | Code|Name|Description | | ---|---|--- | | <a name=\"102\">102</a>|VersionNotFound|  | | <a name=\"104\">104</a>|InstrumentNotFound|  | | <a name=\"105\">105</a>|PropertyNotFound|  | | <a name=\"106\">106</a>|PortfolioRecursionDepth|  | | <a name=\"108\">108</a>|GroupNotFound|  | | <a name=\"109\">109</a>|PortfolioNotFound|  | | <a name=\"110\">110</a>|PropertySchemaNotFound|  | | <a name=\"111\">111</a>|PortfolioAncestryNotFound|  | | <a name=\"112\">112</a>|PortfolioWithIdAlreadyExists|  | | <a name=\"113\">113</a>|OrphanedPortfolio|  | | <a name=\"119\">119</a>|MissingBaseClaims|  | | <a name=\"121\">121</a>|PropertyNotDefined|  | | <a name=\"122\">122</a>|CannotDeleteSystemProperty|  | | <a name=\"123\">123</a>|CannotModifyImmutablePropertyField|  | | <a name=\"124\">124</a>|PropertyAlreadyExists|  | | <a name=\"125\">125</a>|InvalidPropertyLifeTime|  | | <a name=\"127\">127</a>|CannotModifyDefaultDataType|  | | <a name=\"128\">128</a>|GroupAlreadyExists|  | | <a name=\"129\">129</a>|NoSuchDataType|  | | <a name=\"132\">132</a>|ValidationError|  | | <a name=\"133\">133</a>|LoopDetectedInGroupHierarchy|  | | <a name=\"135\">135</a>|SubGroupAlreadyExists|  | | <a name=\"138\">138</a>|PriceSourceNotFound|  | | <a name=\"139\">139</a>|AnalyticStoreNotFound|  | | <a name=\"141\">141</a>|AnalyticStoreAlreadyExists|  | | <a name=\"143\">143</a>|ClientInstrumentAlreadyExists|  | | <a name=\"144\">144</a>|DuplicateInParameterSet|  | | <a name=\"147\">147</a>|ResultsNotFound|  | | <a name=\"148\">148</a>|OrderFieldNotInResultSet|  | | <a name=\"149\">149</a>|OperationFailed|  | | <a name=\"150\">150</a>|ElasticSearchError|  | | <a name=\"151\">151</a>|InvalidParameterValue|  | | <a name=\"153\">153</a>|CommandProcessingFailure|  | | <a name=\"154\">154</a>|EntityStateConstructionFailure|  | | <a name=\"155\">155</a>|EntityTimelineDoesNotExist|  | | <a name=\"156\">156</a>|EventPublishFailure|  | | <a name=\"157\">157</a>|InvalidRequestFailure|  | | <a name=\"158\">158</a>|EventPublishUnknown|  | | <a name=\"159\">159</a>|EventQueryFailure|  | | <a name=\"160\">160</a>|BlobDidNotExistFailure|  | | <a name=\"162\">162</a>|SubSystemRequestFailure|  | | <a name=\"163\">163</a>|SubSystemConfigurationFailure|  | | <a name=\"165\">165</a>|FailedToDelete|  | | <a name=\"166\">166</a>|UpsertClientInstrumentFailure|  | | <a name=\"167\">167</a>|IllegalAsAtInterval|  | | <a name=\"168\">168</a>|IllegalBitemporalQuery|  | | <a name=\"169\">169</a>|InvalidAlternateId|  | | <a name=\"170\">170</a>|CannotAddSourcePortfolioPropertyExplicitly|  | | <a name=\"171\">171</a>|EntityAlreadyExistsInGroup|  | | <a name=\"173\">173</a>|EntityWithIdAlreadyExists|  | | <a name=\"174\">174</a>|DerivedPortfolioDetailsDoNotExist|  | | <a name=\"176\">176</a>|PortfolioWithNameAlreadyExists|  | | <a name=\"177\">177</a>|InvalidTransactions|  | | <a name=\"178\">178</a>|ReferencePortfolioNotFound|  | | <a name=\"179\">179</a>|DuplicateIdFailure|  | | <a name=\"180\">180</a>|CommandRetrievalFailure|  | | <a name=\"181\">181</a>|DataFilterApplicationFailure|  | | <a name=\"182\">182</a>|SearchFailed|  | | <a name=\"183\">183</a>|MovementsEngineConfigurationKeyFailure|  | | <a name=\"184\">184</a>|FxRateSourceNotFound|  | | <a name=\"185\">185</a>|AccrualSourceNotFound|  | | <a name=\"186\">186</a>|AccessDenied|  | | <a name=\"187\">187</a>|InvalidIdentityToken|  | | <a name=\"188\">188</a>|InvalidRequestHeaders|  | | <a name=\"189\">189</a>|PriceNotFound|  | | <a name=\"190\">190</a>|InvalidSubHoldingKeysProvided|  | | <a name=\"191\">191</a>|DuplicateSubHoldingKeysProvided|  | | <a name=\"192\">192</a>|CutDefinitionNotFound|  | | <a name=\"193\">193</a>|CutDefinitionInvalid|  | | <a name=\"200\">200</a>|InvalidUnitForDataType|  | | <a name=\"201\">201</a>|InvalidTypeForDataType|  | | <a name=\"202\">202</a>|InvalidValueForDataType|  | | <a name=\"203\">203</a>|UnitNotDefinedForDataType|  | | <a name=\"204\">204</a>|UnitsNotSupportedOnDataType|  | | <a name=\"205\">205</a>|CannotSpecifyUnitsOnDataType|  | | <a name=\"206\">206</a>|UnitSchemaInconsistentWithDataType|  | | <a name=\"207\">207</a>|UnitDefinitionNotSpecified|  | | <a name=\"208\">208</a>|DuplicateUnitDefinitionsSpecified|  | | <a name=\"209\">209</a>|InvalidUnitsDefinition|  | | <a name=\"210\">210</a>|InvalidInstrumentIdentifierUnit|  | | <a name=\"211\">211</a>|HoldingsAdjustmentDoesNotExist|  | | <a name=\"212\">212</a>|CouldNotBuildExcelUrl|  | | <a name=\"213\">213</a>|CouldNotGetExcelVersion|  | | <a name=\"214\">214</a>|InstrumentByCodeNotFound|  | | <a name=\"215\">215</a>|EntitySchemaDoesNotExist|  | | <a name=\"216\">216</a>|FeatureNotSupportedOnPortfolioType|  | | <a name=\"217\">217</a>|QuoteNotFoundFailure|  | | <a name=\"219\">219</a>|InvalidInstrumentDefinition|  | | <a name=\"221\">221</a>|InstrumentUpsertFailure|  | | <a name=\"222\">222</a>|ReferencePortfolioRequestNotSupported|  | | <a name=\"223\">223</a>|TransactionPortfolioRequestNotSupported|  | | <a name=\"224\">224</a>|InvalidPropertyValueAssignment|  | | <a name=\"230\">230</a>|TransactionTypeNotFound|  | | <a name=\"231\">231</a>|TransactionTypeDuplication|  | | <a name=\"232\">232</a>|PortfolioDoesNotExistAtGivenDate|  | | <a name=\"233\">233</a>|QueryParserFailure|  | | <a name=\"234\">234</a>|DuplicateConstituentFailure|  | | <a name=\"235\">235</a>|UnresolvedInstrumentConstituentFailure|  | | <a name=\"236\">236</a>|UnresolvedInstrumentInTransitionFailure|  | | <a name=\"300\">300</a>|MissingRecipeFailure|  | | <a name=\"301\">301</a>|DependenciesFailure|  | | <a name=\"304\">304</a>|PortfolioPreprocessFailure|  | | <a name=\"310\">310</a>|ValuationEngineFailure|  | | <a name=\"311\">311</a>|TaskFactoryFailure|  | | <a name=\"312\">312</a>|TaskEvaluationFailure|  | | <a name=\"350\">350</a>|InstrumentFailure|  | | <a name=\"351\">351</a>|CashFlowsFailure|  | | <a name=\"370\">370</a>|ResultRetrievalFailure|  | | <a name=\"371\">371</a>|ResultProcessingFailure|  | | <a name=\"372\">372</a>|VendorResultProcessingFailure|  | | <a name=\"374\">374</a>|AttemptToUpsertDuplicateQuotes|  | | <a name=\"375\">375</a>|CorporateActionSourceDoesNotExist|  | | <a name=\"376\">376</a>|InstrumentIdentifierAlreadyInUse|  | | <a name=\"-10\">-10</a>|ServerConfigurationError|  | | <a name=\"-1\">-1</a>|Unknown error|  |   # noqa: E501

    OpenAPI spec version: 0.10.33
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient


class TransactionPortfoliosApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_transaction_property(self, scope, code, transaction_id, **kwargs):  # noqa: E501
        """Add transaction properties  # noqa: E501

        Upsert one or more transaction properties to a single transaction in a portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_transaction_property(scope, code, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param str transaction_id: Id of transaction (required)
        :param dict(str, PerpetualPropertyValue) request_body: Transaction properties values
        :return: AddTransactionPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_transaction_property_with_http_info(scope, code, transaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_transaction_property_with_http_info(scope, code, transaction_id, **kwargs)  # noqa: E501
            return data

    def add_transaction_property_with_http_info(self, scope, code, transaction_id, **kwargs):  # noqa: E501
        """Add transaction properties  # noqa: E501

        Upsert one or more transaction properties to a single transaction in a portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_transaction_property_with_http_info(scope, code, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param str transaction_id: Id of transaction (required)
        :param dict(str, PerpetualPropertyValue) request_body: Transaction properties values
        :return: AddTransactionPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'transaction_id', 'request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_transaction_property" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `add_transaction_property`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `add_transaction_property`")  # noqa: E501
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in local_var_params or
                local_var_params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `add_transaction_property`")  # noqa: E501

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
        if 'request_body' in local_var_params:
            body_params = local_var_params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddTransactionPropertyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def adjust_holdings(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Adjust holdings  # noqa: E501

        Adjust one or more holdings in a transaction portfolio    Prompt the creation of transactions in a specific transaction portfolio to bring selected holdings to the specified targets  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adjust_holdings(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: The effective date of the change (required)
        :param list[AdjustHoldingRequest] adjust_holding_request: The selected set of holdings adjustments
        :return: AdjustHolding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.adjust_holdings_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501
        else:
            (data) = self.adjust_holdings_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501
            return data

    def adjust_holdings_with_http_info(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Adjust holdings  # noqa: E501

        Adjust one or more holdings in a transaction portfolio    Prompt the creation of transactions in a specific transaction portfolio to bring selected holdings to the specified targets  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.adjust_holdings_with_http_info(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: The effective date of the change (required)
        :param list[AdjustHoldingRequest] adjust_holding_request: The selected set of holdings adjustments
        :return: AdjustHolding
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at', 'adjust_holding_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adjust_holdings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `adjust_holdings`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `adjust_holdings`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if ('effective_at' not in local_var_params or
                local_var_params['effective_at'] is None):
            raise ValueError("Missing the required parameter `effective_at` when calling `adjust_holdings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501
        if 'effective_at' in local_var_params:
            path_params['effectiveAt'] = local_var_params['effective_at']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'adjust_holding_request' in local_var_params:
            body_params = local_var_params['adjust_holding_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt}', 'POST',
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

    def build_transactions(self, scope, code, **kwargs):  # noqa: E501
        """Build output transactions  # noqa: E501

        Builds and returns the collection of all types of transactions that affect the holdings of a portfolio in to a set of output transactions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.build_transactions(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime as_at: Optional. The AsAt date of the data
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param list[str] instrument_property_keys: Optional. Keys for the instrument property values to be decorated onto the transactions
        :param str filter: Optional. Expression to filter the result set
        :param TransactionQueryParameters transaction_query_parameters: Optional. Transaction query parameters
        :return: VersionedResourceListOfOutputTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.build_transactions_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.build_transactions_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def build_transactions_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Build output transactions  # noqa: E501

        Builds and returns the collection of all types of transactions that affect the holdings of a portfolio in to a set of output transactions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.build_transactions_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime as_at: Optional. The AsAt date of the data
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param list[str] instrument_property_keys: Optional. Keys for the instrument property values to be decorated onto the transactions
        :param str filter: Optional. Expression to filter the result set
        :param TransactionQueryParameters transaction_query_parameters: Optional. Transaction query parameters
        :return: VersionedResourceListOfOutputTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'as_at', 'sort_by', 'start', 'limit', 'instrument_property_keys', 'filter', 'transaction_query_parameters']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method build_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `build_transactions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `build_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'sort_by' in local_var_params:
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
            collection_formats['sortBy'] = 'multi'  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'instrument_property_keys' in local_var_params:
            query_params.append(('instrumentPropertyKeys', local_var_params['instrument_property_keys']))  # noqa: E501
            collection_formats['instrumentPropertyKeys'] = 'multi'  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transaction_query_parameters' in local_var_params:
            body_params = local_var_params['transaction_query_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

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
        """Cancel holdings adjustments  # noqa: E501

        Cancel previous adjust-holdings for the portfolio for a specific date  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_adjust_holdings(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: The effective date of the change (required)
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_adjust_holdings_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_adjust_holdings_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501
            return data

    def cancel_adjust_holdings_with_http_info(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Cancel holdings adjustments  # noqa: E501

        Cancel previous adjust-holdings for the portfolio for a specific date  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_adjust_holdings_with_http_info(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: The effective date of the change (required)
        :return: DeletedEntityResponse
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_adjust_holdings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `cancel_adjust_holdings`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `cancel_adjust_holdings`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if ('effective_at' not in local_var_params or
                local_var_params['effective_at'] is None):
            raise ValueError("Missing the required parameter `effective_at` when calling `cancel_adjust_holdings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501
        if 'effective_at' in local_var_params:
            path_params['effectiveAt'] = local_var_params['effective_at']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt}', 'DELETE',
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

    def create_portfolio(self, scope, **kwargs):  # noqa: E501
        """Create transaction portfolio  # noqa: E501

        Create a transaction portfolio in a specific scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_portfolio(scope, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope into which the transaction portfolio will be created (required)
        :param CreateTransactionPortfolioRequest create_transaction_portfolio_request: The transaction portfolio definition
        :return: Portfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_portfolio_with_http_info(scope, **kwargs)  # noqa: E501
        else:
            (data) = self.create_portfolio_with_http_info(scope, **kwargs)  # noqa: E501
            return data

    def create_portfolio_with_http_info(self, scope, **kwargs):  # noqa: E501
        """Create transaction portfolio  # noqa: E501

        Create a transaction portfolio in a specific scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_portfolio_with_http_info(scope, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope into which the transaction portfolio will be created (required)
        :param CreateTransactionPortfolioRequest create_transaction_portfolio_request: The transaction portfolio definition
        :return: Portfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'create_transaction_portfolio_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_portfolio" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `create_portfolio`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_transaction_portfolio_request' in local_var_params:
            body_params = local_var_params['create_transaction_portfolio_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

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

    def delete_executions(self, scope, code, **kwargs):  # noqa: E501
        """Delete executions  # noqa: E501

        Delete one or more executions from a transaction portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_executions(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param list[str] execution_ids: Ids of executions to delete
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_executions_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_executions_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def delete_executions_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Delete executions  # noqa: E501

        Delete one or more executions from a transaction portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_executions_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param list[str] execution_ids: Ids of executions to delete
        :return: DeletedEntityResponse
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_executions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `delete_executions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `delete_executions`")  # noqa: E501

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

    def delete_property_from_transaction(self, scope, code, transaction_id, **kwargs):  # noqa: E501
        """Delete transaction property  # noqa: E501

        Delete a property value from a single transaction in a portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_property_from_transaction(scope, code, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: Code for the portfolio (required)
        :param str transaction_id: Id of the transaction to delete the property from (required)
        :param str transaction_property_key: The key of the property to be deleted
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_property_from_transaction_with_http_info(scope, code, transaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_property_from_transaction_with_http_info(scope, code, transaction_id, **kwargs)  # noqa: E501
            return data

    def delete_property_from_transaction_with_http_info(self, scope, code, transaction_id, **kwargs):  # noqa: E501
        """Delete transaction property  # noqa: E501

        Delete a property value from a single transaction in a portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_property_from_transaction_with_http_info(scope, code, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: Code for the portfolio (required)
        :param str transaction_id: Id of the transaction to delete the property from (required)
        :param str transaction_property_key: The key of the property to be deleted
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'transaction_id', 'transaction_property_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_property_from_transaction" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `delete_property_from_transaction`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `delete_property_from_transaction`")  # noqa: E501
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in local_var_params or
                local_var_params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `delete_property_from_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501
        if 'transaction_id' in local_var_params:
            path_params['transactionId'] = local_var_params['transaction_id']  # noqa: E501

        query_params = []
        if 'transaction_property_key' in local_var_params:
            query_params.append(('transactionPropertyKey', local_var_params['transaction_property_key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

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

    def delete_transactions(self, scope, code, **kwargs):  # noqa: E501
        """Delete transactions  # noqa: E501

        Delete one or more transactions from a transaction portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_transactions(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param list[str] transaction_ids: Ids of transactions to delete
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_transactions_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_transactions_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def delete_transactions_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Delete transactions  # noqa: E501

        Delete one or more transactions from a transaction portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_transactions_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param list[str] transaction_ids: Ids of transactions to delete
        :return: DeletedEntityResponse
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `delete_transactions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `delete_transactions`")  # noqa: E501

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

    def get_details(self, scope, code, **kwargs):  # noqa: E501
        """Get portfolio details  # noqa: E501

        Get the details document associated with a transaction portfolio                When requesting details from a derived transaction portfolio, the returned set of details could come from a different transaction portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_details(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: Optional. The effective date of the data
        :param datetime as_at: Optional. The AsAt date of the data
        :return: PortfolioDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_details_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_details_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def get_details_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Get portfolio details  # noqa: E501

        Get the details document associated with a transaction portfolio                When requesting details from a derived transaction portfolio, the returned set of details could come from a different transaction portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_details_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: Optional. The effective date of the data
        :param datetime as_at: Optional. The AsAt date of the data
        :return: PortfolioDetails
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `get_details`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_details`")  # noqa: E501

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

        Get the aggregate holdings of a transaction portfolio.  If no effectiveAt or asAt  are supplied then values will be defaulted to the latest system time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_holdings(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param bool by_taxlots: Option to expand holdings to return the underlying tax-lots
        :param datetime effective_at: Optional. The effective date of the portfolio
        :param datetime as_at: Optional. The AsAt date of the data
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param str filter: Optional. Expression to filter the result set
        :param list[str] instrument_property_keys: Optional. Keys for the instrument property values to be decorated onto the holdings
        :return: VersionedResourceListOfPortfolioHolding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_holdings_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_holdings_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def get_holdings_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Get holdings  # noqa: E501

        Get the aggregate holdings of a transaction portfolio.  If no effectiveAt or asAt  are supplied then values will be defaulted to the latest system time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_holdings_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param bool by_taxlots: Option to expand holdings to return the underlying tax-lots
        :param datetime effective_at: Optional. The effective date of the portfolio
        :param datetime as_at: Optional. The AsAt date of the data
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param str filter: Optional. Expression to filter the result set
        :param list[str] instrument_property_keys: Optional. Keys for the instrument property values to be decorated onto the holdings
        :return: VersionedResourceListOfPortfolioHolding
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'by_taxlots', 'effective_at', 'as_at', 'sort_by', 'start', 'limit', 'filter', 'instrument_property_keys']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_holdings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `get_holdings`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_holdings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'by_taxlots' in local_var_params:
            query_params.append(('byTaxlots', local_var_params['by_taxlots']))  # noqa: E501
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'sort_by' in local_var_params:
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
            collection_formats['sortBy'] = 'multi'  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'instrument_property_keys' in local_var_params:
            query_params.append(('instrumentPropertyKeys', local_var_params['instrument_property_keys']))  # noqa: E501
            collection_formats['instrumentPropertyKeys'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

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
        """Get holding adjustment  # noqa: E501

        Get a holdings adjustment for a transaction portfolio at a specific effective time.    A holdings adjustment definition will only be returned if one exists for the specified effective time  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_holdings_adjustment(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: The effective time of the holdings adjustment (required)
        :param datetime as_at: Optional. The AsAt date of the data
        :return: HoldingsAdjustment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_holdings_adjustment_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501
        else:
            (data) = self.get_holdings_adjustment_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501
            return data

    def get_holdings_adjustment_with_http_info(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Get holding adjustment  # noqa: E501

        Get a holdings adjustment for a transaction portfolio at a specific effective time.    A holdings adjustment definition will only be returned if one exists for the specified effective time  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_holdings_adjustment_with_http_info(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: The effective time of the holdings adjustment (required)
        :param datetime as_at: Optional. The AsAt date of the data
        :return: HoldingsAdjustment
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_holdings_adjustment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `get_holdings_adjustment`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_holdings_adjustment`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if ('effective_at' not in local_var_params or
                local_var_params['effective_at'] is None):
            raise ValueError("Missing the required parameter `effective_at` when calling `get_holdings_adjustment`")  # noqa: E501

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

        Get the transactions from a transaction portfolio    When the requested portfolio is a derived transaction portfolio, the returned set of transactions is the union set of all transactions of the parent (and ancestors) and the specified portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime from_transaction_date: Optional. Limit the returned transactions to those with a transaction date equal or later than this date
        :param datetime to_transaction_date: Optional. Limit the returned transactions to those with a transaction date equal or before this date
        :param datetime as_at: Optional. The AsAt date of the data
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param list[str] instrument_property_keys: Optional. Keys for the instrument property values that will be decorated onto the transactions
        :param str filter: Optional. Expression to filter the result set
        :return: VersionedResourceListOfTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transactions_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transactions_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def get_transactions_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Get transactions  # noqa: E501

        Get the transactions from a transaction portfolio    When the requested portfolio is a derived transaction portfolio, the returned set of transactions is the union set of all transactions of the parent (and ancestors) and the specified portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime from_transaction_date: Optional. Limit the returned transactions to those with a transaction date equal or later than this date
        :param datetime to_transaction_date: Optional. Limit the returned transactions to those with a transaction date equal or before this date
        :param datetime as_at: Optional. The AsAt date of the data
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param list[str] instrument_property_keys: Optional. Keys for the instrument property values that will be decorated onto the transactions
        :param str filter: Optional. Expression to filter the result set
        :return: VersionedResourceListOfTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'from_transaction_date', 'to_transaction_date', 'as_at', 'sort_by', 'start', 'limit', 'instrument_property_keys', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `get_transactions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_transactions`")  # noqa: E501

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
        if 'sort_by' in local_var_params:
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
            collection_formats['sortBy'] = 'multi'  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'instrument_property_keys' in local_var_params:
            query_params.append(('instrumentPropertyKeys', local_var_params['instrument_property_keys']))  # noqa: E501
            collection_formats['instrumentPropertyKeys'] = 'multi'  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

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

        Get holdings adjustments from a transaction portfolio in an interval of effective time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings_adjustments(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: Code for the portfolio (required)
        :param datetime from_effective_at: Holdings adjustments between this time (inclusive) and the toEffectiveAt are returned.
        :param datetime to_effective_at: Holdings adjustments between this time (inclusive) and the fromEffectiveAt are returned.
        :param datetime as_at: Optional. The AsAt date of the data
        :return: ResourceListOfHoldingsAdjustmentHeader
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_holdings_adjustments_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.list_holdings_adjustments_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def list_holdings_adjustments_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """List holdings adjustments  # noqa: E501

        Get holdings adjustments from a transaction portfolio in an interval of effective time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings_adjustments_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: Code for the portfolio (required)
        :param datetime from_effective_at: Holdings adjustments between this time (inclusive) and the toEffectiveAt are returned.
        :param datetime to_effective_at: Holdings adjustments between this time (inclusive) and the fromEffectiveAt are returned.
        :param datetime as_at: Optional. The AsAt date of the data
        :return: ResourceListOfHoldingsAdjustmentHeader
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_holdings_adjustments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `list_holdings_adjustments`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `list_holdings_adjustments`")  # noqa: E501

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

    def set_holdings(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Set all holdings on a transaction portfolio  # noqa: E501

        Prompt the creation of transactions in a specific transaction portfolio to bring all holdings to the specified targets  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_holdings(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the transaction portfolio (required)
        :param str code: The code of the transaction portfolio (required)
        :param datetime effective_at: The effective date of the change (required)
        :param list[AdjustHoldingRequest] adjust_holding_request: The complete set of holdings adjustments for the portfolio
        :return: AdjustHolding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_holdings_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501
        else:
            (data) = self.set_holdings_with_http_info(scope, code, effective_at, **kwargs)  # noqa: E501
            return data

    def set_holdings_with_http_info(self, scope, code, effective_at, **kwargs):  # noqa: E501
        """Set all holdings on a transaction portfolio  # noqa: E501

        Prompt the creation of transactions in a specific transaction portfolio to bring all holdings to the specified targets  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_holdings_with_http_info(scope, code, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the transaction portfolio (required)
        :param str code: The code of the transaction portfolio (required)
        :param datetime effective_at: The effective date of the change (required)
        :param list[AdjustHoldingRequest] adjust_holding_request: The complete set of holdings adjustments for the portfolio
        :return: AdjustHolding
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at', 'adjust_holding_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_holdings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `set_holdings`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `set_holdings`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if ('effective_at' not in local_var_params or
                local_var_params['effective_at'] is None):
            raise ValueError("Missing the required parameter `effective_at` when calling `set_holdings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501
        if 'effective_at' in local_var_params:
            path_params['effectiveAt'] = local_var_params['effective_at']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'adjust_holding_request' in local_var_params:
            body_params = local_var_params['adjust_holding_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt}', 'PUT',
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
        """Upsert executions  # noqa: E501

        Inserts new executions, or updates those already present  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_executions(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param list[ExecutionRequest] execution_request: The executions to be updated
        :return: UpsertPortfolioExecutionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upsert_executions_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.upsert_executions_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def upsert_executions_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Upsert executions  # noqa: E501

        Inserts new executions, or updates those already present  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_executions_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param list[ExecutionRequest] execution_request: The executions to be updated
        :return: UpsertPortfolioExecutionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'execution_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_executions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `upsert_executions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `upsert_executions`")  # noqa: E501

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
        if 'execution_request' in local_var_params:
            body_params = local_var_params['execution_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

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

    def upsert_portfolio_details(self, scope, code, **kwargs):  # noqa: E501
        """Upsert details  # noqa: E501

        Update the portfolio details for the specified transaction portfolios or add if it doesn't already exist (in the case of a derived transaction portfolio).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_portfolio_details(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: Optional. The effective date of the change
        :param CreatePortfolioDetails create_portfolio_details: The set of details for the portfolio
        :return: PortfolioDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upsert_portfolio_details_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.upsert_portfolio_details_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def upsert_portfolio_details_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Upsert details  # noqa: E501

        Update the portfolio details for the specified transaction portfolios or add if it doesn't already exist (in the case of a derived transaction portfolio).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_portfolio_details_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code of the portfolio (required)
        :param datetime effective_at: Optional. The effective date of the change
        :param CreatePortfolioDetails create_portfolio_details: The set of details for the portfolio
        :return: PortfolioDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at', 'create_portfolio_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_portfolio_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `upsert_portfolio_details`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `upsert_portfolio_details`")  # noqa: E501

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
        if 'create_portfolio_details' in local_var_params:
            body_params = local_var_params['create_portfolio_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

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

    def upsert_transactions(self, scope, code, **kwargs):  # noqa: E501
        """Upsert transactions into the specified transaction portfolio  # noqa: E501

        Upsert transactions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_transactions(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code for the portfolio (required)
        :param list[TransactionRequest] transaction_request: The transactions to be upserted
        :return: UpsertPortfolioTransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upsert_transactions_with_http_info(scope, code, **kwargs)  # noqa: E501
        else:
            (data) = self.upsert_transactions_with_http_info(scope, code, **kwargs)  # noqa: E501
            return data

    def upsert_transactions_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Upsert transactions into the specified transaction portfolio  # noqa: E501

        Upsert transactions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_transactions_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: The scope of the portfolio (required)
        :param str code: The code for the portfolio (required)
        :param list[TransactionRequest] transaction_request: The transactions to be upserted
        :return: UpsertPortfolioTransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'transaction_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `upsert_transactions`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `upsert_transactions`")  # noqa: E501

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
        if 'transaction_request' in local_var_params:
            body_params = local_var_params['transaction_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

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
