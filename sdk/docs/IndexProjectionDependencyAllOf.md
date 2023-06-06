# IndexProjectionDependencyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the corresponding IndexConvention. E.g. this would be USD for a convention named USD.6M.LIBOR | 
**tenor** | **str** | The tenor of the corresponding IndexConvention. E.g. this would be \&quot;6M\&quot; for a convention named USD.6M.LIBOR | 
**index_name** | **str** | The IndexName of the corresponding IndexConvention. E.g. this would be \&quot;LIBOR\&quot; for a convention named USD.6M.LIBOR | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

## Example

```python
from lusid.models.index_projection_dependency_all_of import IndexProjectionDependencyAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of IndexProjectionDependencyAllOf from a JSON string
index_projection_dependency_all_of_instance = IndexProjectionDependencyAllOf.from_json(json)
# print the JSON string representation of the object
print IndexProjectionDependencyAllOf.to_json()

# convert the object into a dict
index_projection_dependency_all_of_dict = index_projection_dependency_all_of_instance.to_dict()
# create an instance of IndexProjectionDependencyAllOf from a dict
index_projection_dependency_all_of_form_dict = index_projection_dependency_all_of.from_dict(index_projection_dependency_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


