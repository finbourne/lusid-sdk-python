# Compounding

The compounding settings used on interest rate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**averaging_method** | **str** | Defines whether a weighted or unweighted average is used when calculating the average rate.  It applies only when CompoundingMethod &#x3D; ‘Average‘.    Supported string (enumeration) values are: [Unweighted, Weighted]. | [optional] 
**calculation_shift_method** | **str** | Defines which resets and day counts are used for the rate calculation    Supported string (enumeration) values are: [Lookback, NoShift, ObservationPeriodShift, Lockout]. | [optional] 
**compounding_method** | **str** | If the interest rate is simple, compounded or using a pre-computed compounded index.    Supported string (enumeration) values are: [Average, Compounded, CompoundedIndex]. | 
**reset_frequency** | **str** | The interest payment frequency. | 
**shift** | **int** | Defines the number of days to lockout or shift observation period by - should be a non-negative integer | [optional] 
**spread_compounding_method** | **str** | Defines how the computed leg spread is applied to compounded rate.  It applies only when CompoundingMethod &#x3D; ‘Compounded‘ or ‘CompoundedIndex‘.    Available compounding methods:    | Method | Description |  | ------ | ----------- |  | Straight | Compounding rate in each compound period includes the spread. |  | Flat | Compounding rate does not include the spread, and the spread is used for simple interest in each compound period. |  | SpreadExclusive | Compounding rate does not include the spread, and the spread is used for simple interest for whole accrual period. |    The values \&quot;IsdaCompounding\&quot;, \&quot;NoCompounding\&quot;, \&quot;IsdaFlatCompounding\&quot;, and \&quot;None\&quot; are accepted for compatibility  with existing instruments and their use is discouraged.    Supported string (enumeration) values are: [Straight, IsdaCompounding, NoCompounding, SpreadExclusive, IsdaFlatCompounding, Flat, None]. | [optional] 

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


