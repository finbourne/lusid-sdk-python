# GroupReconciliationSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_details** | [**GroupReconciliationRunDetails**](GroupReconciliationRunDetails.md) |  | [optional] 
**group_reconciliation_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**reconciliation_type** | **str** | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; | 
**instance_id** | [**GroupReconciliationInstanceId**](GroupReconciliationInstanceId.md) |  | 
**dates_reconciled** | [**GroupReconciliationDates**](GroupReconciliationDates.md) |  | 
**reconciliation_run_as_at** | **datetime** | The date and time the reconciliation was run | 
**count_comparison_results** | **int** | The total number of comparison results with this InstanceId and ReconciliationType | 
**link_comparison_results** | [**Link**](Link.md) |  | [optional] 
**result_types** | [**GroupReconciliationResultTypes**](GroupReconciliationResultTypes.md) |  | [optional] 
**result_statuses** | [**GroupReconciliationResultStatuses**](GroupReconciliationResultStatuses.md) |  | [optional] 
**review_statuses** | [**GroupReconciliationReviewStatuses**](GroupReconciliationReviewStatuses.md) |  | [optional] 
## Example

```python
from lusid.models.group_reconciliation_summary import GroupReconciliationSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_details: Optional[GroupReconciliationRunDetails] = # Replace with your value
group_reconciliation_definition_id: Optional[ResourceId] = # Replace with your value
reconciliation_type: StrictStr = "example_reconciliation_type"
instance_id: GroupReconciliationInstanceId = # Replace with your value
dates_reconciled: GroupReconciliationDates = # Replace with your value
reconciliation_run_as_at: datetime = # Replace with your value
count_comparison_results: StrictInt = # Replace with your value
count_comparison_results: StrictInt = 42
link_comparison_results: Optional[Link] = # Replace with your value
result_types: Optional[GroupReconciliationResultTypes] = # Replace with your value
result_statuses: Optional[GroupReconciliationResultStatuses] = # Replace with your value
review_statuses: Optional[GroupReconciliationReviewStatuses] = # Replace with your value
group_reconciliation_summary_instance = GroupReconciliationSummary(run_details=run_details, group_reconciliation_definition_id=group_reconciliation_definition_id, reconciliation_type=reconciliation_type, instance_id=instance_id, dates_reconciled=dates_reconciled, reconciliation_run_as_at=reconciliation_run_as_at, count_comparison_results=count_comparison_results, link_comparison_results=link_comparison_results, result_types=result_types, result_statuses=result_statuses, review_statuses=review_statuses)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

