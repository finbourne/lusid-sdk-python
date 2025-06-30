# AggregatedTransactionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_transaction_date** | **datetime** |  | 
**to_transaction_date** | **datetime** |  | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolio or portfolio group identifiers containing the relevant transactions. | [optional] 
**as_at** | **datetime** |  | [optional] 
**metrics** | [**List[AggregateSpec]**](AggregateSpec.md) |  | 
**group_by** | **List[str]** |  | [optional] 
**filters** | [**List[PropertyFilter]**](PropertyFilter.md) |  | [optional] 
**sort** | [**List[OrderBySpec]**](OrderBySpec.md) |  | [optional] 
## Example

```python
from lusid.models.aggregated_transactions_request import AggregatedTransactionsRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
from_transaction_date: datetime = # Replace with your value
to_transaction_date: datetime = # Replace with your value
portfolio_id: Optional[ResourceId] = # Replace with your value
portfolio_entity_ids: Optional[conlist(PortfolioEntityId)] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
metrics: conlist(AggregateSpec) = # Replace with your value
group_by: Optional[conlist(StrictStr)] = # Replace with your value
filters: Optional[conlist(PropertyFilter)] = None
sort: Optional[conlist(OrderBySpec)] = None
aggregated_transactions_request_instance = AggregatedTransactionsRequest(from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, portfolio_id=portfolio_id, portfolio_entity_ids=portfolio_entity_ids, as_at=as_at, metrics=metrics, group_by=group_by, filters=filters, sort=sort)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

