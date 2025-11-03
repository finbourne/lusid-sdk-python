# SettlementProblem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_instruction_id** | **str** | The id of the problematic settlement instruction. Combined with the portfolio id this uniquely identifies a settlement instruction | 
**category** | **str** | The category this instruction belongs to | 
**status** | **str** | The status of the settlement instruction. Possible values are &#39;Invalid&#39; or &#39;Rejected&#39;. | 
## Example

```python
from lusid.models.settlement_problem import SettlementProblem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

settlement_instruction_id: StrictStr = "example_settlement_instruction_id"
category: StrictStr = "example_category"
status: StrictStr = "example_status"
settlement_problem_instance = SettlementProblem(settlement_instruction_id=settlement_instruction_id, category=category, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

