# ResultValue

Base class for representing result values in LUSID.  This base class should not be directly instantiated; each supported ResultValueType has a corresponding inherited class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.result_value import ResultValue

# TODO update the JSON string below
json = "{}"
# create an instance of ResultValue from a JSON string
result_value_instance = ResultValue.from_json(json)
# print the JSON string representation of the object
print ResultValue.to_json()

# convert the object into a dict
result_value_dict = result_value_instance.to_dict()
# create an instance of ResultValue from a dict
result_value_form_dict = result_value.from_dict(result_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


