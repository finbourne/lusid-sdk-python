# OrderInstructionRequest

A request to create or update a Order Instruction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**created_date** | **datetime** | The active date of this order instruction. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | [optional] 
**quantity** | **float** | The quantity of given instrument ordered. | [optional] 
**weight** | **float** | The weight of given instrument ordered. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 

## Example

```python
from lusid.models.order_instruction_request import OrderInstructionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderInstructionRequest from a JSON string
order_instruction_request_instance = OrderInstructionRequest.from_json(json)
# print the JSON string representation of the object
print OrderInstructionRequest.to_json()

# convert the object into a dict
order_instruction_request_dict = order_instruction_request_instance.to_dict()
# create an instance of OrderInstructionRequest from a dict
order_instruction_request_form_dict = order_instruction_request.from_dict(order_instruction_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


