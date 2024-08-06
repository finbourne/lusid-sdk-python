# ComplianceBreachedOrderInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | 
**list_rule_result** | [**List[ComplianceRuleResult]**](ComplianceRuleResult.md) | The Rule Results for a particular compliance run | 

## Example

```python
from lusid.models.compliance_breached_order_info import ComplianceBreachedOrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceBreachedOrderInfo from a JSON string
compliance_breached_order_info_instance = ComplianceBreachedOrderInfo.from_json(json)
# print the JSON string representation of the object
print ComplianceBreachedOrderInfo.to_json()

# convert the object into a dict
compliance_breached_order_info_dict = compliance_breached_order_info_instance.to_dict()
# create an instance of ComplianceBreachedOrderInfo from a dict
compliance_breached_order_info_form_dict = compliance_breached_order_info.from_dict(compliance_breached_order_info_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


