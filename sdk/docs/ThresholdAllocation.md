# ThresholdAllocation

How a threshold is split between the two parties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**we** | **float** | Our share of the threshold. | 
**they** | **float** | The counterparty&#39;s share of the threshold. | 
## Example

```python
from lusid.models.threshold_allocation import ThresholdAllocation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

we: Union[StrictFloat, StrictInt] = # Replace with your value
they: Union[StrictFloat, StrictInt] = # Replace with your value
threshold_allocation_instance = ThresholdAllocation(we=we, they=they)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

