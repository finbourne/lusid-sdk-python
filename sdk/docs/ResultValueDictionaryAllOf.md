# ResultValueDictionaryAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**Dict[str, ResultValue]**](ResultValue.md) | The dictionary elements | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_dictionary_all_of import ResultValueDictionaryAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueDictionaryAllOf from a JSON string
result_value_dictionary_all_of_instance = ResultValueDictionaryAllOf.from_json(json)
# print the JSON string representation of the object
print ResultValueDictionaryAllOf.to_json()

# convert the object into a dict
result_value_dictionary_all_of_dict = result_value_dictionary_all_of_instance.to_dict()
# create an instance of ResultValueDictionaryAllOf from a dict
result_value_dictionary_all_of_form_dict = result_value_dictionary_all_of.from_dict(result_value_dictionary_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


