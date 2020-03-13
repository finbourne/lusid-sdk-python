# CdsInstrument

IL CDS Instrument; Lusid-ibor internal representation of a Credit Default Swap instrument
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | A ticker to uniquely specify then entity against which the cds is written | 
**flow_conventions** | [**list[FlowConventions]**](FlowConventions.md) | Flow Convention details for the legs of the CDS (in practice the conventions for the protection leg are limited/based on premium leg) | 
**coupon_rate** | **float** | The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \&quot;0.05\&quot; meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps. | 
**detail_specification** | [**CdsDetailSpecification**](CdsDetailSpecification.md) |  | 
**start_date** | **datetime** | Starting date of the credit default swap | 
**maturity_date** | **datetime** | Maturity date of the credit default swap | 
**dom_ccy** | **str** | Domestic currency of the credit default swap | 
**instrument_type** | **str** | Instrument type, must be property for JSON. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


