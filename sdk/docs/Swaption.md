# Swaption

A swaption, an option to enter into an interest rate swap.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | 
**is_payer_not_receiver** | **bool** | True if on exercise the holder of the option enters the swap paying fixed, false if floating. | 
**is_delivery_not_cash** | **bool** | True of the option is settled in cash false if by delivery of the swap. | 
**swap** | [**LusidInstrument**](LusidInstrument.md) |  | 
**instrument_type** | **str** | Instrument type, must be property for JSON. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


