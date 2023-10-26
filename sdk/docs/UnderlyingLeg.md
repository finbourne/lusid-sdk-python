# UnderlyingLeg

The underlying instrument representing one side of the TRS and its pay-receive direction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_receive** | **str** | Either Pay or Receive stating direction of the underlying in the swap.    Supported string (enumeration) values are: [Pay, Receive]. | 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | 

## Example

```python
from lusid.models.underlying_leg import UnderlyingLeg

# TODO update the JSON string below
json = "{}"
# create an instance of UnderlyingLeg from a JSON string
underlying_leg_instance = UnderlyingLeg.from_json(json)
# print the JSON string representation of the object
print UnderlyingLeg.to_json()

# convert the object into a dict
underlying_leg_dict = underlying_leg_instance.to_dict()
# create an instance of UnderlyingLeg from a dict
underlying_leg_form_dict = underlying_leg.from_dict(underlying_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


