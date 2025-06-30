# FeeType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the fee type. | 
**description** | **str** | The description of the fee type. | 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the fee type to be created. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fee_type import FeeType
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

href: Optional[StrictStr] = "example_href"
id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
component_transactions: conlist(ComponentTransaction) = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
fee_type_instance = FeeType(href=href, id=id, display_name=display_name, description=description, component_transactions=component_transactions, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

