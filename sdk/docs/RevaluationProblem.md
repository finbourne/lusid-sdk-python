# RevaluationProblem

A reason why a revaluation amount could not be populated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A machine-readable code identifying the type of problem (e.g. MissingFxRate, MissingBookedFxRate). | [optional] 
**message** | **str** | A human-readable description of why the revaluation amount could not be populated. | [optional] 
## Example

```python
from lusid.models.revaluation_problem import RevaluationProblem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: Optional[StrictStr] = "example_code"
message: Optional[StrictStr] = "example_message"
revaluation_problem_instance = RevaluationProblem(code=code, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

