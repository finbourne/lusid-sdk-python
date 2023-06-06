# Compounding

The compounding settings used on interest rate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_shift_method** | **str** | Defines which resets and day counts are used for the rate calculation    Supported string (enumeration) values are: [Lookback, NoShift, ObservationPeriodShift, Lockout]. | [optional] 
**compounding_method** | **str** | If the interest rate is simple or compounded.    Supported string (enumeration) values are: [Average, Compounded]. | 
**reset_frequency** | **str** | The interest payment frequency. | 
**shift** | **int** | Defines the number of days to lockout or shift observation period by - should be a non-negative integer | [optional] 
**spread_compounding_method** | **str** | Defines how the computed leg spread is applied to compounded rate.  It applies only when CompoundingMethod &#x3D; ‘Compounded‘.    Supported string (enumeration) values are: [Straight, IsdaCompounding, NoCompounding, SpreadExclusive, IsdaFlatCompounding, Flat, None]. | 

## Example

```python
from lusid.models.compounding import Compounding

# TODO update the JSON string below
json = "{}"
# create an instance of Compounding from a JSON string
compounding_instance = Compounding.from_json(json)
# print the JSON string representation of the object
print Compounding.to_json()

# convert the object into a dict
compounding_dict = compounding_instance.to_dict()
# create an instance of Compounding from a dict
compounding_form_dict = compounding.from_dict(compounding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


