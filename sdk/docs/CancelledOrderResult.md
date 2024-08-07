# CancelledOrderResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_state** | [**Order**](Order.md) |  | [optional] 

## Example

```python
from lusid.models.cancelled_order_result import CancelledOrderResult

# TODO update the JSON string below
json = "{}"
# create an instance of CancelledOrderResult from a JSON string
cancelled_order_result_instance = CancelledOrderResult.from_json(json)
# print the JSON string representation of the object
print CancelledOrderResult.to_json()

# convert the object into a dict
cancelled_order_result_dict = cancelled_order_result_instance.to_dict()
# create an instance of CancelledOrderResult from a dict
cancelled_order_result_form_dict = cancelled_order_result.from_dict(cancelled_order_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


