# RecDefCurrencies

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | The currency used on the left side of the reconciliation. | 
**right** | **str** | The currency used on the right side of the reconciliation. | 
## Example

```python
from lusid.models.rec_def_currencies import RecDefCurrencies
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: StrictStr = "example_left"
right: StrictStr = "example_right"
rec_def_currencies_instance = RecDefCurrencies(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

