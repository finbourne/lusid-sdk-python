# UpsertRelationalDataPointRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_point_data_series** | [**UpsertRelationalDataPointDataSeries**](UpsertRelationalDataPointDataSeries.md) |  | 
**effective_at** | **str** | The effectiveAt or cut-label datetime of the DataPoint. | 
**value_fields** | **Dict[str, object]** | The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. | 
**meta_data_fields** | **Dict[str, object]** | The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. | [optional] 
## Example

```python
from lusid.models.upsert_relational_data_point_request import UpsertRelationalDataPointRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

data_point_data_series: UpsertRelationalDataPointDataSeries = # Replace with your value
effective_at: StrictStr = "example_effective_at"
value_fields: Dict[str, Any] = # Replace with your value
meta_data_fields: Optional[Dict[str, Any]] = # Replace with your value
upsert_relational_data_point_request_instance = UpsertRelationalDataPointRequest(data_point_data_series=data_point_data_series, effective_at=effective_at, value_fields=value_fields, meta_data_fields=meta_data_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

