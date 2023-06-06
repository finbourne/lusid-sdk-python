# FxForwardsDependencyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domestic_currency** | **str** | DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. | 
**foreign_currency** | **str** | ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. | 
**curve_type** | **str** | Used to describe the format in which the curve is expressed  e.g. FxFwdCurve (general term to describe any representation), TenorFxFwdCurve, PipsFxFwdCurve. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

## Example

```python
from lusid.models.fx_forwards_dependency_all_of import FxForwardsDependencyAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FxForwardsDependencyAllOf from a JSON string
fx_forwards_dependency_all_of_instance = FxForwardsDependencyAllOf.from_json(json)
# print the JSON string representation of the object
print FxForwardsDependencyAllOf.to_json()

# convert the object into a dict
fx_forwards_dependency_all_of_dict = fx_forwards_dependency_all_of_instance.to_dict()
# create an instance of FxForwardsDependencyAllOf from a dict
fx_forwards_dependency_all_of_form_dict = fx_forwards_dependency_all_of.from_dict(fx_forwards_dependency_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


