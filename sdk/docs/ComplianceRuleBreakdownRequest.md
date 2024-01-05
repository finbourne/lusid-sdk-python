# ComplianceRuleBreakdownRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_status** | **str** |  | 
**results_used** | **Dict[str, float]** |  | 
**properties_used** | **Dict[str, List[ModelProperty]]** |  | 
**missing_data_information** | **List[str]** |  | 
**lineage** | [**List[LineageMember]**](LineageMember.md) |  | 

## Example

```python
from lusid.models.compliance_rule_breakdown_request import ComplianceRuleBreakdownRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleBreakdownRequest from a JSON string
compliance_rule_breakdown_request_instance = ComplianceRuleBreakdownRequest.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleBreakdownRequest.to_json()

# convert the object into a dict
compliance_rule_breakdown_request_dict = compliance_rule_breakdown_request_instance.to_dict()
# create an instance of ComplianceRuleBreakdownRequest from a dict
compliance_rule_breakdown_request_form_dict = compliance_rule_breakdown_request.from_dict(compliance_rule_breakdown_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


