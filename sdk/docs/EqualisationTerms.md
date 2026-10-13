# EqualisationTerms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**interest_rate** | **float** |  | [optional] 
**day_count_convention** | **str** |  | [optional] 
## Example

```python
from lusid.models.equalisation_terms import EqualisationTerms
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

enabled: StrictBool
enabled:StrictBool = True
interest_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
day_count_convention: Optional[StrictStr] = "example_day_count_convention"
equalisation_terms_instance = EqualisationTerms(enabled=enabled, interest_rate=interest_rate, day_count_convention=day_count_convention)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

