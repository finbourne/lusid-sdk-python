# PropertyInterval

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**PropertyValue**](PropertyValue.md) |  | 
**effective_range** | [**DateRange**](DateRange.md) |  | 
**as_at_range** | [**DateRange**](DateRange.md) |  | 
**status** | **str** | Indicates whether the value is part of the prevailing effective date timeline for the requested asAt date, or whether it has been superseded by correctional activity | 
## Example

```python
from lusid.models.property_interval import PropertyInterval
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

value: PropertyValue = # Replace with your value
effective_range: DateRange = # Replace with your value
as_at_range: DateRange = # Replace with your value
status: StrictStr = "example_status"
property_interval_instance = PropertyInterval(value=value, effective_range=effective_range, as_at_range=as_at_range, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

