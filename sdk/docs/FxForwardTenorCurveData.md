# FxForwardTenorCurveData

Contains data (i.e. tenors and rates + metadata) for building fx forward curves (when combined with a date to build on)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the quoted rates | 
**dom_ccy** | **str** | Domestic currency of the fx forward | 
**fgn_ccy** | **str** | Foreign currency of the fx forward | 
**tenors** | **List[str]** | Tenors for which the forward rates apply.  For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | 
**rates** | **List[float]** | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy) | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**calendars** | [**List[FxTenorConvention]**](FxTenorConvention.md) | The list of conventions that should be used when interpreting tenors as dates. | [optional] 
**spot_days_calculation_type** | **str** | Configures how to calculate the spot date from the build date using the Calendars provided.  Supported string (enumeration) values are: [ SingleCalendar, UnionCalendars ] | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.fx_forward_tenor_curve_data import FxForwardTenorCurveData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

base_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
fgn_ccy: StrictStr = "example_fgn_ccy"
tenors: List[StrictStr] = # Replace with your value
rates: List[Union[StrictFloat, StrictInt]] = # Replace with your value
lineage: Optional[StrictStr] = "example_lineage"
market_data_options: Optional[MarketDataOptions] = # Replace with your value
calendars: Optional[List[FxTenorConvention]] = # Replace with your value
spot_days_calculation_type: Optional[StrictStr] = "example_spot_days_calculation_type"
market_data_type: StrictStr = "example_market_data_type"
fx_forward_tenor_curve_data_instance = FxForwardTenorCurveData(base_date=base_date, dom_ccy=dom_ccy, fgn_ccy=fgn_ccy, tenors=tenors, rates=rates, lineage=lineage, market_data_options=market_data_options, calendars=calendars, spot_days_calculation_type=spot_days_calculation_type, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

