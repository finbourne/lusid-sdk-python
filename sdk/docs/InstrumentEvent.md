# InstrumentEvent

Base class for representing instrument events in LUSID, such as dividends, stock splits, and option exercises.  This base class should not be directly instantiated; each supported InstrumentEventType has a corresponding inherited class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent | 

## Example

```python
from lusid.models.instrument_event import InstrumentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentEvent from a JSON string
instrument_event_instance = InstrumentEvent.from_json(json)
# print the JSON string representation of the object
print InstrumentEvent.to_json()

# convert the object into a dict
instrument_event_dict = instrument_event_instance.to_dict()
# create an instance of InstrumentEvent from a dict
instrument_event_form_dict = instrument_event.from_dict(instrument_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


