# MarketDataSpecificRule

Extends market data key rules to be able to catch dependencies depending on where the dependency comes from, as opposed to what the dependency is asking for.  For example, a market data rule might instruct all rates curves to be retrieved from a particular scope.  This class gives the ability to set different behaviour depending on what is requesting the rates curve.  Using two specific rules, one could instruct rates curves requested by bonds to be retrieved from a different scope than rates curves requested by swaps.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The market data key pattern which this is a rule for. A dot separated string (A.B.C.D.*) | 
**supplier** | **str** | The market data supplier (where the data comes from) | 
**data_scope** | **str** | The scope in which the data should be found when using this rule. | 
**quote_type** | **str** | The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta | 
**field** | **str** | The conceptual qualification for the field, such as bid, mid, or ask.  The field must be one of a defined set for the given supplier, in the same way as it  is for the Finbourne.WebApi.Interface.Dto.Quotes.QuoteSeriesId | 
**quote_interval** | **str** | Shorthand for the time interval used to select market data. This must be a dot-separated string              nominating a start and end date, for example &#39;5D.0D&#39; to look back 5 days from today (0 days ago). The syntax              is &lt;i&gt;int&lt;/i&gt;&lt;i&gt;char&lt;/i&gt;.&lt;i&gt;int&lt;/i&gt;&lt;i&gt;char&lt;/i&gt;, where &lt;i&gt;char&lt;/i&gt; is one of D(ay), W(eek), M(onth) or Y(ear). | [optional] 
**as_at** | **datetime** | The AsAt predicate specification. | [optional] 
**price_source** | **str** | The source of the quote. For a given provider/supplier of market data there may be an additional qualifier, e.g. the exchange or bank that provided the quote | [optional] 
**mask** | **str** | Allows for partial or complete override of the market asset resolved for a dependency  Either a named override or a dot separated string (A.B.C.D.*).  e.g. for Rates curve &#39;EUR.*&#39; will replace the resolve MarketAsset &#39;GBP/12M&#39;, &#39;GBP/3M&#39; with the EUR equivalent, if there  are no wildcards in the mask, the mask is taken as the MarketAsset for any dependency matching the rule. | [optional] 
**dependency_source_filter** | [**DependencySourceFilter**](DependencySourceFilter.md) |  | 
**source_system** | **str** | Determines from where LUSID should attempt to find the data. Optional and, if omitted, will default to \&quot;Lusid\&quot;.  This means that data will be retrieved from the Quotes store and the ComplexMarketData store.  These can be populated using the Quotes and ComplexMarketData endpoints. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


