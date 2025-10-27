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
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.package import Package
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
order_ids: List[ResourceId] = # Replace with your value
order_instruction_ids: List[ResourceId] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
version: Optional[Version] = None
data_model_membership: Optional[DataModelMembership] = # Replace with your value
links: Optional[List[Link]] = None
package_instance = Package(id=id, order_ids=order_ids, order_instruction_ids=order_instruction_ids, properties=properties, version=version, data_model_membership=data_model_membership, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

