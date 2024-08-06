# FxVolDependency

Economic dependency required to price FX derivative products that contain optionality.  FX Vol surface is a grid of implied volatilities for an array of strikes and tenors,  derived from vanilla option prices in the market.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domestic_currency** | **str** | DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. | 
**foreign_currency** | **str** | ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. | 
**vol_type** | **str** | Volatility type e.g. \&quot;LN\&quot; and \&quot;N\&quot; for log-normal and normal volatility. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

## Example

```python
from lusid.models.fx_vol_dependency import FxVolDependency

# TODO update the JSON string below
json = "{}"
# create an instance of FxVolDependency from a JSON string
fx_vol_dependency_instance = FxVolDependency.from_json(json)
# print the JSON string representation of the object
print FxVolDependency.to_json()

# convert the object into a dict
fx_vol_dependency_dict = fx_vol_dependency_instance.to_dict()
# create an instance of FxVolDependency from a dict
fx_vol_dependency_form_dict = fx_vol_dependency.from_dict(fx_vol_dependency_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


