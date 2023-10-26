# ResultValueCurrency

A simple result for a currency value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value itself | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_currency import ResultValueCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueCurrency from a JSON string
result_value_currency_instance = ResultValueCurrency.from_json(json)
# print the JSON string representation of the object
print ResultValueCurrency.to_json()

# convert the object into a dict
result_value_currency_dict = result_value_currency_instance.to_dict()
# create an instance of ResultValueCurrency from a dict
result_value_currency_form_dict = result_value_currency.from_dict(result_value_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


