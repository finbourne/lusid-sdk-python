# FxForwardTenorPipsCurveData

Contains data (i.e. tenors and pips + metadata) for building fx forward curves (when combined with a spot rate and a date to build on)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the quoted pip rates | 
**dom_ccy** | **str** | Domestic currency of the fx forward | 
**fgn_ccy** | **str** | Foreign currency of the fx forward | 
**tenors** | **List[str]** | Tenors for which the forward rates apply | 
**pip_rates** | **List[float]** | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**calendars** | [**List[FxTenorConvention]**](FxTenorConvention.md) | The list of conventions that should be used when interpreting tenors as dates. | [optional] 
**spot_days_calculation_type** | **str** | Configures how to calculate the spot date from the build date using the Calendars provided.  Supported string (enumeration) values are: [ SingleCalendar, UnionCalendars ] | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 

## Example

```python
from lusid.models.fx_forward_tenor_pips_curve_data import FxForwardTenorPipsCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of FxForwardTenorPipsCurveData from a JSON string
fx_forward_tenor_pips_curve_data_instance = FxForwardTenorPipsCurveData.from_json(json)
# print the JSON string representation of the object
print FxForwardTenorPipsCurveData.to_json()

# convert the object into a dict
fx_forward_tenor_pips_curve_data_dict = fx_forward_tenor_pips_curve_data_instance.to_dict()
# create an instance of FxForwardTenorPipsCurveData from a dict
fx_forward_tenor_pips_curve_data_form_dict = fx_forward_tenor_pips_curve_data.from_dict(fx_forward_tenor_pips_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


