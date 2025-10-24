# RelationalDataPointResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relational_dataset_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**data_series** | [**RelationalDataSeriesResponse**](RelationalDataSeriesResponse.md) |  | 
**effective_at** | **datetime** | The effectiveAt or cut-label datetime of the DataPoint. | 
**value_fields** | [**Dict[str, RelationalDataPointFieldValueResponse]**](RelationalDataPointFieldValueResponse.md) | The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. | 
**meta_data_fields** | [**Dict[str, RelationalDataPointFieldValueResponse]**](RelationalDataPointFieldValueResponse.md) | The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. | 
**effective_at_entered** | **str** | The effectiveAt datetime as entered when the DataPoint was created. | 
## Example

```python
from lusid.models.relational_data_point_response import RelationalDataPointResponse
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr
from datetime import datetime
relational_dataset_definition_id: ResourceId = # Replace with your value
data_series: RelationalDataSeriesResponse = # Replace with your value
effective_at: datetime = # Replace with your value
value_fields: Dict[str, RelationalDataPointFieldValueResponse] = # Replace with your value
meta_data_fields: Dict[str, RelationalDataPointFieldValueResponse] = # Replace with your value
effective_at_entered: StrictStr = "example_effective_at_entered"
relational_data_point_response_instance = RelationalDataPointResponse(relational_dataset_definition_id=relational_dataset_definition_id, data_series=data_series, effective_at=effective_at, value_fields=value_fields, meta_data_fields=meta_data_fields, effective_at_entered=effective_at_entered)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

