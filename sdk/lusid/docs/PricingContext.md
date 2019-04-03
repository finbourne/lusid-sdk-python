# PricingContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_rules** | [**list[VendorModelRule]**](VendorModelRule.md) | The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options. | [optional] 
**model_choice** | [**dict(str, ModelSelection)**](ModelSelection.md) | The choice of which model selection (vendor library, pricing model) to use in evaluation of a given instrument type. | [optional] 
**options** | [**PricingOptions**](PricingOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


