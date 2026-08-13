# ResetSchedule

The schedule on which the price return of the asset leg of a total return swap is observed and exchanged.  Each reset period pays the change in the asset's price over the period, sourced from quoted market data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**first_reset_date** | **datetime** | The date of the first price reset. Optional; when absent the reset dates are rolled forward from the swap start date. | [optional] 
**frequency** | **str** | The frequency at which the asset price is reset and the price return is exchanged, e.g. 3M. | 
**last_reset_date** | **datetime** | The date of the last price reset. Optional; when absent the reset dates are rolled forward until the swap maturity date. | [optional] 
## Example

```python
from lusid.models.reset_schedule import ResetSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

conventions: Optional[FlowConventions] = None
first_reset_date: Optional[datetime] = # Replace with your value
frequency: StrictStr = "example_frequency"
last_reset_date: Optional[datetime] = # Replace with your value
reset_schedule_instance = ResetSchedule(conventions=conventions, first_reset_date=first_reset_date, frequency=frequency, last_reset_date=last_reset_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

