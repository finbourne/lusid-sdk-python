# ComplexMarketData

Base class for representing complex market data in LUSID. Generally speaking, market data is complex when it cannot be represented as a single quote. Examples include discounting curves, projection curves, and volatility surfaces, which are used to compute instrument analytics. This base class should not be directly instantiated; each supported MarketDataType has a corresponding inherited class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.complex_market_data import ComplexMarketData
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

market_data_type: StrictStr = "example_market_data_type"
complex_market_data_instance = ComplexMarketData(market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

