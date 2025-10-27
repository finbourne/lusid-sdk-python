# FieldSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** | The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | [optional] 
**display_order** | **int** |  | [optional] 
## Example

```python
from lusid.models.field_schema import FieldSchema
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[ResourceId] = None
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
type: Optional[StrictStr] = "example_type"
display_order: Optional[StrictInt] = # Replace with your value
display_order: Optional[StrictInt] = None
field_schema_instance = FieldSchema(id=id, display_name=display_name, description=description, type=type, display_order=display_order)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

