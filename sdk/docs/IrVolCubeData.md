# IrVolCubeData

Market Data required to build a volatility cube for swaption pricing,  represented by a list of instruments and corresponding market quotes
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date of the cube - this is the start date of the swaptions on the cube. | 
**instruments** | [**List[LusidInstrument]**](LusidInstrument.md) | Retrieve the set of instruments that define the cube. | 
**quotes** | [**List[MarketQuote]**](MarketQuote.md) | Access the set of quotes that define the cube. | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.ir_vol_cube_data import IrVolCubeData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

base_date: datetime = # Replace with your value
instruments: List[LusidInstrument] = # Replace with your value
quotes: List[MarketQuote] = # Replace with your value
lineage: Optional[StrictStr] = "example_lineage"
version: Optional[Version] = None
market_data_type: StrictStr = "example_market_data_type"
ir_vol_cube_data_instance = IrVolCubeData(base_date=base_date, instruments=instruments, quotes=quotes, lineage=lineage, version=version, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

