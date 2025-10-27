# PackageRequest

A request to create or update a Package.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**order_ids** | [**List[ResourceId]**](ResourceId.md) | Related order ids. | 
**order_instruction_ids** | [**List[ResourceId]**](ResourceId.md) | Related order instruction ids. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
## Example

```python
from lusid.models.package_request import PackageRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
order_ids: List[ResourceId] = # Replace with your value
order_instruction_ids: List[ResourceId] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
package_request_instance = PackageRequest(id=id, order_ids=order_ids, order_instruction_ids=order_instruction_ids, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

