# SetTransactionConfigurationAlias

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**description** | **str** |  | 
**transaction_class** | **str** |  | 
**transaction_role** | **str** |  | 
**is_default** | **bool** |  | [optional] 
## Example

```python
from lusid.models.set_transaction_configuration_alias import SetTransactionConfigurationAlias
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
description: StrictStr = "example_description"
transaction_class: StrictStr = "example_transaction_class"
transaction_role: StrictStr = "example_transaction_role"
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
set_transaction_configuration_alias_instance = SetTransactionConfigurationAlias(type=type, description=description, transaction_class=transaction_class, transaction_role=transaction_role, is_default=is_default)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

