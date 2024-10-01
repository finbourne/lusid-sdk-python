# CancelOrderAndMoveRemainingResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled_order** | [**Order**](Order.md) |  | [optional] 
**new_order** | [**Order**](Order.md) |  | [optional] 
**new_block_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.cancel_order_and_move_remaining_result import CancelOrderAndMoveRemainingResult

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderAndMoveRemainingResult from a JSON string
cancel_order_and_move_remaining_result_instance = CancelOrderAndMoveRemainingResult.from_json(json)
# print the JSON string representation of the object
print CancelOrderAndMoveRemainingResult.to_json()

# convert the object into a dict
cancel_order_and_move_remaining_result_dict = cancel_order_and_move_remaining_result_instance.to_dict()
# create an instance of CancelOrderAndMoveRemainingResult from a dict
cancel_order_and_move_remaining_result_form_dict = cancel_order_and_move_remaining_result.from_dict(cancel_order_and_move_remaining_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


