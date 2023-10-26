# RelatedEntity

Information about the other related entity in the relationship

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity. | 
**entity_id** | **Dict[str, str]** | The identifier of the other related entity in the relationship. It contains &#39;scope&#39; and &#39;code&#39; as keys for identifiers of a Portfolio or Portfolio Group, or &#39;idTypeScope&#39;, &#39;idTypeCode&#39;, &#39;code&#39; as keys for identifiers of a Person or Legal Entity. | 
**display_name** | **str** | The display name of the entity. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties of the entity. This field is empty until further notice. | [optional] 
**scope** | **str** | The scope of the identifier | [optional] 
**lusid_unique_id** | [**LusidUniqueId**](LusidUniqueId.md) |  | [optional] 
**identifiers** | [**List[EntityIdentifier]**](EntityIdentifier.md) | The identifiers of the related entity in the relationship. | 
**href** | **str** | The link to the entity. | [optional] 

## Example

```python
from lusid.models.related_entity import RelatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedEntity from a JSON string
related_entity_instance = RelatedEntity.from_json(json)
# print the JSON string representation of the object
print RelatedEntity.to_json()

# convert the object into a dict
related_entity_dict = related_entity_instance.to_dict()
# create an instance of RelatedEntity from a dict
related_entity_form_dict = related_entity.from_dict(related_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


