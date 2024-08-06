# FundingLegOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_funding_leg_notional** | **str** | Assumption made on future expected notional of the funding leg. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.funding_leg_options import FundingLegOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FundingLegOptions from a JSON string
funding_leg_options_instance = FundingLegOptions.from_json(json)
# print the JSON string representation of the object
print FundingLegOptions.to_json()

# convert the object into a dict
funding_leg_options_dict = funding_leg_options_instance.to_dict()
# create an instance of FundingLegOptions from a dict
funding_leg_options_form_dict = funding_leg_options.from_dict(funding_leg_options_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


