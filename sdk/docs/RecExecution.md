# RecExecution

The execution outcome for a run.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | **str** | The execution outcome. Available values: Succeeded, Failed. | 
**error_detail** | **str** | Detail of the execution failure. Populated when outcome is Failed. | [optional] 
## Example

```python
from lusid.models.rec_execution import RecExecution
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

outcome: StrictStr = "example_outcome"
error_detail: Optional[StrictStr] = "example_error_detail"
rec_execution_instance = RecExecution(outcome=outcome, error_detail=error_detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

