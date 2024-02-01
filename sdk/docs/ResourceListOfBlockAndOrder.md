# ResourceListOfBlockAndOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[BlockAndOrder]**](BlockAndOrder.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_block_and_order import ResourceListOfBlockAndOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfBlockAndOrder from a JSON string
resource_list_of_block_and_order_instance = ResourceListOfBlockAndOrder.from_json(json)
# print the JSON string representation of the object
print ResourceListOfBlockAndOrder.to_json()

# convert the object into a dict
resource_list_of_block_and_order_dict = resource_list_of_block_and_order_instance.to_dict()
# create an instance of ResourceListOfBlockAndOrder from a dict
resource_list_of_block_and_order_form_dict = resource_list_of_block_and_order.from_dict(resource_list_of_block_and_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


