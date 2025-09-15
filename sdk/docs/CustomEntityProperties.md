# CustomEntityProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | 
**entity_type** | **str** | The type of custom entity this is. | 
**identifiers** | [**List[CustomEntityId]**](CustomEntityId.md) | The identifiers the custom entity will be upserted with. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties that decorate the custom entity. | [optional] 
**version** | [**Version**](Version.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.custom_entity_properties import CustomEntityProperties
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

href: StrictStr = "example_href"
entity_type: StrictStr = "example_entity_type"
identifiers: conlist(CustomEntityId) = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Version = # Replace with your value
links: Optional[conlist(Link)] = None
custom_entity_properties_instance = CustomEntityProperties(href=href, entity_type=entity_type, identifiers=identifiers, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

