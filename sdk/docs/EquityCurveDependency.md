# EquityCurveDependency

For indicating a dependency on an EquityCurve.  E.g. When pricing an EquitySwap one may want to make predictions about the price of the underlying equity at future dates.  If so, that model would declare an EquityCurve dependency so that it could obtain predictions from the EquityCurve.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_identifier** | **str** | Type of the code identifying the corresponding equity, e.g. ISIN or CUSIP | 
**code** | **str** | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN | 
**curve_type** | **str** | The curve type of the EquityCurve required. E.g. EquityCurveByPrices | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

## Example

```python
from lusid.models.equity_curve_dependency import EquityCurveDependency

# TODO update the JSON string below
json = "{}"
# create an instance of EquityCurveDependency from a JSON string
equity_curve_dependency_instance = EquityCurveDependency.from_json(json)
# print the JSON string representation of the object
print EquityCurveDependency.to_json()

# convert the object into a dict
equity_curve_dependency_dict = equity_curve_dependency_instance.to_dict()
# create an instance of EquityCurveDependency from a dict
equity_curve_dependency_form_dict = equity_curve_dependency.from_dict(equity_curve_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


