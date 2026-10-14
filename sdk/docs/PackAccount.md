# PackAccount

An account on a partnership configuration pack's chart of accounts.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The account code. | 
**name** | **str** | The account name. | 
**type** | **str** | The account type: Asset, Liability, Capital, Income or Expense. | 
## Example

```python
from lusid.models.pack_account import PackAccount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
name: StrictStr = "example_name"
type: StrictStr = "example_type"
pack_account_instance = PackAccount(code=code, name=name, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

