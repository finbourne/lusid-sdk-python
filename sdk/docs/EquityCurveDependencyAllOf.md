# EquityCurveDependencyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_identifier** | **str** | Type of the code identifying the corresponding equity, e.g. ISIN or CUSIP | 
**code** | **str** | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN | 
**curve_type** | **str** | The curve type of the EquityCurve required. E.g. EquityCurveByPrices | 
**date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


