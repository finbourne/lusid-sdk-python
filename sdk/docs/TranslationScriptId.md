# TranslationScriptId

Id of the Translation Script.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Scope of the translation script. | 
**code** | **str** | Code of the translation script. | 
**version** | **str** | Semantic Version of the translation script of the form MAJOR.MINOR.PATCH. | 

## Example

```python
from lusid.models.translation_script_id import TranslationScriptId

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationScriptId from a JSON string
translation_script_id_instance = TranslationScriptId.from_json(json)
# print the JSON string representation of the object
print TranslationScriptId.to_json()

# convert the object into a dict
translation_script_id_dict = translation_script_id_instance.to_dict()
# create an instance of TranslationScriptId from a dict
translation_script_id_form_dict = translation_script_id.from_dict(translation_script_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


