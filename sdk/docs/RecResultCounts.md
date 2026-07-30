# RecResultCounts

Counts of results broken down by the structural categories that align with the review configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_exceptions** | [**RecOpenExceptionCounts**](RecOpenExceptionCounts.md) |  | 
**closed_exceptions** | [**RecClosedExceptionCounts**](RecClosedExceptionCounts.md) |  | 
**matches** | [**RecMatchCounts**](RecMatchCounts.md) |  | 
## Example

```python
from lusid.models.rec_result_counts import RecResultCounts
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

open_exceptions: RecOpenExceptionCounts = # Replace with your value
closed_exceptions: RecClosedExceptionCounts = # Replace with your value
matches: RecMatchCounts
rec_result_counts_instance = RecResultCounts(open_exceptions=open_exceptions, closed_exceptions=closed_exceptions, matches=matches)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

