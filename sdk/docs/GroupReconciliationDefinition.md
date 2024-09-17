# GroupReconciliationDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** | The name of the Group Reconciliation Definition | [optional] 
**description** | **str** | The description of the Group Reconciliation Definition | [optional] 
**portfolio_entity_ids** | [**GroupReconciliationDefinitionPortfolioEntityIds**](GroupReconciliationDefinitionPortfolioEntityIds.md) |  | [optional] 
**recipe_ids** | [**GroupReconciliationDefinitionRecipeIds**](GroupReconciliationDefinitionRecipeIds.md) |  | [optional] 
**currencies** | [**GroupReconciliationDefinitionCurrencies**](GroupReconciliationDefinitionCurrencies.md) |  | [optional] 
**transaction_date_windows** | [**TransactionDateWindows**](TransactionDateWindows.md) |  | [optional] 
**comparison_ruleset_ids** | [**GroupReconciliationDefinitionComparisonRulesetIds**](GroupReconciliationDefinitionComparisonRulesetIds.md) |  | [optional] 
**break_code_source** | [**BreakCodeSource**](BreakCodeSource.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 

## Example

```python
from lusid.models.group_reconciliation_definition import GroupReconciliationDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationDefinition from a JSON string
group_reconciliation_definition_instance = GroupReconciliationDefinition.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationDefinition.to_json()

# convert the object into a dict
group_reconciliation_definition_dict = group_reconciliation_definition_instance.to_dict()
# create an instance of GroupReconciliationDefinition from a dict
group_reconciliation_definition_form_dict = group_reconciliation_definition.from_dict(group_reconciliation_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


