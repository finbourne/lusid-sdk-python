# YieldCurveData

Market data for a yield curve,  represented by a list of instruments and corresponding market quotes
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date | 
**instruments** | [**List[LusidInstrument]**](LusidInstrument.md) | The set of instruments that define the curve. | 
**quotes** | [**List[MarketQuote]**](MarketQuote.md) | The market quotes corresponding to the the instruments used to define the curve | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.yield_curve_data import YieldCurveData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

base_date: datetime = # Replace with your value
instruments: List[LusidInstrument] = # Replace with your value
quotes: List[MarketQuote] = # Replace with your value
lineage: Optional[StrictStr] = "example_lineage"
market_data_options: Optional[MarketDataOptions] = # Replace with your value
market_data_type: StrictStr = "example_market_data_type"
yield_curve_data_instance = YieldCurveData(base_date=base_date, instruments=instruments, quotes=quotes, lineage=lineage, market_data_options=market_data_options, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

