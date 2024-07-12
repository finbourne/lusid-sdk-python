# InformationalErrorEvent

Event holder containing error information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_detail** | **str** | The details of the error | 
**error_reason** | **str** | The error reason | 
**effective_at** | **datetime** | The effective date of the evaulation | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent | 

## Example

```python
from lusid.models.informational_error_event import InformationalErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of InformationalErrorEvent from a JSON string
informational_error_event_instance = InformationalErrorEvent.from_json(json)
# print the JSON string representation of the object
print InformationalErrorEvent.to_json()

# convert the object into a dict
informational_error_event_dict = informational_error_event_instance.to_dict()
# create an instance of InformationalErrorEvent from a dict
informational_error_event_form_dict = informational_error_event.from_dict(informational_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


