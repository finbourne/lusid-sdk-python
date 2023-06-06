# ResourceListOfProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ModelProperty]**](ModelProperty.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_property import ResourceListOfProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfProperty from a JSON string
resource_list_of_property_instance = ResourceListOfProperty.from_json(json)
# print the JSON string representation of the object
print ResourceListOfProperty.to_json()

# convert the object into a dict
resource_list_of_property_dict = resource_list_of_property_instance.to_dict()
# create an instance of ResourceListOfProperty from a dict
resource_list_of_property_form_dict = resource_list_of_property.from_dict(resource_list_of_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


