# MovedOrderToDifferentBlockResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_block** | [**Block**](Block.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**source_block_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.moved_order_to_different_block_response import MovedOrderToDifferentBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MovedOrderToDifferentBlockResponse from a JSON string
moved_order_to_different_block_response_instance = MovedOrderToDifferentBlockResponse.from_json(json)
# print the JSON string representation of the object
print MovedOrderToDifferentBlockResponse.to_json()

# convert the object into a dict
moved_order_to_different_block_response_dict = moved_order_to_different_block_response_instance.to_dict()
# create an instance of MovedOrderToDifferentBlockResponse from a dict
moved_order_to_different_block_response_form_dict = moved_order_to_different_block_response.from_dict(moved_order_to_different_block_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


