# MarkToMarketConventions

A set of conventions for mark to market. Mark to market is a method   that values financial instruments based on current market prices,   reflecting their current value, rather than historical cost.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_code** | **str** | The calendar to use when generating mark to market cashflows and events. | [optional] 
**hour_offset_tenor** | **str** | The hour tenor component of the time offset against the maturity date.  This is an optional field, if a value is provided it must be a positive value between &#39;0hour&#39; and &#39;23hour&#39;. | [optional] 
**minute_offset_tenor** | **str** | The minute tenor component of the time offset against the maturity date.  This is an optional field, if a value is provided it must be a positive value between &#39;0min&#39; and &#39;59min&#39;. | [optional] 
## Example

```python
from lusid.models.mark_to_market_conventions import MarkToMarketConventions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

calendar_code: Optional[StrictStr] = "example_calendar_code"
hour_offset_tenor: Optional[StrictStr] = "example_hour_offset_tenor"
minute_offset_tenor: Optional[StrictStr] = "example_minute_offset_tenor"
mark_to_market_conventions_instance = MarkToMarketConventions(calendar_code=calendar_code, hour_offset_tenor=hour_offset_tenor, minute_offset_tenor=minute_offset_tenor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

