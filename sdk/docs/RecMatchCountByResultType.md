# RecMatchCountByResultType

Match result counts broken down by result type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | **int** | The number of Match results. | 
**cross** | **int** | The number of Cross results. | 
## Example

```python
from lusid.models.rec_match_count_by_result_type import RecMatchCountByResultType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

match: StrictInt = # Replace with your value
match: StrictInt = 42
cross: StrictInt = # Replace with your value
cross: StrictInt = 42
rec_match_count_by_result_type_instance = RecMatchCountByResultType(match=match, cross=cross)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

