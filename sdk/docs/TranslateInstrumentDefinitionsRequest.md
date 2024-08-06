# TranslateInstrumentDefinitionsRequest

A collection of instruments to translate, along with the target dialect to translate into.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruments** | [**Dict[str, LusidInstrument]**](LusidInstrument.md) | The collection of instruments to translate.                Each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument. | 
**dialect** | **str** | The target dialect that the given instruments should be translated to. | 

## Example

```python
from lusid.models.translate_instrument_definitions_request import TranslateInstrumentDefinitionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateInstrumentDefinitionsRequest from a JSON string
translate_instrument_definitions_request_instance = TranslateInstrumentDefinitionsRequest.from_json(json)
# print the JSON string representation of the object
print TranslateInstrumentDefinitionsRequest.to_json()

# convert the object into a dict
translate_instrument_definitions_request_dict = translate_instrument_definitions_request_instance.to_dict()
# create an instance of TranslateInstrumentDefinitionsRequest from a dict
translate_instrument_definitions_request_form_dict = translate_instrument_definitions_request.from_dict(translate_instrument_definitions_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


