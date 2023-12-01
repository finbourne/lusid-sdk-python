# ComplianceRuleBreakdown


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_status** | **str** | The status of this subset of results. | 
**results_used** | **Dict[str, float]** | Dictionary of AddressKey (as string) and their corresponding decimal values, that were used in this rule. | 
**properties_used** | **Dict[str, List[ModelProperty]]** | Dictionary of PropertyKey (as string) and their corresponding Properties, that were used in this rule | 
**missing_data_information** | **List[str]** | List of string information detailing data that was missing from contributions processed in this rule | 

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


