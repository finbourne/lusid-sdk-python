# ResolveTenorsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | 
**spot_date** | **datetime** |  | 
**eom_rule_applied** | **bool** |  | 
**dates** | **Dict[str, datetime]** |  | 
## Example

```python
from lusid.models.resolve_tenors_response import ResolveTenorsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
spot_date: datetime = # Replace with your value
eom_rule_applied: StrictBool = # Replace with your value
eom_rule_applied:StrictBool = True
dates: Dict[str, datetime]
resolve_tenors_response_instance = ResolveTenorsResponse(start_date=start_date, spot_date=spot_date, eom_rule_applied=eom_rule_applied, dates=dates)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

