# PerformanceReturn

A list of Returns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effectiveAt for the return. | 
**rate_of_return** | **float** | The return number. | 
**opening_market_value** | **float** | The opening market value. | [optional] 
**closing_market_value** | **float** | The closing market value. | [optional] 
**period** | **str** | Upsert the returns on a Daily or Monthly period. Defaults to Daily. | [optional] 
## Example

```python
from lusid.models.performance_return import PerformanceReturn
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_at: datetime = # Replace with your value
rate_of_return: Union[StrictFloat, StrictInt] = # Replace with your value
opening_market_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
closing_market_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
period: Optional[StrictStr] = "example_period"
performance_return_instance = PerformanceReturn(effective_at=effective_at, rate_of_return=rate_of_return, opening_market_value=opening_market_value, closing_market_value=closing_market_value, period=period)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

