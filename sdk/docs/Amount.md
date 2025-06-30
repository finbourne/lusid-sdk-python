# Amount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
## Example

```python
from lusid.models.amount import Amount
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, StrictFloat, StrictInt

value: Optional[Union[StrictFloat, StrictInt]] = None
amount_instance = Amount(value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

