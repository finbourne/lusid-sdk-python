# OrderInstructionSetRequest

A request to create or update multiple OrderInstructions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[OrderInstructionRequest]**](OrderInstructionRequest.md) | A collection of OrderInstructionRequests. | [optional] 

## Example

```python
from lusid.models.order_instruction_set_request import OrderInstructionSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderInstructionSetRequest from a JSON string
order_instruction_set_request_instance = OrderInstructionSetRequest.from_json(json)
# print the JSON string representation of the object
print OrderInstructionSetRequest.to_json()

# convert the object into a dict
order_instruction_set_request_dict = order_instruction_set_request_instance.to_dict()
# create an instance of OrderInstructionSetRequest from a dict
order_instruction_set_request_form_dict = order_instruction_set_request.from_dict(order_instruction_set_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


