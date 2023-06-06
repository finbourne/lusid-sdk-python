# PagedResourceListOfLegalEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[LegalEntity]**](LegalEntity.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_legal_entity import PagedResourceListOfLegalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfLegalEntity from a JSON string
paged_resource_list_of_legal_entity_instance = PagedResourceListOfLegalEntity.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfLegalEntity.to_json()

# convert the object into a dict
paged_resource_list_of_legal_entity_dict = paged_resource_list_of_legal_entity_instance.to_dict()
# create an instance of PagedResourceListOfLegalEntity from a dict
paged_resource_list_of_legal_entity_form_dict = paged_resource_list_of_legal_entity.from_dict(paged_resource_list_of_legal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


