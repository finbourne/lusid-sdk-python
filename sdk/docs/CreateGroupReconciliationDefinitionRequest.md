# CreateGroupReconciliationDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** | The name of the Group Reconciliation Definition | 
**description** | **str** | The description of the Group Reconciliation Definition | [optional] 
**portfolio_entity_ids** | [**GroupReconciliationDefinitionPortfolioEntityIds**](GroupReconciliationDefinitionPortfolioEntityIds.md) |  | 
**recipe_ids** | [**GroupReconciliationDefinitionRecipeIds**](GroupReconciliationDefinitionRecipeIds.md) |  | [optional] 
**currencies** | [**GroupReconciliationDefinitionCurrencies**](GroupReconciliationDefinitionCurrencies.md) |  | [optional] 
**transaction_date_windows** | [**TransactionDateWindows**](TransactionDateWindows.md) |  | [optional] 
**comparison_ruleset_ids** | [**GroupReconciliationDefinitionComparisonRulesetIds**](GroupReconciliationDefinitionComparisonRulesetIds.md) |  | [optional] 
**break_code_source** | [**BreakCodeSource**](BreakCodeSource.md) |  | 

## Example

```python
from lusid.models.create_group_reconciliation_definition_request import CreateGroupReconciliationDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupReconciliationDefinitionRequest from a JSON string
create_group_reconciliation_definition_request_instance = CreateGroupReconciliationDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print CreateGroupReconciliationDefinitionRequest.to_json()

# convert the object into a dict
create_group_reconciliation_definition_request_dict = create_group_reconciliation_definition_request_instance.to_dict()
# create an instance of CreateGroupReconciliationDefinitionRequest from a dict
create_group_reconciliation_definition_request_form_dict = create_group_reconciliation_definition_request.from_dict(create_group_reconciliation_definition_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


