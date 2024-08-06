# ReconciliationBreak

A reconciliation break

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] 
**instrument_uid** | **str** | Unique instrument identifier | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Any other properties that comprise the Sub-Holding Key | 
**left_units** | **float** | Units from the left hand side | 
**right_units** | **float** | Units from the right hand side | 
**difference_units** | **float** | Difference in units | 
**left_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**right_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**difference_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**instrument_properties** | [**List[ModelProperty]**](ModelProperty.md) | Additional features relating to the instrument | 

## Example

```python
from lusid.models.reconciliation_break import ReconciliationBreak

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationBreak from a JSON string
reconciliation_break_instance = ReconciliationBreak.from_json(json)
# print the JSON string representation of the object
print ReconciliationBreak.to_json()

# convert the object into a dict
reconciliation_break_dict = reconciliation_break_instance.to_dict()
# create an instance of ReconciliationBreak from a dict
reconciliation_break_form_dict = reconciliation_break.from_dict(reconciliation_break_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


