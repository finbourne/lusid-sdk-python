# AppendFxForwardPipsCurveData

Used to append a new point to an FX curve defined using `FxForwardPipsCurveData`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Date for which the forward rate applies. | 
**pip_rate** | **float** | Rate provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips. | 
**market_data_type** | **str** | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData | 

## Example

```python
from lusid.models.append_fx_forward_pips_curve_data import AppendFxForwardPipsCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendFxForwardPipsCurveData from a JSON string
append_fx_forward_pips_curve_data_instance = AppendFxForwardPipsCurveData.from_json(json)
# print the JSON string representation of the object
print AppendFxForwardPipsCurveData.to_json()

# convert the object into a dict
append_fx_forward_pips_curve_data_dict = append_fx_forward_pips_curve_data_instance.to_dict()
# create an instance of AppendFxForwardPipsCurveData from a dict
append_fx_forward_pips_curve_data_form_dict = append_fx_forward_pips_curve_data.from_dict(append_fx_forward_pips_curve_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


