# FeeSizeTier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower_bound** | **float** |  | 
**upper_bound** | **float** |  | [optional] 
**rate** | **float** |  | 
## Example

```python
from lusid.models.fee_size_tier import FeeSizeTier
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lower_bound: Union[StrictFloat, StrictInt] = # Replace with your value
upper_bound: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
rate: Union[StrictFloat, StrictInt]
fee_size_tier_instance = FeeSizeTier(lower_bound=lower_bound, upper_bound=upper_bound, rate=rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

