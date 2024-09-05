# SpecificHoldingPricingInfo

Allows a user to specify fallbacks/overrides using Holding fields for sources that match a particular DependencySourceFilter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_source_filter** | [**DependencySourceFilter**](DependencySourceFilter.md) |  | 
**field** | **str** | The Holding field which the fallback/override should use to create a price quote. | 

## Example

```python
from lusid.models.specific_holding_pricing_info import SpecificHoldingPricingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificHoldingPricingInfo from a JSON string
specific_holding_pricing_info_instance = SpecificHoldingPricingInfo.from_json(json)
# print the JSON string representation of the object
print SpecificHoldingPricingInfo.to_json()

# convert the object into a dict
specific_holding_pricing_info_dict = specific_holding_pricing_info_instance.to_dict()
# create an instance of SpecificHoldingPricingInfo from a dict
specific_holding_pricing_info_form_dict = specific_holding_pricing_info.from_dict(specific_holding_pricing_info_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


