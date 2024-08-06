# ComplianceRuleResultPortfolioDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** |  | 

## Example

```python
from lusid.models.compliance_rule_result_portfolio_detail import ComplianceRuleResultPortfolioDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleResultPortfolioDetail from a JSON string
compliance_rule_result_portfolio_detail_instance = ComplianceRuleResultPortfolioDetail.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleResultPortfolioDetail.to_json()

# convert the object into a dict
compliance_rule_result_portfolio_detail_dict = compliance_rule_result_portfolio_detail_instance.to_dict()
# create an instance of ComplianceRuleResultPortfolioDetail from a dict
compliance_rule_result_portfolio_detail_form_dict = compliance_rule_result_portfolio_detail.from_dict(compliance_rule_result_portfolio_detail_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


