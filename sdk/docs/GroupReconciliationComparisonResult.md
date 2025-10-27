# GroupReconciliationComparisonResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**reconciliation_type** | **str** | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; | 
**group_reconciliation_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**instance_id** | [**GroupReconciliationInstanceId**](GroupReconciliationInstanceId.md) |  | 
**comparison_result_id** | **str** | Comparison result identifier, encoded value for core attribute results, aggregate attribute results, reconciliation type and run instanceId. | 
**reconciliation_run_as_at** | **datetime** | The timestamp when the run occurred. | 
**result_type** | **str** | Reconciliation run general result. \&quot;Break\&quot; | \&quot;Match\&quot; | \&quot;PartialMatch\&quot; | \&quot;NotFound | 
**result_status** | **str** | Indicates how a particular result evolves from one run to the next. \&quot;New\&quot; | \&quot;Confirmed\&quot; | \&quot;Changed\&quot; | 
**review_status** | **str** | Status of whether user has provided any input (comments, manual matches, break codes). \&quot;Pending\&quot; | \&quot;Reviewed\&quot; | \&quot;Matched\&quot; | \&quot;Invalid\&quot; | 
**dates_reconciled** | [**GroupReconciliationDates**](GroupReconciliationDates.md) |  | 
**core_attributes** | [**GroupReconciliationCoreAttributeValues**](GroupReconciliationCoreAttributeValues.md) |  | 
**aggregate_attributes** | [**GroupReconciliationAggregateAttributeValues**](GroupReconciliationAggregateAttributeValues.md) |  | 
**user_review** | [**GroupReconciliationUserReview**](GroupReconciliationUserReview.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.group_reconciliation_comparison_result import GroupReconciliationComparisonResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
reconciliation_type: StrictStr = "example_reconciliation_type"
group_reconciliation_definition_id: ResourceId = # Replace with your value
instance_id: GroupReconciliationInstanceId = # Replace with your value
comparison_result_id: StrictStr = "example_comparison_result_id"
reconciliation_run_as_at: datetime = # Replace with your value
result_type: StrictStr = "example_result_type"
result_status: StrictStr = "example_result_status"
review_status: StrictStr = "example_review_status"
dates_reconciled: GroupReconciliationDates = # Replace with your value
core_attributes: GroupReconciliationCoreAttributeValues = # Replace with your value
aggregate_attributes: GroupReconciliationAggregateAttributeValues = # Replace with your value
user_review: Optional[GroupReconciliationUserReview] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
group_reconciliation_comparison_result_instance = GroupReconciliationComparisonResult(id=id, reconciliation_type=reconciliation_type, group_reconciliation_definition_id=group_reconciliation_definition_id, instance_id=instance_id, comparison_result_id=comparison_result_id, reconciliation_run_as_at=reconciliation_run_as_at, result_type=result_type, result_status=result_status, review_status=review_status, dates_reconciled=dates_reconciled, core_attributes=core_attributes, aggregate_attributes=aggregate_attributes, user_review=user_review, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

