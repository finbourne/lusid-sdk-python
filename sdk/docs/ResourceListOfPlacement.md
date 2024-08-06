# ResourceListOfPlacement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Placement]**](Placement.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_placement import ResourceListOfPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfPlacement from a JSON string
resource_list_of_placement_instance = ResourceListOfPlacement.from_json(json)
# print the JSON string representation of the object
print ResourceListOfPlacement.to_json()

# convert the object into a dict
resource_list_of_placement_dict = resource_list_of_placement_instance.to_dict()
# create an instance of ResourceListOfPlacement from a dict
resource_list_of_placement_form_dict = resource_list_of_placement.from_dict(resource_list_of_placement_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


