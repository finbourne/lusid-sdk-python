# TranslationInput

The input to a translation script.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | The serialised entity to be passed to the translation script. This could represent e.g. an instrument in any  dialect. | 

## Example

```python
from lusid.models.translation_input import TranslationInput

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationInput from a JSON string
translation_input_instance = TranslationInput.from_json(json)
# print the JSON string representation of the object
print TranslationInput.to_json()

# convert the object into a dict
translation_input_dict = translation_input_instance.to_dict()
# create an instance of TranslationInput from a dict
translation_input_form_dict = translation_input.from_dict(translation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


