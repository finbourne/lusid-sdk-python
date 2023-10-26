# EquityVolDependency

Economic dependency required to price Equity derivative products that contain optionality.  Equity Vol surface is a grid of implied volatilities for an array of strikes and tenors,  derived from vanilla option prices in the market.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN | 
**domestic_currency** | **str** | The domestic currency of the instrument declaring this dependency. | 
**vol_type** | **str** | Volatility type e.g. \&quot;LN\&quot; and \&quot;N\&quot; for log-normal and normal volatility. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

## Example

```python
from lusid.models.equity_vol_dependency import EquityVolDependency

# TODO update the JSON string below
json = "{}"
# create an instance of EquityVolDependency from a JSON string
equity_vol_dependency_instance = EquityVolDependency.from_json(json)
# print the JSON string representation of the object
print EquityVolDependency.to_json()

# convert the object into a dict
equity_vol_dependency_dict = equity_vol_dependency_instance.to_dict()
# create an instance of EquityVolDependency from a dict
equity_vol_dependency_form_dict = equity_vol_dependency.from_dict(equity_vol_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


