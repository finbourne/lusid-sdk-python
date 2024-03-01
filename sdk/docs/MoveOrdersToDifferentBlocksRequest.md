# MoveOrdersToDifferentBlocksRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BlockAndOrderIdRequest]**](BlockAndOrderIdRequest.md) | A collection of BlockAndOrderId. | 

## Example

```python
from lusid.models.move_orders_to_different_blocks_request import MoveOrdersToDifferentBlocksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MoveOrdersToDifferentBlocksRequest from a JSON string
move_orders_to_different_blocks_request_instance = MoveOrdersToDifferentBlocksRequest.from_json(json)
# print the JSON string representation of the object
print MoveOrdersToDifferentBlocksRequest.to_json()

# convert the object into a dict
move_orders_to_different_blocks_request_dict = move_orders_to_different_blocks_request_instance.to_dict()
# create an instance of MoveOrdersToDifferentBlocksRequest from a dict
move_orders_to_different_blocks_request_form_dict = move_orders_to_different_blocks_request.from_dict(move_orders_to_different_blocks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


