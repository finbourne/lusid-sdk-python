# ResourceListOfDataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[DataType]**](DataType.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_data_type import ResourceListOfDataType

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfDataType from a JSON string
resource_list_of_data_type_instance = ResourceListOfDataType.from_json(json)
# print the JSON string representation of the object
print ResourceListOfDataType.to_json()

# convert the object into a dict
resource_list_of_data_type_dict = resource_list_of_data_type_instance.to_dict()
# create an instance of ResourceListOfDataType from a dict
resource_list_of_data_type_form_dict = resource_list_of_data_type.from_dict(resource_list_of_data_type_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


