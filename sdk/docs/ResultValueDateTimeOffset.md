# ResultValueDateTimeOffset

A simple result for a date time value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** | The value itself | [optional] 
**dimension** | **int** | The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion. | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_date_time_offset import ResultValueDateTimeOffset

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueDateTimeOffset from a JSON string
result_value_date_time_offset_instance = ResultValueDateTimeOffset.from_json(json)
# print the JSON string representation of the object
print ResultValueDateTimeOffset.to_json()

# convert the object into a dict
result_value_date_time_offset_dict = result_value_date_time_offset_instance.to_dict()
# create an instance of ResultValueDateTimeOffset from a dict
result_value_date_time_offset_form_dict = result_value_date_time_offset.from_dict(result_value_date_time_offset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


