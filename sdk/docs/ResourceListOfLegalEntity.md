# ResourceListOfLegalEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[LegalEntity]**](LegalEntity.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_legal_entity import ResourceListOfLegalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfLegalEntity from a JSON string
resource_list_of_legal_entity_instance = ResourceListOfLegalEntity.from_json(json)
# print the JSON string representation of the object
print ResourceListOfLegalEntity.to_json()

# convert the object into a dict
resource_list_of_legal_entity_dict = resource_list_of_legal_entity_instance.to_dict()
# create an instance of ResourceListOfLegalEntity from a dict
resource_list_of_legal_entity_form_dict = resource_list_of_legal_entity.from_dict(resource_list_of_legal_entity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


