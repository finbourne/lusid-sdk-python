# MarginAccounts

The custodian account each party's collateral is held in.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**we_post** | **str** | The code of the custodian account, within each applicable portfolio, that holds collateral we post. Empty means collateral we post is not held in a custodian account the item knows of. | [optional] 
**they_post** | **str** | The code of the custodian account, within each applicable portfolio, that holds collateral the counterparty posts. Empty means collateral they post is not held in a custodian account the item knows of. | [optional] 
## Example

```python
from lusid.models.margin_accounts import MarginAccounts
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

we_post: Optional[StrictStr] = "example_we_post"
they_post: Optional[StrictStr] = "example_they_post"
margin_accounts_instance = MarginAccounts(we_post=we_post, they_post=they_post)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

