# SettlementInstructionWithTransaction

A Settlement Instruction with its Matched Transaction (if any)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_instruction** | [**TransactionSettlementInstruction**](TransactionSettlementInstruction.md) |  | [optional] 
**matched_transaction** | [**OutputTransaction**](OutputTransaction.md) |  | [optional] 
## Example

```python
from lusid.models.settlement_instruction_with_transaction import SettlementInstructionWithTransaction
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

settlement_instruction: Optional[TransactionSettlementInstruction] = # Replace with your value
matched_transaction: Optional[OutputTransaction] = # Replace with your value
settlement_instruction_with_transaction_instance = SettlementInstructionWithTransaction(settlement_instruction=settlement_instruction, matched_transaction=matched_transaction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

