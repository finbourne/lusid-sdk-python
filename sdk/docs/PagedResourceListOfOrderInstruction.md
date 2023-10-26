# PagedResourceListOfOrderInstruction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[OrderInstruction]**](OrderInstruction.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_order_instruction import PagedResourceListOfOrderInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfOrderInstruction from a JSON string
paged_resource_list_of_order_instruction_instance = PagedResourceListOfOrderInstruction.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfOrderInstruction.to_json()

# convert the object into a dict
paged_resource_list_of_order_instruction_dict = paged_resource_list_of_order_instruction_instance.to_dict()
# create an instance of PagedResourceListOfOrderInstruction from a dict
paged_resource_list_of_order_instruction_form_dict = paged_resource_list_of_order_instruction.from_dict(paged_resource_list_of_order_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


