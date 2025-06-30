# ValuationPointDataQueryParameters

The parameters used in getting the ValuationPointData.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | 
## Example

```python
from lusid.models.valuation_point_data_query_parameters import ValuationPointDataQueryParameters
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

end: DateOrDiaryEntry = # Replace with your value
valuation_point_data_query_parameters_instance = ValuationPointDataQueryParameters(end=end)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

