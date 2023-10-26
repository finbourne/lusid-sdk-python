# LookUpPricingModelOptions

Model options for look up pricing.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_accrual** | **bool** | Add Instrument Accrual to Valuation | 
**apply_index_ratio** | **bool** | Apply Index Ratio to price before valuation.  Used for InflationLinkedBond | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, LookUpPricingModelOptions | 

## Example

```python
from lusid.models.look_up_pricing_model_options import LookUpPricingModelOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LookUpPricingModelOptions from a JSON string
look_up_pricing_model_options_instance = LookUpPricingModelOptions.from_json(json)
# print the JSON string representation of the object
print LookUpPricingModelOptions.to_json()

# convert the object into a dict
look_up_pricing_model_options_dict = look_up_pricing_model_options_instance.to_dict()
# create an instance of LookUpPricingModelOptions from a dict
look_up_pricing_model_options_form_dict = look_up_pricing_model_options.from_dict(look_up_pricing_model_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


