# DataType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_value_range** | **str** | The available values are: Open, Closed | 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**value_type** | **str** | The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | 
**acceptable_values** | **List[str]** |  | [optional] 
**unit_schema** | **str** | The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptable_units** | [**List[IUnitDefinitionDto]**](IUnitDefinitionDto.md) |  | [optional] 
**reference_data** | [**ReferenceData**](ReferenceData.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.data_type import DataType
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

type_value_range: StrictStr = "example_type_value_range"
id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
value_type: StrictStr = "example_value_type"
acceptable_values: Optional[conlist(StrictStr)] = # Replace with your value
unit_schema: Optional[StrictStr] = "example_unit_schema"
acceptable_units: Optional[conlist(IUnitDefinitionDto)] = # Replace with your value
reference_data: Optional[ReferenceData] = # Replace with your value
version: Optional[Version] = None
href: Optional[StrictStr] = "example_href"
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
links: Optional[conlist(Link)] = None
data_type_instance = DataType(type_value_range=type_value_range, id=id, display_name=display_name, description=description, value_type=value_type, acceptable_values=acceptable_values, unit_schema=unit_schema, acceptable_units=acceptable_units, reference_data=reference_data, version=version, href=href, staged_modifications=staged_modifications, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

