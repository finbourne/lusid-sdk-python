# AmortisationEvent

Definition of an Amortisation event.  This is an event that describes the occurence of amortisation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_reduced** | **float** | The amount reduced in this amortisation event.  That is, the difference between the previous notional amount and the current notional amount as set in this event. | 
**dom_ccy** | **str** | Domestic currency of the originating instrument | 
**pay_receive** | **str** | Is this event in relation to the Pay or Receive leg | 
**event_status** | **str** | What is the event status, is it a known (ie historic) or unknown (ie projected) event? | 
**payment_date** | **datetime** | The date the principal payment is to be made. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


