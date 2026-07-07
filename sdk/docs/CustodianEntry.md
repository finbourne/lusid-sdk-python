# CustodianEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | [**ResourceId**](ResourceId.md) |  | 
**account_selector** | **str** | Available values: From, To. | [optional] 
## Example

```python
from lusid.models.custodian_entry import CustodianEntry
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

account_id: ResourceId = # Replace with your value
account_selector: Optional[StrictStr] = "example_account_selector"
custodian_entry_instance = CustodianEntry(account_id=account_id, account_selector=account_selector)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

