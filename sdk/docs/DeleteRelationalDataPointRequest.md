# DeleteRelationalDataPointRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_series** | [**DataSeries**](DataSeries.md) |  | 
**effective_at** | **str** | The effectiveAt or cut-label datetime of the DataPoint. | 
## Example

```python
from lusid.models.delete_relational_data_point_request import DeleteRelationalDataPointRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

data_series: DataSeries = # Replace with your value
effective_at: StrictStr = "example_effective_at"
delete_relational_data_point_request_instance = DeleteRelationalDataPointRequest(data_series=data_series, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

