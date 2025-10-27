# CreateRelationDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the relation exists in. | 
**code** | **str** | The code of the relation. Together with the scope this uniquely defines the relation. | 
**source_entity_domain** | **str** | The entity domain of the source entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**target_entity_domain** | **str** | The entity domain of the target entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**display_name** | **str** | The display name of the relation. | 
**outward_description** | **str** | The description to relate source entity object and target entity object. | 
**inward_description** | **str** | The description to relate target entity object and source entity object. | 
**life_time** | **str** | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 
## Example

```python
from lusid.models.create_relation_definition_request import CreateRelationDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
source_entity_domain: StrictStr = "example_source_entity_domain"
target_entity_domain: StrictStr = "example_target_entity_domain"
display_name: StrictStr = "example_display_name"
outward_description: StrictStr = "example_outward_description"
inward_description: StrictStr = "example_inward_description"
life_time: Optional[StrictStr] = "example_life_time"
constraint_style: Optional[StrictStr] = "example_constraint_style"
create_relation_definition_request_instance = CreateRelationDefinitionRequest(scope=scope, code=code, source_entity_domain=source_entity_domain, target_entity_domain=target_entity_domain, display_name=display_name, outward_description=outward_description, inward_description=inward_description, life_time=life_time, constraint_style=constraint_style)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

