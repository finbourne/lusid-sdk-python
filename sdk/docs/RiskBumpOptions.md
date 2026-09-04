# RiskBumpOptions

Per-recipe configuration of the bump sizes used by the finite-difference Risk/* measures.  Results are always reported per ResultSensitivity regardless of the shift used to compute  them: the calculators divide by shift/resultSensitivity, so choosing a wider shift (e.g.  10bp for a market element with coarse quote precision) changes the estimator, not the unit.  Every member is optional and an absent member keeps the historical default.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta_shift** | **float** | The shift applied for delta/gamma bumps on any asset type without an explicit override.  Must be strictly positive. Defaults to 0.0001 (1bp) when not supplied. | [optional] 
**result_sensitivity** | **float** | The move the reported sensitivity is normalised to. Must be strictly positive.  Defaults to 0.0001 (results per 1bp move) when not supplied. | [optional] 
**delta_shift_overrides** | **Dict[str, float]** | Per-asset-type overrides of the delta shift, keyed by asset type (e.g. \&quot;Rates\&quot;, \&quot;Credit\&quot;,  \&quot;Fx\&quot;). Values must be strictly positive. Asset types without an override use DeltaShift. | [optional] 
**ladder_shift_overrides** | **Dict[str, Optional[List[float]]]** | Per-asset-type overrides of the shift grid used by ladder measures, keyed by asset type  (e.g. \&quot;Rates\&quot;, \&quot;Fx\&quot;). Each grid must be non-empty and strictly increasing; zero is a  legitimate rung, as the default grids include the base scenario. Asset types without an  override use the standard grids. | [optional] 
**parity_relative_tolerance** | **float** | The relative tolerance for RiskEngine \&quot;Parity\&quot; checks, applied as  |bump - adjoint| &lt;&#x3D; max(absolute floor, |bump| * tolerance). Defaults to 0.001. | [optional] 
## Example

```python
from lusid.models.risk_bump_options import RiskBumpOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

delta_shift: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
result_sensitivity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
delta_shift_overrides: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
ladder_shift_overrides: Optional[Dict[str, Optional[List[Union[StrictFloat, StrictInt]]]]] = # Replace with your value
parity_relative_tolerance: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
risk_bump_options_instance = RiskBumpOptions(delta_shift=delta_shift, result_sensitivity=result_sensitivity, delta_shift_overrides=delta_shift_overrides, ladder_shift_overrides=ladder_shift_overrides, parity_relative_tolerance=parity_relative_tolerance)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

