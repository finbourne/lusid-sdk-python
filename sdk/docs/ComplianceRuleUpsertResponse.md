# ComplianceRuleUpsertResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, ComplianceRule]**](ComplianceRule.md) |  | 

## Example

```python
from lusid.models.compliance_rule_upsert_response import ComplianceRuleUpsertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleUpsertResponse from a JSON string
compliance_rule_upsert_response_instance = ComplianceRuleUpsertResponse.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleUpsertResponse.to_json()

# convert the object into a dict
compliance_rule_upsert_response_dict = compliance_rule_upsert_response_instance.to_dict()
# create an instance of ComplianceRuleUpsertResponse from a dict
compliance_rule_upsert_response_form_dict = compliance_rule_upsert_response.from_dict(compliance_rule_upsert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


