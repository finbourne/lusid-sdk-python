# CdsModelOptions

Model options for credit default instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_factors_for_current_notional** | **bool** | Determines if calculations that use current notional apply use a constituent weight factor from a quote representing a default. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 

## Example

```python
from lusid.models.cds_model_options import CdsModelOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CdsModelOptions from a JSON string
cds_model_options_instance = CdsModelOptions.from_json(json)
# print the JSON string representation of the object
print CdsModelOptions.to_json()

# convert the object into a dict
cds_model_options_dict = cds_model_options_instance.to_dict()
# create an instance of CdsModelOptions from a dict
cds_model_options_form_dict = cds_model_options.from_dict(cds_model_options_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


