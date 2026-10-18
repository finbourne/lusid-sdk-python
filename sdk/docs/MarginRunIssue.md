# MarginRunIssue

Something a margin run could not do for some of its agreements, and why.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreements** | [**List[ResourceId]**](ResourceId.md) | The collateral agreements the issue concerns. | 
**detail** | **str** | What prevented the agreements from being valued. | 
**shard_id** | **str** | The shard the issue arose in, when it arose while valuing. | [optional] 
## Example

```python
from lusid.models.margin_run_issue import MarginRunIssue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

agreements: List[ResourceId] = # Replace with your value
detail: StrictStr = "example_detail"
shard_id: Optional[StrictStr] = "example_shard_id"
margin_run_issue_instance = MarginRunIssue(agreements=agreements, detail=detail, shard_id=shard_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

