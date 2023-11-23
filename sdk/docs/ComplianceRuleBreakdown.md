# ComplianceRuleBreakdown


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_status** | **str** |  | 
**results_used** | **Dict[str, float]** |  | 
**properties_used** | **Dict[str, List[ModelProperty]]** |  | 
**missing_data_information** | **List[str]** |  | 

## Example

```python
from lusid.models.compliance_rule_breakdown import ComplianceRuleBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleBreakdown from a JSON string
compliance_rule_breakdown_instance = ComplianceRuleBreakdown.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleBreakdown.to_json()

# convert the object into a dict
compliance_rule_breakdown_dict = compliance_rule_breakdown_instance.to_dict()
# create an instance of ComplianceRuleBreakdown from a dict
compliance_rule_breakdown_form_dict = compliance_rule_breakdown.from_dict(compliance_rule_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


