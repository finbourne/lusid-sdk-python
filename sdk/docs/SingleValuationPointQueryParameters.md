# SingleValuationPointQueryParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_or_diary_entry** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | 
**variant** | **str** | Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates. | [optional] 
## Example

```python
from lusid.models.single_valuation_point_query_parameters import SingleValuationPointQueryParameters
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

date_or_diary_entry: DateOrDiaryEntry = # Replace with your value
variant: Optional[StrictStr] = "example_variant"
single_valuation_point_query_parameters_instance = SingleValuationPointQueryParameters(date_or_diary_entry=date_or_diary_entry, variant=variant)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

