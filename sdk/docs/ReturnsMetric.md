# ReturnsMetric

A metric requested from the aggregated-returns (TWR) endpoint. Supports only the  period `Return` (the grid granularity is set on the request via Period, not per metric);  `Alias` is the key the metric appears under in the response's metricsValue dictionary.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Available values: Return. | [optional] 
**alias** | **str** |  | [optional] 
## Example

```python
from lusid.models.returns_metric import ReturnsMetric
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
alias: Optional[StrictStr] = "example_alias"
returns_metric_instance = ReturnsMetric(type=type, alias=alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

