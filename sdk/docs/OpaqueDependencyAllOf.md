# OpaqueDependencyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

## Example

```python
from lusid.models.opaque_dependency_all_of import OpaqueDependencyAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueDependencyAllOf from a JSON string
opaque_dependency_all_of_instance = OpaqueDependencyAllOf.from_json(json)
# print the JSON string representation of the object
print OpaqueDependencyAllOf.to_json()

# convert the object into a dict
opaque_dependency_all_of_dict = opaque_dependency_all_of_instance.to_dict()
# create an instance of OpaqueDependencyAllOf from a dict
opaque_dependency_all_of_form_dict = opaque_dependency_all_of.from_dict(opaque_dependency_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


