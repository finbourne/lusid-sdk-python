# ListComplexMarketDataWithMetaDataResponse

Wraps a Finbourne.WebApi.Interface.Dto.ComplexMarketData.ComplexMarketData object with information that was retrieved from storage with it.  In particular,  the scope that the data was stored in,  and a <seealso cref=\"T:Finbourne.WebApi.Interface.Dto.ComplexMarketData.ComplexMarketDataId\" /> object identifying the market data in that scope.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the listed ComplexMarketData entity is stored in. | [optional] 
**market_data_id** | [**ComplexMarketDataId**](ComplexMarketDataId.md) |  | [optional] 
**market_data** | [**ComplexMarketData**](ComplexMarketData.md) |  | [optional] 

## Example

```python
from lusid.models.list_complex_market_data_with_meta_data_response import ListComplexMarketDataWithMetaDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListComplexMarketDataWithMetaDataResponse from a JSON string
list_complex_market_data_with_meta_data_response_instance = ListComplexMarketDataWithMetaDataResponse.from_json(json)
# print the JSON string representation of the object
print ListComplexMarketDataWithMetaDataResponse.to_json()

# convert the object into a dict
list_complex_market_data_with_meta_data_response_dict = list_complex_market_data_with_meta_data_response_instance.to_dict()
# create an instance of ListComplexMarketDataWithMetaDataResponse from a dict
list_complex_market_data_with_meta_data_response_form_dict = list_complex_market_data_with_meta_data_response.from_dict(list_complex_market_data_with_meta_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


