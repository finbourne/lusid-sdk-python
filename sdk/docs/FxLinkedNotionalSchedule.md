# FxLinkedNotionalSchedule

Schedule for notional changes based on the change in FX rate. Used in the representation of a resettable cross currency interest rate swap.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fx_conventions** | [**FxConventions**](FxConventions.md) |  | 
**varying_notional_currency** | **str** | The currency of the varying notional amount. | 
**varying_notional_fixing_dates** | [**RelativeDateOffset**](RelativeDateOffset.md) |  | 
**varying_notional_interim_exchange_payment_dates** | [**RelativeDateOffset**](RelativeDateOffset.md) |  | [optional] 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid | 
## Example

```python
from lusid.models.fx_linked_notional_schedule import FxLinkedNotionalSchedule
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictStr, validator

fx_conventions: FxConventions = # Replace with your value
varying_notional_currency: StrictStr = "example_varying_notional_currency"
varying_notional_fixing_dates: RelativeDateOffset = # Replace with your value
varying_notional_interim_exchange_payment_dates: Optional[RelativeDateOffset] = # Replace with your value
schedule_type: StrictStr = "example_schedule_type"
fx_linked_notional_schedule_instance = FxLinkedNotionalSchedule(fx_conventions=fx_conventions, varying_notional_currency=varying_notional_currency, varying_notional_fixing_dates=varying_notional_fixing_dates, varying_notional_interim_exchange_payment_dates=varying_notional_interim_exchange_payment_dates, schedule_type=schedule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

