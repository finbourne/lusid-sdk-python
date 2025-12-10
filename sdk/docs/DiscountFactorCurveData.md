# DiscountFactorCurveData

A curve containing discount factors and dates to which they apply
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | BaseDate for the Curve | 
**dates** | **List[datetime]** | Dates for which the discount factors apply | 
**discount_factors** | **List[float]** | Discount factors to be applied to cashflow on the specified dates | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.discount_factor_curve_data import DiscountFactorCurveData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

base_date: datetime = # Replace with your value
dates: List[datetime] = # Replace with your value
discount_factors: List[Union[StrictFloat, StrictInt]] = # Replace with your value
lineage: Optional[StrictStr] = "example_lineage"
market_data_options: Optional[MarketDataOptions] = # Replace with your value
version: Optional[Version] = None
market_data_type: StrictStr = "example_market_data_type"
discount_factor_curve_data_instance = DiscountFactorCurveData(base_date=base_date, dates=dates, discount_factors=discount_factors, lineage=lineage, market_data_options=market_data_options, version=version, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

