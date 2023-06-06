# ResultValueDateTimeOffsetAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** | The value itself | [optional] 
**dimension** | **int** | The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion. | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_date_time_offset_all_of import ResultValueDateTimeOffsetAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueDateTimeOffsetAllOf from a JSON string
result_value_date_time_offset_all_of_instance = ResultValueDateTimeOffsetAllOf.from_json(json)
# print the JSON string representation of the object
print ResultValueDateTimeOffsetAllOf.to_json()

# convert the object into a dict
result_value_date_time_offset_all_of_dict = result_value_date_time_offset_all_of_instance.to_dict()
# create an instance of ResultValueDateTimeOffsetAllOf from a dict
result_value_date_time_offset_all_of_form_dict = result_value_date_time_offset_all_of.from_dict(result_value_date_time_offset_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


