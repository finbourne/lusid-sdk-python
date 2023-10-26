# ResourceListOfOrderInstruction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[OrderInstruction]**](OrderInstruction.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_order_instruction import ResourceListOfOrderInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfOrderInstruction from a JSON string
resource_list_of_order_instruction_instance = ResourceListOfOrderInstruction.from_json(json)
# print the JSON string representation of the object
print ResourceListOfOrderInstruction.to_json()

# convert the object into a dict
resource_list_of_order_instruction_dict = resource_list_of_order_instruction_instance.to_dict()
# create an instance of ResourceListOfOrderInstruction from a dict
resource_list_of_order_instruction_form_dict = resource_list_of_order_instruction.from_dict(resource_list_of_order_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


