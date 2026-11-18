# IndicativeAmountMetric

The amount a seed amount has grown to by the end of each period of the grid: the seed amount multiplied by  one plus the return since the start of the requested window, geometrically linking the period returns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seed_amount** | **str** |  | 
**type** | **str** | Available values: Return, IndicativeAmount. | 
**alias** | **str** |  | [optional] 
## Example

```python
from lusid.models.indicative_amount_metric import IndicativeAmountMetric
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

seed_amount: StrictStr = "example_seed_amount"
type: StrictStr = "example_type"
alias: Optional[StrictStr] = "example_alias"
indicative_amount_metric_instance = IndicativeAmountMetric(seed_amount=seed_amount, type=type, alias=alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

