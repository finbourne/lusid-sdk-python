# PartnerStatementRequest

The request to produce a partner statement over a period.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** | The start of the statement period, exclusive. | 
**period_end** | **datetime** | The end of the statement period, inclusive. | 
**nav_type_code** | **str** | The NAV type to produce the statement under. Defaults to the fund&#39;s primary NAV type. | [optional] 
## Example

```python
from lusid.models.partner_statement_request import PartnerStatementRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

period_start: datetime = # Replace with your value
period_end: datetime = # Replace with your value
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
partner_statement_request_instance = PartnerStatementRequest(period_start=period_start, period_end=period_end, nav_type_code=nav_type_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

