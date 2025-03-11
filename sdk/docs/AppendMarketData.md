# AppendMarketData

Base class for types containing required data to append to complex market data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_type** | **str** | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData | 

## Example

```python
from lusid.models.append_market_data import AppendMarketData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendMarketData from a JSON string
append_market_data_instance = AppendMarketData.from_json(json)
# print the JSON string representation of the object
print AppendMarketData.to_json()

# convert the object into a dict
append_market_data_dict = append_market_data_instance.to_dict()
# create an instance of AppendMarketData from a dict
append_market_data_form_dict = append_market_data.from_dict(append_market_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


