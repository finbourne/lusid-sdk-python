# ReverseStressResponse

The result of a reverse stress solve: the factor the scenario's shifts must be multiplied by to  reach the target loss, together with the whole evaluated ladder so the answer can be checked  rather than taken on trust.                The ladder is part of the answer, not diagnostics. A reverse stress is only meaningful where the  loss moves in one direction with the factor, and the ladder is what shows that it does.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale** | **float** | The solved factor: the multiple of the scenario&#39;s shifts that reaches the target. Null when no  factor within the evaluated range reaches it, in which case Converged is false and the  warnings say so. | [optional] 
**target_pnl** | **float** | The change in value that was asked for, echoed back. | [optional] 
**achieved_pnl** | **float** | The change in value actually produced at the solved scale, measured by a valuation at that  factor rather than interpolated. The gap to the target is the honest error of the solve. | [optional] 
**base_value** | **float** | The unstressed value of the measure over the filtered holdings. | [optional] 
**stressed_value** | **float** | The value of the measure at the solved scale. | [optional] 
**converged** | **bool** | Whether the achieved change is within the requested tolerance of the target. False means the  reported scale is the best reached, not an answer to rely on. | [optional] 
**method** | **str** | How the bracketing factor was turned into the reported one: \&quot;Interpolation\&quot; on a monotone  ladder, \&quot;Bisection\&quot; where the ladder turned back on itself and interpolating between one  bracketing pair would have hidden the others. | [optional] 
**valuations** | **int** | How many valuations the solve ran, the opening ladder counting as one. | [optional] 
**ladder** | [**List[ReverseStressRung]**](ReverseStressRung.md) | Every factor evaluated, in increasing order, including the confirming valuations. | [optional] 
**warnings** | **List[str]** | Anything the caller has to know to read the scale correctly: a non-monotone ladder, a target  out of reach, a solve stopped at the iteration limit. | [optional] 
## Example

```python
from lusid.models.reverse_stress_response import ReverseStressResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scale: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
target_pnl: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
achieved_pnl: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
base_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
stressed_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
converged: Optional[StrictBool] = # Replace with your value
converged:Optional[StrictBool] = None
method: Optional[StrictStr] = "example_method"
valuations: Optional[StrictInt] = # Replace with your value
valuations: Optional[StrictInt] = None
ladder: Optional[List[ReverseStressRung]] = # Replace with your value
warnings: Optional[List[StrictStr]] = # Replace with your value
reverse_stress_response_instance = ReverseStressResponse(scale=scale, target_pnl=target_pnl, achieved_pnl=achieved_pnl, base_value=base_value, stressed_value=stressed_value, converged=converged, method=method, valuations=valuations, ladder=ladder, warnings=warnings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

