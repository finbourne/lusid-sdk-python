# CreateDataTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the data type will be created in. | 
**code** | **str** | The code of the data type. Together with the scope this uniquely defines the data type. | 
**type_value_range** | **str** | Indicates the range of data acceptable by a data type. The available values are: Open, Closed | 
**display_name** | **str** | The display name of the data type. | 
**description** | **str** | The description of the data type. | 
**value_type** | **str** | The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | 
**acceptable_values** | **List[str]** | The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range. | [optional] 
**unit_schema** | **str** | The schema of the data type&#39;s units. The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptable_units** | [**List[CreateUnitDefinition]**](CreateUnitDefinition.md) | The definitions of the acceptable units. | [optional] 
**reference_data** | [**ReferenceData**](ReferenceData.md) |  | [optional] 
## Example

```python
from lusid.models.create_data_type_request import CreateDataTypeRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
type_value_range: StrictStr = "example_type_value_range"
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
value_type: StrictStr = "example_value_type"
acceptable_values: Optional[conlist(StrictStr)] = # Replace with your value
unit_schema: Optional[StrictStr] = "example_unit_schema"
acceptable_units: Optional[conlist(CreateUnitDefinition)] = # Replace with your value
reference_data: Optional[ReferenceData] = # Replace with your value
create_data_type_request_instance = CreateDataTypeRequest(scope=scope, code=code, type_value_range=type_value_range, display_name=display_name, description=description, value_type=value_type, acceptable_values=acceptable_values, unit_schema=unit_schema, acceptable_units=acceptable_units, reference_data=reference_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

