# FxForwardCurveByQuoteReference

Contains data (i.e. tenors and rates + metadata) for building fx forward curves (when combined with a date to build on)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dom_ccy** | **str** | Domestic currency of the fx forward | 
**fgn_ccy** | **str** | Foreign currency of the fx forward | 
**tenors** | **List[str]** | Tenors for which the forward rates apply | 
**quote_references** | **List[Dict[str, str]]** | For each tenor, a collection of identifiers. These will be looked up in the LUSID Quote Store to resolve the actual rates.  Accepts an array of Dictionary&lt;string, string&gt;. The keys of each dictionary must be chosen from the following enumeration:  [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  For example: &lt;br /&gt;  \&quot;quoteReferences\&quot;: [{\&quot;ClientInternal\&quot;: \&quot;SomeIdentifierForFirstTenor\&quot;},{\&quot;ClientInternal\&quot;: \&quot;SomeIdentifierForSecondTenor\&quot;} | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**calendars** | [**List[FxTenorConvention]**](FxTenorConvention.md) | The list of conventions that should be used when interpreting tenors as dates. | [optional] 
**spot_days_calculation_type** | **str** | Configures how to calculate the spot date from the build date using the Calendars provided.  Supported string (enumeration) values are: [ SingleCalendar, UnionCalendars ] | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 

## Example

```python
from lusid.models.fx_forward_curve_by_quote_reference import FxForwardCurveByQuoteReference

# TODO update the JSON string below
json = "{}"
# create an instance of FxForwardCurveByQuoteReference from a JSON string
fx_forward_curve_by_quote_reference_instance = FxForwardCurveByQuoteReference.from_json(json)
# print the JSON string representation of the object
print FxForwardCurveByQuoteReference.to_json()

# convert the object into a dict
fx_forward_curve_by_quote_reference_dict = fx_forward_curve_by_quote_reference_instance.to_dict()
# create an instance of FxForwardCurveByQuoteReference from a dict
fx_forward_curve_by_quote_reference_form_dict = fx_forward_curve_by_quote_reference.from_dict(fx_forward_curve_by_quote_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


