# TriggerEvent

Definition of a trigger event.  This is an event that occurs on transformation of an option instrument being  triggered by a barrier/touch price level being hit by the underlying asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | The underlying price level that triggers the event | 
**trigger_type** | **str** | The type of the trigger; valid options are Knock-In, Knock-Out, Touch or No-Touch | 
**trigger_direction** | **str** | The direction of the trigger; valid options are Up and Down | 
**trigger_date** | **datetime** | The date the trigger happens at. | 
**maturity_date** | **datetime** | The date the trigger takes effect. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


