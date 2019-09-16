# PricingOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_selection** | [**ModelSelection**](ModelSelection.md) |  | [optional] 
**use_instrument_type_to_determine_pricer** | **bool** | If true then use the instrument type to set the default instrument pricer  This applies where no more specific set of overrides are provided on a per-vendor and instrument basis. | [optional] 
**allow_any_instruments_with_sec_uid_to_price_off_lookup** | **bool** | By default, one would not expect to price and exotic instrument, i.e. an instrument with a complicated  instrument definition simply through looking up a price as there should be a better way of evaluating it.  To override that behaviour and allow lookup for a price from the instrument identifier(s), set this to true. | [optional] 
**allow_partially_successful_evaluation** | **bool** | If true then a failure in task evaluation doesn&#39;t cause overall failure.  results will be returned where they succeeded and annotation elsewhere | [optional] 
**produce_separate_result_for_linear_otc_legs** | **bool** | If true (default), when pricing an Fx-Forward or Interest Rate Swap, Future and other linearly separable products, product two results, one for each leg  rather than a single line result with the amalgamated/summed pv from both legs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


