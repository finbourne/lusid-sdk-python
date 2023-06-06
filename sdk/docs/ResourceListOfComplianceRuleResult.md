# ResourceListOfComplianceRuleResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ComplianceRuleResult]**](ComplianceRuleResult.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_compliance_rule_result import ResourceListOfComplianceRuleResult

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfComplianceRuleResult from a JSON string
resource_list_of_compliance_rule_result_instance = ResourceListOfComplianceRuleResult.from_json(json)
# print the JSON string representation of the object
print ResourceListOfComplianceRuleResult.to_json()

# convert the object into a dict
resource_list_of_compliance_rule_result_dict = resource_list_of_compliance_rule_result_instance.to_dict()
# create an instance of ResourceListOfComplianceRuleResult from a dict
resource_list_of_compliance_rule_result_form_dict = resource_list_of_compliance_rule_result.from_dict(resource_list_of_compliance_rule_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


