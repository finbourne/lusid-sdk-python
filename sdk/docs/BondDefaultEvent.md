# BondDefaultEvent

Indicates when an issuer has defaulted on an obligation due to technical default, missed payments, or bankruptcy filing.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | The date the bond default occurred. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent | 

## Example

```python
from lusid.models.bond_default_event import BondDefaultEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BondDefaultEvent from a JSON string
bond_default_event_instance = BondDefaultEvent.from_json(json)
# print the JSON string representation of the object
print BondDefaultEvent.to_json()

# convert the object into a dict
bond_default_event_dict = bond_default_event_instance.to_dict()
# create an instance of BondDefaultEvent from a dict
bond_default_event_form_dict = bond_default_event.from_dict(bond_default_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


