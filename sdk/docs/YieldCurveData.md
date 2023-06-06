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
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

## Example

```python
from lusid.models.yield_curve_data import YieldCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of YieldCurveData from a JSON string
yield_curve_data_instance = YieldCurveData.from_json(json)
# print the JSON string representation of the object
print YieldCurveData.to_json()

# convert the object into a dict
yield_curve_data_dict = yield_curve_data_instance.to_dict()
# create an instance of YieldCurveData from a dict
yield_curve_data_form_dict = yield_curve_data.from_dict(yield_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


