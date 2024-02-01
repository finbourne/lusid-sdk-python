# BlockAndOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**order** | [**Order**](Order.md) |  | 

## Example

```python
from lusid.models.block_and_order import BlockAndOrder

# TODO update the JSON string below
json = "{}"
# create an instance of BlockAndOrder from a JSON string
block_and_order_instance = BlockAndOrder.from_json(json)
# print the JSON string representation of the object
print BlockAndOrder.to_json()

# convert the object into a dict
block_and_order_dict = block_and_order_instance.to_dict()
# create an instance of BlockAndOrder from a dict
block_and_order_form_dict = block_and_order.from_dict(block_and_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


