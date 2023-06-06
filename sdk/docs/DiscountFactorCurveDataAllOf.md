# DiscountFactorCurveDataAllOf


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
from lusid.models.discount_factor_curve_data_all_of import DiscountFactorCurveDataAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountFactorCurveDataAllOf from a JSON string
discount_factor_curve_data_all_of_instance = DiscountFactorCurveDataAllOf.from_json(json)
# print the JSON string representation of the object
print DiscountFactorCurveDataAllOf.to_json()

# convert the object into a dict
discount_factor_curve_data_all_of_dict = discount_factor_curve_data_all_of_instance.to_dict()
# create an instance of DiscountFactorCurveDataAllOf from a dict
discount_factor_curve_data_all_of_form_dict = discount_factor_curve_data_all_of.from_dict(discount_factor_curve_data_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


