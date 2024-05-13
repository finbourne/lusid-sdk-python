# ScripDividendEvent

A scrip dividend issued to shareholders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Date on which the dividend was announced / declared. | [optional] 
**ex_date** | **datetime** | The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate. | 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | [optional] 
**payment_date** | **datetime** | The date the company pays out dividends to shareholders. | 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent | 

## Example

```python
from lusid.models.scrip_dividend_event import ScripDividendEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScripDividendEvent from a JSON string
scrip_dividend_event_instance = ScripDividendEvent.from_json(json)
# print the JSON string representation of the object
print ScripDividendEvent.to_json()

# convert the object into a dict
scrip_dividend_event_dict = scrip_dividend_event_instance.to_dict()
# create an instance of ScripDividendEvent from a dict
scrip_dividend_event_form_dict = scrip_dividend_event.from_dict(scrip_dividend_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


