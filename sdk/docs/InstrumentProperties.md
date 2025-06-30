# InstrumentProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The instrument properties. These will be from the &#39;Instrument&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_properties import InstrumentProperties
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
instrument_properties_instance = InstrumentProperties(href=href, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

