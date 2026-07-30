# RecExceptionCountByClosureType

Closed exception result counts broken down by closure type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleared** | **int** | The number of Cleared results. | 
**accepted** | **int** | The number of Accepted results. | 
**force_matched** | **int** | The number of Force Matched results. | 
## Example

```python
from lusid.models.rec_exception_count_by_closure_type import RecExceptionCountByClosureType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cleared: StrictInt = # Replace with your value
cleared: StrictInt = 42
accepted: StrictInt = # Replace with your value
accepted: StrictInt = 42
force_matched: StrictInt = # Replace with your value
force_matched: StrictInt = 42
rec_exception_count_by_closure_type_instance = RecExceptionCountByClosureType(cleared=cleared, accepted=accepted, force_matched=force_matched)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

