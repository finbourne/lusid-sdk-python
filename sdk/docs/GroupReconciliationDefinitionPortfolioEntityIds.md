# GroupReconciliationDefinitionPortfolioEntityIds


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | Portfolio Entity Id of the left side of a reconciliation | 
**right** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | Portfolio Entity Id of the right side of a reconciliation | 

## Example

```python
from lusid.models.group_reconciliation_definition_portfolio_entity_ids import GroupReconciliationDefinitionPortfolioEntityIds

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationDefinitionPortfolioEntityIds from a JSON string
group_reconciliation_definition_portfolio_entity_ids_instance = GroupReconciliationDefinitionPortfolioEntityIds.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationDefinitionPortfolioEntityIds.to_json()

# convert the object into a dict
group_reconciliation_definition_portfolio_entity_ids_dict = group_reconciliation_definition_portfolio_entity_ids_instance.to_dict()
# create an instance of GroupReconciliationDefinitionPortfolioEntityIds from a dict
group_reconciliation_definition_portfolio_entity_ids_form_dict = group_reconciliation_definition_portfolio_entity_ids.from_dict(group_reconciliation_definition_portfolio_entity_ids_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


