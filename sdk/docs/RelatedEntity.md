# RelatedEntity

Information about the other related entity in the relationship
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity. | 
**entity_id** | **Dict[str, str]** | The identifier of the other related entity in the relationship. It contains &#39;scope&#39; and &#39;code&#39; as keys for identifiers of a Portfolio or Portfolio Group, or &#39;idTypeScope&#39;, &#39;idTypeCode&#39;, &#39;code&#39; as keys for identifiers of a Person or Legal entity, or &#39;scope&#39;, &#39;identifierType&#39;, &#39;identifierValue&#39; as keys for identifiers of an Instrument | 
**display_name** | **str** | The display name of the entity. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties of the entity. This field is empty until further notice. | [optional] 
**scope** | **str** | The scope of the identifier | [optional] 
**lusid_unique_id** | [**LusidUniqueId**](LusidUniqueId.md) |  | [optional] 
**identifiers** | [**List[EntityIdentifier]**](EntityIdentifier.md) | The identifiers of the related entity in the relationship. | 
**href** | **str** | The link to the entity. | [optional] 
## Example

```python
from lusid.models.related_entity import RelatedEntity
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

entity_type: StrictStr = "example_entity_type"
entity_id: Dict[str, StrictStr] = # Replace with your value
display_name: StrictStr = "example_display_name"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
scope: Optional[StrictStr] = "example_scope"
lusid_unique_id: Optional[LusidUniqueId] = # Replace with your value
identifiers: conlist(EntityIdentifier) = # Replace with your value
href: Optional[StrictStr] = "example_href"
related_entity_instance = RelatedEntity(entity_type=entity_type, entity_id=entity_id, display_name=display_name, properties=properties, scope=scope, lusid_unique_id=lusid_unique_id, identifiers=identifiers, href=href)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

