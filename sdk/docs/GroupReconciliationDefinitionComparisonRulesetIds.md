# GroupReconciliationDefinitionComparisonRulesetIds


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_reconciliation** | [**ResourceId**](ResourceId.md) |  | [optional] 
**holding_reconciliation** | [**ResourceId**](ResourceId.md) |  | [optional] 
**valuation_reconciliation** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.group_reconciliation_definition_comparison_ruleset_ids import GroupReconciliationDefinitionComparisonRulesetIds

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationDefinitionComparisonRulesetIds from a JSON string
group_reconciliation_definition_comparison_ruleset_ids_instance = GroupReconciliationDefinitionComparisonRulesetIds.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationDefinitionComparisonRulesetIds.to_json()

# convert the object into a dict
group_reconciliation_definition_comparison_ruleset_ids_dict = group_reconciliation_definition_comparison_ruleset_ids_instance.to_dict()
# create an instance of GroupReconciliationDefinitionComparisonRulesetIds from a dict
group_reconciliation_definition_comparison_ruleset_ids_form_dict = group_reconciliation_definition_comparison_ruleset_ids.from_dict(group_reconciliation_definition_comparison_ruleset_ids_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


