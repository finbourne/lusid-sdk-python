# CustodianAccountsUpsertResponse

The upsert accounts response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**custodian_accounts** | [**List[CustodianAccount]**](CustodianAccount.md) | The Custodian Accounts which have been upserted. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.custodian_accounts_upsert_response import CustodianAccountsUpsertResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
custodian_accounts: Optional[conlist(CustodianAccount)] = # Replace with your value
links: Optional[conlist(Link)] = None
custodian_accounts_upsert_response_instance = CustodianAccountsUpsertResponse(href=href, version=version, custodian_accounts=custodian_accounts, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

