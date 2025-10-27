# ConstantVolatilitySurface

Market Data required to build a volatility surface for pricing.  Single constant volatility point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date of the engine - this is the reference date for resolution of tenors. | 
**asset_type** | **str** | What is the asset that the engine is for.  Supported string (enumeration) values are: [Cash, Commodity, Credit, Equity, Fx, Rates, FxVol, IrVol, EquityVol, HolidayCalendar, IndexConvention, FlowConvention, CdsFlowConvention, CorporateActions, FxForwards, Quote, Inflation, EquityCurve, All, VendorOpaque]. | 
**lineage** | **str** |  | [optional] 
**volatility** | **float** | Volatility value. | 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.constant_volatility_surface import ConstantVolatilitySurface
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

base_date: datetime = # Replace with your value
asset_type: StrictStr = "example_asset_type"
lineage: Optional[StrictStr] = "example_lineage"
volatility: Union[StrictFloat, StrictInt] = # Replace with your value
market_data_type: StrictStr = "example_market_data_type"
constant_volatility_surface_instance = ConstantVolatilitySurface(base_date=base_date, asset_type=asset_type, lineage=lineage, volatility=volatility, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

