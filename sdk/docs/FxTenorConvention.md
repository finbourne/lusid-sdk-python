# FxTenorConvention

A wrapper of conventions that should be used when interpreting tenors in the context of FX.  For instance, can be used to control how tenors are interpreted on an FxForwardTenorCurveData instance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_code** | **str** | The code of the holiday calendar that should be used when interpreting FX tenors. | 
**spot_days** | **int** | The minimum number of business days that must pass within this calendar when calculating the spot date. | 

## Example

```python
from lusid.models.fx_tenor_convention import FxTenorConvention

# TODO update the JSON string below
json = "{}"
# create an instance of FxTenorConvention from a JSON string
fx_tenor_convention_instance = FxTenorConvention.from_json(json)
# print the JSON string representation of the object
print FxTenorConvention.to_json()

# convert the object into a dict
fx_tenor_convention_dict = fx_tenor_convention_instance.to_dict()
# create an instance of FxTenorConvention from a dict
fx_tenor_convention_form_dict = fx_tenor_convention.from_dict(fx_tenor_convention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


