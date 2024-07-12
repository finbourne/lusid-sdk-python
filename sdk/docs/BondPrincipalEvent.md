# BondPrincipalEvent

Definition of a Bond Principal Event  This is an event that describes the occurence of a cashflow due to the principal payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of the principal payment | 
**ex_date** | **datetime** | Ex-Dividend date of the principal payment | 
**payment_date** | **datetime** | Payment date of the principal payment | 
**principal_per_unit** | **float** | Principal per unit | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent | 

## Example

```python
from lusid.models.bond_principal_event import BondPrincipalEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BondPrincipalEvent from a JSON string
bond_principal_event_instance = BondPrincipalEvent.from_json(json)
# print the JSON string representation of the object
print BondPrincipalEvent.to_json()

# convert the object into a dict
bond_principal_event_dict = bond_principal_event_instance.to_dict()
# create an instance of BondPrincipalEvent from a dict
bond_principal_event_form_dict = bond_principal_event.from_dict(bond_principal_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


