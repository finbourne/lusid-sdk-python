# AppendComplexMarketDataRequest

The details of the point to be appended to a complex market data item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_id** | [**ComplexMarketDataId**](ComplexMarketDataId.md) |  | 
**append_market_data** | [**AppendMarketData**](AppendMarketData.md) |  | 

## Example

```python
from lusid.models.append_complex_market_data_request import AppendComplexMarketDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppendComplexMarketDataRequest from a JSON string
append_complex_market_data_request_instance = AppendComplexMarketDataRequest.from_json(json)
# print the JSON string representation of the object
print AppendComplexMarketDataRequest.to_json()

# convert the object into a dict
append_complex_market_data_request_dict = append_complex_market_data_request_instance.to_dict()
# create an instance of AppendComplexMarketDataRequest from a dict
append_complex_market_data_request_form_dict = append_complex_market_data_request.from_dict(append_complex_market_data_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


