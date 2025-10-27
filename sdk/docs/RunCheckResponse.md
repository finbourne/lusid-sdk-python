# RunCheckResponse

Response containing the results of running data quality checks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_quality_check_results** | [**List[DataQualityCheckResult]**](DataQualityCheckResult.md) | Collection of data quality check results | [optional] 
## Example

```python
from lusid.models.run_check_response import RunCheckResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

data_quality_check_results: Optional[List[DataQualityCheckResult]] = # Replace with your value
run_check_response_instance = RunCheckResponse(data_quality_check_results=data_quality_check_results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

