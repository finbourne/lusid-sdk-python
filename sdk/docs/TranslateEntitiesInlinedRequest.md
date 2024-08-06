# TranslateEntitiesInlinedRequest

Request to translate financial entities with a given script body.  The output of the translation is validated against a schema specified in the request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_payloads** | [**Dict[str, TranslationInput]**](TranslationInput.md) | Entity payloads to be translated indexed by (ephemeral) unique correlation ids. | 
**script_body** | **str** | The body of the translation script to use for translating the entities. | 
**var_schema** | [**DialectSchema**](DialectSchema.md) |  | [optional] 

## Example

```python
from lusid.models.translate_entities_inlined_request import TranslateEntitiesInlinedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateEntitiesInlinedRequest from a JSON string
translate_entities_inlined_request_instance = TranslateEntitiesInlinedRequest.from_json(json)
# print the JSON string representation of the object
print TranslateEntitiesInlinedRequest.to_json()

# convert the object into a dict
translate_entities_inlined_request_dict = translate_entities_inlined_request_instance.to_dict()
# create an instance of TranslateEntitiesInlinedRequest from a dict
translate_entities_inlined_request_form_dict = translate_entities_inlined_request.from_dict(translate_entities_inlined_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


