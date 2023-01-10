# TransitionEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The announcement date of the corporate action | [optional] 
**ex_date** | **datetime** | The ex date of the corporate action | [optional] 
**record_date** | **datetime** | The record date of the corporate action | [optional] 
**payment_date** | **datetime** | The payment date of the corporate action | [optional] 
**input_transition** | [**InputTransition**](InputTransition.md) |  | [optional] 
**output_transitions** | [**list[OutputTransition]**](OutputTransition.md) | The resulting transitions from this event | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


