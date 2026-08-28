# GetAddressKeyAliasResponse

The response to a singular address key alias read. There is deliberately no failure block on this  type: every route returning it is a singular (or list-of-singular) read, never a batch keyed  lookup, so there is no per-key error to report - an invalid entity is rejected at upsert and  a failed read fails the whole request. The IGetResponse batch members below throw for the  same reason; do not reintroduce a Failed property when copying this shape.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**value** | [**AddressKeyAlias**](AddressKeyAlias.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.get_address_key_alias_response import GetAddressKeyAliasResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
value: Optional[AddressKeyAlias] = None
links: Optional[List[Link]] = None
get_address_key_alias_response_instance = GetAddressKeyAliasResponse(href=href, value=value, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

