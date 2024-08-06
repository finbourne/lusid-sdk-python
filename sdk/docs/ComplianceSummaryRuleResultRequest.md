# ComplianceSummaryRuleResultRequest


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
**rule_breakdown** | [**List[ComplianceRuleBreakdownRequest]**](ComplianceRuleBreakdownRequest.md) |  | 

## Example

```python
from lusid.models.compliance_summary_rule_result_request import ComplianceSummaryRuleResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceSummaryRuleResultRequest from a JSON string
compliance_summary_rule_result_request_instance = ComplianceSummaryRuleResultRequest.from_json(json)
# print the JSON string representation of the object
print ComplianceSummaryRuleResultRequest.to_json()

# convert the object into a dict
compliance_summary_rule_result_request_dict = compliance_summary_rule_result_request_instance.to_dict()
# create an instance of ComplianceSummaryRuleResultRequest from a dict
compliance_summary_rule_result_request_form_dict = compliance_summary_rule_result_request.from_dict(compliance_summary_rule_result_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


