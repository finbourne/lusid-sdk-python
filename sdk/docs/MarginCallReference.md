# MarginCallReference

A pointer to a margin call in another run.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | The run the referenced call belongs to. | 
**call_id** | **str** | The business key of the referenced call. | 
## Example

```python
from lusid.models.margin_call_reference import MarginCallReference
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
call_id: StrictStr = "example_call_id"
margin_call_reference_instance = MarginCallReference(run_id=run_id, call_id=call_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

