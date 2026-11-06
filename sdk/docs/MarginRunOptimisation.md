# MarginRunOptimisation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | How far the pass got. One of Pending, Completed, Skipped or Failed. | 
**recommendation_count** | **int** | How many recommendations the pass made. | 
**detail** | **str** | What the pass left out and why, or why it failed. Null when nothing was left out. | [optional] 
## Example

```python
from lusid.models.margin_run_optimisation import MarginRunOptimisation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: StrictStr = "example_status"
recommendation_count: StrictInt = # Replace with your value
recommendation_count: StrictInt = 42
detail: Optional[StrictStr] = "example_detail"
margin_run_optimisation_instance = MarginRunOptimisation(status=status, recommendation_count=recommendation_count, detail=detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

