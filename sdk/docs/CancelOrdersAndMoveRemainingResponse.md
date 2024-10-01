# CancelOrdersAndMoveRemainingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, CancelOrderAndMoveRemainingResult]**](CancelOrderAndMoveRemainingResult.md) | The orders which have been successfully cancelled, and any remaining quantities moved. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The orders that could not be cancelled, along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Meta data associated with the cancellation event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.cancel_orders_and_move_remaining_response import CancelOrdersAndMoveRemainingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrdersAndMoveRemainingResponse from a JSON string
cancel_orders_and_move_remaining_response_instance = CancelOrdersAndMoveRemainingResponse.from_json(json)
# print the JSON string representation of the object
print CancelOrdersAndMoveRemainingResponse.to_json()

# convert the object into a dict
cancel_orders_and_move_remaining_response_dict = cancel_orders_and_move_remaining_response_instance.to_dict()
# create an instance of CancelOrdersAndMoveRemainingResponse from a dict
cancel_orders_and_move_remaining_response_form_dict = cancel_orders_and_move_remaining_response.from_dict(cancel_orders_and_move_remaining_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


