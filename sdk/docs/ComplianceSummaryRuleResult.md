# ComplianceSummaryRuleResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | [**ResourceId**](ResourceId.md) |  | 
**template_id** | [**ResourceId**](ResourceId.md) |  | 
**variation** | **str** |  | 
**rule_status** | **str** |  | 
**affected_portfolios** | [**List[ResourceId]**](ResourceId.md) |  | 
**affected_orders** | [**List[ResourceId]**](ResourceId.md) |  | 
**parameters_used** | **Dict[str, str]** |  | 
**rule_breakdown** | [**List[ComplianceRuleBreakdown]**](ComplianceRuleBreakdown.md) |  | 

## Example

```python
from lusid.models.compliance_summary_rule_result import ComplianceSummaryRuleResult

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceSummaryRuleResult from a JSON string
compliance_summary_rule_result_instance = ComplianceSummaryRuleResult.from_json(json)
# print the JSON string representation of the object
print ComplianceSummaryRuleResult.to_json()

# convert the object into a dict
compliance_summary_rule_result_dict = compliance_summary_rule_result_instance.to_dict()
# create an instance of ComplianceSummaryRuleResult from a dict
compliance_summary_rule_result_form_dict = compliance_summary_rule_result.from_dict(compliance_summary_rule_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


