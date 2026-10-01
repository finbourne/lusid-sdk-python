# UpsertRecDefinitionPropertiesResponse

The properties upserted onto a rec definition.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The rec definition properties that were upserted. These will be from the &#39;RecDefinition&#39; domain. Properties deleted by the request are not included. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_rec_definition_properties_response import UpsertRecDefinitionPropertiesResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
upsert_rec_definition_properties_response_instance = UpsertRecDefinitionPropertiesResponse(href=href, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

