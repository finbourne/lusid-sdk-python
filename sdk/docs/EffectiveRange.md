# EffectiveRange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **datetime** | The effective from datetime that this range applies to. | [optional] 
**until_date** | **datetime** | The effective from datetime that this range applies to. | [optional] 
## Example

```python
from lusid.models.effective_range import EffectiveRange
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

from_date: Optional[datetime] = # Replace with your value
until_date: Optional[datetime] = # Replace with your value
effective_range_instance = EffectiveRange(from_date=from_date, until_date=until_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

