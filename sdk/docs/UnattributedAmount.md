# UnattributedAmount

An amount on the income summary an allocation run could not attribute to any pool.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **str** | The general ledger account the unattributed amount sits in. | 
**amount** | **float** | The amount allocated to the partner. | 
**reason** | **str** | Why the amount could not be attributed. | 
## Example

```python
from lusid.models.unattributed_amount import UnattributedAmount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

gl_code: StrictStr = "example_gl_code"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
reason: StrictStr = "example_reason"
unattributed_amount_instance = UnattributedAmount(gl_code=gl_code, amount=amount, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

