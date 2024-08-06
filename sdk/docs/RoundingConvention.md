# RoundingConvention

Certain bonds will follow certain rounding conventions.  For example, Thai government bonds will round accrued interest and cashflow values 2dp, whereas for  French government bonds, the rounding is to 7dp.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**face_value** | **float** | The face value to round against.  The number to be rounded is scaled to this face value before being rounded, and then re-scaled to the holding amount.  For example if rounding an accrued interest value using a FaceValue of 1,000, but 10,000 units are held,  then the initial calculated value would be divided by 10,000, then multiplied by 1,000 and rounded per the convention.  The result of this would then be divided by 1,000 and multiplied by 10,000 to get the final value. | [optional] 
**precision** | **int** | The precision of the rounding.  The decimal places to which the rounding takes place. | [optional] 
**rounding_target** | **str** | The target of the rounding convention.  Accepted values are &#39;AccruedInterest&#39;, &#39;Cashflows&#39;, or &#39;All&#39;    Supported string (enumeration) values are: [All, AccruedInterest, Cashflows]. | [optional] 
**rounding_type** | **str** | The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Floor, Ceiling, Nearest]. | [optional] 

## Example

```python
from lusid.models.rounding_convention import RoundingConvention

# TODO update the JSON string below
json = "{}"
# create an instance of RoundingConvention from a JSON string
rounding_convention_instance = RoundingConvention.from_json(json)
# print the JSON string representation of the object
print RoundingConvention.to_json()

# convert the object into a dict
rounding_convention_dict = rounding_convention_instance.to_dict()
# create an instance of RoundingConvention from a dict
rounding_convention_form_dict = rounding_convention.from_dict(rounding_convention_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


