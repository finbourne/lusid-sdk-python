# OpenEvent

The opening of an instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor_date** | **datetime** | The date on the which the instrument was opened. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent | 

## Example

```python
from lusid.models.open_event import OpenEvent

# TODO update the JSON string below
json = "{}"
# create an instance of OpenEvent from a JSON string
open_event_instance = OpenEvent.from_json(json)
# print the JSON string representation of the object
print OpenEvent.to_json()

# convert the object into a dict
open_event_dict = open_event_instance.to_dict()
# create an instance of OpenEvent from a dict
open_event_form_dict = open_event.from_dict(open_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


