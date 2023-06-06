# EquityCurveByPricesDataAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the provided prices | 
**dates** | **List[datetime]** | Dates provided for the forward price of the Equity at the corresponding price in Prices.  These dates should be in the future with respect to the BaseDate. | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**prices** | **List[float]** | Prices provided for the forward price of the Equity at the corresponding date in Dates. | 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

## Example

```python
from lusid.models.equity_curve_by_prices_data_all_of import EquityCurveByPricesDataAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of EquityCurveByPricesDataAllOf from a JSON string
equity_curve_by_prices_data_all_of_instance = EquityCurveByPricesDataAllOf.from_json(json)
# print the JSON string representation of the object
print EquityCurveByPricesDataAllOf.to_json()

# convert the object into a dict
equity_curve_by_prices_data_all_of_dict = equity_curve_by_prices_data_all_of_instance.to_dict()
# create an instance of EquityCurveByPricesDataAllOf from a dict
equity_curve_by_prices_data_all_of_form_dict = equity_curve_by_prices_data_all_of.from_dict(equity_curve_by_prices_data_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


