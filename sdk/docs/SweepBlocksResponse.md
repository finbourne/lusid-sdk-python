# SweepBlocksResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, ResourceId]**](ResourceId.md) | The identifiers of blocks which have been successfully swept, indexed by ephemeral request-lived id. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The identifiers of blocks that could not be swept, along with a reason for their failure. | [optional] 
## Example

```python
from lusid.models.sweep_blocks_response import SweepBlocksResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, ResourceId]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
sweep_blocks_response_instance = SweepBlocksResponse(values=values, failed=failed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

