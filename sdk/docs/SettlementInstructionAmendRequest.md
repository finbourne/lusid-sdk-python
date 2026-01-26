# SettlementInstructionAmendRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_instruction_id** | **str** |  | 
**operation** | **str** |  | [optional] 
**properties** | [**List[PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
## Example

```python
from lusid.models.settlement_instruction_amend_request import SettlementInstructionAmendRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

settlement_instruction_id: StrictStr = "example_settlement_instruction_id"
operation: Optional[StrictStr] = "example_operation"
properties: Optional[List[PerpetualProperty]] = None
settlement_instruction_amend_request_instance = SettlementInstructionAmendRequest(settlement_instruction_id=settlement_instruction_id, operation=operation, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

