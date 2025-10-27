# SequenceDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**increment** | **int** | The Resource Id of the sequence definition | 
**min_value** | **int** | The minimum value of the sequence | 
**max_value** | **int** | The maximum value of the sequence | 
**start** | **int** | The start value of the sequence | 
**value** | **int** | The last used value of the sequence | [optional] 
**cycle** | **bool** | Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. | 
**pattern** | **str** | The pattern to be used to generate next values in the sequence. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.sequence_definition import SequenceDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
increment: StrictInt = # Replace with your value
min_value: StrictInt = # Replace with your value
max_value: StrictInt = # Replace with your value
start: StrictInt = # Replace with your value
value: Optional[StrictInt] = # Replace with your value
cycle: StrictBool = # Replace with your value
cycle:StrictBool = True
pattern: Optional[StrictStr] = "example_pattern"
links: Optional[List[Link]] = None
sequence_definition_instance = SequenceDefinition(id=id, increment=increment, min_value=min_value, max_value=max_value, start=start, value=value, cycle=cycle, pattern=pattern, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

