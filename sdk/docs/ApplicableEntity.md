# ApplicableEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of entity (e.g., Instrument, Portfolio) that this DataSeries applies to. | 
**entity_scope** | **str** | The scope of the entity. | [optional] 
**identifier_scope** | **str** | The scope of the identifier used to uniquely identify the entity. | [optional] 
**identifier_type** | **str** | The type of identifier (e.g., Figi, Isin) used to uniquely identify the entity. | [optional] 
**identifier_value** | **str** | The value of the identifier used to uniquely identify the entity. | [optional] 
**sub_entity_id** | **str** | An optional sub-entity identifier, if applicable. | [optional] 
## Example

```python
from lusid.models.applicable_entity import ApplicableEntity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: StrictStr = "example_entity_type"
entity_scope: Optional[StrictStr] = "example_entity_scope"
identifier_scope: Optional[StrictStr] = "example_identifier_scope"
identifier_type: Optional[StrictStr] = "example_identifier_type"
identifier_value: Optional[StrictStr] = "example_identifier_value"
sub_entity_id: Optional[StrictStr] = "example_sub_entity_id"
applicable_entity_instance = ApplicableEntity(entity_type=entity_type, entity_scope=entity_scope, identifier_scope=identifier_scope, identifier_type=identifier_type, identifier_value=identifier_value, sub_entity_id=sub_entity_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

