# CashFlowValue

Result class for a cash flow value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The payment date of the cash flow | 
**diagnostics** | [**ResultValueDictionary**](ResultValueDictionary.md) |  | [optional] 
**cash_flow_lineage** | [**CashFlowLineage**](CashFlowLineage.md) |  | [optional] 
**payment_amount** | **float** | The amount paid or received | 
**payment_ccy** | **str** | The currency of the transaction | 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.cash_flow_value import CashFlowValue

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowValue from a JSON string
cash_flow_value_instance = CashFlowValue.from_json(json)
# print the JSON string representation of the object
print CashFlowValue.to_json()

# convert the object into a dict
cash_flow_value_dict = cash_flow_value_instance.to_dict()
# create an instance of CashFlowValue from a dict
cash_flow_value_form_dict = cash_flow_value.from_dict(cash_flow_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


