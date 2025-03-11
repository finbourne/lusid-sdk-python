# AppendFxForwardTenorCurveData

Used to append a new point to an FX curve defined using `FxForwardTenorCurveData`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenor** | **str** | Tenor for which the forward rate applies. | 
**rate** | **float** | Rate provided for the fx forward (price in FgnCcy per unit of DomCcy). | 
**market_data_type** | **str** | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData | 

## Example

```python
from lusid.models.append_fx_forward_tenor_curve_data import AppendFxForwardTenorCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendFxForwardTenorCurveData from a JSON string
append_fx_forward_tenor_curve_data_instance = AppendFxForwardTenorCurveData.from_json(json)
# print the JSON string representation of the object
print AppendFxForwardTenorCurveData.to_json()

# convert the object into a dict
append_fx_forward_tenor_curve_data_dict = append_fx_forward_tenor_curve_data_instance.to_dict()
# create an instance of AppendFxForwardTenorCurveData from a dict
append_fx_forward_tenor_curve_data_form_dict = append_fx_forward_tenor_curve_data.from_dict(append_fx_forward_tenor_curve_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


