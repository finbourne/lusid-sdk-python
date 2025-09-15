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
**break_code_source** | [**BreakCodeSource**](BreakCodeSource.md) |  | [optional] 
**primary_schedule** | [**PrimarySchedule**](PrimarySchedule.md) |  | [optional] 
## Example

```python
from lusid.models.create_group_reconciliation_definition_request import CreateGroupReconciliationDefinitionRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

id: Optional[ResourceId] = None
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
portfolio_entity_ids: GroupReconciliationDefinitionPortfolioEntityIds = # Replace with your value
recipe_ids: Optional[GroupReconciliationDefinitionRecipeIds] = # Replace with your value
currencies: Optional[GroupReconciliationDefinitionCurrencies] = None
transaction_date_windows: Optional[TransactionDateWindows] = # Replace with your value
comparison_ruleset_ids: Optional[GroupReconciliationDefinitionComparisonRulesetIds] = # Replace with your value
break_code_source: Optional[BreakCodeSource] = # Replace with your value
primary_schedule: Optional[PrimarySchedule] = # Replace with your value
create_group_reconciliation_definition_request_instance = CreateGroupReconciliationDefinitionRequest(id=id, display_name=display_name, description=description, portfolio_entity_ids=portfolio_entity_ids, recipe_ids=recipe_ids, currencies=currencies, transaction_date_windows=transaction_date_windows, comparison_ruleset_ids=comparison_ruleset_ids, break_code_source=break_code_source, primary_schedule=primary_schedule)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

