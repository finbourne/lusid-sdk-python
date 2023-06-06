# CashDividendEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gross_amount** | **float** | The before tax amount for each share held being paid out to shareholders. | 
**payment_date** | **datetime** | The date the company pays out dividends to shareholders. | 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.cash_dividend_event_all_of import CashDividendEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CashDividendEventAllOf from a JSON string
cash_dividend_event_all_of_instance = CashDividendEventAllOf.from_json(json)
# print the JSON string representation of the object
print CashDividendEventAllOf.to_json()

# convert the object into a dict
cash_dividend_event_all_of_dict = cash_dividend_event_all_of_instance.to_dict()
# create an instance of CashDividendEventAllOf from a dict
cash_dividend_event_all_of_form_dict = cash_dividend_event_all_of.from_dict(cash_dividend_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


