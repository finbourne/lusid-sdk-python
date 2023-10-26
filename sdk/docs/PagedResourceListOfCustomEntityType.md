# PagedResourceListOfCustomEntityType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[CustomEntityType]**](CustomEntityType.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_custom_entity_type import PagedResourceListOfCustomEntityType

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfCustomEntityType from a JSON string
paged_resource_list_of_custom_entity_type_instance = PagedResourceListOfCustomEntityType.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfCustomEntityType.to_json()

# convert the object into a dict
paged_resource_list_of_custom_entity_type_dict = paged_resource_list_of_custom_entity_type_instance.to_dict()
# create an instance of PagedResourceListOfCustomEntityType from a dict
paged_resource_list_of_custom_entity_type_form_dict = paged_resource_list_of_custom_entity_type.from_dict(paged_resource_list_of_custom_entity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


