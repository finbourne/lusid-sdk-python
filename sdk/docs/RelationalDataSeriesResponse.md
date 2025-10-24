# RelationalDataSeriesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_scope** | **str** | The scope of the DataSeries. | 
**applicable_entity** | [**ApplicableEntity**](ApplicableEntity.md) |  | 
**series_identifiers** | [**Dict[str, RelationalDataPointFieldValueResponse]**](RelationalDataPointFieldValueResponse.md) | The identifiers that uniquely define this DataSeries, structured according to the FieldSchema of the parent RelationalDatasetDefinition. | 
## Example

```python
from lusid.models.relational_data_series_response import RelationalDataSeriesResponse
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

series_scope: StrictStr = "example_series_scope"
applicable_entity: ApplicableEntity = # Replace with your value
series_identifiers: Dict[str, RelationalDataPointFieldValueResponse] = # Replace with your value
relational_data_series_response_instance = RelationalDataSeriesResponse(series_scope=series_scope, applicable_entity=applicable_entity, series_identifiers=series_identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

