# AccountsUpsertResponse

The upsert accounts response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**accounts** | [**List[Account]**](Account.md) | The Accounts which have been upserted. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.accounts_upsert_response import AccountsUpsertResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
accounts: Optional[conlist(Account)] = # Replace with your value
links: Optional[conlist(Link)] = None
accounts_upsert_response_instance = AccountsUpsertResponse(href=href, version=version, accounts=accounts, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

