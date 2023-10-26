# ResultValueString

A simple result value holding a string

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | the value itself | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_string import ResultValueString

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueString from a JSON string
result_value_string_instance = ResultValueString.from_json(json)
# print the JSON string representation of the object
print ResultValueString.to_json()

# convert the object into a dict
result_value_string_dict = result_value_string_instance.to_dict()
# create an instance of ResultValueString from a dict
result_value_string_form_dict = result_value_string.from_dict(result_value_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


