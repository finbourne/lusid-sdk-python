# SettlementCycle

The settlement cycle for an instrument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_day_offset** | **int** |  | 
**calendars** | [**List[ResourceId]**](ResourceId.md) |  | 

## Example

```python
from lusid.models.settlement_cycle import SettlementCycle

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementCycle from a JSON string
settlement_cycle_instance = SettlementCycle.from_json(json)
# print the JSON string representation of the object
print SettlementCycle.to_json()

# convert the object into a dict
settlement_cycle_dict = settlement_cycle_instance.to_dict()
# create an instance of SettlementCycle from a dict
settlement_cycle_form_dict = settlement_cycle.from_dict(settlement_cycle_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


