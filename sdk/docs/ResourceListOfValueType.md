# ResourceListOfValueType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ValueType]**](ValueType.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_value_type import ResourceListOfValueType

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfValueType from a JSON string
resource_list_of_value_type_instance = ResourceListOfValueType.from_json(json)
# print the JSON string representation of the object
print ResourceListOfValueType.to_json()

# convert the object into a dict
resource_list_of_value_type_dict = resource_list_of_value_type_instance.to_dict()
# create an instance of ResourceListOfValueType from a dict
resource_list_of_value_type_form_dict = resource_list_of_value_type.from_dict(resource_list_of_value_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


