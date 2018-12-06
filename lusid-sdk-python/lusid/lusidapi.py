# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from . import models


class LUSIDAPIConfiguration(Configuration):
    """Configuration for LUSIDAPI
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'http://localhost'

        super(LUSIDAPIConfiguration, self).__init__(base_url)

        self.add_user_agent('lusidapi/{}'.format(VERSION))

        self.credentials = credentials


class LUSIDAPI(object):
    """# Introduction
    This page documents the [LUSID APIs](https://api.lusid.com/swagger), which allows authorised clients to query and update their data within the LUSID platform.
    SDKs to interact with the LUSID APIs are available in the following languages :
    * [C#](https://github.com/finbourne/lusid-sdk-csharp)
    * [Java](https://github.com/finbourne/lusid-sdk-java)
    * [JavaScript](https://github.com/finbourne/lusid-sdk-js)
    * [Python](https://github.com/finbourne/lusid-sdk-python)
    # Data Model
    The LUSID API has a relatively lightweight but extremely powerful data model.   One of the goals of LUSID was not to enforce on clients a single rigid data model but rather to provide a flexible foundation onto which clients can streamline their data.   One of the primary tools to extend the data model is through using properties.  Properties can be associated with amongst others: -
    * Transactions
    * Instruments
    * Portfolios
    The LUSID data model is exposed through the LUSID APIs.  The APIs provide access to both business objects and the meta data used to configure the systems behaviours.   The key business entities are: -
    * **Portfolios**
    A portfolio is the primary container for transactions and holdings.
    * **Derived Portfolios**
    Derived portfolios allow portfolios to be created based on other portfolios, by overriding or overlaying specific items
    * **Holdings**
    A holding is a position account for a instrument within a portfolio.  Holdings can only be adjusted via transactions.
    * **Transactions**
    A Transaction is a source of transactions used to manipulate holdings.
    * **Corporate Actions**
    A corporate action is a market event which occurs to a instrument, for example a stock split
    * **Instruments**
    A instrument represents a currency, tradable instrument or OTC contract that is attached to a transaction and a holding.
    * **Properties**
    Several entities allow additional user defined properties to be associated with them.   For example, a Portfolio manager may be associated with a portfolio
    Meta data includes: -
    * **Transaction Types**
    Transactions are booked with a specific transaction type.  The types are client defined and are used to map the Transaction to a series of movements which update the portfolio holdings.
    * **Properties Types**
    Types of user defined properties used within the system.
    This section describes the data model that LUSID exposes via the APIs.
    ## Scope
    All data in LUSID is segregated at the client level.  Entities in LUSID are identifiable by a unique code.  Every entity lives within a logical data partition known as a Scope.  Scope is an identity namespace allowing two entities with the same unique code to co-exist within individual address spaces.
    For example, prices for equities from different vendors may be uploaded into different scopes such as `client/vendor1` and `client/vendor2`.  A portfolio may then be valued using either of the price sources by referencing the appropriate scope.
    LUSID Clients cannot access scopes of other clients.
    ## Schema
    A detailed description of the entities used by the API and parameters for endpoints which take a JSON document can be retrieved via the `schema` endpoint.
    ## Instruments
    LUSID has its own built-in instrument master which you can use to master your own instrument universe.
    Every instrument must be created with one or more unique market identifiers, such as [FIGI](https://openfigi.com/) or RIC code. For any non-listed instruments (eg OTCs), you can upload an instrument against a custom ID of your choosing.
    In addition, LUSID will allocate each instrument a unique 'LUSID instrument identifier'. The LUSID instrument identifier is what is used when uploading transactions, holdings, prices, etc. The API exposes an `instrument/lookup` endpoint which can be used to lookup these LUSID identifiers using their market identifiers.
    Cash can be referenced using the ISO currency code prefixed with "`CCY_`" e.g. `CCY_GBP`
    ## Instrument Prices (Analytics)
    Instrument prices are stored in LUSID's Analytics Store
    | Field|Type|Description |
    | ---|---|--- |
    | InstrumentUid|string|Unique instrument identifier |
    | Value|decimal|Value of the analytic, eg price |
    | Denomination|string|Underlying unit of the analytic, eg currency, EPS etc. |
    ## Instrument Data
    Instrument data can be uploaded to the system using the [Instrument Properties](#tag/InstrumentProperties) endpoint.
    | Field|Type|Description |
    | ---|---|--- |
    | LusidInstrumentId|string|Unique instrument identifier |
    ## Portfolios
    Portfolios are the top-level entity containers within LUSID, containing transactions, corporate actions and holdings.    The transactions build up the portfolio holdings on which valuations, analytics profit &amp; loss and risk can be calculated.
    Properties can be associated with Portfolios to add in additional model data.  Portfolio properties can be changed over time as well.  For example, to allow a Portfolio Manager to be linked with a Portfolio.
    Additionally, portfolios can be securitised and held by other portfolios, allowing LUSID to perform "drill-through" into underlying fund holdings
    ### Reference Portfolios
    Reference portfolios are portfolios that contain only weights, as opposed to transactions, and are designed to represent entities such as indices.
    ### Derived Portfolios
    LUSID also allows for a portfolio to be composed of another portfolio via derived portfolios.  A derived portfolio can contain its own transactions and also inherits any transactions from its parent portfolio.  Any changes made to the parent portfolio are automatically reflected in derived portfolio.
    Derived portfolios in conjunction with scopes are a powerful construct.  For example, to do pre-trade what-if analysis, a derived portfolio could be created a new namespace linked to the underlying live (parent) portfolio.  Analysis can then be undertaken on the derived portfolio without affecting the live portfolio.
    ### Portfolio Groups
    Portfolio groups allow the construction of a hierarchy from portfolios and groups.  Portfolio operations on the group are executed on an aggregated set of portfolios in the hierarchy.
    For example:
    * Global Portfolios _(group)_
      * APAC _(group)_
        * Hong Kong _(portfolio)_
        * Japan _(portfolio)_
      * Europe _(group)_
        * France _(portfolio)_
        * Germany _(portfolio)_
      * UK _(portfolio)_
    In this example **Global Portfolios** is a group that consists of an aggregate of **Hong Kong**, **Japan**, **France**, **Germany** and **UK** portfolios.
    ### Movements Engine
    The Movements engine sits on top of the immutable event store and is used to manage the relationship between input trading actions and their associated portfolio holdings.
    The movements engine reads in the following entity types:-
    * Posting Transactions
    * Applying Corporate Actions
    * Holding Adjustments
    These are converted to one or more movements and used by the movements engine to calculate holdings.  At the same time it also calculates running balances, and realised P&amp;L.  The outputs from the movements engine are holdings and transactions.
    ## Transactions
    A transaction represents an economic activity against a Portfolio.
    Transactions are processed according to a configuration. This will tell the LUSID engine how to interpret the transaction and correctly update the holdings. LUSID comes with a set of transaction types you can use out of the box, or you can configure your own set(s) of transactions.
    For more details see the [LUSID Getting Started Guide for transaction configuration.](https://support.finbourne.com/hc/en-us/articles/360016737511-Configuring-Transaction-Types)
    | Field|Type|Description |
    | ---|---|--- |
    | TransactionId|string|Unique transaction identifier |
    | Type|string|LUSID transaction type code - Buy, Sell, StockIn, StockOut, etc |
    | InstrumentUid|string|Unique instrument identifier |
    | TransactionDate|datetime|Transaction date |
    | SettlementDate|datetime|Settlement date |
    | Units|decimal|Quantity of transaction in units of the instrument |
    | TransactionPrice|tradeprice|Execution price for the transaction |
    | TotalConsideration|currencyandamount|Total value of the transaction in settlement currency |
    | ExchangeRate|decimal|Rate between transaction and settle currency |
    | TransactionCurrency|currency|Transaction currency |
    | CounterpartyId|string|Counterparty identifier |
    | Source|string|Where this transaction came from |
    | NettingSet|string|  |
    From these fields, the following values can be calculated
     * **Transaction value in Transaction currency**: TotalConsideration / ExchangeRate
     * **Transaction value in Portfolio currency**: Transaction value in Transaction currency * TradeToPortfolioRate
    ### Example Transactions
    #### A Common Purchase Example
    Three example transactions are shown in the table below.
    They represent a purchase of USD denominated IBM shares within a Sterling denominated portfolio.
     * The first two transactions are for separate buy and fx trades
       * Buying 500 IBM shares for $71,480.00
       * A foreign exchange conversion to fund the IBM purchase. (Buy $71,480.00 for &amp;#163;54,846.60)
     * The third transaction is an alternate version of the above trades. Buying 500 IBM shares and settling directly in Sterling.
    | Column |  Buy Trade | Fx Trade | Buy Trade with foreign Settlement |
    | ----- | ----- | ----- | ----- |
    | TransactionId | FBN00001 | FBN00002 | FBN00003 |
    | Type | Buy | FxBuy | Buy |
    | InstrumentUid | FIGI_BBG000BLNNH6 | CCY_USD | FIGI_BBG000BLNNH6 |
    | TransactionDate | 2018-08-02 | 2018-08-02 | 2018-08-02 |
    | SettlementDate | 2018-08-06 | 2018-08-06 | 2018-08-06 |
    | Units | 500 | 71480 | 500 |
    | TransactionPrice | 142.96 | 1 | 142.96 |
    | TradeCurrency | USD | USD | USD |
    | ExchangeRate | 1 | 0.7673 | 0.7673 |
    | TotalConsideration.Amount | 71480.00 | 54846.60 | 54846.60 |
    | TotalConsideration.Currency | USD | GBP | GBP |
    | Trade/default/TradeToPortfolioRate&amp;ast; | 0.7673 | 0.7673 | 0.7673 |
    [&amp;ast; This is a property field]
    #### A Forward FX Example
    LUSID has a flexible transaction modelling system, and there are a number of different ways of modelling forward fx trades.
    The default LUSID transaction types are FwdFxBuy and FwdFxSell. Other types and behaviours can be configured as required.
    Using these transaction types, the holdings query will report two forward positions. One in each currency.
    Since an FX trade is an exchange of one currency for another, the following two 6 month forward transactions are equivalent:
    | Column |  Forward 'Sell' Trade | Forward 'Buy' Trade |
    | ----- | ----- | ----- |
    | TransactionId | FBN00004 | FBN00005 |
    | Type | FwdFxSell | FwdFxBuy |
    | InstrumentUid | CCY_GBP | CCY_USD |
    | TransactionDate | 2018-08-02 | 2018-08-02 |
    | SettlementDate | 2019-02-06 | 2019-02-06 |
    | Units | 10000.00 | 13142.00 |
    | TransactionPrice |1 | 1 |
    | TradeCurrency | GBP | USD |
    | ExchangeRate | 1.3142 | 0.760919 |
    | TotalConsideration.Amount | 13142.00 | 10000.00 |
    | TotalConsideration.Currency | USD | GBP |
    | Trade/default/TradeToPortfolioRate | 1.0 | 0.760919 |
    ## Holdings
    A holding represents a position in a instrument or cash on a given date.
    | Field|Type|Description |
    | ---|---|--- |
    | InstrumentUid|string|Unique instrument identifier |
    | HoldingType|string|Type of holding, eg Position, Balance, CashCommitment, Receivable, ForwardFX |
    | Units|decimal|Quantity of holding |
    | SettledUnits|decimal|Settled quantity of holding |
    | Cost|currencyandamount|Book cost of holding in transaction currency |
    | CostPortfolioCcy|currencyandamount|Book cost of holding in portfolio currency |
    | Transaction|Transaction|If this is commitment-type holding, the transaction behind it |
    ## Corporate Actions
    Corporate actions are represented within LUSID in terms of a set of instrument-specific 'transitions'.  These transitions are used to specify the participants of the corporate action, and the effect that the corporate action will have on holdings in those participants.
    *Corporate action*
    | Field|Type|Description |
    | ---|---|--- |
    | SourceId|id|  |
    | CorporateActionCode|code|  |
    | AnnouncementDate|datetime|  |
    | ExDate|datetime|  |
    | RecordDate|datetime|  |
    | PaymentDate|datetime|  |
    *Transition*
    | Field|Type|Description |
    | ---|---|--- |
    ## Property
    Properties are key-value pairs that can be applied to any entity within a domain (where a domain is `trade`, `portfolio`, `security` etc).  Properties must be defined before use with a `PropertyDefinition` and can then subsequently be added to entities.
    # Schemas
    The following headers are returned on all responses from LUSID
    | Name | Purpose |
    | --- | --- |
    | lusid-meta-duration | Duration of the request |
    | lusid-meta-success | Whether or not LUSID considered the request to be successful |
    | lusid-meta-requestId | The unique identifier for the request |
    | lusid-schema-url | Url of the schema for the data being returned |
    | lusid-property-schema-url | Url of the schema for any properties |
    # Error Codes
    | Code|Name|Description |
    | ---|---|--- |
    | &lt;a name="100"&gt;100&lt;/a&gt;|Personalisations not found|The personalisation(s) identified by the pattern provided could not be found, either because it does not exist or it has been deleted. Please check the pattern your provided. |
    | &lt;a name="101"&gt;101&lt;/a&gt;|NonRecursivePersonalisation|  |
    | &lt;a name="102"&gt;102&lt;/a&gt;|VersionNotFound|  |
    | &lt;a name="104"&gt;104&lt;/a&gt;|InstrumentNotFound|  |
    | &lt;a name="105"&gt;105&lt;/a&gt;|PropertyNotFound|  |
    | &lt;a name="106"&gt;106&lt;/a&gt;|PortfolioRecursionDepth|  |
    | &lt;a name="108"&gt;108&lt;/a&gt;|GroupNotFound|  |
    | &lt;a name="109"&gt;109&lt;/a&gt;|PortfolioNotFound|  |
    | &lt;a name="110"&gt;110&lt;/a&gt;|PropertySchemaNotFound|  |
    | &lt;a name="111"&gt;111&lt;/a&gt;|PortfolioAncestryNotFound|  |
    | &lt;a name="112"&gt;112&lt;/a&gt;|PortfolioWithIdAlreadyExists|  |
    | &lt;a name="113"&gt;113&lt;/a&gt;|OrphanedPortfolio|  |
    | &lt;a name="119"&gt;119&lt;/a&gt;|MissingBaseClaims|  |
    | &lt;a name="121"&gt;121&lt;/a&gt;|PropertyNotDefined|  |
    | &lt;a name="122"&gt;122&lt;/a&gt;|CannotDeleteSystemProperty|  |
    | &lt;a name="123"&gt;123&lt;/a&gt;|CannotModifyImmutablePropertyField|  |
    | &lt;a name="124"&gt;124&lt;/a&gt;|PropertyAlreadyExists|  |
    | &lt;a name="125"&gt;125&lt;/a&gt;|InvalidPropertyLifeTime|  |
    | &lt;a name="127"&gt;127&lt;/a&gt;|CannotModifyDefaultDataType|  |
    | &lt;a name="128"&gt;128&lt;/a&gt;|GroupAlreadyExists|  |
    | &lt;a name="129"&gt;129&lt;/a&gt;|NoSuchDataType|  |
    | &lt;a name="132"&gt;132&lt;/a&gt;|ValidationError|  |
    | &lt;a name="133"&gt;133&lt;/a&gt;|LoopDetectedInGroupHierarchy|  |
    | &lt;a name="135"&gt;135&lt;/a&gt;|SubGroupAlreadyExists|  |
    | &lt;a name="138"&gt;138&lt;/a&gt;|PriceSourceNotFound|  |
    | &lt;a name="139"&gt;139&lt;/a&gt;|AnalyticStoreNotFound|  |
    | &lt;a name="141"&gt;141&lt;/a&gt;|AnalyticStoreAlreadyExists|  |
    | &lt;a name="143"&gt;143&lt;/a&gt;|ClientInstrumentAlreadyExists|  |
    | &lt;a name="144"&gt;144&lt;/a&gt;|DuplicateInParameterSet|  |
    | &lt;a name="147"&gt;147&lt;/a&gt;|ResultsNotFound|  |
    | &lt;a name="148"&gt;148&lt;/a&gt;|OrderFieldNotInResultSet|  |
    | &lt;a name="149"&gt;149&lt;/a&gt;|OperationFailed|  |
    | &lt;a name="150"&gt;150&lt;/a&gt;|ElasticSearchError|  |
    | &lt;a name="151"&gt;151&lt;/a&gt;|InvalidParameterValue|  |
    | &lt;a name="153"&gt;153&lt;/a&gt;|CommandProcessingFailure|  |
    | &lt;a name="154"&gt;154&lt;/a&gt;|EntityStateConstructionFailure|  |
    | &lt;a name="155"&gt;155&lt;/a&gt;|EntityTimelineDoesNotExist|  |
    | &lt;a name="156"&gt;156&lt;/a&gt;|EventPublishFailure|  |
    | &lt;a name="157"&gt;157&lt;/a&gt;|InvalidRequestFailure|  |
    | &lt;a name="158"&gt;158&lt;/a&gt;|EventPublishUnknown|  |
    | &lt;a name="159"&gt;159&lt;/a&gt;|EventQueryFailure|  |
    | &lt;a name="160"&gt;160&lt;/a&gt;|BlobDidNotExistFailure|  |
    | &lt;a name="162"&gt;162&lt;/a&gt;|SubSystemRequestFailure|  |
    | &lt;a name="163"&gt;163&lt;/a&gt;|SubSystemConfigurationFailure|  |
    | &lt;a name="165"&gt;165&lt;/a&gt;|FailedToDelete|  |
    | &lt;a name="166"&gt;166&lt;/a&gt;|UpsertClientInstrumentFailure|  |
    | &lt;a name="167"&gt;167&lt;/a&gt;|IllegalAsAtInterval|  |
    | &lt;a name="168"&gt;168&lt;/a&gt;|IllegalBitemporalQuery|  |
    | &lt;a name="169"&gt;169&lt;/a&gt;|InvalidAlternateId|  |
    | &lt;a name="170"&gt;170&lt;/a&gt;|CannotAddSourcePortfolioPropertyExplicitly|  |
    | &lt;a name="171"&gt;171&lt;/a&gt;|EntityAlreadyExistsInGroup|  |
    | &lt;a name="173"&gt;173&lt;/a&gt;|EntityWithIdAlreadyExists|  |
    | &lt;a name="174"&gt;174&lt;/a&gt;|PortfolioDetailsDoNotExist|  |
    | &lt;a name="176"&gt;176&lt;/a&gt;|PortfolioWithNameAlreadyExists|  |
    | &lt;a name="177"&gt;177&lt;/a&gt;|InvalidTransactions|  |
    | &lt;a name="178"&gt;178&lt;/a&gt;|ReferencePortfolioNotFound|  |
    | &lt;a name="179"&gt;179&lt;/a&gt;|DuplicateIdFailure|  |
    | &lt;a name="180"&gt;180&lt;/a&gt;|CommandRetrievalFailure|  |
    | &lt;a name="181"&gt;181&lt;/a&gt;|DataFilterApplicationFailure|  |
    | &lt;a name="182"&gt;182&lt;/a&gt;|SearchFailed|  |
    | &lt;a name="183"&gt;183&lt;/a&gt;|MovementsEngineConfigurationKeyFailure|  |
    | &lt;a name="184"&gt;184&lt;/a&gt;|FxRateSourceNotFound|  |
    | &lt;a name="185"&gt;185&lt;/a&gt;|AccrualSourceNotFound|  |
    | &lt;a name="186"&gt;186&lt;/a&gt;|EntitlementsFailure|  |
    | &lt;a name="187"&gt;187&lt;/a&gt;|InvalidIdentityToken|  |
    | &lt;a name="188"&gt;188&lt;/a&gt;|InvalidRequestHeaders|  |
    | &lt;a name="189"&gt;189&lt;/a&gt;|PriceNotFound|  |
    | &lt;a name="190"&gt;190&lt;/a&gt;|InvalidSubHoldingKeysProvided|  |
    | &lt;a name="191"&gt;191&lt;/a&gt;|DuplicateSubHoldingKeysProvided|  |
    | &lt;a name="192"&gt;192&lt;/a&gt;|CutDefinitionNotFound|  |
    | &lt;a name="193"&gt;193&lt;/a&gt;|CutDefinitionInvalid|  |
    | &lt;a name="200"&gt;200&lt;/a&gt;|InvalidUnitForDataType|  |
    | &lt;a name="201"&gt;201&lt;/a&gt;|InvalidTypeForDataType|  |
    | &lt;a name="202"&gt;202&lt;/a&gt;|InvalidValueForDataType|  |
    | &lt;a name="203"&gt;203&lt;/a&gt;|UnitNotDefinedForDataType|  |
    | &lt;a name="204"&gt;204&lt;/a&gt;|UnitsNotSupportedOnDataType|  |
    | &lt;a name="205"&gt;205&lt;/a&gt;|CannotSpecifyUnitsOnDataType|  |
    | &lt;a name="206"&gt;206&lt;/a&gt;|UnitSchemaInconsistentWithDataType|  |
    | &lt;a name="207"&gt;207&lt;/a&gt;|UnitDefinitionNotSpecified|  |
    | &lt;a name="208"&gt;208&lt;/a&gt;|DuplicateUnitDefinitionsSpecified|  |
    | &lt;a name="209"&gt;209&lt;/a&gt;|InvalidUnitsDefinition|  |
    | &lt;a name="210"&gt;210&lt;/a&gt;|InvalidInstrumentIdentifierUnit|  |
    | &lt;a name="211"&gt;211&lt;/a&gt;|HoldingsAdjustmentDoesNotExist|  |
    | &lt;a name="212"&gt;212&lt;/a&gt;|CouldNotBuildExcelUrl|  |
    | &lt;a name="213"&gt;213&lt;/a&gt;|CouldNotGetExcelVersion|  |
    | &lt;a name="214"&gt;214&lt;/a&gt;|InstrumentByCodeNotFound|  |
    | &lt;a name="215"&gt;215&lt;/a&gt;|EntitySchemaDoesNotExist|  |
    | &lt;a name="216"&gt;216&lt;/a&gt;|FeatureNotSupportedOnPortfolioType|  |
    | &lt;a name="217"&gt;217&lt;/a&gt;|QuoteNotFoundFailure|  |
    | &lt;a name="219"&gt;219&lt;/a&gt;|InvalidInstrumentDefinition|  |
    | &lt;a name="221"&gt;221&lt;/a&gt;|InstrumentUpsertFailure|  |
    | &lt;a name="222"&gt;222&lt;/a&gt;|ReferencePortfolioRequestNotSupported|  |
    | &lt;a name="223"&gt;223&lt;/a&gt;|TransactionPortfolioRequestNotSupported|  |
    | &lt;a name="224"&gt;224&lt;/a&gt;|InvalidPropertyValueAssignment|  |
    | &lt;a name="230"&gt;230&lt;/a&gt;|TransactionTypeNotFound|  |
    | &lt;a name="231"&gt;231&lt;/a&gt;|TransactionTypeDuplication|  |
    | &lt;a name="232"&gt;232&lt;/a&gt;|PortfolioDoesNotExistAtGivenDate|  |
    | &lt;a name="-10"&gt;-10&lt;/a&gt;|ServerConfigurationError|  |
    | &lt;a name="-1"&gt;-1&lt;/a&gt;|Unknown error|  |

    :ivar config: Configuration for client.
    :vartype config: LUSIDAPIConfiguration

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = LUSIDAPIConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '0.8.53'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def list_analytic_stores(
            self, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """List analytic stores.

        List all defined analytic stores.

        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfAnalyticStoreKey or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfAnalyticStoreKey or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_analytic_stores.metadata['url']

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfAnalyticStoreKey', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_analytic_stores.metadata = {'url': '/api/analytics'}

    def create_analytic_store(
            self, request=None, custom_headers=None, raw=False, **operation_config):
        """Create analytic store.

        Create a new analytic store for the specified scope and date.

        :param request: A populated analytic store definition
        :type request: ~lusid.models.CreateAnalyticStoreRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AnalyticStore or ClientRawResponse if raw=true
        :rtype: ~lusid.models.AnalyticStore or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_analytic_store.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreateAnalyticStoreRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('AnalyticStore', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_analytic_store.metadata = {'url': '/api/analytics'}

    def get_analytic_store(
            self, scope, year, month, day, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get analytic store.

        Get the meta data associated with a specified scope and date
        combination (analytic store).

        :param scope: The analytics data scope
        :type scope: str
        :param year: The year component of the date for the data in the scope
        :type year: int
        :param month: The month component of the date for the data in the
         scope
        :type month: int
        :param day: The day component of the date for the data in the scope
        :type day: int
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AnalyticStore or ClientRawResponse if raw=true
        :rtype: ~lusid.models.AnalyticStore or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_analytic_store.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'year': self._serialize.url("year", year, 'int'),
            'month': self._serialize.url("month", month, 'int'),
            'day': self._serialize.url("day", day, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AnalyticStore', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_analytic_store.metadata = {'url': '/api/analytics/{scope}/{year}/{month}/{day}'}

    def delete_analytic_store(
            self, scope, year, month, day, custom_headers=None, raw=False, **operation_config):
        """Delete analytic store.

        Delete stored analytic data in the specified scope for the specified
        date.

        :param scope: The analytics data scope
        :type scope: str
        :param year: The year component of the date
        :type year: int
        :param month: The month component of the date
        :type month: int
        :param day: The day component of the date
        :type day: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_analytic_store.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'year': self._serialize.url("year", year, 'int'),
            'month': self._serialize.url("month", month, 'int'),
            'day': self._serialize.url("day", day, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_analytic_store.metadata = {'url': '/api/analytics/{scope}/{year}/{month}/{day}'}

    def set_analytics(
            self, scope, year, month, day, data=None, custom_headers=None, raw=False, **operation_config):
        """Set analytic data.

        Store the complete set of analytics for an existing analytic store for
        the specified scope and date.

        :param scope: The scope of the data being stored
        :type scope: str
        :param year: The year component of the date for the data
        :type year: int
        :param month: The month component of the date for the data
        :type month: int
        :param day: The day component of the date for the data
        :type day: int
        :param data: The analytic data being inserted
        :type data: list[~lusid.models.InstrumentAnalytic]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AnalyticStore or ClientRawResponse if raw=true
        :rtype: ~lusid.models.AnalyticStore or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.set_analytics.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'year': self._serialize.url("year", year, 'int'),
            'month': self._serialize.url("month", month, 'int'),
            'day': self._serialize.url("day", day, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if data is not None:
            body_content = self._serialize.body(data, '[InstrumentAnalytic]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AnalyticStore', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    set_analytics.metadata = {'url': '/api/analytics/{scope}/{year}/{month}/{day}/prices'}

    def get_corporate_actions(
            self, scope, code, from_effective_at=None, to_effective_at=None, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get corporate actions.

        Gets corporate actions from a specific corporate action source.

        :param scope: The scope of the corporate action source
        :type scope: str
        :param code: The code of the corporate action source
        :type code: str
        :param from_effective_at: Optional. The start effective date of the
         data range
        :type from_effective_at: datetime
        :param to_effective_at: Optional. The end effective date of the data
         range
        :type to_effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfCorporateAction or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfCorporateAction or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_corporate_actions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_effective_at is not None:
            query_parameters['fromEffectiveAt'] = self._serialize.query("from_effective_at", from_effective_at, 'iso-8601')
        if to_effective_at is not None:
            query_parameters['toEffectiveAt'] = self._serialize.query("to_effective_at", to_effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfCorporateAction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_corporate_actions.metadata = {'url': '/api/corporateactions/{scope}/{code}'}

    def batch_upsert_corporate_actions(
            self, scope, code, actions=None, custom_headers=None, raw=False, **operation_config):
        """Upsert corporate actions.

        Attempt to create/update one or more corporate action in a specified
        corporate action source. Failed actions will be identified in the body
        of the response.

        :param scope: The scope of corporate action source
        :type scope: str
        :param code: The code of the corporate action source
        :type code: str
        :param actions: The corporate action definitions
        :type actions: list[~lusid.models.CreateCorporateAction]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertCorporateActionsResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.UpsertCorporateActionsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.batch_upsert_corporate_actions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if actions is not None:
            body_content = self._serialize.body(actions, '[CreateCorporateAction]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('UpsertCorporateActionsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    batch_upsert_corporate_actions.metadata = {'url': '/api/corporateactions/{scope}/{code}'}

    def create_data_type(
            self, request=None, custom_headers=None, raw=False, **operation_config):
        """Create data type definition.

        Create a new data type definition
        Data types cannot be created in either the "default" or "system"
        scopes.

        :param request: The definition of the new data type
        :type request: ~lusid.models.CreateDataTypeRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DataType or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DataType or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_data_type.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreateDataTypeRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('DataType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_data_type.metadata = {'url': '/api/datatypes'}

    def list_data_types(
            self, scope, include_default=None, include_system=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """List data types.

        List all data types in a specified scope.

        :param scope: The requested scope of the data types
        :type scope: str
        :param include_default: Whether to additionally include those data
         types in the "default" scope
        :type include_default: bool
        :param include_system: Whether to additionally include those data
         types in the "system" scope
        :type include_system: bool
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfDataType or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfDataType or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_data_types.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if include_default is not None:
            query_parameters['includeDefault'] = self._serialize.query("include_default", include_default, 'bool')
        if include_system is not None:
            query_parameters['includeSystem'] = self._serialize.query("include_system", include_system, 'bool')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfDataType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_data_types.metadata = {'url': '/api/datatypes/{scope}'}

    def get_data_type(
            self, scope, code, custom_headers=None, raw=False, **operation_config):
        """Get data type definition.

        Get the definition of a specified data type.

        :param scope: The scope of the data type
        :type scope: str
        :param code: The code of the data type
        :type code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DataType or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DataType or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_data_type.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DataType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_data_type.metadata = {'url': '/api/datatypes/{scope}/{code}'}

    def update_data_type(
            self, scope, code, request=None, custom_headers=None, raw=False, **operation_config):
        """Update data type definition.

        Update the definition of the specified existing data type
        Not all elements within a data type definition are modifiable due to
        the potential implications for data
        already stored against the types.

        :param scope: The scope of the data type
        :type scope: str
        :param code: The code of the data type
        :type code: str
        :param request: The updated definition of the data type
        :type request: ~lusid.models.UpdateDataTypeRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DataType or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DataType or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update_data_type.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdateDataTypeRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DataType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_data_type.metadata = {'url': '/api/datatypes/{scope}/{code}'}

    def get_units_from_data_type(
            self, scope, code, units=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get units from data type.

        Get the definitions of the specified units associated bound to a
        specific data type.

        :param scope: The scope of the data type
        :type scope: str
        :param code: The code of the data type
        :type code: str
        :param units: One or more unit identifiers for which the definition is
         being requested
        :type units: list[str]
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfIUnitDefinitionDto or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfIUnitDefinitionDto or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_units_from_data_type.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if units is not None:
            query_parameters['units'] = self._serialize.query("units", units, '[str]', div=',')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfIUnitDefinitionDto', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_units_from_data_type.metadata = {'url': '/api/datatypes/{scope}/{code}/units'}

    def create_derived_portfolio(
            self, scope, portfolio=None, custom_headers=None, raw=False, **operation_config):
        """Create derived transaction portfolio.

        Creates a transaction portfolio that derives from an existing
        transaction portfolio. In a derived portfolio, parts of the portfolio
        can either be specific to this portfolio, or can be inherited from a
        "parent". Different parts of the portfolio (e.g. transactions or
        properties) are combined in different ways. The portfolio details are
        either overridden in entirety, or not at all. The same is true for
        properties. Transactions on a derived portfolio are merged with its
        parent portfolio's transactions. If the parent portfolio is itself a
        derived portfolio, transactions from that parent are also merged (and
        that parent's portfolio's, if it is also a derived portfolio, and so
        on).

        :param scope: The scope into which to create the new derived portfolio
        :type scope: str
        :param portfolio: The root object of the new derived portfolio,
         containing a populated reference portfolio id and reference scope
        :type portfolio:
         ~lusid.models.CreateDerivedTransactionPortfolioRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Portfolio or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_derived_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if portfolio is not None:
            body_content = self._serialize.body(portfolio, 'CreateDerivedTransactionPortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_derived_portfolio.metadata = {'url': '/api/derivedtransactionportfolios/{scope}'}

    def delete_derived_portfolio_details(
            self, scope, code, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Delete portfolio details.

        Deletes the portfolio details for the specified derived transaction
        portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: The effective date of the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_derived_portfolio_details.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_derived_portfolio_details.metadata = {'url': '/api/derivedtransactionportfolios/{scope}/{code}/details'}

    def list_instruments(
            self, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get all of the currently mastered instruments in LUSID.

        Lists all instruments that have been mastered within LUSID.

        :param as_at: The AsAt time
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfInstrument or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfInstrument or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_instruments.metadata['url']

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfInstrument', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_instruments.metadata = {'url': '/api/instruments'}

    def upsert_instruments(
            self, requests=None, custom_headers=None, raw=False, **operation_config):
        """Upsert instruments.

        Attempt to master one or more instruments in LUSID's instrument master.
        Each instrument is keyed by some unique key. This key is unimportant,
        and serves only as a method to identify created instruments in the
        response.
        The response will return both the collection of successfully created
        instruments, as well as those that were rejected and why their creation
        failed. They will be keyed against the key supplied in the
        request.
        It is important to always check the 'Failed' set for any unsuccessful
        results.

        :param requests: The instrument definitions
        :type requests: dict[str, ~lusid.models.UpsertInstrumentRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertInstrumentsResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.UpsertInstrumentsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_instruments.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if requests is not None:
            body_content = self._serialize.body(requests, '{UpsertInstrumentRequest}')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('UpsertInstrumentsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_instruments.metadata = {'url': '/api/instruments'}

    def get_instrument(
            self, type, id, effective_at=None, as_at=None, instrument_property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Get instrument definition.

        Get an individual instrument by the one of its unique instrument
        identifiers. Optionally, it is possible to decorate each instrument
        with specified property data.

        :param type: The type of identifier being supplied. Possible values
         include: 'Undefined', 'LusidInstrumentId', 'ReutersAssetId', 'CINS',
         'Isin', 'Sedol', 'Cusip', 'Ticker', 'ClientInternal', 'Figi',
         'CompositeFigi', 'ShareClassFigi', 'Wertpapier', 'RIC', 'QuotePermId'
        :type type: str
        :param id: The identifier of the requested instrument
        :type id: str
        :param effective_at: Optional. The effective date of the query
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the query
        :type as_at: datetime
        :param instrument_property_keys: Optional. Keys of the properties to
         be decorated on to the instrument
        :type instrument_property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Instrument or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Instrument or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_instrument.metadata['url']
        path_format_arguments = {
            'type': self._serialize.url("type", type, 'str'),
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Instrument', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_instrument.metadata = {'url': '/api/instruments/{type}/{id}'}

    def update_instrument_identifier(
            self, type, id, request=None, custom_headers=None, raw=False, **operation_config):
        """Update instrument identifier.

        Adds, updates, or removes an identifier on an instrument.

        :param type: The type of identifier being supplied. Possible values
         include: 'Undefined', 'LusidInstrumentId', 'ReutersAssetId', 'CINS',
         'Isin', 'Sedol', 'Cusip', 'Ticker', 'ClientInternal', 'Figi',
         'CompositeFigi', 'ShareClassFigi', 'Wertpapier', 'RIC', 'QuotePermId'
        :type type: str
        :param id: The instrument identifier
        :type id: str
        :param request: The identifier to add, update, or remove
        :type request: ~lusid.models.UpdateInstrumentIdentifierRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Instrument or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Instrument or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update_instrument_identifier.metadata['url']
        path_format_arguments = {
            'type': self._serialize.url("type", type, 'str'),
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdateInstrumentIdentifierRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('Instrument', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_instrument_identifier.metadata = {'url': '/api/instruments/{type}/{id}'}

    def delete_instrument(
            self, type, id, custom_headers=None, raw=False, **operation_config):
        """Delete instrument.

        Attempt to delete one or more "client" instruments.
        The response will include those instruments that could not be deleted
        (as well as any available details).
        It is important to always check the 'Failed' set for any unsuccessful
        results.

        :param type: The type of identifier being supplied. Possible values
         include: 'Undefined', 'LusidInstrumentId', 'ReutersAssetId', 'CINS',
         'Isin', 'Sedol', 'Cusip', 'Ticker', 'ClientInternal', 'Figi',
         'CompositeFigi', 'ShareClassFigi', 'Wertpapier', 'RIC', 'QuotePermId'
        :type type: str
        :param id: The instrument identifier
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeleteInstrumentResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeleteInstrumentResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_instrument.metadata['url']
        path_format_arguments = {
            'type': self._serialize.url("type", type, 'str'),
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeleteInstrumentResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_instrument.metadata = {'url': '/api/instruments/{type}/{id}'}

    def find_external_instruments(
            self, code_type=None, codes=None, custom_headers=None, raw=False, **operation_config):
        """Find externally mastered instruments.

        Search for a set of instruments from an external instrument mastering
        service.

        :param code_type: The type of codes to search for. Possible values
         include: 'Undefined', 'LusidInstrumentId', 'ReutersAssetId', 'CINS',
         'Isin', 'Sedol', 'Cusip', 'Ticker', 'ClientInternal', 'Figi',
         'CompositeFigi', 'ShareClassFigi', 'Wertpapier', 'RIC', 'QuotePermId'
        :type code_type: str
        :param codes: The collection of instruments to search for
        :type codes: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FindInstrumentsResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.FindInstrumentsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.find_external_instruments.metadata['url']

        # Construct parameters
        query_parameters = {}
        if code_type is not None:
            query_parameters['codeType'] = self._serialize.query("code_type", code_type, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if codes is not None:
            body_content = self._serialize.body(codes, '[str]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('FindInstrumentsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    find_external_instruments.metadata = {'url': '/api/instruments/$find'}

    def get_instruments(
            self, code_type=None, codes=None, effective_at=None, as_at=None, instrument_property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Get instrument definition.

        Get a collection of instruments by a set of identifiers. Optionally, it
        is possible to decorate each instrument with specified property data.

        :param code_type: the type of codes being specified. Possible values
         include: 'Undefined', 'LusidInstrumentId', 'ReutersAssetId', 'CINS',
         'Isin', 'Sedol', 'Cusip', 'Ticker', 'ClientInternal', 'Figi',
         'CompositeFigi', 'ShareClassFigi', 'Wertpapier', 'RIC', 'QuotePermId'
        :type code_type: str
        :param codes: The identifiers of the instruments to get
        :type codes: list[str]
        :param effective_at: Optional. The effective date of the request
        :type effective_at: datetime
        :param as_at: Optional. The as at date of the request
        :type as_at: datetime
        :param instrument_property_keys: Optional. Keys of the properties to
         be decorated on to the instrument
        :type instrument_property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: GetInstrumentsResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.GetInstrumentsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_instruments.metadata['url']

        # Construct parameters
        query_parameters = {}
        if code_type is not None:
            query_parameters['codeType'] = self._serialize.query("code_type", code_type, 'str')
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if codes is not None:
            body_content = self._serialize.body(codes, '[str]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GetInstrumentsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_instruments.metadata = {'url': '/api/instruments/$get'}

    def find_instruments(
            self, aliases=None, effective_at=None, as_at=None, instrument_property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Search instrument definition.

        Get a collection of instruments by a set of identifiers. Optionally, it
        is possible to decorate each instrument with specified property data.

        :param aliases: The list of market aliases (e.g ISIN, Ticker) to find
         instruments by.
        :type aliases: list[~lusid.models.Property]
        :param effective_at: Optional. The effective date of the query
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the query
        :type as_at: datetime
        :param instrument_property_keys: Optional. Keys of the properties to
         be decorated on to the instrument
        :type instrument_property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfInstrument or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfInstrument or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.find_instruments.metadata['url']

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if aliases is not None:
            body_content = self._serialize.body(aliases, '[Property]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfInstrument', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    find_instruments.metadata = {'url': '/api/instruments/$query'}

    def upsert_instruments_properties(
            self, instrument_properties=None, custom_headers=None, raw=False, **operation_config):
        """Upsert instrument properties.

        Attempt to upsert property data for one or more instruments,
        properties, and effective dates.
        The response will include the details of any failures that occurred
        during data storage.
        It is important to always check the 'Failed' collection for any
        unsuccessful results.

        :param instrument_properties: The instrument property data
        :type instrument_properties: list[~lusid.models.InstrumentProperty]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertInstrumentPropertiesResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.UpsertInstrumentPropertiesResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_instruments_properties.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if instrument_properties is not None:
            body_content = self._serialize.body(instrument_properties, '[InstrumentProperty]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('UpsertInstrumentPropertiesResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_instruments_properties.metadata = {'url': '/api/instruments/$upsertproperties'}

    def get_instrument_identifiers(
            self, custom_headers=None, raw=False, **operation_config):
        """Get allowable instrument identifiers.

        Gets the set of identifiers that have been configured as unique
        identifiers for instruments.
        Only CodeTypes returned from this end point can be used as identifiers
        for instruments.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfCodeType or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfCodeType or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_instrument_identifiers.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfCodeType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_instrument_identifiers.metadata = {'url': '/api/instruments/identifiers'}

    def get_saml_identity_provider_id(
            self, domain, custom_headers=None, raw=False, **operation_config):
        """Get SAML Identity Provider.

        Get the unique identifier for the SAML 2.0 Identity Provider to be used
        for domain.

        :param domain: The domain that the user will be logging in to
        :type domain: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: str or ClientRawResponse if raw=true
        :rtype: str or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_saml_identity_provider_id.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_saml_identity_provider_id.metadata = {'url': '/api/login/saml/{domain}'}

    def get_excel_download_url(
            self, version=None, custom_headers=None, raw=False, **operation_config):
        """Get Excel download url.

        Request an authorised url for an Excel client version.

        :param version: The requested version of the Excel plugin
        :type version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: str or ClientRawResponse if raw=true
        :rtype: str or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_excel_download_url.metadata['url']

        # Construct parameters
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query("version", version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_excel_download_url.metadata = {'url': '/api/metadata/downloads/excel'}

    def get_excel_addin(
            self, version=None, custom_headers=None, raw=False, **operation_config):
        """Download Excel Addin.

        Download the LUSID Excel Addin for Microsoft Excel. Not providing a
        specific value will return the latest version being returned.

        :param version: The requested version of the Excel plugin
        :type version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FileResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.FileResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_excel_addin.metadata['url']

        # Construct parameters
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query("version", version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('FileResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_excel_addin.metadata = {'url': '/api/metadata/downloads/exceladdin'}

    def get_lusid_versions(
            self, custom_headers=None, raw=False, **operation_config):
        """Get LUSID versions.

        Get the semantic versions associated with LUSID and its ecosystem.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VersionSummaryDto or ClientRawResponse if raw=true
        :rtype: ~lusid.models.VersionSummaryDto or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_lusid_versions.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionSummaryDto', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_lusid_versions.metadata = {'url': '/api/metadata/versions'}

    def get_personalisations(
            self, pattern=None, scope=None, recursive=False, wildcards=False, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get personalisation.

        Get a personalisation, recursing to get any referenced if required.

        :param pattern: The search pattern or specific key
        :type pattern: str
        :param scope: Optional. The scope level to request for. Possible
         values include: 'User', 'Group', 'Default', 'All'
        :type scope: str
        :param recursive: Optional. Whether to recurse into dereference
         recursive settings
        :type recursive: bool
        :param wildcards: Optional. Whether to apply wildcards to the provided
         pattern and pull back any matching
        :type wildcards: bool
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPersonalisation or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfPersonalisation or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_personalisations.metadata['url']

        # Construct parameters
        query_parameters = {}
        if pattern is not None:
            query_parameters['pattern'] = self._serialize.query("pattern", pattern, 'str')
        if scope is not None:
            query_parameters['scope'] = self._serialize.query("scope", scope, 'str')
        if recursive is not None:
            query_parameters['recursive'] = self._serialize.query("recursive", recursive, 'bool')
        if wildcards is not None:
            query_parameters['wildcards'] = self._serialize.query("wildcards", wildcards, 'bool')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPersonalisation', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_personalisations.metadata = {'url': '/api/personalisations'}

    def upsert_personalisations(
            self, personalisations=None, custom_headers=None, raw=False, **operation_config):
        """Upsert personalisations.

        Upsert one or more personalisations.

        :param personalisations: The set of personalisations to persist
        :type personalisations: list[~lusid.models.Personalisation]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertPersonalisationResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.UpsertPersonalisationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_personalisations.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if personalisations is not None:
            body_content = self._serialize.body(personalisations, '[Personalisation]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('UpsertPersonalisationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_personalisations.metadata = {'url': '/api/personalisations'}

    def delete_personalisation(
            self, key=None, scope=None, group=None, custom_headers=None, raw=False, **operation_config):
        """Delete a personalisation.

        Delete a personalisation at a specific scope (or use scope ALL to purge
        the setting entirely).

        :param key: The key of the setting to be deleted
        :type key: str
        :param scope: The scope to delete at (use ALL to purge the setting
         entirely). Possible values include: 'User', 'Group', 'Default', 'All'
        :type scope: str
        :param group: Optional. If deleting a setting at group level, specify
         the group here
        :type group: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_personalisation.metadata['url']

        # Construct parameters
        query_parameters = {}
        if key is not None:
            query_parameters['key'] = self._serialize.query("key", key, 'str')
        if scope is not None:
            query_parameters['scope'] = self._serialize.query("scope", scope, 'str')
        if group is not None:
            query_parameters['group'] = self._serialize.query("group", group, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_personalisation.metadata = {'url': '/api/personalisations'}

    def list_portfolio_groups(
            self, scope, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """List groups in scope.

        Lists all portfolio groups in a specified scope.

        :param scope: The scope
        :type scope: str
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfPortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_portfolio_groups.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_portfolio_groups.metadata = {'url': '/api/portfoliogroups/{scope}'}

    def create_portfolio_group(
            self, scope, request=None, custom_headers=None, raw=False, **operation_config):
        """Create group.

        Create a new portfolio group.

        :param scope: The scope into which the portfolio group will be created
        :type scope: str
        :param request: The definition of the new portfolio group
        :type request: ~lusid.models.CreatePortfolioGroupRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreatePortfolioGroupRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_portfolio_group.metadata = {'url': '/api/portfoliogroups/{scope}'}

    def get_portfolio_group(
            self, scope, code, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get portfolio group.

        Get the definition of the specified portfolio group.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The code of the portfolio group
        :type code: str
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_group.metadata = {'url': '/api/portfoliogroups/{scope}/{code}'}

    def update_portfolio_group(
            self, scope, code, request=None, custom_headers=None, raw=False, **operation_config):
        """Update group.

        Update the definition of the specified existing portfolio group.
        Not all elements within a portfolio group definition are modifiable
        after creation.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The code of the portfolio group
        :type code: str
        :param request: The updated definition of the portfolio group
        :type request: ~lusid.models.UpdatePortfolioGroupRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdatePortfolioGroupRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_portfolio_group.metadata = {'url': '/api/portfoliogroups/{scope}/{code}'}

    def delete_portfolio_group(
            self, scope, code, custom_headers=None, raw=False, **operation_config):
        """Delete group.

        Deletes the definition of the specified portfolio group.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The code of the portfolio group
        :type code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio_group.metadata = {'url': '/api/portfoliogroups/{scope}/{code}'}

    def get_aggregation_by_group(
            self, scope, code, request=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data in a portfolio group.

        Aggregate data sourced from the specified portfolio group.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The code of the portfolio group
        :type code: str
        :param request: The request specifying the parameters of the
         aggregation
        :type request: ~lusid.models.AggregationRequest
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ListAggregationResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ListAggregationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_aggregation_by_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ListAggregationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_aggregation_by_group.metadata = {'url': '/api/portfoliogroups/{scope}/{code}/$aggregate'}

    def get_nested_aggregation_by_group(
            self, scope, code, request=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data in a portfolio group, as nested.

        Obsolete - Aggregate data sourced from the specified portfolio group
        into a nested structure. Data is nested following the group-by
        specifications.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The code of the portfolio group
        :type code: str
        :param request: The request specifying the parameters of the
         aggregation
        :type request: ~lusid.models.AggregationRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: NestedAggregationResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.NestedAggregationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_nested_aggregation_by_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('NestedAggregationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_nested_aggregation_by_group.metadata = {'url': '/api/portfoliogroups/{scope}/{code}/$aggregatenested'}

    def get_portfolio_group_commands(
            self, scope, code, from_as_at=None, to_as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get commands.

        Gets all commands that modified a specific portfolio group.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The code of the portfolio group
        :type code: str
        :param from_as_at: Optional. Filters commands by those that were
         processed at or after this date and time
        :type from_as_at: datetime
        :param to_as_at: Optional. Filters commands by those that were
         processed at or before this date and time
        :type to_as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfProcessedCommand or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfProcessedCommand or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_portfolio_group_commands.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_as_at is not None:
            query_parameters['fromAsAt'] = self._serialize.query("from_as_at", from_as_at, 'iso-8601')
        if to_as_at is not None:
            query_parameters['toAsAt'] = self._serialize.query("to_as_at", to_as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfProcessedCommand', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_group_commands.metadata = {'url': '/api/portfoliogroups/{scope}/{code}/commands'}

    def get_portfolio_group_expansion(
            self, scope, code, effective_at=None, as_at=None, property_filter=None, custom_headers=None, raw=False, **operation_config):
        """Get a full expansion of a portfolio group.

        Lists all portfolios in a group, and all sub groups. Portfolios are
        decorated with their properties.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: Optional. The effective date of the data
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param property_filter: Optional. The restricted set of properties
         that should be returned
        :type property_filter: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ExpandedGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ExpandedGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_portfolio_group_expansion.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if property_filter is not None:
            query_parameters['propertyFilter'] = self._serialize.query("property_filter", property_filter, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ExpandedGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_group_expansion.metadata = {'url': '/api/portfoliogroups/{scope}/{code}/expansion'}

    def add_portfolio_to_group(
            self, scope, code, portfolio_id=None, custom_headers=None, raw=False, **operation_config):
        """Add portfolio to group.

        Adds a portfolio to a previously defined portfolio group.

        :param scope: The scope of the portfolio group to which a portfolio is
         being added
        :type scope: str
        :param code: The code of the portfolio group to which a portfolio is
         being added
        :type code: str
        :param portfolio_id: The id of the portfolio
        :type portfolio_id: ~lusid.models.ResourceId
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.add_portfolio_to_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if portfolio_id is not None:
            body_content = self._serialize.body(portfolio_id, 'ResourceId')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_portfolio_to_group.metadata = {'url': '/api/portfoliogroups/{scope}/{code}/portfolios'}

    def delete_portfolio_from_group(
            self, scope, code, portfolio_scope, portfolio_code, custom_headers=None, raw=False, **operation_config):
        """Remove portfolio from group.

        Removes a portfolio from a portfolio group.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The code of the portfolio group
        :type code: str
        :param portfolio_scope: The scope of the portfolio being removed
        :type portfolio_scope: str
        :param portfolio_code: The code of the portfolio being removed
        :type portfolio_code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_portfolio_from_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'portfolioScope': self._serialize.url("portfolio_scope", portfolio_scope, 'str'),
            'portfolioCode': self._serialize.url("portfolio_code", portfolio_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio_from_group.metadata = {'url': '/api/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode}'}

    def add_sub_group_to_group(
            self, scope, code, portfolio_group_id=None, custom_headers=None, raw=False, **operation_config):
        """Add group to group.

        Adds a portfolio group, as a sub-group, to an existing portfolio group.

        :param scope: The scope of the portfolio group to which a sub-group is
         being added
        :type scope: str
        :param code: The code of the portfolio group to which a sub-group is
         being added
        :type code: str
        :param portfolio_group_id: The id of the portfolio group being added
         as a sub-group
        :type portfolio_group_id: ~lusid.models.ResourceId
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.add_sub_group_to_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if portfolio_group_id is not None:
            body_content = self._serialize.body(portfolio_group_id, 'ResourceId')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_sub_group_to_group.metadata = {'url': '/api/portfoliogroups/{scope}/{code}/subgroups'}

    def delete_sub_group_from_group(
            self, scope, code, subgroup_scope, subgroup_code, custom_headers=None, raw=False, **operation_config):
        """Remove group from group.

        Remove a portfolio group (sub-group) from a parent portfolio group.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The code of the portfolio group
        :type code: str
        :param subgroup_scope: The scope of the sub-group being removed
        :type subgroup_scope: str
        :param subgroup_code: The code of the sub-group being removed
        :type subgroup_code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_sub_group_from_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'subgroupScope': self._serialize.url("subgroup_scope", subgroup_scope, 'str'),
            'subgroupCode': self._serialize.url("subgroup_code", subgroup_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_sub_group_from_group.metadata = {'url': '/api/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode}'}

    def list_portfolio_scopes(
            self, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """List portfolio scopes.

        Lists all scopes that are either currently or have previously had
        portfolios in them.

        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Filter to be applied to the list of scopes
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfScope or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfScope or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_portfolio_scopes.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfScope', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_portfolio_scopes.metadata = {'url': '/api/portfolios'}

    def list_portfolios(
            self, scope, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """List portfolios.

        List all the portfolios in the specified scope.

        :param scope: The scope
        :type scope: str
        :param effective_at: Optional. The effective date of the data
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPortfolio or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfPortfolio or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_portfolios.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPortfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_portfolios.metadata = {'url': '/api/portfolios/{scope}'}

    def get_portfolio(
            self, scope, code, effective_at=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get portfolio definition.

        Retrieves the basic set of information about a portfolio using the
        specified scope and code.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: Optional. The effective date of the data
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Portfolio or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio.metadata = {'url': '/api/portfolios/{scope}/{code}'}

    def update_portfolio(
            self, scope, code, request=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Update portfolio definition.

        Update the definition of a specific portfolio. Note, some parts of a
        portfolio definition are not available for modification after the
        initial creation.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param request: The updated portfolio definition
        :type request: ~lusid.models.UpdatePortfolioRequest
        :param effective_at: Optional. The effective date for the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Portfolio or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdatePortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_portfolio.metadata = {'url': '/api/portfolios/{scope}/{code}'}

    def delete_portfolio(
            self, scope, code, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Delete portfolio.

        Delete a portfolio at the specified effectiveAt.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: Optional. The effective date of the deletion
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio.metadata = {'url': '/api/portfolios/{scope}/{code}'}

    def get_aggregation_by_portfolio(
            self, scope, code, request=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data in a portfolio.

        Aggregate data sourced from the specified portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param request: The request specifying the parameters of the
         aggregation
        :type request: ~lusid.models.AggregationRequest
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ListAggregationResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ListAggregationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_aggregation_by_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ListAggregationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_aggregation_by_portfolio.metadata = {'url': '/api/portfolios/{scope}/{code}/$aggregate'}

    def get_portfolio_commands(
            self, scope, code, from_as_at=None, to_as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get commands.

        Gets all commands that modified a specific portfolio, including any
        input transactions.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param from_as_at: Optional. Filters commands by those that were
         processed at or after this date and time
        :type from_as_at: datetime
        :param to_as_at: Optional. Filters commands by those that were
         processed at or before this date and time
        :type to_as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfProcessedCommand or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfProcessedCommand or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_portfolio_commands.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_as_at is not None:
            query_parameters['fromAsAt'] = self._serialize.query("from_as_at", from_as_at, 'iso-8601')
        if to_as_at is not None:
            query_parameters['toAsAt'] = self._serialize.query("to_as_at", to_as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfProcessedCommand', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_commands.metadata = {'url': '/api/portfolios/{scope}/{code}/commands'}

    def get_portfolio_properties(
            self, scope, code, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get portfolio properties.

        Get the properties of a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: Optional. The effective date of the data
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioProperties or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioProperties or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_portfolio_properties.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioProperties', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_properties.metadata = {'url': '/api/portfolios/{scope}/{code}/properties'}

    def upsert_portfolio_properties(
            self, scope, code, portfolio_properties=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Upsert properties.

        Upsert one or more property values to a portfolio for the specified
        effectiveAt. All properties must be of the domain Portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param portfolio_properties: The property values to be upserted to the
         portfolio
        :type portfolio_properties: dict[str, ~lusid.models.PropertyValue]
        :param effective_at: Optional. The effective date of the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioProperties or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioProperties or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_portfolio_properties.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if portfolio_properties is not None:
            body_content = self._serialize.body(portfolio_properties, '{PropertyValue}')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioProperties', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_portfolio_properties.metadata = {'url': '/api/portfolios/{scope}/{code}/properties'}

    def delete_portfolio_properties(
            self, scope, code, effective_at=None, portfolio_property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Delete portfolio properties.

        Delete one, many or all property values from a portfolio for the
        specified effectiveAt
        Specifying no effectiveAt will delete all properties.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Optional. The effective date of the deletion
        :type effective_at: datetime
        :param portfolio_property_keys: Optional. The keys of the properties
         to be deleted. None specified indicates the intention to delete all
         properties from the portfolio
        :type portfolio_property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_portfolio_properties.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if portfolio_property_keys is not None:
            query_parameters['portfolioPropertyKeys'] = self._serialize.query("portfolio_property_keys", portfolio_property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio_properties.metadata = {'url': '/api/portfolios/{scope}/{code}/properties'}

    def reconcile_holdings(
            self, request=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Reconcile portfolio holdings.

        Reconcile the holdings of two portfolios.

        :param request: The specifications of the inputs to the reconciliation
        :type request: ~lusid.models.PortfoliosReconciliationRequest
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfReconciliationBreak or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfReconciliationBreak or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.reconcile_holdings.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'PortfoliosReconciliationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfReconciliationBreak', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    reconcile_holdings.metadata = {'url': '/api/portfolios/$reconcileholdings'}

    def get_multiple_property_definitions(
            self, property_keys=None, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get multiple property definitions.

        Get one or more property definitions.

        :param property_keys: One or more keys for properties for which the
         schema should be returned
        :type property_keys: list[str]
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPropertyDefinition or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfPropertyDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_multiple_property_definitions.metadata['url']

        # Construct parameters
        query_parameters = {}
        if property_keys is not None:
            query_parameters['propertyKeys'] = self._serialize.query("property_keys", property_keys, '[str]', div=',')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPropertyDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_multiple_property_definitions.metadata = {'url': '/api/propertydefinitions'}

    def create_property_definition(
            self, definition=None, custom_headers=None, raw=False, **operation_config):
        """Define a new property.

        Create a new property definition.

        :param definition: The definition of the new property
        :type definition: ~lusid.models.CreatePropertyDefinitionRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PropertyDefinition or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PropertyDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_property_definition.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if definition is not None:
            body_content = self._serialize.body(definition, 'CreatePropertyDefinitionRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PropertyDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_property_definition.metadata = {'url': '/api/propertydefinitions'}

    def get_property_definition(
            self, domain, scope, code, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get property definition.

        Retrieve the definition for the identified property.

        :param domain: The Property Domain of the requested property. Possible
         values include: 'Trade', 'Portfolio', 'Security', 'Holding',
         'ReferenceHolding', 'TxnType', 'Instrument'
        :type domain: str
        :param scope: The scope of the requested property
        :type scope: str
        :param code: The code of the requested property
        :type code: str
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PropertyDefinition or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PropertyDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_property_definition.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertyDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_property_definition.metadata = {'url': '/api/propertydefinitions/{domain}/{scope}/{code}'}

    def update_property_definition(
            self, domain, scope, code, definition=None, custom_headers=None, raw=False, **operation_config):
        """Update the definition of the specified existing property.

        Not all elements within a property definition are modifiable due to the
        potential implications for data
        already stored against these properties.

        :param domain: The Property Domain of the property being updated.
         Possible values include: 'Trade', 'Portfolio', 'Security', 'Holding',
         'ReferenceHolding', 'TxnType', 'Instrument'
        :type domain: str
        :param scope: The scope of the property to be updated
        :type scope: str
        :param code: The code of the property to be updated
        :type code: str
        :param definition: The updated definition of the property
        :type definition: ~lusid.models.UpdatePropertyDefinitionRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PropertyDefinition or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PropertyDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update_property_definition.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if definition is not None:
            body_content = self._serialize.body(definition, 'UpdatePropertyDefinitionRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertyDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_property_definition.metadata = {'url': '/api/propertydefinitions/{domain}/{scope}/{code}'}

    def delete_property_definition(
            self, domain, scope, code, custom_headers=None, raw=False, **operation_config):
        """Delete property definition.

        Delete the definition of the specified property.

        :param domain: The Property Domain of the property to be deleted.
         Possible values include: 'Trade', 'Portfolio', 'Security', 'Holding',
         'ReferenceHolding', 'TxnType', 'Instrument'
        :type domain: str
        :param scope: The scope of the property to be deleted
        :type scope: str
        :param code: The code of the property to be deleted
        :type code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_property_definition.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_property_definition.metadata = {'url': '/api/propertydefinitions/{domain}/{scope}/{code}'}

    def upsert_quotes(
            self, scope, quotes=None, custom_headers=None, raw=False, **operation_config):
        """Add quotes.

        Add quotes effective at the specified time. If a quote is added with
        the same id (and is effective at the same time) as an existing quote,
        then the more recently added quote will be returned when queried.

        :param scope: The scope of the quotes
        :type scope: str
        :param quotes: The quotes to add
        :type quotes: list[~lusid.models.UpsertQuoteRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertQuotesResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.UpsertQuotesResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_quotes.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if quotes is not None:
            body_content = self._serialize.body(quotes, '[UpsertQuoteRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpsertQuotesResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_quotes.metadata = {'url': '/api/quotes/{scope}'}

    def delete_quote(
            self, scope, quotes=None, custom_headers=None, raw=False, **operation_config):
        """Delete a quote.

        Delete the specified quotes. In order for a quote to be deleted the id
        and effectiveFrom date must exactly match.

        :param scope: The scope of the quote
        :type scope: str
        :param quotes: The quotes to delete
        :type quotes: list[~lusid.models.DeleteQuoteRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeleteQuotesResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeleteQuotesResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_quote.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if quotes is not None:
            body_content = self._serialize.body(quotes, '[DeleteQuoteRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeleteQuotesResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_quote.metadata = {'url': '/api/quotes/{scope}/$delete'}

    def get_quotes(
            self, scope, quote_ids=None, effective_at=None, as_at=None, max_age=None, page=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get quotes.

        Get quotes effective at the specified date/time (if any). An optional
        maximum age of quotes can be specified, and is infinite by default.
        Quotes which are older than this at the time of the effective date/time
        will not be returned.
        MaxAge is a duration of time represented in an ISO8601 format, eg.
        P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).
        The results are paged, and by default the 1st page of results is
        returned with a limit of 100 results per page.

        :param scope: The scope of the quotes
        :type scope: str
        :param quote_ids: The ids of the quotes
        :type quote_ids: list[~lusid.models.QuoteId]
        :param effective_at: Optional. The date/time from which the quotes are
         effective
        :type effective_at: datetime
        :param as_at: Optional. The 'AsAt' date/time
        :type as_at: datetime
        :param max_age: Optional. The quote staleness tolerance
        :type max_age: str
        :param page: Optional. The page of results to return
        :type page: int
        :param limit: Optional. The number of results per page
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: GetQuotesResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.GetQuotesResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_quotes.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if max_age is not None:
            query_parameters['maxAge'] = self._serialize.query("max_age", max_age, 'str')
        if page is not None:
            query_parameters['page'] = self._serialize.query("page", page, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if quote_ids is not None:
            body_content = self._serialize.body(quote_ids, '[QuoteId]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GetQuotesResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_quotes.metadata = {'url': '/api/quotes/{scope}/$get'}

    def create_reference_portfolio(
            self, scope, reference_portfolio=None, custom_headers=None, raw=False, **operation_config):
        """Create reference portfolio.

        Create a new reference portfolio.

        :param scope: The intended scope of the portfolio
        :type scope: str
        :param reference_portfolio: The portfolio creation request object
        :type reference_portfolio:
         ~lusid.models.CreateReferencePortfolioRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Portfolio or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_reference_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if reference_portfolio is not None:
            body_content = self._serialize.body(reference_portfolio, 'CreateReferencePortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_reference_portfolio.metadata = {'url': '/api/referenceportfolios/{scope}'}

    def get_reference_portfolio_constituents(
            self, scope, code, effective_at, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get constituents.

        Get all the constituents in the specified reference portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: The effective date of the constituents to
         retrieve
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use the
         '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: GetReferencePortfolioConstituentsResponse or
         ClientRawResponse if raw=true
        :rtype: ~lusid.models.GetReferencePortfolioConstituentsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_reference_portfolio_constituents.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GetReferencePortfolioConstituentsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_reference_portfolio_constituents.metadata = {'url': '/api/referenceportfolios/{scope}/{code}/{effectiveAt}/constituents'}

    def upsert_reference_portfolio_constituents(
            self, scope, code, constituents=None, custom_headers=None, raw=False, **operation_config):
        """Add constituents.

        Add constituents to the specified reference portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param constituents: The constituents to upload to the portfolio
        :type constituents:
         ~lusid.models.UpsertReferencePortfolioConstituentsRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertReferencePortfolioConstituentsResponse or
         ClientRawResponse if raw=true
        :rtype: ~lusid.models.UpsertReferencePortfolioConstituentsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_reference_portfolio_constituents.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if constituents is not None:
            body_content = self._serialize.body(constituents, 'UpsertReferencePortfolioConstituentsRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpsertReferencePortfolioConstituentsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_reference_portfolio_constituents.metadata = {'url': '/api/referenceportfolios/{scope}/{code}/constituents'}

    def get_results(
            self, scope, key, date_parameter, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get results.

        Retrieve some previously stored results.

        :param scope: The scope of the data
        :type scope: str
        :param key: The key that identifies the data
        :type key: str
        :param date_parameter: The date for which the data was loaded
        :type date_parameter: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Results or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Results or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_results.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'key': self._serialize.url("key", key, 'str'),
            'date': self._serialize.url("date_parameter", date_parameter, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Results', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_results.metadata = {'url': '/api/results/{scope}/{key}/{date}'}

    def upsert_results(
            self, scope, key, date_parameter, request=None, custom_headers=None, raw=False, **operation_config):
        """Upsert results.

        Upsert pre-calculated results against a specified scope/key/date
        combination.

        :param scope: The scope of the data
        :type scope: str
        :param key: The key that identifies the data
        :type key: str
        :param date_parameter: The date for which the data is relevant
        :type date_parameter: datetime
        :param request: The results to upload
        :type request: ~lusid.models.CreateResults
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Results or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Results or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_results.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'key': self._serialize.url("key", key, 'str'),
            'date': self._serialize.url("date_parameter", date_parameter, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreateResults')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Results', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_results.metadata = {'url': '/api/results/{scope}/{key}/{date}'}

    def get_aggregation_by_result_set(
            self, scope, results_key, request=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate using result data.

        Aggregate data from a previously-run Result data set into a flat row of
        results.

        :param scope: The scope of the Result data set
        :type scope: str
        :param results_key: The key of the Result data set
        :type results_key: str
        :param request: The request specifying the parameters of the
         aggregation
        :type request: ~lusid.models.AggregationRequest
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ListAggregationResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ListAggregationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_aggregation_by_result_set.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'resultsKey': self._serialize.url("results_key", results_key, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ListAggregationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_aggregation_by_result_set.metadata = {'url': '/api/results/{scope}/{resultsKey}/$aggregate'}

    def list_entities(
            self, custom_headers=None, raw=False, **operation_config):
        """List entities.

        List all available entities for which schema information is available.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfString or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfString or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_entities.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfString', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_entities.metadata = {'url': '/api/schemas/entities'}

    def get_entity_schema(
            self, entity, custom_headers=None, raw=False, **operation_config):
        """Get schema.

        Gets the schema and meta-data for a given entity.

        :param entity: The name of a valid entity
        :type entity: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Schema or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Schema or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_entity_schema.metadata['url']
        path_format_arguments = {
            'entity': self._serialize.url("entity", entity, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Schema', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_entity_schema.metadata = {'url': '/api/schemas/entities/{entity}'}

    def get_property_schema(
            self, property_keys=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get property schema.

        Get the schemas for the provided list of property keys.

        :param property_keys: One or more property keys for which the schema
         is requested
        :type property_keys: list[str]
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PropertySchema or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PropertySchema or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_property_schema.metadata['url']

        # Construct parameters
        query_parameters = {}
        if property_keys is not None:
            query_parameters['propertyKeys'] = self._serialize.query("property_keys", property_keys, '[str]', div=',')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertySchema', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_property_schema.metadata = {'url': '/api/schemas/properties'}

    def get_value_types(
            self, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get value types.

        Gets the available value types for which a schema is available.

        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfValueType or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfValueType or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_value_types.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfValueType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_value_types.metadata = {'url': '/api/schemas/types'}

    def portfolio_groups_search(
            self, request=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Search portfolio groups.

        Search through all portfolio groups.

        :param request: A valid Elasticsearch 5.x request
        :type request: object
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfPortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.portfolio_groups_search.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'object')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    portfolio_groups_search.metadata = {'url': '/api/search/portfoliogroups'}

    def portfolios_search(
            self, request=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Search portfolios.

        Search through all portfolios.

        :param request: A valid Elasticsearch 5.x request
        :type request: object
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPortfolioSearchResult or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfPortfolioSearchResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.portfolios_search.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'object')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPortfolioSearchResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    portfolios_search.metadata = {'url': '/api/search/portfolios'}

    def properties_search(
            self, request=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Search property definitions.

        Search through all property definitions.

        :param request: A valid Elasticsearch 5.x request
        :type request: object
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPropertyDefinition or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.ResourceListOfPropertyDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.properties_search.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'object')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPropertyDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    properties_search.metadata = {'url': '/api/search/propertydefinitions'}

    def list_configuration_transaction_types(
            self, custom_headers=None, raw=False, **operation_config):
        """List transaction types.

        Get the list of persisted transaction types.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfTransactionConfigurationData or
         ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfTransactionConfigurationData or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_configuration_transaction_types.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfTransactionConfigurationData', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_configuration_transaction_types.metadata = {'url': '/api/systemconfiguration/transactiontypes'}

    def set_configuration_transaction_types(
            self, types=None, custom_headers=None, raw=False, **operation_config):
        """Set transaction types.

        Set all transaction types to be used by the movements engine, for the
        organisation
        WARNING! Changing these mappings will have a material impact on how
        data, new and old, is processed and aggregated by LUSID. This will
        affect your whole organisation. Only change if you are fully aware of
        the implications of the change.

        :param types: The complete set of transaction type definitions
        :type types: list[~lusid.models.TransactionConfigurationDataRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfTransactionConfigurationData or
         ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfTransactionConfigurationData or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.set_configuration_transaction_types.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if types is not None:
            body_content = self._serialize.body(types, '[TransactionConfigurationDataRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfTransactionConfigurationData', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    set_configuration_transaction_types.metadata = {'url': '/api/systemconfiguration/transactiontypes'}

    def create_configuration_transaction_type(
            self, type=None, custom_headers=None, raw=False, **operation_config):
        """Create transaction type.

        Create a new transaction type by specifying a definition and the
        mappings to movements.

        :param type: A transaction type definition
        :type type: ~lusid.models.TransactionConfigurationDataRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfTransactionConfigurationData or
         ClientRawResponse if raw=true
        :rtype: ~lusid.models.ResourceListOfTransactionConfigurationData or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_configuration_transaction_type.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if type is not None:
            body_content = self._serialize.body(type, 'TransactionConfigurationDataRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('ResourceListOfTransactionConfigurationData', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_configuration_transaction_type.metadata = {'url': '/api/systemconfiguration/transactiontypes'}

    def create_portfolio(
            self, scope, create_request=None, custom_headers=None, raw=False, **operation_config):
        """Create transaction portfolio.

        Create a transaction portfolio in a specific scope.

        :param scope: The scope into which the transaction portfolio will be
         created
        :type scope: str
        :param create_request: The transaction portfolio definition
        :type create_request: ~lusid.models.CreateTransactionPortfolioRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusid.models.Portfolio or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if create_request is not None:
            body_content = self._serialize.body(create_request, 'CreateTransactionPortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_portfolio.metadata = {'url': '/api/transactionportfolios/{scope}'}

    def get_details(
            self, scope, code, effective_at=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get portfolio details.

        Get the details document associated with a transaction portfolio
        When requesting details from a derived transaction portfolio, the
        returned set of details could come from a different transaction
        portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: Optional. The effective date of the data
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioDetails or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_details.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_details.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/details'}

    def upsert_portfolio_details(
            self, scope, code, details=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Upsert details.

        Update the portfolio details for the specified transaction portfolios
        or add if it doesn't already exist (in the case of a derived
        transaction portfolio).

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param details: The set of details for the portfolio
        :type details: ~lusid.models.CreatePortfolioDetails
        :param effective_at: Optional. The effective date of the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioDetails or ClientRawResponse if raw=true
        :rtype: ~lusid.models.PortfolioDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_portfolio_details.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if details is not None:
            body_content = self._serialize.body(details, 'CreatePortfolioDetails')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_portfolio_details.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/details'}

    def upsert_executions(
            self, scope, code, executions=None, custom_headers=None, raw=False, **operation_config):
        """Upsert executions.

        Inserts new executions, or updates those already present.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param executions: The executions to be updated
        :type executions: list[~lusid.models.ExecutionRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertPortfolioExecutionsResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.UpsertPortfolioExecutionsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_executions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if executions is not None:
            body_content = self._serialize.body(executions, '[ExecutionRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpsertPortfolioExecutionsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_executions.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/executions'}

    def get_holdings(
            self, scope, code, by_taxlots=None, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, filter=None, instrument_property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Get holdings.

        Get the aggregate holdings of a transaction portfolio.  If no
        effectiveAt or asAt
        are supplied then values will be defaulted to the latest system time.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param by_taxlots: Option to expand holdings to return the underlying
         tax-lots
        :type by_taxlots: bool
        :param effective_at: Optional. The effective date of the portfolio
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param instrument_property_keys: Optional. Keys for the instrument
         property values to be decorated onto the holdings
        :type instrument_property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VersionedResourceListOfPortfolioHolding or ClientRawResponse
         if raw=true
        :rtype: ~lusid.models.VersionedResourceListOfPortfolioHolding or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if by_taxlots is not None:
            query_parameters['byTaxlots'] = self._serialize.query("by_taxlots", by_taxlots, 'bool')
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionedResourceListOfPortfolioHolding', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_holdings.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/holdings'}

    def set_holdings(
            self, scope, code, effective_at, holding_adjustments=None, custom_headers=None, raw=False, **operation_config):
        """Set all holdings on a transaction portfolio.

        Prompt the creation of transactions in a specific transaction portfolio
        to bring all holdings to the specified targets.

        :param scope: The scope of the transaction portfolio
        :type scope: str
        :param code: The code of the transaction portfolio
        :type code: str
        :param effective_at: The effective date of the change
        :type effective_at: datetime
        :param holding_adjustments: The complete set of holdings adjustments
         for the portfolio
        :type holding_adjustments: list[~lusid.models.AdjustHoldingRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AdjustHolding or ClientRawResponse if raw=true
        :rtype: ~lusid.models.AdjustHolding or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.set_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if holding_adjustments is not None:
            body_content = self._serialize.body(holding_adjustments, '[AdjustHoldingRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdjustHolding', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    set_holdings.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt}'}

    def adjust_holdings(
            self, scope, code, effective_at, holding_adjustments=None, custom_headers=None, raw=False, **operation_config):
        """Adjust holdings.

        Adjust one or more holdings in a transaction portfolio
        Prompt the creation of transactions in a specific transaction portfolio
        to bring selected holdings to the specified targets.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: The effective date of the change
        :type effective_at: datetime
        :param holding_adjustments: The selected set of holdings adjustments
        :type holding_adjustments: list[~lusid.models.AdjustHoldingRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AdjustHolding or ClientRawResponse if raw=true
        :rtype: ~lusid.models.AdjustHolding or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.adjust_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if holding_adjustments is not None:
            body_content = self._serialize.body(holding_adjustments, '[AdjustHoldingRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdjustHolding', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    adjust_holdings.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt}'}

    def cancel_adjust_holdings(
            self, scope, code, effective_at, custom_headers=None, raw=False, **operation_config):
        """Cancel holdings adjustments.

        Cancel previous adjust-holdings for the portfolio for a specific date.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: The effective date of the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.cancel_adjust_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    cancel_adjust_holdings.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt}'}

    def list_holdings_adjustments(
            self, scope, code, from_effective_at=None, to_effective_at=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """List holdings adjustments.

        Get holdings adjustments from a transaction portfolio in an interval of
        effective time.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param from_effective_at: Holdings adjustments between this time
         (inclusive) and the toEffectiveAt are returned.
        :type from_effective_at: datetime
        :param to_effective_at: Holdings adjustments between this time
         (inclusive) and the fromEffectiveAt are returned.
        :type to_effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfHoldingsAdjustmentHeader or ClientRawResponse
         if raw=true
        :rtype: ~lusid.models.ResourceListOfHoldingsAdjustmentHeader or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_holdings_adjustments.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_effective_at is not None:
            query_parameters['fromEffectiveAt'] = self._serialize.query("from_effective_at", from_effective_at, 'iso-8601')
        if to_effective_at is not None:
            query_parameters['toEffectiveAt'] = self._serialize.query("to_effective_at", to_effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfHoldingsAdjustmentHeader', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_holdings_adjustments.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/holdingsadjustments'}

    def get_holdings_adjustment(
            self, scope, code, effective_at, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get holding adjustment.

        Get a holdings adjustment for a transaction portfolio at a specific
        effective time.
        A holdings adjustment definition will only be returned if one exists
        for the specified effective time.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param effective_at: The effective time of the holdings adjustment
        :type effective_at: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: HoldingsAdjustment or ClientRawResponse if raw=true
        :rtype: ~lusid.models.HoldingsAdjustment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_holdings_adjustment.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('HoldingsAdjustment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_holdings_adjustment.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt}'}

    def get_transactions(
            self, scope, code, from_transaction_date=None, to_transaction_date=None, as_at=None, sort_by=None, start=None, limit=None, instrument_property_keys=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get transactions.

        Get the transactions from a transaction portfolio
        When the requested portfolio is a derived transaction portfolio, the
        returned set of transactions is the union set of all transactions of
        the parent (and ancestors) and the specified portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param from_transaction_date: Optional. Limit the returned
         transactions to those with a transaction date equal or later than this
         date
        :type from_transaction_date: datetime
        :param to_transaction_date: Optional. Limit the returned transactions
         to those with a transaction date equal or before this date
        :type to_transaction_date: datetime
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param instrument_property_keys: Optional. Keys for the instrument
         property values that will be decorated onto the transactions
        :type instrument_property_keys: list[str]
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VersionedResourceListOfTransaction or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.VersionedResourceListOfTransaction or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_transactions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_transaction_date is not None:
            query_parameters['fromTransactionDate'] = self._serialize.query("from_transaction_date", from_transaction_date, 'iso-8601')
        if to_transaction_date is not None:
            query_parameters['toTransactionDate'] = self._serialize.query("to_transaction_date", to_transaction_date, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionedResourceListOfTransaction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_transactions.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/transactions'}

    def upsert_transactions(
            self, scope, code, transactions=None, custom_headers=None, raw=False, **operation_config):
        """Upsert transactions into the specified transaction portfolio.

        Upsert transactions.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code for the portfolio
        :type code: str
        :param transactions: The transactions to be upserted
        :type transactions: list[~lusid.models.TransactionRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertPortfolioTransactionsResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.UpsertPortfolioTransactionsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.upsert_transactions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if transactions is not None:
            body_content = self._serialize.body(transactions, '[TransactionRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpsertPortfolioTransactionsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_transactions.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/transactions'}

    def delete_transactions(
            self, scope, code, transaction_ids=None, custom_headers=None, raw=False, **operation_config):
        """Delete transactions.

        Delete one or more transactions from a transaction portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param transaction_ids: Ids of transactions to delete
        :type transaction_ids: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_transactions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if transaction_ids is not None:
            query_parameters['transactionIds'] = self._serialize.query("transaction_ids", transaction_ids, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_transactions.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/transactions'}

    def add_transaction_property(
            self, scope, code, transaction_id, transaction_properties=None, custom_headers=None, raw=False, **operation_config):
        """Add transaction properties.

        Upsert one or more transaction properties to a single transaction in a
        portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param transaction_id: Id of transaction
        :type transaction_id: str
        :param transaction_properties: Transaction properties values
        :type transaction_properties: dict[str,
         ~lusid.models.PerpetualPropertyValue]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AddTransactionPropertyResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusid.models.AddTransactionPropertyResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.add_transaction_property.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'transactionId': self._serialize.url("transaction_id", transaction_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if transaction_properties is not None:
            body_content = self._serialize.body(transaction_properties, '{PerpetualPropertyValue}')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AddTransactionPropertyResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_transaction_property.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties'}

    def delete_property_from_transaction(
            self, scope, code, transaction_id, transaction_property_key=None, custom_headers=None, raw=False, **operation_config):
        """Delete transaction property.

        Delete a property value from a single transaction in a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param transaction_id: Id of the transaction to delete the property
         from
        :type transaction_id: str
        :param transaction_property_key: The key of the property to be deleted
        :type transaction_property_key: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusid.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_property_from_transaction.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'transactionId': self._serialize.url("transaction_id", transaction_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if transaction_property_key is not None:
            query_parameters['transactionPropertyKey'] = self._serialize.query("transaction_property_key", transaction_property_key, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_property_from_transaction.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties'}

    def build_transactions(
            self, scope, code, as_at=None, sort_by=None, start=None, limit=None, instrument_property_keys=None, filter=None, parameters=None, custom_headers=None, raw=False, **operation_config):
        """Build output transactions.

        Builds and returns the collection of all types of transactions that
        affect the holdings of a portfolio in to a set of output transactions.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The code of the portfolio
        :type code: str
        :param as_at: Optional. The AsAt date of the data
        :type as_at: datetime
        :param sort_by: Optional. Order the results by these fields. Use use
         the '-' sign to denote descending order e.g. -MyFieldName
        :type sort_by: list[str]
        :param start: Optional. When paginating, skip this number of results
        :type start: int
        :param limit: Optional. When paginating, limit the number of returned
         results to this many.
        :type limit: int
        :param instrument_property_keys: Optional. Keys for the instrument
         property values to be decorated onto the transactions
        :type instrument_property_keys: list[str]
        :param filter: Optional. Expression to filter the result set
        :type filter: str
        :param parameters: Optional. Transaction query parameters
        :type parameters: ~lusid.models.TransactionQueryParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VersionedResourceListOfOutputTransaction or ClientRawResponse
         if raw=true
        :rtype: ~lusid.models.VersionedResourceListOfOutputTransaction or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<lusid.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.build_transactions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if parameters is not None:
            body_content = self._serialize.body(parameters, 'TransactionQueryParameters')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionedResourceListOfOutputTransaction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    build_transactions.metadata = {'url': '/api/transactionportfolios/{scope}/{code}/transactions/$build'}
