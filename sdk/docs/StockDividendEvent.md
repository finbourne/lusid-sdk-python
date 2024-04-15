# StockDividendEvent

A payment to shareholders that consists of additional shares rather than cash.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Date on which the dividend was announced / declared. | [optional] 
**ex_date** | **datetime** | The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate. | 
**payment_date** | **datetime** | The date the company pays out dividends to shareholders. | 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent | 

## Example

```python
from lusid.models.stock_dividend_event import StockDividendEvent

# TODO update the JSON string below
json = "{}"
# create an instance of StockDividendEvent from a JSON string
stock_dividend_event_instance = StockDividendEvent.from_json(json)
# print the JSON string representation of the object
print StockDividendEvent.to_json()

# convert the object into a dict
stock_dividend_event_dict = stock_dividend_event_instance.to_dict()
# create an instance of StockDividendEvent from a dict
stock_dividend_event_form_dict = stock_dividend_event.from_dict(stock_dividend_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


