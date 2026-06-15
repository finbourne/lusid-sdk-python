# UpsertAddressKeyAliasRequest

A request to upsert an address key alias.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_key_alias** | [**AddressKeyAlias**](AddressKeyAlias.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_address_key_alias_request import UpsertAddressKeyAliasRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

address_key_alias: Optional[AddressKeyAlias] = # Replace with your value
upsert_address_key_alias_request_instance = UpsertAddressKeyAliasRequest(address_key_alias=address_key_alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

