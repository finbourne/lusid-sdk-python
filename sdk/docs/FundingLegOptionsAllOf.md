# FundingLegOptionsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_funding_leg_notional** | **str** | Assumption made on future expected notional of the funding leg. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.funding_leg_options_all_of import FundingLegOptionsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FundingLegOptionsAllOf from a JSON string
funding_leg_options_all_of_instance = FundingLegOptionsAllOf.from_json(json)
# print the JSON string representation of the object
print FundingLegOptionsAllOf.to_json()

# convert the object into a dict
funding_leg_options_all_of_dict = funding_leg_options_all_of_instance.to_dict()
# create an instance of FundingLegOptionsAllOf from a dict
funding_leg_options_all_of_form_dict = funding_leg_options_all_of.from_dict(funding_leg_options_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


