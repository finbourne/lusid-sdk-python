# ResourceListOfBlockAndOrders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[BlockAndOrders]**](BlockAndOrders.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_block_and_orders import ResourceListOfBlockAndOrders

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfBlockAndOrders from a JSON string
resource_list_of_block_and_orders_instance = ResourceListOfBlockAndOrders.from_json(json)
# print the JSON string representation of the object
print ResourceListOfBlockAndOrders.to_json()

# convert the object into a dict
resource_list_of_block_and_orders_dict = resource_list_of_block_and_orders_instance.to_dict()
# create an instance of ResourceListOfBlockAndOrders from a dict
resource_list_of_block_and_orders_form_dict = resource_list_of_block_and_orders.from_dict(resource_list_of_block_and_orders_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


