# GroupReconciliationDefinitionPortfolioEntityIds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | Portfolio Entity Id of the left side of a reconciliation | 
**right** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | Portfolio Entity Id of the right side of a reconciliation | 
## Example

```python
from lusid.models.group_reconciliation_definition_portfolio_entity_ids import GroupReconciliationDefinitionPortfolioEntityIds
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: List[PortfolioEntityId] = # Replace with your value
right: List[PortfolioEntityId] = # Replace with your value
group_reconciliation_definition_portfolio_entity_ids_instance = GroupReconciliationDefinitionPortfolioEntityIds(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

