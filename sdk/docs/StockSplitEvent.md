# StockSplitEvent

A split in the company's shares. Shareholders are given additional company shares based on the terms of the stock split.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equity_split_ratio** | **float** | This number describes the rate at which the company will be dividing their current shares outstanding. It is displayed as new shares per old. | 
**payment_date** | **datetime** | Date on which the stock-split takes effect. | 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.stock_split_event import StockSplitEvent

# TODO update the JSON string below
json = "{}"
# create an instance of StockSplitEvent from a JSON string
stock_split_event_instance = StockSplitEvent.from_json(json)
# print the JSON string representation of the object
print StockSplitEvent.to_json()

# convert the object into a dict
stock_split_event_dict = stock_split_event_instance.to_dict()
# create an instance of StockSplitEvent from a dict
stock_split_event_form_dict = stock_split_event.from_dict(stock_split_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


