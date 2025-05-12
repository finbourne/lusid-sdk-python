# ResourceListOfReturnsEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ReturnsEntity]**](ReturnsEntity.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_returns_entity import ResourceListOfReturnsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfReturnsEntity from a JSON string
resource_list_of_returns_entity_instance = ResourceListOfReturnsEntity.from_json(json)
# print the JSON string representation of the object
print ResourceListOfReturnsEntity.to_json()

# convert the object into a dict
resource_list_of_returns_entity_dict = resource_list_of_returns_entity_instance.to_dict()
# create an instance of ResourceListOfReturnsEntity from a dict
resource_list_of_returns_entity_form_dict = resource_list_of_returns_entity.from_dict(resource_list_of_returns_entity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


