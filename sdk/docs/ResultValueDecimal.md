# ResultValueDecimal

A simple result for a decimal value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The value itself | [optional] 
**dimension** | **int** | The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion. | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value_decimal import ResultValueDecimal

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValueDecimal from a JSON string
result_value_decimal_instance = ResultValueDecimal.from_json(json)
# print the JSON string representation of the object
print ResultValueDecimal.to_json()

# convert the object into a dict
result_value_decimal_dict = result_value_decimal_instance.to_dict()
# create an instance of ResultValueDecimal from a dict
result_value_decimal_form_dict = result_value_decimal.from_dict(result_value_decimal_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


