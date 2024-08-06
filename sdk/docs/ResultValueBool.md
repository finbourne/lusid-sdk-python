# ResultValueBool

A simple result for a boolean value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** | The value itself | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_bool import ResultValueBool

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueBool from a JSON string
result_value_bool_instance = ResultValueBool.from_json(json)
# print the JSON string representation of the object
print ResultValueBool.to_json()

# convert the object into a dict
result_value_bool_dict = result_value_bool_instance.to_dict()
# create an instance of ResultValueBool from a dict
result_value_bool_form_dict = result_value_bool.from_dict(result_value_bool_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


