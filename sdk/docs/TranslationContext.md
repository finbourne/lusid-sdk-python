# TranslationContext

Options for overriding default scripted translation configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_scripted_translation** | **bool** |  | [optional] 
**script_map** | [**ScriptMapReference**](ScriptMapReference.md) |  | [optional] 

## Example

```python
from lusid.models.translation_context import TranslationContext

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationContext from a JSON string
translation_context_instance = TranslationContext.from_json(json)
# print the JSON string representation of the object
print TranslationContext.to_json()

# convert the object into a dict
translation_context_dict = translation_context_instance.to_dict()
# create an instance of TranslationContext from a dict
translation_context_form_dict = translation_context.from_dict(translation_context_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


