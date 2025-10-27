# CreateRelationshipDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the relationship definition exists in. | 
**code** | **str** | The code of the relationship definition. Together with the scope this uniquely defines the relationship definition. | 
**source_entity_type** | **str** | The entity type of the source entity object. Allowed values are &#39;Portfolio&#39;, &#39;PortfolioGroup&#39;, &#39;Person&#39;, &#39;LegalEntity&#39;, &#39;Instrument&#39; or a custom entity type prefixed with &#39;~&#39;. | 
**target_entity_type** | **str** | The entity type of the target entity object. Allowed values are &#39;Portfolio&#39;, &#39;PortfolioGroup&#39;, &#39;Person&#39;, &#39;LegalEntity&#39;, &#39;Instrument&#39; or a custom entity type prefixed with &#39;~&#39;. | 
**display_name** | **str** | The display name of the relationship definition. | 
**outward_description** | **str** | The description to relate source entity object and target entity object. | 
**inward_description** | **str** | The description to relate target entity object and source entity object. | 
**life_time** | **str** | Describes how the relationships can change over time. Allowed values are &#39;Perpetual&#39; and &#39;TimeVariant&#39;, defaults to &#39;Perpetual&#39; if not specified. | [optional] 
**relationship_cardinality** | **str** | Describes the cardinality of the relationship with a specific source entity object and relationships under this definition. Allowed values are &#39;ManyToMany&#39; and &#39;ManyToOne&#39;, defaults to &#39;ManyToMany&#39; if not specified. | [optional] 
## Example

```python
from lusid.models.create_relationship_definition_request import CreateRelationshipDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
source_entity_type: StrictStr = "example_source_entity_type"
target_entity_type: StrictStr = "example_target_entity_type"
display_name: StrictStr = "example_display_name"
outward_description: StrictStr = "example_outward_description"
inward_description: StrictStr = "example_inward_description"
life_time: Optional[StrictStr] = "example_life_time"
relationship_cardinality: Optional[StrictStr] = "example_relationship_cardinality"
create_relationship_definition_request_instance = CreateRelationshipDefinitionRequest(scope=scope, code=code, source_entity_type=source_entity_type, target_entity_type=target_entity_type, display_name=display_name, outward_description=outward_description, inward_description=inward_description, life_time=life_time, relationship_cardinality=relationship_cardinality)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

