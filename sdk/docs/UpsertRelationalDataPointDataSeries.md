# UpsertRelationalDataPointDataSeries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_scope** | **str** | The scope of the DataSeries. | 
**applicable_entity** | [**ApplicableEntity**](ApplicableEntity.md) |  | 
**series_identifiers** | **Dict[str, Optional[object]]** | The identifiers that uniquely define this DataSeries, if any, structured according to the FieldSchema of the parent RelationalDatasetDefinition. | [optional] 
## Example

```python
from lusid.models.upsert_relational_data_point_data_series import UpsertRelationalDataPointDataSeries
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

series_scope: StrictStr = "example_series_scope"
applicable_entity: ApplicableEntity = # Replace with your value
series_identifiers: Optional[Dict[str, Any]] = # Replace with your value
upsert_relational_data_point_data_series_instance = UpsertRelationalDataPointDataSeries(series_scope=series_scope, applicable_entity=applicable_entity, series_identifiers=series_identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

