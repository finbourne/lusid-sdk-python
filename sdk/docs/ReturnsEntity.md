# ReturnsEntity

Returns entity, used for configuring the calculation of aggregated returns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**recipe_entity** | **str** | Entity a recipe is retrieved from for use in the aggregated returns calculation. Either RecipeId or RecipeEntity must be specified. | [optional] 
**fee_handling** | **str** | Configures how fees are handled in the aggregated returns calculation. | [optional] 
**flow_handling** | **str** | Configures how flows are handled in the aggregated returns calculation. | [optional] 
**business_calendar** | **str** | Calendar used in the aggregated returns calculation. | [optional] 
**handle_flow_discrepancy** | **str** | Configures handling for the case where net flows do not match the sum of tagged flows. | [optional] 

## Example

```python
from lusid.models.returns_entity import ReturnsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsEntity from a JSON string
returns_entity_instance = ReturnsEntity.from_json(json)
# print the JSON string representation of the object
print ReturnsEntity.to_json()

# convert the object into a dict
returns_entity_dict = returns_entity_instance.to_dict()
# create an instance of ReturnsEntity from a dict
returns_entity_form_dict = returns_entity.from_dict(returns_entity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


