# FxForwardPipsCurveData

Contains data (i.e. dates and pips + metadata) for building fx forward curves (when combined with a spot rate to build on)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the quoted pip rates | 
**dom_ccy** | **str** | Domestic currency of the fx forward | 
**fgn_ccy** | **str** | Foreign currency of the fx forward | 
**dates** | **List[datetime]** | Dates for which the forward rates apply | 
**pip_rates** | **List[float]** | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

## Example

```python
from lusid.models.fx_forward_pips_curve_data import FxForwardPipsCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of FxForwardPipsCurveData from a JSON string
fx_forward_pips_curve_data_instance = FxForwardPipsCurveData.from_json(json)
# print the JSON string representation of the object
print FxForwardPipsCurveData.to_json()

# convert the object into a dict
fx_forward_pips_curve_data_dict = fx_forward_pips_curve_data_instance.to_dict()
# create an instance of FxForwardPipsCurveData from a dict
fx_forward_pips_curve_data_form_dict = fx_forward_pips_curve_data.from_dict(fx_forward_pips_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


