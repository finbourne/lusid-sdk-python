# OptionEntry

Strike price against par and associated date for a bond call.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strike** | **float** | The strike on this date | 
**var_date** | **datetime** | The date at which the option can be actioned at this strike | 
**end_date** | **datetime** | If American exercise, this is the end of the exercise period. Optional field. Defaults to the Date field if not set. | [optional] 
## Example

```python
from lusid.models.option_entry import OptionEntry
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt
from datetime import datetime
strike: Union[StrictFloat, StrictInt] = # Replace with your value
var_date: datetime = # Replace with your value
end_date: Optional[datetime] = # Replace with your value
option_entry_instance = OptionEntry(strike=strike, var_date=var_date, end_date=end_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

