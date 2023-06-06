# LifeCycleEventValueAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | The effective date of the event | [optional] 
**event_values** | [**ResultValueDictionary**](ResultValueDictionary.md) |  | [optional] 
**event_lineage** | [**LifeCycleEventLineage**](LifeCycleEventLineage.md) |  | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 

## Example

```python
from lusid.models.life_cycle_event_value_all_of import LifeCycleEventValueAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of LifeCycleEventValueAllOf from a JSON string
life_cycle_event_value_all_of_instance = LifeCycleEventValueAllOf.from_json(json)
# print the JSON string representation of the object
print LifeCycleEventValueAllOf.to_json()

# convert the object into a dict
life_cycle_event_value_all_of_dict = life_cycle_event_value_all_of_instance.to_dict()
# create an instance of LifeCycleEventValueAllOf from a dict
life_cycle_event_value_all_of_form_dict = life_cycle_event_value_all_of.from_dict(life_cycle_event_value_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


