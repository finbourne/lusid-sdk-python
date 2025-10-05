# ValuationPointDataQueryParameters

The parameters used in getting the ValuationPointData.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**end** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | 
## Example

```python
from lusid.models.valuation_point_data_query_parameters import ValuationPointDataQueryParameters
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

start: Optional[DateOrDiaryEntry] = None
end: DateOrDiaryEntry = # Replace with your value
valuation_point_data_query_parameters_instance = ValuationPointDataQueryParameters(start=start, end=end)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

