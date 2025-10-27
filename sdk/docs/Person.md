# Person

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the Person | [optional] 
**description** | **str** | The description of the Person | [optional] 
**href** | **str** | The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**lusid_person_id** | **str** | The unique LUSID Person Identifier of the Person. | [optional] 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Person. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Person. There can be multiple properties associated with a property key. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the Person. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.person import Person
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
href: Optional[StrictStr] = "example_href"
lusid_person_id: Optional[StrictStr] = "example_lusid_person_id"
identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
relationships: Optional[List[Relationship]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
person_instance = Person(display_name=display_name, description=description, href=href, lusid_person_id=lusid_person_id, identifiers=identifiers, properties=properties, relationships=relationships, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

