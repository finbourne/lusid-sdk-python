# LifeCycleEventValue

The instrument life cycle event result value type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | The effective date of the event | [optional] 
**event_values** | [**ResultValueDictionary**](ResultValueDictionary.md) |  | [optional] 
**event_lineage** | [**LifeCycleEventLineage**](LifeCycleEventLineage.md) |  | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.life_cycle_event_value import LifeCycleEventValue

# TODO update the JSON string below
json = "{}"
# create an instance of LifeCycleEventValue from a JSON string
life_cycle_event_value_instance = LifeCycleEventValue.from_json(json)
# print the JSON string representation of the object
print LifeCycleEventValue.to_json()

# convert the object into a dict
life_cycle_event_value_dict = life_cycle_event_value_instance.to_dict()
# create an instance of LifeCycleEventValue from a dict
life_cycle_event_value_form_dict = life_cycle_event_value.from_dict(life_cycle_event_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


