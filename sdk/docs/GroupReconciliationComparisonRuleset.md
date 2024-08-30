# GroupReconciliationComparisonRuleset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the ruleset | 
**reconciliation_type** | **str** | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; | 
**core_attribute_rules** | [**List[GroupReconciliationCoreAttributeRule]**](GroupReconciliationCoreAttributeRule.md) | The core comparison rules | 
**aggregate_attribute_rules** | [**List[GroupReconciliationAggregateAttributeRule]**](GroupReconciliationAggregateAttributeRule.md) | The aggregate comparison rules | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.group_reconciliation_comparison_ruleset import GroupReconciliationComparisonRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationComparisonRuleset from a JSON string
group_reconciliation_comparison_ruleset_instance = GroupReconciliationComparisonRuleset.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationComparisonRuleset.to_json()

# convert the object into a dict
group_reconciliation_comparison_ruleset_dict = group_reconciliation_comparison_ruleset_instance.to_dict()
# create an instance of GroupReconciliationComparisonRuleset from a dict
group_reconciliation_comparison_ruleset_form_dict = group_reconciliation_comparison_ruleset.from_dict(group_reconciliation_comparison_ruleset_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


