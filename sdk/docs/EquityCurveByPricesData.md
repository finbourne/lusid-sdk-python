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
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 

## Example

```python
from lusid.models.equity_curve_by_prices_data import EquityCurveByPricesData

# TODO update the JSON string below
json = "{}"
# create an instance of EquityCurveByPricesData from a JSON string
equity_curve_by_prices_data_instance = EquityCurveByPricesData.from_json(json)
# print the JSON string representation of the object
print EquityCurveByPricesData.to_json()

# convert the object into a dict
equity_curve_by_prices_data_dict = equity_curve_by_prices_data_instance.to_dict()
# create an instance of EquityCurveByPricesData from a dict
equity_curve_by_prices_data_form_dict = equity_curve_by_prices_data.from_dict(equity_curve_by_prices_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


