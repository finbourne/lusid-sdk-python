# AccumulationEvent

Accumulation dividend

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Date on which the dividend was announced / declared. | [optional] 
**dividend_currency** | **str** | Payment currency | 
**dividend_rate** | **float** | Dividend rate or payment rate as a percentage.  i.e. 5% is written as 0.05 | 
**ex_date** | **datetime** | The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate. | 
**payment_date** | **datetime** | The date the company pays out dividends to shareholders. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent | 

## Example

```python
from lusid.models.accumulation_event import AccumulationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AccumulationEvent from a JSON string
accumulation_event_instance = AccumulationEvent.from_json(json)
# print the JSON string representation of the object
print AccumulationEvent.to_json()

# convert the object into a dict
accumulation_event_dict = accumulation_event_instance.to_dict()
# create an instance of AccumulationEvent from a dict
accumulation_event_form_dict = accumulation_event.from_dict(accumulation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


