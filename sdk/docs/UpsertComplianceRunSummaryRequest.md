# UpsertComplianceRunSummaryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**instigated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**schedule** | **str** |  | 
**results** | [**List[ComplianceSummaryRuleResultRequest]**](ComplianceSummaryRuleResultRequest.md) |  | 

## Example

```python
from lusid.models.upsert_compliance_run_summary_request import UpsertComplianceRunSummaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertComplianceRunSummaryRequest from a JSON string
upsert_compliance_run_summary_request_instance = UpsertComplianceRunSummaryRequest.from_json(json)
# print the JSON string representation of the object
print UpsertComplianceRunSummaryRequest.to_json()

# convert the object into a dict
upsert_compliance_run_summary_request_dict = upsert_compliance_run_summary_request_instance.to_dict()
# create an instance of UpsertComplianceRunSummaryRequest from a dict
upsert_compliance_run_summary_request_form_dict = upsert_compliance_run_summary_request.from_dict(upsert_compliance_run_summary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


