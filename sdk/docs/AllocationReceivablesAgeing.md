# AllocationReceivablesAgeing

What each investor still owes on a booked capital call as of a date, and how late it is.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of** | **datetime** | The date the receivables are aged as of. | [optional] 
**due_date** | **datetime** | The date the cash was due. | [optional] 
**outstanding** | **float** | The total still owed across all investor records. | [optional] 
**receivables** | [**List[AllocationReceivable]**](AllocationReceivable.md) | One entry per investor record that was called. | [optional] 
## Example

```python
from lusid.models.allocation_receivables_ageing import AllocationReceivablesAgeing
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_of: Optional[datetime] = # Replace with your value
due_date: Optional[datetime] = # Replace with your value
outstanding: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
receivables: Optional[List[AllocationReceivable]] = # Replace with your value
allocation_receivables_ageing_instance = AllocationReceivablesAgeing(as_of=as_of, due_date=due_date, outstanding=outstanding, receivables=receivables)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

