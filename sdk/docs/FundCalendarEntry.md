# FundCalendarEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_type** | **str** | The type of the Fund Calendar Entry. Only &#39;ValuationPoint&#39; currently supported. The available values are: ValuationPointFundCalendarEntry | 
## Example

```python
from lusid.models.fund_calendar_entry import FundCalendarEntry
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

entry_type: StrictStr = "example_entry_type"
fund_calendar_entry_instance = FundCalendarEntry(entry_type=entry_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

