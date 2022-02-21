# InlineValuationRequest

Specification object for the parameters of an inline valuation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**as_at** | **datetime** | The asAt date to use | [optional] 
**metrics** | [**list[AggregateSpec]**](AggregateSpec.md) | The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec(&#39;Holding/default/PV&#39;,&#39;Sum&#39;) for returning the PV (present value) of holdings  AggregateSpec(&#39;Holding/default/Units&#39;,&#39;Sum&#39;) for returning the units of holidays  AggregateSpec(&#39;Instrument/default/LusidInstrumentId&#39;,&#39;Value&#39;) for returning the Lusid Instrument identifier | 
**group_by** | **list[str]** | The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out. | [optional] 
**filters** | [**list[PropertyFilter]**](PropertyFilter.md) | A set of filters to use to reduce the data found in a request. Equivalent to the &#39;where ...&#39; part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value. | [optional] 
**sort** | [**list[OrderBySpec]**](OrderBySpec.md) | A (possibly empty/null) set of specifications for how to order the results. | [optional] 
**report_currency** | **str** | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place. | [optional] 
**equip_with_subtotals** | **bool** | Flag directing the Valuation call to populate the results with subtotals of aggregates. | [optional] 
**valuation_schedule** | [**ValuationSchedule**](ValuationSchedule.md) |  | [optional] 
**instruments** | [**list[WeightedInstrument]**](WeightedInstrument.md) | The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


