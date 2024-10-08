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

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationComparisonResult from a JSON string
group_reconciliation_comparison_result_instance = GroupReconciliationComparisonResult.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationComparisonResult.to_json()

# convert the object into a dict
group_reconciliation_comparison_result_dict = group_reconciliation_comparison_result_instance.to_dict()
# create an instance of GroupReconciliationComparisonResult from a dict
group_reconciliation_comparison_result_form_dict = group_reconciliation_comparison_result.from_dict(group_reconciliation_comparison_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


