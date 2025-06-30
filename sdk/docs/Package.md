# Package

A structure used to describe the structure of an order or orders that make up a non-trivial trade.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**order_ids** | [**List[ResourceId]**](ResourceId.md) | Related order ids. | 
**order_instruction_ids** | [**List[ResourceId]**](ResourceId.md) | Related order instruction ids. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.package import Package
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

id: ResourceId = # Replace with your value
order_ids: conlist(ResourceId) = # Replace with your value
order_instruction_ids: conlist(ResourceId) = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
package_instance = Package(id=id, order_ids=order_ids, order_instruction_ids=order_instruction_ids, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

