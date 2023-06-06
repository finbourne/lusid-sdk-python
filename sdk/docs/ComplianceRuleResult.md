# ComplianceRuleResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The unique identifierof a compliance rule | 
**rule_name** | **str** | The User-given name of the rule | 
**rule_description** | **str** | The User-given description of the rule | 
**portfolio** | [**ResourceId**](ResourceId.md) |  | 
**passed** | **bool** | The result of an individual compliance run, true if passed | 
**result_value** | **float** | The calculation result that was used to confirm a pass/fail | 
**rule_information_match** | **str** | The value matched by the rule | 
**rule_information_key** | **str** | The property key matched by the rule | 
**rule_lower_limit** | **float** | The lower limit of the rule | 
**rule_upper_limit** | **float** | The upper limit of the rule | 

## Example

```python
from lusid.models.compliance_rule_result import ComplianceRuleResult

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleResult from a JSON string
compliance_rule_result_instance = ComplianceRuleResult.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleResult.to_json()

# convert the object into a dict
compliance_rule_result_dict = compliance_rule_result_instance.to_dict()
# create an instance of ComplianceRuleResult from a dict
compliance_rule_result_form_dict = compliance_rule_result.from_dict(compliance_rule_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


