# Account

An account
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Account. | 
**description** | **str** | A description for the Account. | [optional] 
**type** | **str** | The Account type. Can have the values: Asset/Liabilities/Income/Expense/Capital/Revenue. | 
**status** | **str** | The Account status. Can be Active, Inactive or Deleted. The available values are: Active, Inactive, Deleted | 
**control** | **str** | This allows users to specify whether this a protected Account that prevents direct manual journal adjustment. Can have the values: System/ManualIt will default to “Manual”. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Account. | [optional] 
## Example

```python
from lusid.models.account import Account
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
description: Optional[StrictStr] = "example_description"
type: StrictStr = "example_type"
status: StrictStr = "example_status"
control: Optional[StrictStr] = "example_control"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
account_instance = Account(code=code, description=description, type=type, status=status, control=control, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

