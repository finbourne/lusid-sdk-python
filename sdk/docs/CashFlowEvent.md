# CashFlowEvent

Definition of a CashFlow event.  This is an event that describes the occurence of a cashflow and associated information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_flow_value** | [**CashFlowValue**](CashFlowValue.md) |  | 
**event_type** | **str** | What type of internal event does this represent; coupon, principal, premium etc. | [readonly] 
**event_status** | **str** | What is the event status, is it a known (ie historic) or unknown (ie projected) event? | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


