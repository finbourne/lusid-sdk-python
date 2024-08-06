# BlockAndOrders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**orders** | [**List[Order]**](Order.md) |  | 

## Example

```python
from lusid.models.block_and_orders import BlockAndOrders

# TODO update the JSON string below
json = "{}"
# create an instance of BlockAndOrders from a JSON string
block_and_orders_instance = BlockAndOrders.from_json(json)
# print the JSON string representation of the object
print BlockAndOrders.to_json()

# convert the object into a dict
block_and_orders_dict = block_and_orders_instance.to_dict()
# create an instance of BlockAndOrders from a dict
block_and_orders_form_dict = block_and_orders.from_dict(block_and_orders_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


