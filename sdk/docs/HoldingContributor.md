# HoldingContributor

A list of transactions contributed to a holding.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**Transaction**](Transaction.md) |  | 
**holding_id** | **int** | The unique holding identifier | [optional] 
**movements** | [**List[MovementSettlementSummary]**](MovementSettlementSummary.md) | Movements contributed to holding | [optional] 
## Example

```python
from lusid.models.holding_contributor import HoldingContributor
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, conlist

transaction: Transaction = # Replace with your value
holding_id: Optional[StrictInt] = # Replace with your value
movements: Optional[conlist(MovementSettlementSummary)] = # Replace with your value
holding_contributor_instance = HoldingContributor(transaction=transaction, holding_id=holding_id, movements=movements)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

