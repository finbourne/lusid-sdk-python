# DeleteAccountsResponse

The delete accounts response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**account_ids** | **List[str]** | The Accounts which have been soft/hard deleted. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.delete_accounts_response import DeleteAccountsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

version: Optional[Version] = None
account_ids: Optional[conlist(StrictStr)] = # Replace with your value
links: Optional[conlist(Link)] = None
delete_accounts_response_instance = DeleteAccountsResponse(version=version, account_ids=account_ids, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

