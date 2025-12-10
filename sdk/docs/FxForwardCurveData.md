# FxForwardCurveData

Contains data (i.e. dates and rates + metadata) for building fx forward curves
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the quoted rates | 
**dom_ccy** | **str** | Domestic currency of the fx forward | 
**fgn_ccy** | **str** | Foreign currency of the fx forward | 
**dates** | **List[datetime]** | Dates for which the forward rates apply | 
**rates** | **List[float]** | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy) | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.fx_forward_curve_data import FxForwardCurveData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

base_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
fgn_ccy: StrictStr = "example_fgn_ccy"
dates: List[datetime] = # Replace with your value
rates: List[Union[StrictFloat, StrictInt]] = # Replace with your value
lineage: Optional[StrictStr] = "example_lineage"
market_data_options: Optional[MarketDataOptions] = # Replace with your value
version: Optional[Version] = None
market_data_type: StrictStr = "example_market_data_type"
fx_forward_curve_data_instance = FxForwardCurveData(base_date=base_date, dom_ccy=dom_ccy, fgn_ccy=fgn_ccy, dates=dates, rates=rates, lineage=lineage, market_data_options=market_data_options, version=version, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

