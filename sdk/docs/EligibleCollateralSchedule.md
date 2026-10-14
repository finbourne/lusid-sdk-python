# EligibleCollateralSchedule

An eligible collateral schedule: the collateral a party may post under a margin arrangement and the valuation  percentage each class of collateral is accepted at.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**description** | **str** | A description of the Eligible Collateral Schedule. Optional. | [optional] 
**rows** | [**List[EligibleCollateralRow]**](EligibleCollateralRow.md) | The classes of collateral that may be posted, each with the valuation percentage it is accepted at. At least one and at most 200 rows. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties to decorate onto the Eligible Collateral Schedule. Filterable. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.eligible_collateral_schedule import EligibleCollateralSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
description: Optional[StrictStr] = "example_description"
rows: Optional[List[EligibleCollateralRow]] = # Replace with your value
version: Optional[Version] = None
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
links: Optional[List[Link]] = None
eligible_collateral_schedule_instance = EligibleCollateralSchedule(href=href, id=id, description=description, rows=rows, version=version, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

