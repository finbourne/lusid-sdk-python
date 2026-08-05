# ScenarioDiagnostics

Diagnostics for the scenario shifts a valuation applied: every market data target changed by a  shift, with values before and after, plus warnings for market data that matched a shift but could  not honour it. Populated whenever the valuation ran with a request-level scenario or  scenario-decorated metrics; null otherwise. The same material is written to the market data  manifest.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | [**List[AppliedScenarioShift]**](AppliedScenarioShift.md) | One entry per market data target changed by a shift. | [optional] 
**skipped** | **List[str]** | Market data that matched a shift but was skipped (e.g. an element type that does not support  transformation), with the reason. Prefixed with the scenario&#39;s \&quot;scope/code\&quot; reference. | [optional] 
**omitted_applied** | **int** | The number of further applied records omitted from this section, when the valuation changed  more targets than the section carries (large portfolios over long schedules). Null when  nothing was omitted. The market data manifest always carries the complete set. | [optional] 
## Example

```python
from lusid.models.scenario_diagnostics import ScenarioDiagnostics
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

applied: Optional[List[AppliedScenarioShift]] = # Replace with your value
skipped: Optional[List[StrictStr]] = # Replace with your value
omitted_applied: Optional[StrictInt] = # Replace with your value
omitted_applied: Optional[StrictInt] = None
scenario_diagnostics_instance = ScenarioDiagnostics(applied=applied, skipped=skipped, omitted_applied=omitted_applied)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

