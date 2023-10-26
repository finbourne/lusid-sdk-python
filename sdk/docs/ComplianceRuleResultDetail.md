# ComplianceRuleResultDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | [**ResourceId**](ResourceId.md) |  | 
**affected_portfolios_details** | [**List[ComplianceRuleResultPortfolioDetail]**](ComplianceRuleResultPortfolioDetail.md) |  | 
**affected_orders** | [**List[ResourceId]**](ResourceId.md) |  | 
**template_id** | [**ResourceId**](ResourceId.md) |  | 
**template_description** | **str** |  | 
**template_variation** | **str** |  | 
**status** | **str** |  | 
**rule_name** | **str** |  | 
**rule_description** | **str** |  | 
**outcome** | **str** |  | 

## Example

```python
from lusid.models.compliance_rule_result_detail import ComplianceRuleResultDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleResultDetail from a JSON string
compliance_rule_result_detail_instance = ComplianceRuleResultDetail.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleResultDetail.to_json()

# convert the object into a dict
compliance_rule_result_detail_dict = compliance_rule_result_detail_instance.to_dict()
# create an instance of ComplianceRuleResultDetail from a dict
compliance_rule_result_detail_form_dict = compliance_rule_result_detail.from_dict(compliance_rule_result_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


