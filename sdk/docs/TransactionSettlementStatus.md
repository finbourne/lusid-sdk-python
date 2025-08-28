# TransactionSettlementStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier for the transaction. | 
**settlement_buckets** | [**List[TransactionSettlementBucket]**](TransactionSettlementBucket.md) | The transaction&#39;s external movements (ie: with SettlementMode&#x3D;External) are grouped into buckets with each bucket uniquely defined by the combination of SettlementCategory, LusidInstrumentId, InstrumentScope and ContractualSettlementDate. | [optional] 
**invalid_instructions** | [**List[TransactionSettlementInstruction]**](TransactionSettlementInstruction.md) | Invalid settlement instructions where the referenced transaction exists but the settlement bucket implied by the settlement instruction does not exist. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transaction_settlement_status import TransactionSettlementStatus
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

transaction_id: StrictStr = "example_transaction_id"
settlement_buckets: Optional[conlist(TransactionSettlementBucket)] = # Replace with your value
invalid_instructions: Optional[conlist(TransactionSettlementInstruction)] = # Replace with your value
links: Optional[conlist(Link)] = None
transaction_settlement_status_instance = TransactionSettlementStatus(transaction_id=transaction_id, settlement_buckets=settlement_buckets, invalid_instructions=invalid_instructions, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

