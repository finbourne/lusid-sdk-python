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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start: Optional[DateOrDiaryEntry] = None
end: DateOrDiaryEntry
valuation_point_data_query_parameters_instance = ValuationPointDataQueryParameters(start=start, end=end)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

