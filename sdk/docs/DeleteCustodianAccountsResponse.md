# DeleteCustodianAccountsResponse

The delete custodian accounts response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**custodian_account_ids** | [**List[ResourceId]**](ResourceId.md) | The Custodian Accounts which have been soft/hard deleted. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.delete_custodian_accounts_response import DeleteCustodianAccountsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

version: Optional[Version] = None
custodian_account_ids: Optional[List[ResourceId]] = # Replace with your value
links: Optional[List[Link]] = None
delete_custodian_accounts_response_instance = DeleteCustodianAccountsResponse(version=version, custodian_account_ids=custodian_account_ids, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

