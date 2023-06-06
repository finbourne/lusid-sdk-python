# FxDependencyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domestic_currency** | **str** | DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. | 
**foreign_currency** | **str** | ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. | 
**var_date** | **datetime** | The effectiveAt of the fx rate. | 
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

## Example

```python
from lusid.models.fx_dependency_all_of import FxDependencyAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FxDependencyAllOf from a JSON string
fx_dependency_all_of_instance = FxDependencyAllOf.from_json(json)
# print the JSON string representation of the object
print FxDependencyAllOf.to_json()

# convert the object into a dict
fx_dependency_all_of_dict = fx_dependency_all_of_instance.to_dict()
# create an instance of FxDependencyAllOf from a dict
fx_dependency_all_of_form_dict = fx_dependency_all_of.from_dict(fx_dependency_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


