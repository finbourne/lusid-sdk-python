# LusidEntityResult

Represents LUSID entity details for a data quality check result
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The as-at timestamp for the entity | [optional] 
**effective_at** | **datetime** | The effective-at timestamp for the entity | [optional] 
**entity_type** | **str** | The type of the LUSID entity | [optional] 
**scope** | **str** | The scope of the entity | [optional] 
**identifier_key** | **str** | The identifier key for the entity | [optional] 
**identifier_value** | **str** | The identifier value for the entity | [optional] 
**entity_unique_id** | **str** | The unique identifier for the entity | [optional] 
**display_name** | **str** | The display name of the entity | [optional] 
## Example

```python
from lusid.models.lusid_entity_result import LusidEntityResult
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from datetime import datetime
as_at: Optional[datetime] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
entity_type: Optional[StrictStr] = "example_entity_type"
scope: Optional[StrictStr] = "example_scope"
identifier_key: Optional[StrictStr] = "example_identifier_key"
identifier_value: Optional[StrictStr] = "example_identifier_value"
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
display_name: Optional[StrictStr] = "example_display_name"
lusid_entity_result_instance = LusidEntityResult(as_at=as_at, effective_at=effective_at, entity_type=entity_type, scope=scope, identifier_key=identifier_key, identifier_value=identifier_value, entity_unique_id=entity_unique_id, display_name=display_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

