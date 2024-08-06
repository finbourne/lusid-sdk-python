# UpsertComplianceRunSummaryResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**instigated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**schedule** | **str** |  | 
**results** | [**List[ComplianceSummaryRuleResult]**](ComplianceSummaryRuleResult.md) |  | 

## Example

```python
from lusid.models.upsert_compliance_run_summary_result import UpsertComplianceRunSummaryResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertComplianceRunSummaryResult from a JSON string
upsert_compliance_run_summary_result_instance = UpsertComplianceRunSummaryResult.from_json(json)
# print the JSON string representation of the object
print UpsertComplianceRunSummaryResult.to_json()

# convert the object into a dict
upsert_compliance_run_summary_result_dict = upsert_compliance_run_summary_result_instance.to_dict()
# create an instance of UpsertComplianceRunSummaryResult from a dict
upsert_compliance_run_summary_result_form_dict = upsert_compliance_run_summary_result.from_dict(upsert_compliance_run_summary_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


