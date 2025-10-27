# LegalEntity

Representation of Legal Entity on LUSID API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the Legal Entity | [optional] 
**description** | **str** | The description of the Legal Entity | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**lusid_legal_entity_id** | **str** | The unique LUSID Legal Entity Identifier of the Legal Entity. | [optional] 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Legal Entity. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Legal Entity. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the Legal Entity. | [optional] 
**counterparty_risk_information** | [**CounterpartyRiskInformation**](CounterpartyRiskInformation.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.legal_entity import LegalEntity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
href: Optional[StrictStr] = "example_href"
lusid_legal_entity_id: Optional[StrictStr] = "example_lusid_legal_entity_id"
identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
relationships: Optional[List[Relationship]] = # Replace with your value
counterparty_risk_information: Optional[CounterpartyRiskInformation] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
legal_entity_instance = LegalEntity(display_name=display_name, description=description, href=href, lusid_legal_entity_id=lusid_legal_entity_id, identifiers=identifiers, properties=properties, relationships=relationships, counterparty_risk_information=counterparty_risk_information, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

