# AddBusinessDaysToDateResponse

The date that is the requested number of business days after the given start date
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** |  | 
## Example

```python
from lusid.models.add_business_days_to_date_response import AddBusinessDaysToDateResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: datetime
add_business_days_to_date_response_instance = AddBusinessDaysToDateResponse(value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

