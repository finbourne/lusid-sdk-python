# TranslateEntitiesRequest

Request to translate financial entities with a specified script stored in LUSID,  specified in the request by its id. The output of the translation is validated against a dialect stored in LUSID,  again specified in the request by its id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_payloads** | [**Dict[str, TranslationInput]**](TranslationInput.md) | Entity payloads to be translated, indexed by (ephemeral) unique correlation ids. | 
**script_id** | [**TranslationScriptId**](TranslationScriptId.md) |  | 
**dialect_id** | [**DialectId**](DialectId.md) |  | [optional] 

## Example

```python
from lusid.models.translate_entities_request import TranslateEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateEntitiesRequest from a JSON string
translate_entities_request_instance = TranslateEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print TranslateEntitiesRequest.to_json()

# convert the object into a dict
translate_entities_request_dict = translate_entities_request_instance.to_dict()
# create an instance of TranslateEntitiesRequest from a dict
translate_entities_request_form_dict = translate_entities_request.from_dict(translate_entities_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


