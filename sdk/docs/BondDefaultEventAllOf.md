# BondDefaultEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Percentage or amount of each share held to be given to shareholders. | 
**coupon_paid_date** | **datetime** | Date that the missed coupon is paid if payment is made within grace period. | 
**default_status** | **str** | The status of the bond default (i.e., technical or default)    Supported string (enumeration) values are: [Technical, Default]. | 
**default_type** | **str** | The type of the default. (coupon payment, principal payment, covenant ...)    Supported string (enumeration) values are: [CouponPayment, CouponAndPrincipalPayment, PrincipalPayment, Covenant, Bankruptcy, BuyBackOption]. | 
**grace_end_date** | **datetime** | Date the grace period for making coupon payment ends. | 
**payment_date** | **datetime** | The date the coupon payment was missed. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


