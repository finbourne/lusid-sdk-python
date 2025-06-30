# EffectiveRange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **datetime** | The effective from datetime that this range applies to. | [optional] 
**until_date** | **datetime** | The effective from datetime that this range applies to. | [optional] 
## Example

```python
from lusid.models.effective_range import EffectiveRange
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field
from datetime import datetime
from_date: Optional[datetime] = # Replace with your value
until_date: Optional[datetime] = # Replace with your value
effective_range_instance = EffectiveRange(from_date=from_date, until_date=until_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

