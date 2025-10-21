# RunCheckResponse

Response containing the results of running data quality checks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_quality_check_results** | [**List[DataQualityCheckResult]**](DataQualityCheckResult.md) | Collection of data quality check results | [optional] 
## Example

```python
from lusid.models.run_check_response import RunCheckResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

data_quality_check_results: Optional[conlist(DataQualityCheckResult)] = # Replace with your value
run_check_response_instance = RunCheckResponse(data_quality_check_results=data_quality_check_results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

