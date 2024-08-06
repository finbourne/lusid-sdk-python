# LifeCycleEventLineage

The lineage of the event value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The type of the event | [optional] 
**instrument_type** | **str** | The instrument type of the instrument for the event. | [optional] 
**instrument_id** | **str** | The LUID of the instrument for the event. | [optional] 
**leg_id** | **str** | Leg id for the event. | [optional] 
**source_transaction_id** | **str** | The source transaction of the instrument for the event. | [optional] 

## Example

```python
from lusid.models.life_cycle_event_lineage import LifeCycleEventLineage

# TODO update the JSON string below
json = "{}"
# create an instance of LifeCycleEventLineage from a JSON string
life_cycle_event_lineage_instance = LifeCycleEventLineage.from_json(json)
# print the JSON string representation of the object
print LifeCycleEventLineage.to_json()

# convert the object into a dict
life_cycle_event_lineage_dict = life_cycle_event_lineage_instance.to_dict()
# create an instance of LifeCycleEventLineage from a dict
life_cycle_event_lineage_form_dict = life_cycle_event_lineage.from_dict(life_cycle_event_lineage_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


