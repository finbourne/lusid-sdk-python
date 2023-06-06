# EquityVolSurfaceData

Market Data for an equity vol surface, represented by a list of instruments and corresponding market quotes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date of the surface | 
**instruments** | [**List[LusidInstrument]**](LusidInstrument.md) | The set of instruments that define the surface. | 
**quotes** | [**List[MarketQuote]**](MarketQuote.md) | The set of market quotes that define the surface, in NormalVol or LogNormalVol terms. | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

## Example

```python
from lusid.models.equity_vol_surface_data import EquityVolSurfaceData

# TODO update the JSON string below
json = "{}"
# create an instance of EquityVolSurfaceData from a JSON string
equity_vol_surface_data_instance = EquityVolSurfaceData.from_json(json)
# print the JSON string representation of the object
print EquityVolSurfaceData.to_json()

# convert the object into a dict
equity_vol_surface_data_dict = equity_vol_surface_data_instance.to_dict()
# create an instance of EquityVolSurfaceData from a dict
equity_vol_surface_data_form_dict = equity_vol_surface_data.from_dict(equity_vol_surface_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


