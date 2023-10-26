# UpsertComplianceRuleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | 
**template_id** | [**ResourceId**](ResourceId.md) |  | 
**variation** | **str** |  | 
**portfolio_group_id** | [**ResourceId**](ResourceId.md) |  | 
**parameters** | [**Dict[str, ComplianceParameter]**](ComplianceParameter.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | 

## Example

```python
from lusid.models.upsert_compliance_rule_request import UpsertComplianceRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertComplianceRuleRequest from a JSON string
upsert_compliance_rule_request_instance = UpsertComplianceRuleRequest.from_json(json)
# print the JSON string representation of the object
print UpsertComplianceRuleRequest.to_json()

# convert the object into a dict
upsert_compliance_rule_request_dict = upsert_compliance_rule_request_instance.to_dict()
# create an instance of UpsertComplianceRuleRequest from a dict
upsert_compliance_rule_request_form_dict = upsert_compliance_rule_request.from_dict(upsert_compliance_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


