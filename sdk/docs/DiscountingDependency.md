# DiscountingDependency

For indicating a dependency on discounting for a given currency.  E.g Valuing a Bond with the Discounting model will declare a DiscountingDependency  for the domestic currency of the bond to account for the time-value of the future cashFlows of the bond.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency that needs to be discounted. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

## Example

```python
from lusid.models.discounting_dependency import DiscountingDependency

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountingDependency from a JSON string
discounting_dependency_instance = DiscountingDependency.from_json(json)
# print the JSON string representation of the object
print DiscountingDependency.to_json()

# convert the object into a dict
discounting_dependency_dict = discounting_dependency_instance.to_dict()
# create an instance of DiscountingDependency from a dict
discounting_dependency_form_dict = discounting_dependency.from_dict(discounting_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


