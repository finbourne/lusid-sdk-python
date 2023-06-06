# CashFlowValueSetAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashflows** | [**List[CashFlowValue]**](CashFlowValue.md) | The set of cash flows in the result | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.cash_flow_value_set_all_of import CashFlowValueSetAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowValueSetAllOf from a JSON string
cash_flow_value_set_all_of_instance = CashFlowValueSetAllOf.from_json(json)
# print the JSON string representation of the object
print CashFlowValueSetAllOf.to_json()

# convert the object into a dict
cash_flow_value_set_all_of_dict = cash_flow_value_set_all_of_instance.to_dict()
# create an instance of CashFlowValueSetAllOf from a dict
cash_flow_value_set_all_of_form_dict = cash_flow_value_set_all_of.from_dict(cash_flow_value_set_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


