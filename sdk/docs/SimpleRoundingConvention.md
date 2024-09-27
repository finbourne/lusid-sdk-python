# SimpleRoundingConvention

Certain bonds will follow certain rounding conventions.  For example, Thai government bonds will round accrued interest and cashflow values 2dp, whereas for  French government bonds, the rounding is to 7dp.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**precision** | **int** | The precision of the rounding. The decimal places or significant figures to which the rounding takes place. | [optional] 
**rounding_type** | **str** | The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Nearest]. | [optional] 

## Example

```python
from lusid.models.simple_rounding_convention import SimpleRoundingConvention

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleRoundingConvention from a JSON string
simple_rounding_convention_instance = SimpleRoundingConvention.from_json(json)
# print the JSON string representation of the object
print SimpleRoundingConvention.to_json()

# convert the object into a dict
simple_rounding_convention_dict = simple_rounding_convention_instance.to_dict()
# create an instance of SimpleRoundingConvention from a dict
simple_rounding_convention_form_dict = simple_rounding_convention.from_dict(simple_rounding_convention_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


