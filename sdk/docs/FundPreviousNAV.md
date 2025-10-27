# FundPreviousNAV

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the previous NAV. | [optional] 
## Example

```python
from lusid.models.fund_previous_nav import FundPreviousNAV
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fund_previous_nav_instance = FundPreviousNAV(amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

