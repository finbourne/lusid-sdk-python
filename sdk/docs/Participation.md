# Participation

The record an order's participation in a specific placement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placement_id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**Version**](Version.md) |  | [optional] 
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.participation import Participation
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

id: ResourceId = # Replace with your value
placement_id: ResourceId = # Replace with your value
order_id: ResourceId = # Replace with your value
version: Optional[Version] = None
data_model_membership: Optional[DataModelMembership] = # Replace with your value
links: Optional[conlist(Link)] = None
participation_instance = Participation(id=id, placement_id=placement_id, order_id=order_id, version=version, data_model_membership=data_model_membership, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

