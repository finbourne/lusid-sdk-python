# FxForwardModelOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward_rate_observable_type** | **str** | The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid | 
**discounting_method** | **str** | The available values are: Standard, ConstantTimeValueOfMoney, Invalid | 
**convert_to_report_ccy** | **bool** | Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, LookUpPricingModelOptions | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


