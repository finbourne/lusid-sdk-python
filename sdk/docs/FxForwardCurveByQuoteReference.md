# FxForwardCurveByQuoteReference

Contains data (i.e. tenors and rates + metadata) for building fx forward curves (when combined with a date to build on)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dom_ccy** | **str** | Domestic currency of the fx forward | 
**fgn_ccy** | **str** | Foreign currency of the fx forward | 
**tenors** | **List[str]** | Tenors for which the forward rates apply. For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | 
**quote_references** | **List[Dict[str, str]]** | For each tenor, a collection of identifiers. These will be looked up in the LUSID Quote Store to resolve the actual rates. Accepts an array of Dictionary&lt;string, string&gt;. The keys of each dictionary must be chosen from the following enumeration: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. For example:  \&quot;quoteReferences\&quot;: [{\&quot;ClientInternal\&quot;: \&quot;SomeIdentifierForFirstTenor\&quot;},{\&quot;ClientInternal\&quot;: \&quot;SomeIdentifierForSecondTenor\&quot;} | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**calendars** | [**List[FxTenorConvention]**](FxTenorConvention.md) | The list of conventions that should be used when interpreting tenors as dates. | [optional] 
**spot_days_calculation_type** | **str** | Configures how to calculate the spot date from the build date using the Calendars provided. Supported string (enumeration) values are: [ SingleCalendar, UnionCalendars ] | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 
## Example

```python
from lusid.models.fx_forward_curve_by_quote_reference import FxForwardCurveByQuoteReference
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictStr, conlist, constr, validator

dom_ccy: StrictStr = "example_dom_ccy"
fgn_ccy: StrictStr = "example_fgn_ccy"
tenors: conlist(StrictStr) = # Replace with your value
quote_references: conlist(Dict[str, StrictStr]) = # Replace with your value
lineage: Optional[StrictStr] = "example_lineage"
market_data_options: Optional[MarketDataOptions] = # Replace with your value
calendars: Optional[conlist(FxTenorConvention)] = # Replace with your value
spot_days_calculation_type: Optional[StrictStr] = "example_spot_days_calculation_type"
market_data_type: StrictStr = "example_market_data_type"
fx_forward_curve_by_quote_reference_instance = FxForwardCurveByQuoteReference(dom_ccy=dom_ccy, fgn_ccy=fgn_ccy, tenors=tenors, quote_references=quote_references, lineage=lineage, market_data_options=market_data_options, calendars=calendars, spot_days_calculation_type=spot_days_calculation_type, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

