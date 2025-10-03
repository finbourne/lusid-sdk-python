# BatchUpsertTransactionSettlementInstructionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, TransactionSettlementInstruction]**](TransactionSettlementInstruction.md) | The settlement instructions which have been successfully upserted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The request ids of the settlement instructions which could not be upserted, along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_upsert_transaction_settlement_instruction_response import BatchUpsertTransactionSettlementInstructionResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, TransactionSettlementInstruction]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[conlist(Link)] = None
batch_upsert_transaction_settlement_instruction_response_instance = BatchUpsertTransactionSettlementInstructionResponse(href=href, values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

