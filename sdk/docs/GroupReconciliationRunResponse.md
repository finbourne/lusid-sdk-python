# GroupReconciliationRunResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reconciliation_summaries** | [**List[GroupReconciliationSummary]**](GroupReconciliationSummary.md) | One summary record for each of the \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; reconciliations performed | 
## Example

```python
from lusid.models.group_reconciliation_run_response import GroupReconciliationRunResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reconciliation_summaries: List[GroupReconciliationSummary] = # Replace with your value
group_reconciliation_run_response_instance = GroupReconciliationRunResponse(reconciliation_summaries=reconciliation_summaries)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

