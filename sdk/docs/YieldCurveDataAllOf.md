# YieldCurveDataAllOf


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
from lusid.models.yield_curve_data_all_of import YieldCurveDataAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of YieldCurveDataAllOf from a JSON string
yield_curve_data_all_of_instance = YieldCurveDataAllOf.from_json(json)
# print the JSON string representation of the object
print YieldCurveDataAllOf.to_json()

# convert the object into a dict
yield_curve_data_all_of_dict = yield_curve_data_all_of_instance.to_dict()
# create an instance of YieldCurveDataAllOf from a dict
yield_curve_data_all_of_form_dict = yield_curve_data_all_of.from_dict(yield_curve_data_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


