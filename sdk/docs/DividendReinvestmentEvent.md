# DividendReinvestmentEvent

Event for dividend reinvestments.  Elections for cash or the associated security.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Date on which the dividend was announced / declared. | [optional] 
**cash_elections** | [**List[CashElection]**](CashElection.md) | CashElection for this DividendReinvestmentEvent | 
**ex_date** | **datetime** | The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate. | 
**payment_date** | **datetime** | The date the company pays out dividends to shareholders. | 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | 
**security_elections** | [**List[SecurityElection]**](SecurityElection.md) | SecurityElection for this DividendReinvestmentEvent | 
**security_settlement_date** | **datetime** | The settlement date of the additional units.  Equal to the PaymentDate if not provided. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent | 

## Example

```python
from lusid.models.dividend_reinvestment_event import DividendReinvestmentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DividendReinvestmentEvent from a JSON string
dividend_reinvestment_event_instance = DividendReinvestmentEvent.from_json(json)
# print the JSON string representation of the object
print DividendReinvestmentEvent.to_json()

# convert the object into a dict
dividend_reinvestment_event_dict = dividend_reinvestment_event_instance.to_dict()
# create an instance of DividendReinvestmentEvent from a dict
dividend_reinvestment_event_form_dict = dividend_reinvestment_event.from_dict(dividend_reinvestment_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


