# AccountHolderIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A client-defined key used to identify the Account Holder, unique within the Investment Account | 
**scope** | **str** | The scope in which the Investor Record lies. | 
**identifiers** | **Dict[str, Optional[str]]** | Single Account Holder identifier that should target the desired Investor Record. | 
## Example

```python
from lusid.models.account_holder_identifier import AccountHolderIdentifier
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
scope: StrictStr = "example_scope"
identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
account_holder_identifier_instance = AccountHolderIdentifier(key=key, scope=scope, identifiers=identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

