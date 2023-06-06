# FxForwardCurveDataAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the quoted rates | 
**dom_ccy** | **str** | Domestic currency of the fx forward | 
**fgn_ccy** | **str** | Foreign currency of the fx forward | 
**dates** | **List[datetime]** | Dates for which the forward rates apply | 
**rates** | **List[float]** | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy) | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

## Example

```python
from lusid.models.fx_forward_curve_data_all_of import FxForwardCurveDataAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FxForwardCurveDataAllOf from a JSON string
fx_forward_curve_data_all_of_instance = FxForwardCurveDataAllOf.from_json(json)
# print the JSON string representation of the object
print FxForwardCurveDataAllOf.to_json()

# convert the object into a dict
fx_forward_curve_data_all_of_dict = fx_forward_curve_data_all_of_instance.to_dict()
# create an instance of FxForwardCurveDataAllOf from a dict
fx_forward_curve_data_all_of_form_dict = fx_forward_curve_data_all_of.from_dict(fx_forward_curve_data_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


