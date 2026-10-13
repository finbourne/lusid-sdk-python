# RecyclingTerms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**cap_percentage_of_commitments** | **float** |  | [optional] 
**recycling_end_date** | **datetime** |  | [optional] 
## Example

```python
from lusid.models.recycling_terms import RecyclingTerms
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

enabled: StrictBool
enabled:StrictBool = True
cap_percentage_of_commitments: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
recycling_end_date: Optional[datetime] = # Replace with your value
recycling_terms_instance = RecyclingTerms(enabled=enabled, cap_percentage_of_commitments=cap_percentage_of_commitments, recycling_end_date=recycling_end_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

