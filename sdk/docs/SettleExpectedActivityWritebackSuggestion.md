# SettleExpectedActivityWritebackSuggestion

Suggests a settlement instruction that settles the expected activity of the target item, using the  settlement confirmed by the origin item on the other side of the result. The request is upsertable as-is.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_pattern** | [**WritebackResultPattern**](WritebackResultPattern.md) |  | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**settlement_instruction_request** | [**SettlementInstructionRequest**](SettlementInstructionRequest.md) |  | 
**writeback_type** | **str** | Polymorphic discriminator, carrying the same values as writebackType on the matching ruleset&#39;s writeback configuration. Supported types: SettleExpectedActivity. Available values: SettleExpectedActivity. | 
## Example

```python
from lusid.models.settle_expected_activity_writeback_suggestion import SettleExpectedActivityWritebackSuggestion
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

result_pattern: WritebackResultPattern = # Replace with your value
portfolio_id: ResourceId = # Replace with your value
settlement_instruction_request: SettlementInstructionRequest = # Replace with your value
writeback_type: StrictStr = "example_writeback_type"
settle_expected_activity_writeback_suggestion_instance = SettleExpectedActivityWritebackSuggestion(result_pattern=result_pattern, portfolio_id=portfolio_id, settlement_instruction_request=settlement_instruction_request, writeback_type=writeback_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

