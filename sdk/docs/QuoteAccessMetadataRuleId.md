# QuoteAccessMetadataRuleId

An identifier that uniquely identifies a set of Quote access control metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The platform or vendor that provided the quote. The available values are: Client, DataScope, Lusid, Edi, TraderMade, FactSet, SIX, Bloomberg, Rimes | [optional] 
**price_source** | **str** | The source or originator of the quote, e.g. a bank or financial institution. | [optional] 
**instrument_id** | **str** | The value of the instrument identifier that uniquely identifies the instrument that the quote is for, e.g. &#39;BBG00JX0P539&#39;. | [optional] 
**instrument_id_type** | **str** | The type of instrument identifier used to uniquely identify the instrument that the quote is for, e.g. &#39;Figi&#39;. | [optional] 
**quote_type** | **str** | The type of the quote. This allows for quotes other than prices e.g. rates or spreads to be used. | [optional] 
**field** | **str** | The field of the quote e.g. bid, mid, ask etc. This should be consistent across a time series of quotes. The allowed values depend on the provider according to the following rules: Client : *Any value is accepted*; DataScope : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;; Lusid : *Any value is accepted*; Edi : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;last&#39;; TraderMade : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;high&#39;, &#39;low&#39;; FactSet : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;; SIX : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;last&#39;; Bloomberg : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;last&#39;; Rimes : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;last&#39; | [optional] 

## Example

```python
from lusid.models.quote_access_metadata_rule_id import QuoteAccessMetadataRuleId

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteAccessMetadataRuleId from a JSON string
quote_access_metadata_rule_id_instance = QuoteAccessMetadataRuleId.from_json(json)
# print the JSON string representation of the object
print QuoteAccessMetadataRuleId.to_json()

# convert the object into a dict
quote_access_metadata_rule_id_dict = quote_access_metadata_rule_id_instance.to_dict()
# create an instance of QuoteAccessMetadataRuleId from a dict
quote_access_metadata_rule_id_form_dict = quote_access_metadata_rule_id.from_dict(quote_access_metadata_rule_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


