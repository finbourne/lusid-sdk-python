# ResultValueCurrencyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value itself | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_currency_all_of import ResultValueCurrencyAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueCurrencyAllOf from a JSON string
result_value_currency_all_of_instance = ResultValueCurrencyAllOf.from_json(json)
# print the JSON string representation of the object
print ResultValueCurrencyAllOf.to_json()

# convert the object into a dict
result_value_currency_all_of_dict = result_value_currency_all_of_instance.to_dict()
# create an instance of ResultValueCurrencyAllOf from a dict
result_value_currency_all_of_form_dict = result_value_currency_all_of.from_dict(result_value_currency_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


