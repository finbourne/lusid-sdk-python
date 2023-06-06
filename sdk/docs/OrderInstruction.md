# OrderInstruction

Record of an order instruction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**created_date** | **datetime** | The active date of this order instruction. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**quantity** | **float** | The quantity of given instrument ordered. | [optional] 
**weight** | **float** | The weight of given instrument ordered. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**instrument_scope** | **str** | The scope in which the instrument lies | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument ordered. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.order_instruction import OrderInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of OrderInstruction from a JSON string
order_instruction_instance = OrderInstruction.from_json(json)
# print the JSON string representation of the object
print OrderInstruction.to_json()

# convert the object into a dict
order_instruction_dict = order_instruction_instance.to_dict()
# create an instance of OrderInstruction from a dict
order_instruction_form_dict = order_instruction.from_dict(order_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


