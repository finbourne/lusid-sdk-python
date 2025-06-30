# FxRateSchedule

Schedule to define fx conversion of cashflows on complex bonds. If an fx schedule is defined then  on payment schedule generation the coupon and principal payoffs will be wrapped in an fx rate payoff method.  Either the fx rate is predefined (fixed) or relies on fx resets (floating).  Used in representation of dual currency bond.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**fx_conversion_types** | **List[str]** | List of flags to indicate if coupon payments, principal payments or both are converted | [optional] 
**rate** | **float** | FxRate used to convert payments. Assumed to be in units of the ToCurrency so conversion is paymentAmount x fxRate | [optional] 
**to_currency** | **str** | Currency that payments are converted to | [optional] 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid | 
## Example

```python
from lusid.models.fx_rate_schedule import FxRateSchedule
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, validator

flow_conventions: Optional[FlowConventions] = # Replace with your value
fx_conversion_types: Optional[conlist(StrictStr)] = # Replace with your value
rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
to_currency: Optional[StrictStr] = "example_to_currency"
schedule_type: StrictStr = "example_schedule_type"
fx_rate_schedule_instance = FxRateSchedule(flow_conventions=flow_conventions, fx_conversion_types=fx_conversion_types, rate=rate, to_currency=to_currency, schedule_type=schedule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

