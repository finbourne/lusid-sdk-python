# SingleValuationPointQueryParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_or_diary_entry** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
## Example

```python
from lusid.models.single_valuation_point_query_parameters import SingleValuationPointQueryParameters
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

date_or_diary_entry: Optional[DateOrDiaryEntry] = # Replace with your value
single_valuation_point_query_parameters_instance = SingleValuationPointQueryParameters(date_or_diary_entry=date_or_diary_entry)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

