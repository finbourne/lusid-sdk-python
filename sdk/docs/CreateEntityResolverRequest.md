# CreateEntityResolverRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**entity_type** | **str** | The entity type that a specific resolution configuration is applicable to (e.g. Instrument). | 
**description** | **str** | Describes what this specific identifier order is used for. | [optional] 
**identifier_matching_order** | [**List[IdentifierForResolution]**](IdentifierForResolution.md) | Ordered collection of related identifier keys that are used to define which identifier takes priority in resolving an entity. | 
## Example

```python
from lusid.models.create_entity_resolver_request import CreateEntityResolverRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
entity_type: StrictStr = "example_entity_type"
description: Optional[StrictStr] = "example_description"
identifier_matching_order: List[IdentifierForResolution] = # Replace with your value
create_entity_resolver_request_instance = CreateEntityResolverRequest(id=id, entity_type=entity_type, description=description, identifier_matching_order=identifier_matching_order)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

