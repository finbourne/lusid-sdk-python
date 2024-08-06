# EquityAllOfIdentifiers

External market codes and identifiers for the equity, e.g. IBM

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
from lusid.models.equity_all_of_identifiers import EquityAllOfIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of EquityAllOfIdentifiers from a JSON string
equity_all_of_identifiers_instance = EquityAllOfIdentifiers.from_json(json)
# print the JSON string representation of the object
print EquityAllOfIdentifiers.to_json()

# convert the object into a dict
equity_all_of_identifiers_dict = equity_all_of_identifiers_instance.to_dict()
# create an instance of EquityAllOfIdentifiers from a dict
equity_all_of_identifiers_form_dict = equity_all_of_identifiers.from_dict(equity_all_of_identifiers_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


