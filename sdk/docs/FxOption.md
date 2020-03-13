# FxOption

Lusid-ibor DTO representation of a plain vanilla FX Option instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the option. | 
**option_maturity_date** | **datetime** | The maturity date of the option. | 
**option_settlement_date** | **datetime** | The settlement date of the option. | 
**is_delivery_not_cash** | **bool** | True of the option is settled in cash false if delivery. | 
**is_call_not_put** | **bool** | True if the option is a call, false if the option is a put. | 
**strike** | **float** | The strike of the option. | 
**dom_ccy** | **str** | The domestic currency of the FX. | 
**fgn_ccy** | **str** | The foreign currency of the FX. | 
**instrument_type** | **str** | Instrument type, must be property for JSON. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


