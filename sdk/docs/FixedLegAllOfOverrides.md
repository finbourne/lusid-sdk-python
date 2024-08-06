# FixedLegAllOfOverrides

Any overriding data for notionals, spreads or rates that would affect generation of a leg.  This supports the case where an amortisation schedule is given but otherwise generation is allowed as usual.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amortization** | **List[float]** |  | [optional] 
**spreads** | **List[float]** |  | [optional] 

## Example

```python
from lusid.models.fixed_leg_all_of_overrides import FixedLegAllOfOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of FixedLegAllOfOverrides from a JSON string
fixed_leg_all_of_overrides_instance = FixedLegAllOfOverrides.from_json(json)
# print the JSON string representation of the object
print FixedLegAllOfOverrides.to_json()

# convert the object into a dict
fixed_leg_all_of_overrides_dict = fixed_leg_all_of_overrides_instance.to_dict()
# create an instance of FixedLegAllOfOverrides from a dict
fixed_leg_all_of_overrides_form_dict = fixed_leg_all_of_overrides.from_dict(fixed_leg_all_of_overrides_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


