# CustomEntityResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**entity_type** | **str** | The type of custom entity this is. | 
**version** | [**Version**](Version.md) |  | 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**display_name** | **str** | A display label for the custom entity. | 
**description** | **str** | A description of the custom entity. | [optional] 
**identifiers** | [**List[CustomEntityId]**](CustomEntityId.md) | The identifiers the custom entity will be upserted with. | 
**fields** | [**List[CustomEntityField]**](CustomEntityField.md) | The fields that decorate the custom entity. | 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the custom entity. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties that decorate the custom entity. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.custom_entity_response import CustomEntityResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
entity_type: StrictStr = "example_entity_type"
version: Version
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
identifiers: List[CustomEntityId] = # Replace with your value
fields: List[CustomEntityField] = # Replace with your value
relationships: List[Relationship] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
links: Optional[List[Link]] = None
custom_entity_response_instance = CustomEntityResponse(href=href, entity_type=entity_type, version=version, staged_modifications=staged_modifications, display_name=display_name, description=description, identifiers=identifiers, fields=fields, relationships=relationships, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

