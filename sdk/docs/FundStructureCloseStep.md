# FundStructureCloseStep

One member's step in a fund structure close.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_short_code** | **str** | The node code of the member in the structure. | 
**fund** | [**ResourceId**](ResourceId.md) |  | 
**step** | **int** | The position of the member in the close order. | 
**status** | **str** | What happened to the member. Available values: Finalised, AlreadyFinal, Failed, Skipped. | 
**failure** | **str** | The failure that stopped the member finalising, if any. | [optional] 
## Example

```python
from lusid.models.fund_structure_close_step import FundStructureCloseStep
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

member_short_code: StrictStr = "example_member_short_code"
fund: ResourceId
step: StrictInt = # Replace with your value
step: StrictInt = 42
status: StrictStr = "example_status"
failure: Optional[StrictStr] = "example_failure"
fund_structure_close_step_instance = FundStructureCloseStep(member_short_code=member_short_code, fund=fund, step=step, status=status, failure=failure)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

