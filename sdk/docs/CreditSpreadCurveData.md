# CreditSpreadCurveData

A credit spread curve matching tenors against par spread quotes
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the quoted rates | 
**dom_ccy** | **str** | Domestic currency of the curve | 
**tenors** | **List[str]** | The tenors for which the rates apply For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | 
**spreads** | **List[float]** | Par spread quotes corresponding to the tenors. | 
**recovery_rate** | **float** | The recovery rate in default. | 
**reference_date** | **datetime** | If tenors are provided, this is the date against which the tenors will be resolved. This is of importance to CDX spread quotes, which are usually quoted in tenors relative to the CDX start date. In this case, the ReferenceDate would be equal to the CDX start date, and the BaseDate would be the date for which the spreads are valid. If not provided, this defaults to the BaseDate of the curve. | [optional] 
**maturities** | **List[datetime]** | The maturity dates for which the rates apply. Either tenors or maturities should be provided, not both. | [optional] 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.credit_spread_curve_data import CreditSpreadCurveData
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
base_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
tenors: conlist(StrictStr) = # Replace with your value
spreads: conlist(Union[StrictFloat, StrictInt]) = # Replace with your value
recovery_rate: Union[StrictFloat, StrictInt] = # Replace with your value
reference_date: Optional[datetime] = # Replace with your value
maturities: Optional[conlist(datetime)] = # Replace with your value
lineage: Optional[StrictStr] = "example_lineage"
market_data_options: Optional[MarketDataOptions] = # Replace with your value
market_data_type: StrictStr = "example_market_data_type"
credit_spread_curve_data_instance = CreditSpreadCurveData(base_date=base_date, dom_ccy=dom_ccy, tenors=tenors, spreads=spreads, recovery_rate=recovery_rate, reference_date=reference_date, maturities=maturities, lineage=lineage, market_data_options=market_data_options, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

