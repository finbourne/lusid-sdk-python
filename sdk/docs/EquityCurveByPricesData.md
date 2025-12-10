# EquityCurveByPricesData

Contains data (i.e. dates and prices + metadata) for building Equity curves
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the provided prices | 
**dates** | **List[datetime]** | Dates provided for the forward price of the Equity at the corresponding price in Prices.  These dates should be in the future with respect to the BaseDate. | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**prices** | **List[float]** | Prices provided for the forward price of the Equity at the corresponding date in Dates. | 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.equity_curve_by_prices_data import EquityCurveByPricesData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

base_date: datetime = # Replace with your value
dates: List[datetime] = # Replace with your value
lineage: Optional[StrictStr] = "example_lineage"
prices: List[Union[StrictFloat, StrictInt]] = # Replace with your value
market_data_options: Optional[MarketDataOptions] = # Replace with your value
version: Optional[Version] = None
market_data_type: StrictStr = "example_market_data_type"
equity_curve_by_prices_data_instance = EquityCurveByPricesData(base_date=base_date, dates=dates, lineage=lineage, prices=prices, market_data_options=market_data_options, version=version, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

