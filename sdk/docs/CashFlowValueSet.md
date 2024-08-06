# CashFlowValueSet

Result value for a collection of cash flow values

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashflows** | [**List[CashFlowValue]**](CashFlowValue.md) | The set of cash flows in the result | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.cash_flow_value_set import CashFlowValueSet

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowValueSet from a JSON string
cash_flow_value_set_instance = CashFlowValueSet.from_json(json)
# print the JSON string representation of the object
print CashFlowValueSet.to_json()

# convert the object into a dict
cash_flow_value_set_dict = cash_flow_value_set_instance.to_dict()
# create an instance of CashFlowValueSet from a dict
cash_flow_value_set_form_dict = cash_flow_value_set.from_dict(cash_flow_value_set_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


