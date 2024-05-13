# AmortisationEvent

Definition of an Amortisation event.  This is an event that describes the occurence of amortisation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_reduced** | **float** | The amount reduced in this amortisation event.  That is, the difference between the previous notional amount and the current notional amount as set in this event. | 
**dom_ccy** | **str** | Domestic currency of the originating instrument | 
**pay_receive** | **str** | Is this event in relation to the Pay or Receive leg | 
**payment_date** | **datetime** | The date the principal payment is to be made. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent | 

## Example

```python
from lusid.models.amortisation_event import AmortisationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AmortisationEvent from a JSON string
amortisation_event_instance = AmortisationEvent.from_json(json)
# print the JSON string representation of the object
print AmortisationEvent.to_json()

# convert the object into a dict
amortisation_event_dict = amortisation_event_instance.to_dict()
# create an instance of AmortisationEvent from a dict
amortisation_event_form_dict = amortisation_event.from_dict(amortisation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


