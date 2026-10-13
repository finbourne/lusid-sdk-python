# AllocationEventBasisDiagnostics

What the basis source found when it read the register for an Allocation Event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant_count** | **int** | The number of investor records whose basis values were read. | [optional] 
**excluded** | **List[str]** | The investor records the map&#39;s exceptions kept out of the event. | [optional] 
**warnings** | [**List[AllocationEventBasisWarning]**](AllocationEventBasisWarning.md) | Anything the source had to work around, for example MissingFeeRate on a line without a management fee rate. | [optional] 
## Example

```python
from lusid.models.allocation_event_basis_diagnostics import AllocationEventBasisDiagnostics
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

participant_count: Optional[StrictInt] = # Replace with your value
participant_count: Optional[StrictInt] = None
excluded: Optional[List[StrictStr]] = # Replace with your value
warnings: Optional[List[AllocationEventBasisWarning]] = # Replace with your value
allocation_event_basis_diagnostics_instance = AllocationEventBasisDiagnostics(participant_count=participant_count, excluded=excluded, warnings=warnings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

