# CreateSequenceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the sequence definition to create | 
**increment** | **int** | The value to increment between each value in the sequence | [optional] 
**min_value** | **int** | The minimum value of the sequence | [optional] 
**max_value** | **int** | The maximum value of the sequence | [optional] 
**start** | **int** | The start value of the sequence | [optional] 
**cycle** | **bool** | Set to true to start the sequence over again when it reaches the end. Defaults to false if not provided. | [optional] 
**pattern** | **str** | The pattern to be used to generate next values in the sequence. Defaults to null if not provided. | [optional] 
## Example

```python
from lusid.models.create_sequence_request import CreateSequenceRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, constr, validator

code: StrictStr = "example_code"
increment: Optional[StrictInt] = # Replace with your value
min_value: Optional[StrictInt] = # Replace with your value
max_value: Optional[StrictInt] = # Replace with your value
start: Optional[StrictInt] = # Replace with your value
cycle: Optional[StrictBool] = # Replace with your value
cycle:Optional[StrictBool] = None
pattern: Optional[StrictStr] = "example_pattern"
create_sequence_request_instance = CreateSequenceRequest(code=code, increment=increment, min_value=min_value, max_value=max_value, start=start, cycle=cycle, pattern=pattern)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

