# PagedResourceListOfTranslationScriptId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[TranslationScriptId]**](TranslationScriptId.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_translation_script_id import PagedResourceListOfTranslationScriptId

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfTranslationScriptId from a JSON string
paged_resource_list_of_translation_script_id_instance = PagedResourceListOfTranslationScriptId.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfTranslationScriptId.to_json()

# convert the object into a dict
paged_resource_list_of_translation_script_id_dict = paged_resource_list_of_translation_script_id_instance.to_dict()
# create an instance of PagedResourceListOfTranslationScriptId from a dict
paged_resource_list_of_translation_script_id_form_dict = paged_resource_list_of_translation_script_id.from_dict(paged_resource_list_of_translation_script_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


