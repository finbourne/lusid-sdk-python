# ComplianceRuleResultV2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**instigated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**schedule** | **str** |  | 
**rule_result** | [**ComplianceSummaryRuleResult**](ComplianceSummaryRuleResult.md) |  | 

## Example

```python
from lusid.models.compliance_rule_result_v2 import ComplianceRuleResultV2

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleResultV2 from a JSON string
compliance_rule_result_v2_instance = ComplianceRuleResultV2.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleResultV2.to_json()

# convert the object into a dict
compliance_rule_result_v2_dict = compliance_rule_result_v2_instance.to_dict()
# create an instance of ComplianceRuleResultV2 from a dict
compliance_rule_result_v2_form_dict = compliance_rule_result_v2.from_dict(compliance_rule_result_v2_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


