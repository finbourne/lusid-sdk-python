# ApplicableEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of entity (e.g., Instrument, Portfolio) that this DataSeries applies to. | 
**entity_scope** | **str** | The scope of the entity. | [optional] 
**identifier_scope** | **str** | The scope of the identifier used to uniquely identify the entity. | [optional] 
**identifier_type** | **str** | The type of identifier (e.g., Figi, Isin) used to uniquely identify the entity. | [optional] 
**identifier_value** | **str** | The value of the identifier used to uniquely identify the entity. | [optional] 
## Example

```python
from lusid.models.applicable_entity import ApplicableEntity
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

entity_type: StrictStr = "example_entity_type"
entity_scope: Optional[StrictStr] = "example_entity_scope"
identifier_scope: Optional[StrictStr] = "example_identifier_scope"
identifier_type: Optional[StrictStr] = "example_identifier_type"
identifier_value: Optional[StrictStr] = "example_identifier_value"
applicable_entity_instance = ApplicableEntity(entity_type=entity_type, entity_scope=entity_scope, identifier_scope=identifier_scope, identifier_type=identifier_type, identifier_value=identifier_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

