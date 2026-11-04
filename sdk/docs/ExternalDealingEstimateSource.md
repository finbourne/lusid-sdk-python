# ExternalDealingEstimateSource

The system that sent an external order set, and its own reference for the batch.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system** | **str** |  | 
**reference** | **str** |  | [optional] 
## Example

```python
from lusid.models.external_dealing_estimate_source import ExternalDealingEstimateSource
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

system: StrictStr = "example_system"
reference: Optional[StrictStr] = "example_reference"
external_dealing_estimate_source_instance = ExternalDealingEstimateSource(system=system, reference=reference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

