# CommodityCalendarSchedule

Schedule describing the periodic calendar-average settlement periods of a commodity calendar swap.  Each period settles in cash against the average of the observed commodity price over the period.  The schedule is currently stored and validated only; period expansion is not yet implemented.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The date from which the first settlement period accrues. | [optional] 
**maturity_date** | **datetime** | The date on which the final settlement period ends. | [optional] 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**payment_currency** | **str** | The currency in which each periodic cash settlement is paid. | [optional] 
**stub_type** | **str** | How any non-integral first or last period is handled when generating the settlement periods.  If not specified, this defaults to None.                Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both]. Available values: None, ShortFront, ShortBack, LongBack, LongFront, Both, Invalid. | [optional] 
**schedule_type** | **str** | Available values: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, PikSchedule, CommodityCalendarSchedule, Invalid, CancelSchedule. | 
## Example

```python
from lusid.models.commodity_calendar_schedule import CommodityCalendarSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: Optional[datetime] = # Replace with your value
maturity_date: Optional[datetime] = # Replace with your value
flow_conventions: Optional[FlowConventions] = # Replace with your value
payment_currency: Optional[StrictStr] = "example_payment_currency"
stub_type: Optional[StrictStr] = "example_stub_type"
schedule_type: StrictStr = "example_schedule_type"
commodity_calendar_schedule_instance = CommodityCalendarSchedule(start_date=start_date, maturity_date=maturity_date, flow_conventions=flow_conventions, payment_currency=payment_currency, stub_type=stub_type, schedule_type=schedule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

