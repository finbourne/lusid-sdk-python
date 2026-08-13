# RecResultException

The exception lifecycle of a rec result. Present only for exception result types  (Break, PartialMatch, PartialCross); null for Match and Cross.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Whether the exception is Open or Closed. Available values: Open, Closed. | 
**closure_type** | **str** | How the exception was closed. Non-null only when status is Closed. Available values: Cleared, Accepted, ForceMatched. | [optional] 
**as_at_closed** | **datetime** | The asAt of the transaction that closed the exception. Non-null only when status is Closed. | [optional] 
**as_at_closure_invalidated** | **datetime** | First-failure bookmark: the asAt at which a judgement closure&#39;s validity condition first failed against the latest run&#39;s data. | [optional] 
## Example

```python
from lusid.models.rec_result_exception import RecResultException
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: StrictStr = "example_status"
closure_type: Optional[StrictStr] = "example_closure_type"
as_at_closed: Optional[datetime] = # Replace with your value
as_at_closure_invalidated: Optional[datetime] = # Replace with your value
rec_result_exception_instance = RecResultException(status=status, closure_type=closure_type, as_at_closed=as_at_closed, as_at_closure_invalidated=as_at_closure_invalidated)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

