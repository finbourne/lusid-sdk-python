# SwapInstrument

IL Swap Instrument; Lusid-ibor internal representation of a swap instrument                A swap is the exchange of two sets of cashflows, occurring at one or more dates in one or more currencies.  These may include a notional exchange at the start and, or, maturity of the trade. Depending upon the choice of  payment currency, payment frequency and so on they can be used to match sets of future obligations
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Starting date of the swap | 
**maturity_date** | **datetime** | Maturity date of the swap | 
**legs** | [**list[InstrumentLeg]**](InstrumentLeg.md) | True if the swap is amortizing | 
**notional** | **float** | The notional. | 
**is_amortizing** | **bool** | True if the swap is amortizing | 
**notional_exchange_type** | **str** | True notional exchange type. | 
**instrument_type** | **str** | Instrument type, must be property for JSON. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


