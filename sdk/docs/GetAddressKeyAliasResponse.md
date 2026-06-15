# GetAddressKeyAliasResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**value** | [**AddressKeyAlias**](AddressKeyAlias.md) |  | [optional] 
**failed** | [**ErrorDetail**](ErrorDetail.md) |  | [optional] 
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
failed: Optional[ErrorDetail] = None
links: Optional[List[Link]] = None
get_address_key_alias_response_instance = GetAddressKeyAliasResponse(href=href, value=value, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

