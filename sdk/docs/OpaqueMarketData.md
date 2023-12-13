# OpaqueMarketData

A representation of an un-built piece of complex market data, to allow for passing through  to the vendor library for building.  The market data will usually be in some standard form such as XML or Json, representing a curve or surface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **str** | The document as a string. | 
**format** | **str** | What format is the document stored in, e.g. Xml.  Supported string (enumeration) values are: [Unknown, Xml, Json, Csv]. | 
**name** | **str** | Internal name of document. This is not used for search, it is simply a designator that helps identify the document  and could be anything (filename, ftp address or similar) | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 

## Example

```python
from lusid.models.opaque_market_data import OpaqueMarketData

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueMarketData from a JSON string
opaque_market_data_instance = OpaqueMarketData.from_json(json)
# print the JSON string representation of the object
print OpaqueMarketData.to_json()

# convert the object into a dict
opaque_market_data_dict = opaque_market_data_instance.to_dict()
# create an instance of OpaqueMarketData from a dict
opaque_market_data_form_dict = opaque_market_data.from_dict(opaque_market_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


