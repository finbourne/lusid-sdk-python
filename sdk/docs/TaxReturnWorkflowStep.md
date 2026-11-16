# TaxReturnWorkflowStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The workflow status of the return. Available values: Draft, Prepared, Reviewed, SignedOff, Final. Available values: Draft, Prepared, Reviewed, SignedOff, Final. | [optional] 
**as_at** | **datetime** | The time the workflow step was recorded. | [optional] 
**reason** | **str** | The reason given when the return was advanced or sent back. | [optional] 
## Example

```python
from lusid.models.tax_return_workflow_step import TaxReturnWorkflowStep
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: Optional[StrictStr] = "example_status"
as_at: Optional[datetime] = # Replace with your value
reason: Optional[StrictStr] = "example_reason"
tax_return_workflow_step_instance = TaxReturnWorkflowStep(status=status, as_at=as_at, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

