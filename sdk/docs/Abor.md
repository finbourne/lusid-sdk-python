# Abor

An Abor entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Abor. | [optional] 
**description** | **str** | The description for the Abor. | [optional] 
**portfolio_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The list with the portfolio ids which are part of the Abor. Note: These must all have the same base currency. | 
**abor_configuration_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Abor. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**base_currency** | **str** | The base currency of the abor based on contained portfolio base currencies. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.abor import Abor
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
portfolio_ids: List[PortfolioEntityId] = # Replace with your value
abor_configuration_id: Optional[ResourceId] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
base_currency: Optional[StrictStr] = "example_base_currency"
links: Optional[List[Link]] = None
abor_instance = Abor(href=href, id=id, display_name=display_name, description=description, portfolio_ids=portfolio_ids, abor_configuration_id=abor_configuration_id, properties=properties, version=version, base_currency=base_currency, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

