# CorporateActionSource

A corporate action source
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**display_name** | **str** | The name of the corporate action source | [optional] 
**description** | **str** | The description of the corporate action source | [optional] 
**instrument_scopes** | **List[str]** | The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.corporate_action_source import CorporateActionSource
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
id: Optional[ResourceId] = None
version: Optional[Version] = None
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
instrument_scopes: Optional[conlist(StrictStr)] = # Replace with your value
links: Optional[conlist(Link)] = None
corporate_action_source_instance = CorporateActionSource(href=href, id=id, version=version, display_name=display_name, description=description, instrument_scopes=instrument_scopes, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

