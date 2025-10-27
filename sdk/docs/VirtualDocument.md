# VirtualDocument

Virtual document consists of (potentially several) upserted documents.                The documents get parsed according to the provided data map on upsert, the collection of resulting values in  aggregated in a virtual document
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | [**StructuredResultDataId**](StructuredResultDataId.md) |  | [optional] 
**data** | [**List[VirtualDocumentRow]**](VirtualDocumentRow.md) | The data inside the document | [optional] 
## Example

```python
from lusid.models.virtual_document import VirtualDocument
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

document_id: Optional[StructuredResultDataId] = # Replace with your value
data: Optional[List[VirtualDocumentRow]] = # Replace with your value
virtual_document_instance = VirtualDocument(document_id=document_id, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

