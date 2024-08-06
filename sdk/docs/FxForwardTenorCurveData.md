# FxForwardTenorCurveData

Contains data (i.e. tenors and rates + metadata) for building fx forward curves (when combined with a date to build on)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the quoted rates | 
**dom_ccy** | **str** | Domestic currency of the fx forward | 
**fgn_ccy** | **str** | Foreign currency of the fx forward | 
**tenors** | **List[str]** | Tenors for which the forward rates apply.  For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | 
**rates** | **List[float]** | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy) | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**calendars** | [**List[FxTenorConvention]**](FxTenorConvention.md) | The list of conventions that should be used when interpreting tenors as dates. | [optional] 
**spot_days_calculation_type** | **str** | Configures how to calculate the spot date from the build date using the Calendars provided.  Supported string (enumeration) values are: [ SingleCalendar, UnionCalendars ] | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 

## Example

```python
from lusid.models.fx_forward_tenor_curve_data import FxForwardTenorCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of FxForwardTenorCurveData from a JSON string
fx_forward_tenor_curve_data_instance = FxForwardTenorCurveData.from_json(json)
# print the JSON string representation of the object
print FxForwardTenorCurveData.to_json()

# convert the object into a dict
fx_forward_tenor_curve_data_dict = fx_forward_tenor_curve_data_instance.to_dict()
# create an instance of FxForwardTenorCurveData from a dict
fx_forward_tenor_curve_data_form_dict = fx_forward_tenor_curve_data.from_dict(fx_forward_tenor_curve_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


