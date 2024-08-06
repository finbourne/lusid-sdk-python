# ResultValueDictionary

Result value for a collection of key-value pairs. Used for diagnostics associated to a cash flow, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**Dict[str, ResultValue]**](ResultValue.md) | The dictionary elements | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_dictionary import ResultValueDictionary

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueDictionary from a JSON string
result_value_dictionary_instance = ResultValueDictionary.from_json(json)
# print the JSON string representation of the object
print ResultValueDictionary.to_json()

# convert the object into a dict
result_value_dictionary_dict = result_value_dictionary_instance.to_dict()
# create an instance of ResultValueDictionary from a dict
result_value_dictionary_form_dict = result_value_dictionary.from_dict(result_value_dictionary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


