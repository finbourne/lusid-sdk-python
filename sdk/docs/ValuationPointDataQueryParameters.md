# ValuationPointDataQueryParameters

The parameters used in getting the ValuationPointData.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**end** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | 
**exclude_cleardown_module** | **bool** | By deafult this flag is set to false, if this is set to true, no cleardown module will be applied to the trial balance. | [optional] 
## Example

```python
from lusid.models.valuation_point_data_query_parameters import ValuationPointDataQueryParameters
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool

start: Optional[DateOrDiaryEntry] = None
end: DateOrDiaryEntry = # Replace with your value
exclude_cleardown_module: Optional[StrictBool] = # Replace with your value
exclude_cleardown_module:Optional[StrictBool] = None
valuation_point_data_query_parameters_instance = ValuationPointDataQueryParameters(start=start, end=end, exclude_cleardown_module=exclude_cleardown_module)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

