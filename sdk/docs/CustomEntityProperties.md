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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: StrictStr = "example_href"
entity_type: StrictStr = "example_entity_type"
identifiers: List[CustomEntityId] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Version
links: Optional[List[Link]] = None
custom_entity_properties_instance = CustomEntityProperties(href=href, entity_type=entity_type, identifiers=identifiers, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

