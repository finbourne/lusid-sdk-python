# AppendFxForwardCurveByQuoteReference

Used to append a new point to an FX curve defined using `FxForwardCurveByQuoteReference`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenor** | **str** | Tenor for which the forward rate applies. | 
**quote_reference** | **Dict[str, str]** | A collection of identifiers for the tenor, which will be used to query the LUSID Quote Store to resolve the actual rates. The keys must be chosen from the following enumeration: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  For example:  \&quot;quoteReference\&quot;: {\&quot;ClientInternal\&quot;: \&quot;SomeIdentifierForTenor\&quot;} | 
**market_data_type** | **str** | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData | 
## Example

```python
from lusid.models.append_fx_forward_curve_by_quote_reference import AppendFxForwardCurveByQuoteReference
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator

tenor: StrictStr = "example_tenor"
quote_reference: Dict[str, StrictStr] = # Replace with your value
market_data_type: StrictStr = "example_market_data_type"
append_fx_forward_curve_by_quote_reference_instance = AppendFxForwardCurveByQuoteReference(tenor=tenor, quote_reference=quote_reference, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

