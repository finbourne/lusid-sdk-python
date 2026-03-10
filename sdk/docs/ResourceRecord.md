# ResourceRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_scope** | **str** | The scope of the deployment this record is part of. | 
**deployment_code** | **str** | The code of the deployment this record is part of. | 
**resource_id** | **str** | The unique identifier of the resource associated with this record. | 
**format** | **str** | A semver format identifier for the resource record. | 
**resource_type** | **str** | The type of resource associated with this record. | 
**resource_state** | **object** | The state of the resource associated with this record. | 
**dependencies** | **List[str]** | A collection of resource identifiers that this resource depends on. | 
**tracking_state** | **object** | The tracking state of the resource record. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for the resource record at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.resource_record import ResourceRecord
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

deployment_scope: StrictStr = "example_deployment_scope"
deployment_code: StrictStr = "example_deployment_code"
resource_id: StrictStr = "example_resource_id"
format: StrictStr = "example_format"
resource_type: StrictStr = "example_resource_type"
resource_state: Optional[Any] = # Replace with your value
dependencies: List[StrictStr] = # Replace with your value
tracking_state: Optional[Any] = # Replace with your value
version: Optional[Version] = None
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
resource_record_instance = ResourceRecord(deployment_scope=deployment_scope, deployment_code=deployment_code, resource_id=resource_id, format=format, resource_type=resource_type, resource_state=resource_state, dependencies=dependencies, tracking_state=tracking_state, version=version, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

