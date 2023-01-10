# StockSplitEvent

A split in the company's shares. Shareholders are given additional company shares based on the terms of the stock split.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equity_split_ratio** | **float** | This number describes the rate at which the company will be dividing their current shares outstanding. It is displayed as new shares per old. | 
**payment_date** | **datetime** | Date on which the stock-split takes effect. | 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


