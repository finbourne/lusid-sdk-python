# GroupReconciliationDefinitionPortfolioEntityIds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | Portfolio Entity Id of the left side of a reconciliation | 
**right** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | Portfolio Entity Id of the right side of a reconciliation | 
## Example

```python
from lusid.models.group_reconciliation_definition_portfolio_entity_ids import GroupReconciliationDefinitionPortfolioEntityIds
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

left: conlist(PortfolioEntityId, min_items=1) = Field(..., description="Portfolio Entity Id of the left side of a reconciliation")
right: conlist(PortfolioEntityId, min_items=1) = Field(..., description="Portfolio Entity Id of the right side of a reconciliation")
group_reconciliation_definition_portfolio_entity_ids_instance = GroupReconciliationDefinitionPortfolioEntityIds(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

