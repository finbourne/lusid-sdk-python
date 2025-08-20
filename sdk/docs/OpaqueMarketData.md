# OpaqueMarketData

A representation of an un-built piece of complex market data, to allow for passing through to the vendor library for building. The market data will usually be in some standard form such as XML or Json, representing a curve or surface.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **str** | The document as a string. | 
**format** | **str** | What format is the document stored in, e.g. Xml. Supported string (enumeration) values are: [Unknown, Xml, Json, Csv]. | 
**name** | **str** | Internal name of document. This is not used for search, it is simply a designator that helps identify the document and could be anything (filename, ftp address or similar) | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.opaque_market_data import OpaqueMarketData
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictStr, constr, validator

document: StrictStr = "example_document"
format: StrictStr = "example_format"
name: StrictStr = "example_name"
lineage: Optional[StrictStr] = "example_lineage"
market_data_type: StrictStr = "example_market_data_type"
opaque_market_data_instance = OpaqueMarketData(document=document, format=format, name=name, lineage=lineage, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

