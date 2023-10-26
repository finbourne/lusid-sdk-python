# ComplianceRuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**template_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**variation** | **str** |  | [optional] 
**portfolio_group_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**parameters** | [**Dict[str, ComplianceParameter]**](ComplianceParameter.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.compliance_rule_response import ComplianceRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleResponse from a JSON string
compliance_rule_response_instance = ComplianceRuleResponse.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleResponse.to_json()

# convert the object into a dict
compliance_rule_response_dict = compliance_rule_response_instance.to_dict()
# create an instance of ComplianceRuleResponse from a dict
compliance_rule_response_form_dict = compliance_rule_response.from_dict(compliance_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


