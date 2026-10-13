# FundClosing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closing_id** | **str** |  | 
**closing_date** | **datetime** |  | 
**is_final** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from lusid.models.fund_closing import FundClosing
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

closing_id: StrictStr = "example_closing_id"
closing_date: datetime = # Replace with your value
is_final: Optional[StrictBool] = # Replace with your value
is_final:Optional[StrictBool] = None
description: Optional[StrictStr] = "example_description"
fund_closing_instance = FundClosing(closing_id=closing_id, closing_date=closing_date, is_final=is_final, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

