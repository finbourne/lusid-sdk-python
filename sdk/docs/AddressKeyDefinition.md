# AddressKeyDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_key** | **str** | The address key of the address key definition. | 
**type** | **str** | The type of the address key definition | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.address_key_definition import AddressKeyDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

address_key: StrictStr = "example_address_key"
type: StrictStr = "example_type"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
address_key_definition_instance = AddressKeyDefinition(address_key=address_key, type=type, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

