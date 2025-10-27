# HoldingIdsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_ids** | **List[int]** | The array of unique holding identifiers | 
## Example

```python
from lusid.models.holding_ids_request import HoldingIdsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_ids: List[StrictInt] = # Replace with your value
holding_ids_request_instance = HoldingIdsRequest(holding_ids=holding_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

