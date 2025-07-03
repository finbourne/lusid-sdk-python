# Fund

A Fund entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Fund. | [optional] 
**description** | **str** | A description for the Fund. | [optional] 
**base_currency** | **str** | The base currency of the Fund in ISO 4217 currency code format. All portfolios must be of a matching base currency. | [optional] 
**portfolio_ids** | [**List[PortfolioEntityIdWithDetails]**](PortfolioEntityIdWithDetails.md) | A list of the portfolios on the fund, which are part of the Fund. Note: These must all have the same base currency, which must also much the Fund Base Currency. | [optional] 
**fund_configuration_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**abor_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**share_class_instruments** | [**List[InstrumentResolutionDetail]**](InstrumentResolutionDetail.md) | Details the user-provided instrument identifiers and the instrument resolved from them. | [optional] 
**type** | **str** | The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39; | 
**inception_date** | **datetime** | Inception date of the Fund | 
**decimal_places** | **int** | Number of decimal places for reporting | [optional] 
**year_end_date** | [**DayMonth**](DayMonth.md) |  | [optional] 
**primary_nav_type** | [**NavTypeDefinition**](NavTypeDefinition.md) |  | [optional] 
**additional_nav_types** | [**List[NavTypeDefinition]**](NavTypeDefinition.md) | The definitions for any additional NAVs on the Fund. | [optional] 
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
base_currency: Optional[StrictStr] = "example_base_currency"
portfolio_ids: Optional[conlist(PortfolioEntityIdWithDetails)] = # Replace with your value
fund_configuration_id: Optional[ResourceId] = # Replace with your value
abor_id: Optional[ResourceId] = # Replace with your value
share_class_instruments: Optional[conlist(InstrumentResolutionDetail)] = # Replace with your value
type: StrictStr = "example_type"
inception_date: datetime = # Replace with your value
decimal_places: Optional[conint(strict=True, le=30, ge=0)] = Field(None, alias="decimalPlaces", description="Number of decimal places for reporting")
decimal_places: Optional[StrictInt] = None
year_end_date: Optional[DayMonth] = # Replace with your value
primary_nav_type: Optional[NavTypeDefinition] = # Replace with your value
additional_nav_types: Optional[conlist(NavTypeDefinition)] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
fund_instance = Fund(href=href, id=id, display_name=display_name, description=description, base_currency=base_currency, portfolio_ids=portfolio_ids, fund_configuration_id=fund_configuration_id, abor_id=abor_id, share_class_instruments=share_class_instruments, type=type, inception_date=inception_date, decimal_places=decimal_places, year_end_date=year_end_date, primary_nav_type=primary_nav_type, additional_nav_types=additional_nav_types, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

