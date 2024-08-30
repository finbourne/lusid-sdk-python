# NewInstrument

Set of identifiers of an existing instrument that will be the subject of a SpinOffEvent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers. | 
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers. | [optional] [readonly] 
**instrument_scope** | **str** | The scope in which the instrument lies, resolved from the instrument identifiers. | [optional] [readonly] 
**dom_ccy** | **str** | The domestic currency of the instrument, resolved from the instrument identifiers. | [optional] [readonly] 

## Example

```python
from lusid.models.new_instrument import NewInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of NewInstrument from a JSON string
new_instrument_instance = NewInstrument.from_json(json)
# print the JSON string representation of the object
print NewInstrument.to_json()

# convert the object into a dict
new_instrument_dict = new_instrument_instance.to_dict()
# create an instance of NewInstrument from a dict
new_instrument_form_dict = new_instrument.from_dict(new_instrument_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


