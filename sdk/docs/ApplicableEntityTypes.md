# ApplicableEntityTypes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_entity_types_to_add** | **List[str]** | The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.). | [optional] 
**applicable_entity_types_to_remove** | **List[str]** | The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.). | [optional] 
## Example

```python
from lusid.models.applicable_entity_types import ApplicableEntityTypes
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

applicable_entity_types_to_add: Optional[List[StrictStr]] = # Replace with your value
applicable_entity_types_to_remove: Optional[List[StrictStr]] = # Replace with your value
applicable_entity_types_instance = ApplicableEntityTypes(applicable_entity_types_to_add=applicable_entity_types_to_add, applicable_entity_types_to_remove=applicable_entity_types_to_remove)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

