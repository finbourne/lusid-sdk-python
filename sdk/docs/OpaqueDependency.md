# OpaqueDependency

Represents a dependency that could not be understood as an externally exposed dependency.  If this is an unexpected dependency, then please contact support.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

## Example

```python
from lusid.models.opaque_dependency import OpaqueDependency

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueDependency from a JSON string
opaque_dependency_instance = OpaqueDependency.from_json(json)
# print the JSON string representation of the object
print OpaqueDependency.to_json()

# convert the object into a dict
opaque_dependency_dict = opaque_dependency_instance.to_dict()
# create an instance of OpaqueDependency from a dict
opaque_dependency_form_dict = opaque_dependency.from_dict(opaque_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


