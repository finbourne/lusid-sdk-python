# FundAmount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The value of the amount in the fund currency. | [optional] 
## Example

```python
from lusid.models.fund_amount import FundAmount
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fund_amount_instance = FundAmount(value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

