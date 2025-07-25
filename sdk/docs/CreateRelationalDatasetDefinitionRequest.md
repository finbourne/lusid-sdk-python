# CreateRelationalDatasetDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | A user-friendly display name for the relational dataset definition. | 
**description** | **str** | A detailed description of the relational dataset definition and its purpose. | [optional] 
**applicable_entity_types** | **List[str]** | The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.). | 
**field_schema** | [**List[RelationalDatasetFieldDefinition]**](RelationalDatasetFieldDefinition.md) | The schema defining the structure and data types of the relational dataset. | 
## Example

```python
from lusid.models.create_relational_dataset_definition_request import CreateRelationalDatasetDefinitionRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
applicable_entity_types: conlist(StrictStr) = # Replace with your value
field_schema: conlist(RelationalDatasetFieldDefinition) = # Replace with your value
create_relational_dataset_definition_request_instance = CreateRelationalDatasetDefinitionRequest(id=id, display_name=display_name, description=description, applicable_entity_types=applicable_entity_types, field_schema=field_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

