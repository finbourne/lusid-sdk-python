# AppendFxForwardCurveByQuoteReference

Used to append a new point to an FX curve defined using `FxForwardCurveByQuoteReference`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenor** | **str** | Tenor for which the forward rate applies. | 
**quote_reference** | **Dict[str, str]** | A collection of identifiers for the tenor, which will be used to query the LUSID Quote Store to resolve the actual rates.  The keys must be chosen from the following enumeration:  [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].    For example:    \&quot;quoteReference\&quot;: {\&quot;ClientInternal\&quot;: \&quot;SomeIdentifierForTenor\&quot;} | 
**market_data_type** | **str** | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData | 

## Example

```python
from lusid.models.append_fx_forward_curve_by_quote_reference import AppendFxForwardCurveByQuoteReference

# TODO update the JSON string below
json = "{}"
# create an instance of AppendFxForwardCurveByQuoteReference from a JSON string
append_fx_forward_curve_by_quote_reference_instance = AppendFxForwardCurveByQuoteReference.from_json(json)
# print the JSON string representation of the object
print AppendFxForwardCurveByQuoteReference.to_json()

# convert the object into a dict
append_fx_forward_curve_by_quote_reference_dict = append_fx_forward_curve_by_quote_reference_instance.to_dict()
# create an instance of AppendFxForwardCurveByQuoteReference from a dict
append_fx_forward_curve_by_quote_reference_form_dict = append_fx_forward_curve_by_quote_reference.from_dict(append_fx_forward_curve_by_quote_reference_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


