# TranslationScript


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**TranslationScriptId**](TranslationScriptId.md) |  | 
**body** | **str** | Body of the translation script, i.e. the actual translation code. | 
**version** | [**Version**](Version.md) |  | [optional] 

## Example

```python
from lusid.models.translation_script import TranslationScript

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationScript from a JSON string
translation_script_instance = TranslationScript.from_json(json)
# print the JSON string representation of the object
print TranslationScript.to_json()

# convert the object into a dict
translation_script_dict = translation_script_instance.to_dict()
# create an instance of TranslationScript from a dict
translation_script_form_dict = translation_script.from_dict(translation_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


