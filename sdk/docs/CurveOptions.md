# CurveOptions

Options for configuring how ComplexMarketData representing a 'curve' is interpreted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_count_convention** | **str** | Day count convention of the curve. Defaults to \&quot;Act360\&quot;. | [optional] 
**front_extrapolation_type** | **str** | What type of extrapolation is used to build the curve  Imagine that the curve is facing the observer(you), then the \&quot;front\&quot; direction is the closest point on the curve onward. &lt;br /&gt;  example: 0D tenor to past  Defaults to \&quot;Flat\&quot;. Supported string (enumeration) values are: [None, Flat, Linear]. | [optional] 
**back_extrapolation_type** | **str** | What type of extrapolation is used to build the curve.  &lt;br /&gt;  Imagine that the curve is facing the observer(you), then the \&quot;back\&quot; direction is the furthest point on the curve onward. &lt;br /&gt;  example: 30Y tenor to infinity  Defaults to \&quot;Flat\&quot;. Supported string (enumeration) values are: [None, Flat, Linear]. | [optional] 
**market_data_options_type** | **str** | The available values are: CurveOptions | 

## Example

```python
from lusid.models.curve_options import CurveOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CurveOptions from a JSON string
curve_options_instance = CurveOptions.from_json(json)
# print the JSON string representation of the object
print CurveOptions.to_json()

# convert the object into a dict
curve_options_dict = curve_options_instance.to_dict()
# create an instance of CurveOptions from a dict
curve_options_form_dict = curve_options.from_dict(curve_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


