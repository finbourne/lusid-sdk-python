# FundCalendarEntries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_calendar_entries_type** | **str** | The type of the Calendar Entry. The available values are: FinalisedValuationPoint, FundEstimateValuationPoint, FundBookmark | 
## Example

```python
from lusid.models.fund_calendar_entries import FundCalendarEntries
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_calendar_entries_type: StrictStr = "example_fund_calendar_entries_type"
fund_calendar_entries_instance = FundCalendarEntries(fund_calendar_entries_type=fund_calendar_entries_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

