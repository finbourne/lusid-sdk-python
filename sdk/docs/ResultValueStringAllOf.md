# ResultValueStringAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | the value itself | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_string_all_of import ResultValueStringAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueStringAllOf from a JSON string
result_value_string_all_of_instance = ResultValueStringAllOf.from_json(json)
# print the JSON string representation of the object
print ResultValueStringAllOf.to_json()

# convert the object into a dict
result_value_string_all_of_dict = result_value_string_all_of_instance.to_dict()
# create an instance of ResultValueStringAllOf from a dict
result_value_string_all_of_form_dict = result_value_string_all_of.from_dict(result_value_string_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


