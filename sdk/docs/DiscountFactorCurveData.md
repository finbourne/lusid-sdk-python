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
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

## Example

```python
from lusid.models.discount_factor_curve_data import DiscountFactorCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountFactorCurveData from a JSON string
discount_factor_curve_data_instance = DiscountFactorCurveData.from_json(json)
# print the JSON string representation of the object
print DiscountFactorCurveData.to_json()

# convert the object into a dict
discount_factor_curve_data_dict = discount_factor_curve_data_instance.to_dict()
# create an instance of DiscountFactorCurveData from a dict
discount_factor_curve_data_form_dict = discount_factor_curve_data.from_dict(discount_factor_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


