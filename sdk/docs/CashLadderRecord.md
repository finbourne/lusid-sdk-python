# CashLadderRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** |  | [optional] 
**open** | **float** |  | 
**activities** | **Dict[str, float]** |  | 
**close** | **float** |  | 
## Example

```python
from lusid.models.cash_ladder_record import CashLadderRecord
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_date: Optional[datetime] = # Replace with your value
open: Union[StrictFloat, StrictInt]
activities: Dict[str, Union[StrictFloat, StrictInt]]
close: Union[StrictFloat, StrictInt]
cash_ladder_record_instance = CashLadderRecord(effective_date=effective_date, open=open, activities=activities, close=close)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

