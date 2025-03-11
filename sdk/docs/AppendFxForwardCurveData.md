# AppendFxForwardCurveData

Used to append a new point to an FX curve defined using `FxForwardCurveData`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Date for which the forward rate applies. | 
**rate** | **float** | Rate provided for the fx forward (price in FgnCcy per unit of DomCcy). | 
**market_data_type** | **str** | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData | 

## Example

```python
from lusid.models.append_fx_forward_curve_data import AppendFxForwardCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendFxForwardCurveData from a JSON string
append_fx_forward_curve_data_instance = AppendFxForwardCurveData.from_json(json)
# print the JSON string representation of the object
print AppendFxForwardCurveData.to_json()

# convert the object into a dict
append_fx_forward_curve_data_dict = append_fx_forward_curve_data_instance.to_dict()
# create an instance of AppendFxForwardCurveData from a dict
append_fx_forward_curve_data_form_dict = append_fx_forward_curve_data.from_dict(append_fx_forward_curve_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


