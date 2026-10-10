# SwingTriggerEvaluation

How a Market swing trigger was evaluated at a valuation point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fired** | **bool** | Whether the net cashflow was in the trigger&#39;s direction and above its threshold. | 
**threshold** | **float** | The trigger&#39;s threshold. | 
**metric** | **str** | What the threshold measured: NetCashflowAbsolute or NetCashflowPctOfNav. | 
## Example

```python
from lusid.models.swing_trigger_evaluation import SwingTriggerEvaluation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fired: StrictBool = # Replace with your value
fired:StrictBool = True
threshold: Union[StrictFloat, StrictInt] = # Replace with your value
metric: StrictStr = "example_metric"
swing_trigger_evaluation_instance = SwingTriggerEvaluation(fired=fired, threshold=threshold, metric=metric)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

