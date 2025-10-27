# PreviousNAV

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**ShareClassAmount**](ShareClassAmount.md) |  | [optional] 
## Example

```python
from lusid.models.previous_nav import PreviousNAV
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amount: Optional[ShareClassAmount] = None
previous_nav_instance = PreviousNAV(amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

