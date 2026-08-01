# ScenarioPreviewResponse

The result of previewing a scenario: every market data target the scenario's shifts changed, with  values before and after, plus warnings for market data that matched a shift but could not honour it.  An empty applied list means the scenario would touch nothing for this portfolio and recipe.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | [**List[ScenarioPreviewAppliedShift]**](ScenarioPreviewAppliedShift.md) | One entry per market data target changed by a shift. | [optional] 
**skipped** | **List[str]** | Market data that matched a shift but was skipped (e.g. an element type that does not support  transformation), with the reason. | [optional] 
## Example

```python
from lusid.models.scenario_preview_response import ScenarioPreviewResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

applied: Optional[List[ScenarioPreviewAppliedShift]] = # Replace with your value
skipped: Optional[List[StrictStr]] = # Replace with your value
scenario_preview_response_instance = ScenarioPreviewResponse(applied=applied, skipped=skipped)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

