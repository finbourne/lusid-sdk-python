# ComplianceRuleUpsertRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**type** | **str** |  | 
**property_key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**lower_bound** | **float** |  | 
**upper_bound** | **float** |  | 
**schedule** | **str** |  | 
**hard_requirement** | **bool** |  | 
**target_portfolio_ids** | [**List[ResourceId]**](ResourceId.md) |  | 
**description** | **str** |  | [optional] 
**address_key** | **str** |  | [optional] 

## Example

```python
from lusid.models.compliance_rule_upsert_request import ComplianceRuleUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleUpsertRequest from a JSON string
compliance_rule_upsert_request_instance = ComplianceRuleUpsertRequest.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleUpsertRequest.to_json()

# convert the object into a dict
compliance_rule_upsert_request_dict = compliance_rule_upsert_request_instance.to_dict()
# create an instance of ComplianceRuleUpsertRequest from a dict
compliance_rule_upsert_request_form_dict = compliance_rule_upsert_request.from_dict(compliance_rule_upsert_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


