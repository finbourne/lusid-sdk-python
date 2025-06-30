# UpsertResultValuesDataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | [**StructuredResultDataId**](StructuredResultDataId.md) |  | 
**key** | **Dict[str, str]** | The structured unit result data key. | [optional] 
**data_address** | **str** | The address of the piece of unit result data | [optional] 
**result_value** | [**ResultValue**](ResultValue.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_result_values_data_request import UpsertResultValuesDataRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

document_id: StructuredResultDataId = # Replace with your value
key: Optional[Dict[str, StrictStr]] = # Replace with your value
data_address: Optional[StrictStr] = "example_data_address"
result_value: Optional[ResultValue] = # Replace with your value
upsert_result_values_data_request_instance = UpsertResultValuesDataRequest(document_id=document_id, key=key, data_address=data_address, result_value=result_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

