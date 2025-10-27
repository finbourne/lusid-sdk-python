# FundAmount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The value of the amount in the fund currency. | [optional] 
## Example

```python
from lusid.models.fund_amount import FundAmount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fund_amount_instance = FundAmount(value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

