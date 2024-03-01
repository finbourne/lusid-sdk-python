# UnitsRatio

The number of units you have after the event (output) for a given number of units you have prior to the event (input).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **float** | Input amount.  Denominator of the Ratio | 
**output** | **float** | Output amount. Numerator of the Ratio | 

## Example

```python
from lusid.models.units_ratio import UnitsRatio

# TODO update the JSON string below
json = "{}"
# create an instance of UnitsRatio from a JSON string
units_ratio_instance = UnitsRatio.from_json(json)
# print the JSON string representation of the object
print UnitsRatio.to_json()

# convert the object into a dict
units_ratio_dict = units_ratio_instance.to_dict()
# create an instance of UnitsRatio from a dict
units_ratio_form_dict = units_ratio.from_dict(units_ratio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


