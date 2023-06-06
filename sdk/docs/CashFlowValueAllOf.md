# CashFlowValueAllOf


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
from lusid.models.cash_flow_value_all_of import CashFlowValueAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowValueAllOf from a JSON string
cash_flow_value_all_of_instance = CashFlowValueAllOf.from_json(json)
# print the JSON string representation of the object
print CashFlowValueAllOf.to_json()

# convert the object into a dict
cash_flow_value_all_of_dict = cash_flow_value_all_of_instance.to_dict()
# create an instance of CashFlowValueAllOf from a dict
cash_flow_value_all_of_form_dict = cash_flow_value_all_of.from_dict(cash_flow_value_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


