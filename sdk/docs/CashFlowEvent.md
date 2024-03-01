# CashFlowEvent

Definition of a CashFlow event.  This is an event that describes the occurence of a cashflow and associated information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_flow_value** | [**CashFlowValue**](CashFlowValue.md) |  | 
**event_type** | **str** | What type of internal event does this represent; coupon, principal, premium etc. | [readonly] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent | 

## Example

```python
from lusid.models.cash_flow_event import CashFlowEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowEvent from a JSON string
cash_flow_event_instance = CashFlowEvent.from_json(json)
# print the JSON string representation of the object
print CashFlowEvent.to_json()

# convert the object into a dict
cash_flow_event_dict = cash_flow_event_instance.to_dict()
# create an instance of CashFlowEvent from a dict
cash_flow_event_form_dict = cash_flow_event.from_dict(cash_flow_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


