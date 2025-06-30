# GroupReconciliationRunResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reconciliation_summaries** | [**List[GroupReconciliationSummary]**](GroupReconciliationSummary.md) | One summary record for each of the \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; reconciliations performed | 
## Example

```python
from lusid.models.group_reconciliation_run_response import GroupReconciliationRunResponse
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

reconciliation_summaries: conlist(GroupReconciliationSummary) = # Replace with your value
group_reconciliation_run_response_instance = GroupReconciliationRunResponse(reconciliation_summaries=reconciliation_summaries)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

