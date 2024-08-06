# AssetLeg

The underlying instrument representing one side of the TRS and its pay-receive direction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**LusidInstrument**](LusidInstrument.md) |  | 
**pay_receive** | **str** | Either Pay or Receive stating direction of the asset in the swap.    Supported string (enumeration) values are: [Pay, Receive]. | 

## Example

```python
from lusid.models.asset_leg import AssetLeg

# TODO update the JSON string below
json = "{}"
# create an instance of AssetLeg from a JSON string
asset_leg_instance = AssetLeg.from_json(json)
# print the JSON string representation of the object
print AssetLeg.to_json()

# convert the object into a dict
asset_leg_dict = asset_leg_instance.to_dict()
# create an instance of AssetLeg from a dict
asset_leg_form_dict = asset_leg.from_dict(asset_leg_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


