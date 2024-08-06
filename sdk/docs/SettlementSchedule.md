# SettlementSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_id** | **str** |  | [optional] 
**settlement_date** | **datetime** |  | [optional] 
**units** | **float** |  | [optional] 

## Example

```python
from lusid.models.settlement_schedule import SettlementSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementSchedule from a JSON string
settlement_schedule_instance = SettlementSchedule.from_json(json)
# print the JSON string representation of the object
print SettlementSchedule.to_json()

# convert the object into a dict
settlement_schedule_dict = settlement_schedule_instance.to_dict()
# create an instance of SettlementSchedule from a dict
settlement_schedule_form_dict = settlement_schedule.from_dict(settlement_schedule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


