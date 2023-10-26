# ComplexMarketData

Base class for representing complex market data in LUSID.  Generally speaking, market data is complex when it cannot be represented as a single quote.  Examples include discounting curves, projection curves, and volatility surfaces, which are used to compute instrument analytics.  This base class should not be directly instantiated; each supported MarketDataType has a corresponding inherited class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

## Example

```python
from lusid.models.complex_market_data import ComplexMarketData

# TODO update the JSON string below
json = "{}"
# create an instance of ComplexMarketData from a JSON string
complex_market_data_instance = ComplexMarketData.from_json(json)
# print the JSON string representation of the object
print ComplexMarketData.to_json()

# convert the object into a dict
complex_market_data_dict = complex_market_data_instance.to_dict()
# create an instance of ComplexMarketData from a dict
complex_market_data_form_dict = complex_market_data.from_dict(complex_market_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


