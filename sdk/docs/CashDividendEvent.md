# CashDividendEvent

A cash distribution paid out to shareholders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The date the company begins distributing the dividend. | 
**ex_date** | **datetime** | The first business day on which the dividend is not owed to the buying party. | 
**cash_elections** | [**List[CashElection]**](CashElection.md) | Possible elections for this event, each keyed with a unique identifier. | 
**announcement_date** | **datetime** | Date on which the dividend is announced by the company. | [optional] 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent | 

## Example

```python
from lusid.models.cash_dividend_event import CashDividendEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CashDividendEvent from a JSON string
cash_dividend_event_instance = CashDividendEvent.from_json(json)
# print the JSON string representation of the object
print CashDividendEvent.to_json()

# convert the object into a dict
cash_dividend_event_dict = cash_dividend_event_instance.to_dict()
# create an instance of CashDividendEvent from a dict
cash_dividend_event_form_dict = cash_dividend_event.from_dict(cash_dividend_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


