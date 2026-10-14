# FeeRateTier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** |  | 
**threshold** | **float** |  | [optional] 
## Example

```python
from lusid.models.fee_rate_tier import FeeRateTier
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rate: Union[StrictFloat, StrictInt]
threshold: Optional[Union[StrictFloat, StrictInt]] = None
fee_rate_tier_instance = FeeRateTier(rate=rate, threshold=threshold)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

