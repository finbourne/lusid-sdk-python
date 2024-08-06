# TranslateEntitiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, TranslationResult]**](TranslationResult.md) | The entities that were successfully translated. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The error details corresponding to entities that failed to be translated. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.translate_entities_response import TranslateEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateEntitiesResponse from a JSON string
translate_entities_response_instance = TranslateEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print TranslateEntitiesResponse.to_json()

# convert the object into a dict
translate_entities_response_dict = translate_entities_response_instance.to_dict()
# create an instance of TranslateEntitiesResponse from a dict
translate_entities_response_form_dict = translate_entities_response.from_dict(translate_entities_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


