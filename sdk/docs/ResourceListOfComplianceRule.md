# ResourceListOfComplianceRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ComplianceRule]**](ComplianceRule.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_compliance_rule import ResourceListOfComplianceRule

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfComplianceRule from a JSON string
resource_list_of_compliance_rule_instance = ResourceListOfComplianceRule.from_json(json)
# print the JSON string representation of the object
print ResourceListOfComplianceRule.to_json()

# convert the object into a dict
resource_list_of_compliance_rule_dict = resource_list_of_compliance_rule_instance.to_dict()
# create an instance of ResourceListOfComplianceRule from a dict
resource_list_of_compliance_rule_form_dict = resource_list_of_compliance_rule.from_dict(resource_list_of_compliance_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


