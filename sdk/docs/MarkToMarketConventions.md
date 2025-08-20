# MarkToMarketConventions

A set of conventions for mark to market. Mark to market is a method  that values financial instruments based on current market prices,  reflecting their current value, rather than historical cost.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_code** | **str** | The calendar to use when generating mark to market cashflows and events. | [optional] 
## Example

```python
from lusid.models.mark_to_market_conventions import MarkToMarketConventions
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

calendar_code: Optional[StrictStr] = "example_calendar_code"
mark_to_market_conventions_instance = MarkToMarketConventions(calendar_code=calendar_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

