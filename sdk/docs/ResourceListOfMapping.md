# ResourceListOfMapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Mapping]**](Mapping.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_mapping import ResourceListOfMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfMapping from a JSON string
resource_list_of_mapping_instance = ResourceListOfMapping.from_json(json)
# print the JSON string representation of the object
print ResourceListOfMapping.to_json()

# convert the object into a dict
resource_list_of_mapping_dict = resource_list_of_mapping_instance.to_dict()
# create an instance of ResourceListOfMapping from a dict
resource_list_of_mapping_form_dict = resource_list_of_mapping.from_dict(resource_list_of_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


