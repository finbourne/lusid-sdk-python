# UpdateReferenceDataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_definitions** | [**List[FieldDefinition]**](FieldDefinition.md) | Definition of a reference data field. | 
**request_values** | [**List[FieldValue]**](FieldValue.md) | Reference data. | 
## Example

```python
from lusid.models.update_reference_data_request import UpdateReferenceDataRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

request_definitions: conlist(FieldDefinition) = # Replace with your value
request_values: conlist(FieldValue) = # Replace with your value
update_reference_data_request_instance = UpdateReferenceDataRequest(request_definitions=request_definitions, request_values=request_values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

