# CancelOrdersAndMoveRemainingRequest

A request to create or update a Order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_order_id** | [**ResourceId**](ResourceId.md) |  | 
**move_remaining_to_order_id** | [**ResourceId**](ResourceId.md) |  | 
**move_remaining_to_block_id** | [**ResourceId**](ResourceId.md) |  | 

## Example

```python
from lusid.models.cancel_orders_and_move_remaining_request import CancelOrdersAndMoveRemainingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrdersAndMoveRemainingRequest from a JSON string
cancel_orders_and_move_remaining_request_instance = CancelOrdersAndMoveRemainingRequest.from_json(json)
# print the JSON string representation of the object
print CancelOrdersAndMoveRemainingRequest.to_json()

# convert the object into a dict
cancel_orders_and_move_remaining_request_dict = cancel_orders_and_move_remaining_request_instance.to_dict()
# create an instance of CancelOrdersAndMoveRemainingRequest from a dict
cancel_orders_and_move_remaining_request_form_dict = cancel_orders_and_move_remaining_request.from_dict(cancel_orders_and_move_remaining_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


