# AppliedScenarioShift

One market data target changed by one scenario shift during a valuation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario** | **str** | The \&quot;scope/code\&quot; reference of the scenario the shift belongs to. | [optional] 
**effective_at** | **datetime** | The effective date of the market data the shift was applied to. | [optional] 
**shift** | **str** | Description of the shift, e.g. \&quot;PriceShift on &#39;SCENARIO_EQUITY&#39;\&quot;. | [optional] 
**target** | **str** | Description of the market data target the shift changed. | [optional] 
**value_before** | **float** | The target&#39;s value before the shift. Null for multi-point targets (e.g. whole curves) where a  single number is not meaningful. | [optional] 
**value_after** | **float** | The target&#39;s value after the shift. Null for multi-point targets. | [optional] 
## Example

```python
from lusid.models.applied_scenario_shift import AppliedScenarioShift
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scenario: Optional[StrictStr] = "example_scenario"
effective_at: Optional[datetime] = # Replace with your value
shift: Optional[StrictStr] = "example_shift"
target: Optional[StrictStr] = "example_target"
value_before: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
value_after: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
applied_scenario_shift_instance = AppliedScenarioShift(scenario=scenario, effective_at=effective_at, shift=shift, target=target, value_before=value_before, value_after=value_after)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

