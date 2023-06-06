# UpsertComplexMarketDataRequest

The details of the complex market data item to upsert into Lusid.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_id** | [**ComplexMarketDataId**](ComplexMarketDataId.md) |  | 
**market_data** | [**ComplexMarketData**](ComplexMarketData.md) |  | 

## Example

```python
from lusid.models.upsert_complex_market_data_request import UpsertComplexMarketDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertComplexMarketDataRequest from a JSON string
upsert_complex_market_data_request_instance = UpsertComplexMarketDataRequest.from_json(json)
# print the JSON string representation of the object
print UpsertComplexMarketDataRequest.to_json()

# convert the object into a dict
upsert_complex_market_data_request_dict = upsert_complex_market_data_request_instance.to_dict()
# create an instance of UpsertComplexMarketDataRequest from a dict
upsert_complex_market_data_request_form_dict = upsert_complex_market_data_request.from_dict(upsert_complex_market_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


