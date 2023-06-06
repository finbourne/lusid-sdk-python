# StockSplitEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equity_split_ratio** | **float** | This number describes the rate at which the company will be dividing their current shares outstanding. It is displayed as new shares per old. | 
**payment_date** | **datetime** | Date on which the stock-split takes effect. | 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.stock_split_event_all_of import StockSplitEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of StockSplitEventAllOf from a JSON string
stock_split_event_all_of_instance = StockSplitEventAllOf.from_json(json)
# print the JSON string representation of the object
print StockSplitEventAllOf.to_json()

# convert the object into a dict
stock_split_event_all_of_dict = stock_split_event_all_of_instance.to_dict()
# create an instance of StockSplitEventAllOf from a dict
stock_split_event_all_of_form_dict = stock_split_event_all_of.from_dict(stock_split_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


