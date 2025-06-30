# Fund

A Fund entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Fund. | [optional] 
**description** | **str** | A description for the Fund. | [optional] 
**fund_configuration_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**abor_id** | [**ResourceId**](ResourceId.md) |  | 
**share_class_instruments** | [**List[InstrumentResolutionDetail]**](InstrumentResolutionDetail.md) | Details the user-provided instrument identifiers and the instrument resolved from them. | [optional] 
**type** | **str** | The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39; | 
**inception_date** | **datetime** | Inception date of the Fund | 
**decimal_places** | **int** | Number of decimal places for reporting | [optional] 
**year_end_date** | [**DayMonth**](DayMonth.md) |  | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fund import Fund
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conint, conlist, constr, validator
from datetime import datetime
href: Optional[StrictStr] = "example_href"
id: ResourceId = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
fund_configuration_id: Optional[ResourceId] = # Replace with your value
abor_id: ResourceId = # Replace with your value
share_class_instruments: Optional[conlist(InstrumentResolutionDetail)] = # Replace with your value
type: StrictStr = "example_type"
inception_date: datetime = # Replace with your value
decimal_places: Optional[conint(strict=True, le=30, ge=0)] = Field(None, alias="decimalPlaces", description="Number of decimal places for reporting")
decimal_places: Optional[StrictInt] = None
year_end_date: DayMonth = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
fund_instance = Fund(href=href, id=id, display_name=display_name, description=description, fund_configuration_id=fund_configuration_id, abor_id=abor_id, share_class_instruments=share_class_instruments, type=type, inception_date=inception_date, decimal_places=decimal_places, year_end_date=year_end_date, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

