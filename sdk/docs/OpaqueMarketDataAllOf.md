# OpaqueMarketDataAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **str** | The document as a string. | 
**format** | **str** | What format is the document stored in, e.g. Xml.  Supported string (enumeration) values are: [Unknown, Xml, Json, Csv]. | 
**name** | **str** | Internal name of document. This is not used for search, it is simply a designator that helps identify the document  and could be anything (filename, ftp address or similar) | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

## Example

```python
from lusid.models.opaque_market_data_all_of import OpaqueMarketDataAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueMarketDataAllOf from a JSON string
opaque_market_data_all_of_instance = OpaqueMarketDataAllOf.from_json(json)
# print the JSON string representation of the object
print OpaqueMarketDataAllOf.to_json()

# convert the object into a dict
opaque_market_data_all_of_dict = opaque_market_data_all_of_instance.to_dict()
# create an instance of OpaqueMarketDataAllOf from a dict
opaque_market_data_all_of_form_dict = opaque_market_data_all_of.from_dict(opaque_market_data_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


