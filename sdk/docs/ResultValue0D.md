# ResultValue0D

Result value representing a 0D result. These results can be equipped with a unit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | **str** | Unit of the result | [optional] 
**value** | **float** | The value of the result | [optional] 
**dimension** | **int** | The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion. | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value0_d import ResultValue0D

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValue0D from a JSON string
result_value0_d_instance = ResultValue0D.from_json(json)
# print the JSON string representation of the object
print ResultValue0D.to_json()

# convert the object into a dict
result_value0_d_dict = result_value0_d_instance.to_dict()
# create an instance of ResultValue0D from a dict
result_value0_d_form_dict = result_value0_d.from_dict(result_value0_d_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


