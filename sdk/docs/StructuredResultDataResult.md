# StructuredResultDataResult

Represents structured result data document and row details for a data quality check result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity, e.g. \&quot;SrsRow\&quot;. | [optional] 
**as_at** | **datetime** | The as-at timestamp the document was read at | [optional] 
**effective_at** | **datetime** | The effective-at timestamp the document was read at | [optional] 
**document_effective_at** | **datetime** | The effective date of the upload the row was read from: the latest upload at or before effectiveAt | [optional] 
**scope** | **str** | The scope of the document | [optional] 
**code** | **str** | The code of the document | [optional] 
**source** | **str** | The platform or vendor that provided the document | [optional] 
**result_type** | **str** | The document&#39;s result type | [optional] 
**row_identifiers** | **Dict[str, Optional[str]]** | The row&#39;s identifier columns, keyed by address key. Populated when entityType is \&quot;SrsRow\&quot;. | [optional] 
## Example

```python
from lusid.models.structured_result_data_result import StructuredResultDataResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: Optional[StrictStr] = "example_entity_type"
as_at: Optional[datetime] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
document_effective_at: Optional[datetime] = # Replace with your value
scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
source: Optional[StrictStr] = "example_source"
result_type: Optional[StrictStr] = "example_result_type"
row_identifiers: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
structured_result_data_result_instance = StructuredResultDataResult(entity_type=entity_type, as_at=as_at, effective_at=effective_at, document_effective_at=document_effective_at, scope=scope, code=code, source=source, result_type=result_type, row_identifiers=row_identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

