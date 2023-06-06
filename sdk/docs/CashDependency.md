# CashDependency

For indicating a dependency upon a currency.  E.g. A Bond will declare a CashDependency for its domestic currency.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The Currency that is depended upon. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

## Example

```python
from lusid.models.cash_dependency import CashDependency

# TODO update the JSON string below
json = "{}"
# create an instance of CashDependency from a JSON string
cash_dependency_instance = CashDependency.from_json(json)
# print the JSON string representation of the object
print CashDependency.to_json()

# convert the object into a dict
cash_dependency_dict = cash_dependency_instance.to_dict()
# create an instance of CashDependency from a dict
cash_dependency_form_dict = cash_dependency.from_dict(cash_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


