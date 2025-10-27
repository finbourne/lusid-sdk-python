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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction: Transaction
holding_id: Optional[StrictInt] = # Replace with your value
movements: Optional[List[MovementSettlementSummary]] = # Replace with your value
holding_contributor_instance = HoldingContributor(transaction=transaction, holding_id=holding_id, movements=movements)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

