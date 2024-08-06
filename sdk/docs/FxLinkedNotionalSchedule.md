# FxLinkedNotionalSchedule

Schedule for notional changes based on the change in FX rate.  Used in the representation of a resettable cross currency interest rate swap.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fx_conventions** | [**FxConventions**](FxConventions.md) |  | 
**varying_notional_currency** | **str** | The currency of the varying notional amount. | 
**varying_notional_fixing_dates** | [**RelativeDateOffset**](RelativeDateOffset.md) |  | 
**varying_notional_interim_exchange_payment_dates** | [**RelativeDateOffset**](RelativeDateOffset.md) |  | [optional] 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid | 

## Example

```python
from lusid.models.fx_linked_notional_schedule import FxLinkedNotionalSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of FxLinkedNotionalSchedule from a JSON string
fx_linked_notional_schedule_instance = FxLinkedNotionalSchedule.from_json(json)
# print the JSON string representation of the object
print FxLinkedNotionalSchedule.to_json()

# convert the object into a dict
fx_linked_notional_schedule_dict = fx_linked_notional_schedule_instance.to_dict()
# create an instance of FxLinkedNotionalSchedule from a dict
fx_linked_notional_schedule_form_dict = fx_linked_notional_schedule.from_dict(fx_linked_notional_schedule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


