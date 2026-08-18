# InflationCurveData

Market data for an inflation curve, represented by a list of zero-coupon inflation swap  instruments and corresponding market quotes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_date** | **datetime** | Build date of the curve - this is the reference date for resolution of the swap constituents. | 
**instruments** | [**List[LusidInstrument]**](LusidInstrument.md) | The set of instruments that define the curve.  The only supported instrument type is: [InflationSwap]. | 
**quotes** | [**List[MarketQuote]**](MarketQuote.md) | The market quotes corresponding to the the instruments used to define the curve | 
**seasonal_factors** | **List[float]** | Optional multiplicative seasonal adjustment factors, one per calendar month starting from January.  If provided there must be exactly 12 factors. | [optional] 
**output_type** | **str** | What the values of the built curve represent.  Supported string (enumeration) values are: [Level, Ratio].  Defaults to \&quot;Level\&quot; if not provided. | [optional] 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**market_data_type** | **str** | Available values: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface, InflationCurveData. | 
## Example

```python
from lusid.models.inflation_curve_data import InflationCurveData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

build_date: datetime = # Replace with your value
instruments: List[LusidInstrument] = # Replace with your value
quotes: List[MarketQuote] = # Replace with your value
seasonal_factors: Optional[List[Union[StrictFloat, StrictInt]]] = # Replace with your value
output_type: Optional[StrictStr] = "example_output_type"
lineage: Optional[StrictStr] = "example_lineage"
market_data_options: Optional[MarketDataOptions] = # Replace with your value
version: Optional[Version] = None
market_data_type: StrictStr = "example_market_data_type"
inflation_curve_data_instance = InflationCurveData(build_date=build_date, instruments=instruments, quotes=quotes, seasonal_factors=seasonal_factors, output_type=output_type, lineage=lineage, market_data_options=market_data_options, version=version, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

