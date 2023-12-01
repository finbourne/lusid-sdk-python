# UpsertTranslationScriptRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**TranslationScriptId**](TranslationScriptId.md) |  | 
**body** | **str** | Body of the translation script, i.e. the actual translation code. | 

## Example

```python
from lusid.models.upsert_translation_script_request import UpsertTranslationScriptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertTranslationScriptRequest from a JSON string
upsert_translation_script_request_instance = UpsertTranslationScriptRequest.from_json(json)
# print the JSON string representation of the object
print UpsertTranslationScriptRequest.to_json()

# convert the object into a dict
upsert_translation_script_request_dict = upsert_translation_script_request_instance.to_dict()
# create an instance of UpsertTranslationScriptRequest from a dict
upsert_translation_script_request_form_dict = upsert_translation_script_request.from_dict(upsert_translation_script_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


