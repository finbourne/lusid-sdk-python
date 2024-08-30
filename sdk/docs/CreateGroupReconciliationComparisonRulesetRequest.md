# CreateGroupReconciliationComparisonRulesetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the ruleset | 
**reconciliation_type** | **str** | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; | 
**core_attribute_rules** | [**List[GroupReconciliationCoreAttributeRule]**](GroupReconciliationCoreAttributeRule.md) | The core comparison rules | 
**aggregate_attribute_rules** | [**List[GroupReconciliationAggregateAttributeRule]**](GroupReconciliationAggregateAttributeRule.md) | The aggregate comparison rules | 

## Example

```python
from lusid.models.create_group_reconciliation_comparison_ruleset_request import CreateGroupReconciliationComparisonRulesetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupReconciliationComparisonRulesetRequest from a JSON string
create_group_reconciliation_comparison_ruleset_request_instance = CreateGroupReconciliationComparisonRulesetRequest.from_json(json)
# print the JSON string representation of the object
print CreateGroupReconciliationComparisonRulesetRequest.to_json()

# convert the object into a dict
create_group_reconciliation_comparison_ruleset_request_dict = create_group_reconciliation_comparison_ruleset_request_instance.to_dict()
# create an instance of CreateGroupReconciliationComparisonRulesetRequest from a dict
create_group_reconciliation_comparison_ruleset_request_form_dict = create_group_reconciliation_comparison_ruleset_request.from_dict(create_group_reconciliation_comparison_ruleset_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


