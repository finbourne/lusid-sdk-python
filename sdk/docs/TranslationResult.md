# TranslationResult

The result of invoking a translation script.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | The serialised entity the translation script produced. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Any properties the translation script produced. | 

## Example

```python
from lusid.models.translation_result import TranslationResult

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationResult from a JSON string
translation_result_instance = TranslationResult.from_json(json)
# print the JSON string representation of the object
print TranslationResult.to_json()

# convert the object into a dict
translation_result_dict = translation_result_instance.to_dict()
# create an instance of TranslationResult from a dict
translation_result_form_dict = translation_result.from_dict(translation_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


