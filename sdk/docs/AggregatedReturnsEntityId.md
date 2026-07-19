# AggregatedReturnsEntityId

Identifies an entity whose aggregated (time-weighted) returns are calculated: its scope, code and  type. Mirrors the valuation endpoint's entity identifier. Currently, supports only the  `Portfolio` entity type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 
**entity_type** | **str** | Available values: Portfolio. | 
## Example

```python
from lusid.models.aggregated_returns_entity_id import AggregatedReturnsEntityId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
entity_type: StrictStr = "example_entity_type"
aggregated_returns_entity_id_instance = AggregatedReturnsEntityId(scope=scope, code=code, entity_type=entity_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

