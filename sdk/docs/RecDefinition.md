# RecDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the rec definition. | 
**description** | **str** | A description of the rec definition. | [optional] 
**side_names** | [**RecDefSideNames**](RecDefSideNames.md) |  | [optional] 
**details** | [**RecDefinitionDetails**](RecDefinitionDetails.md) |  | 
**review_configuration** | [**RecReviewConfiguration**](RecReviewConfiguration.md) |  | 
**date_policy** | [**RecDatePolicy**](RecDatePolicy.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties in the RecDefinition domain. On update, a property with a null value is deleted and omitted properties are left unchanged. Filterable and sortable. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.rec_definition import RecDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
side_names: Optional[RecDefSideNames] = # Replace with your value
details: RecDefinitionDetails
review_configuration: RecReviewConfiguration = # Replace with your value
date_policy: RecDatePolicy = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
rec_definition_instance = RecDefinition(id=id, display_name=display_name, description=description, side_names=side_names, details=details, review_configuration=review_configuration, date_policy=date_policy, properties=properties, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

