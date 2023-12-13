# WeightedInstrumentInLineLookupIdentifiers

External market codes and identifiers for the equity, e.g. IBM.  Required for valuation via SimpleStatic (look-up pricing).  Valuation will not succeed without a matching quote.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_instrument_id** | **str** |  | [optional] 
**isin** | **str** |  | [optional] 
**sedol** | **str** |  | [optional] 
**cusip** | **str** |  | [optional] 
**client_internal** | **str** |  | [optional] 
**figi** | **str** |  | [optional] 
**ric** | **str** |  | [optional] 
**quote_perm_id** | **str** |  | [optional] 
**red_code** | **str** |  | [optional] 
**bbgid** | **str** |  | [optional] 
**ice_code** | **str** |  | [optional] 

## Example

```python
from lusid.models.weighted_instrument_in_line_lookup_identifiers import WeightedInstrumentInLineLookupIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of WeightedInstrumentInLineLookupIdentifiers from a JSON string
weighted_instrument_in_line_lookup_identifiers_instance = WeightedInstrumentInLineLookupIdentifiers.from_json(json)
# print the JSON string representation of the object
print WeightedInstrumentInLineLookupIdentifiers.to_json()

# convert the object into a dict
weighted_instrument_in_line_lookup_identifiers_dict = weighted_instrument_in_line_lookup_identifiers_instance.to_dict()
# create an instance of WeightedInstrumentInLineLookupIdentifiers from a dict
weighted_instrument_in_line_lookup_identifiers_form_dict = weighted_instrument_in_line_lookup_identifiers.from_dict(weighted_instrument_in_line_lookup_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


