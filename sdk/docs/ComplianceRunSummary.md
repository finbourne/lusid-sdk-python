# ComplianceRunSummary


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
from lusid.models.compliance_run_summary import ComplianceRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRunSummary from a JSON string
compliance_run_summary_instance = ComplianceRunSummary.from_json(json)
# print the JSON string representation of the object
print ComplianceRunSummary.to_json()

# convert the object into a dict
compliance_run_summary_dict = compliance_run_summary_instance.to_dict()
# create an instance of ComplianceRunSummary from a dict
compliance_run_summary_form_dict = compliance_run_summary.from_dict(compliance_run_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


